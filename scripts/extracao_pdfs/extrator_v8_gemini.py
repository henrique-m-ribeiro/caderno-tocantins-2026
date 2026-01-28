#!/usr/bin/env python3
"""
Extrator v8 - Expandido para Finanças Públicas e Agropecuária
Autor: Gemini (Google AI)
Data: 2026-01-28
Objetivo: 95%+ de cobertura de dados quantitativos

Novidades V8:
- Finanças Públicas: Receitas, Despesas, FPM, ICMS
- Agropecuária: Rebanhos (bovino, suíno, aves), Produção (soja, milho, arroz)
- Saída em Excel consolidado
"""

import pdfplumber
import pandas as pd
import re
import os
import json
import time
import sys

# ==============================================================================
# CONFIGURAÇÃO E CONSTANTES
# ==============================================================================

# Mapeamento de palavras-chave para identificar páginas de cada capítulo
PAGE_KEYWORDS = {
    "demography": ["demografia", "população total", "densidade demográfica"],
    "idh": ["índice de desenvolvimento humano", "idhm"],
    "economy": ["economia", "pib", "produto interno bruto", "valor adicionado bruto"],
    "education": ["educação", "alfabetização", "ideb", "ensino fundamental"],
    "health": ["saúde", "mortalidade infantil", "leitos", "estabelecimentos de saúde"],
    "sanitation": ["saneamento", "abastecimento de água", "esgotamento sanitário"],
    "finance": ["finanças públicas", "receitas orçamentárias", "despesas orçamentárias", "fundo de participação"], # NOVO V8
    "agriculture": ["agropecuária", "produção agrícola", "rebanho", "lavoura temporária"] # NOVO V8
}

# Regex para capturar valores numéricos brasileiros (1.000,00) no final de linhas
REGEX_MONEY = r"([\d\.]+,\d{2})"
REGEX_INT = r"([\d\.]+)"

# ==============================================================================
# FUNÇÕES DE UTILIDADE
# ==============================================================================

def sanitize_number(value_str):
    """
    Converte string numérica brasileira (1.234,56) para float (1234.56).
    Remove caracteres não numéricos como 'R$', '%', etc.
    """
    if not value_str:
        return None

    # Remove R$, espaços e caracteres indesejados, mantendo apenas dígitos, pontos e vírgulas
    clean_str = re.sub(r'[^\d.,]', '', str(value_str)).strip()

    if not clean_str:
        return None

    try:
        # Caso padrão brasileiro: 1.000,00 -> 1000.00
        if ',' in clean_str:
            clean_str = clean_str.replace('.', '').replace(',', '.')
        # Caso onde pode haver erro de OCR e vir como 1000.00 (formato US)
        elif clean_str.count('.') == 1:
            pass
        # Caso 1.000 (sem decimal) -> 1000
        else:
            clean_str = clean_str.replace('.', '')

        return float(clean_str)
    except ValueError:
        return None

def extract_text_from_page(page):
    """Extrai texto cru da página preservando layout básico."""
    return page.extract_text()

# ==============================================================================
# MOTORES DE EXTRAÇÃO (ESPECIALISTAS POR CAPÍTULO)
# ==============================================================================

def extract_demography(text):
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        # População
        if "população total" in line_lower:
            parts = line.split()
            # Tenta pegar o último token numérico
            for part in reversed(parts):
                val = sanitize_number(part)
                if val:
                    data["População Total"] = val
                    break

        # Densidade
        if "densidade demográfica" in line_lower:
            parts = line.split()
            for part in reversed(parts):
                val = sanitize_number(part)
                if val:
                    data["Densidade Demográfica"] = val
                    break

        # Área Territorial (Geralmente aparece no cabeçalho ou demografia)
        if "área da unidade territorial" in line_lower or "área (km²)" in line_lower:
             parts = line.split()
             for part in reversed(parts):
                val = sanitize_number(part)
                if val:
                    data["Área Territorial (km²)"] = val
                    break
    return data

def extract_idh(text):
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()
        if "idhm" in line_lower and "2010" in line_lower: # Geralmente o dado mais recente é 2010
             parts = line.split()
             for part in reversed(parts):
                val = sanitize_number(part)
                if val and val < 1.0: # IDH é sempre < 1
                    data["IDHM (2010)"] = val
                    break
    return data

def extract_economy(text):
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        # PIB
        if "pib per capita" in line_lower:
            matches = re.findall(REGEX_MONEY, line)
            if matches:
                data["PIB Per Capita (R$)"] = sanitize_number(matches[-1])
        elif "produto interno bruto" in line_lower or "pib a preços correntes" in line_lower:
             # Evitar pegar o ano no título
             parts = line.split()
             # Lógica heurística: pegar o maior valor numérico da linha que parece dinheiro
             vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
             if vals:
                 # Assumindo que o PIB total é um valor grande
                 valid_vals = [v for v in vals if v > 2000]
                 if valid_vals:
                     data["PIB Total (R$ x1000)"] = valid_vals[-1]

        # VAB (Valor Adicionado Bruto)
        if "agropecuária" in line_lower and "serviços" not in line_lower:
             parts = line.split()
             vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
             if vals: data["VAB Agropecuária"] = vals[-1]

        if "indústria" in line_lower:
             parts = line.split()
             vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
             if vals: data["VAB Indústria"] = vals[-1]

        if "serviços" in line_lower and "administração" not in line_lower:
             parts = line.split()
             vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
             if vals: data["VAB Serviços"] = vals[-1]

        if "administração" in line_lower and "pública" in line_lower:
             parts = line.split()
             vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
             if vals: data["VAB Adm Pública"] = vals[-1]

    return data

def extract_education(text):
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        if "taxa de alfabetização" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Taxa Alfabetização"] = vals[-1]

        if "ideb" in line_lower and "iniciais" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["IDEB Anos Iniciais"] = vals[-1]

        if "ideb" in line_lower and "finais" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["IDEB Anos Finais"] = vals[-1]

    return data

def extract_health(text):
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        if "mortalidade infantil" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Mortalidade Infantil"] = vals[-1]

        if "número de leitos" in line_lower or "leitos de internação" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Leitos SUS"] = vals[-1]

        # V8: Novos campos
        if "estabelecimentos de saúde" in line_lower:
             parts = line.split()
             vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
             if vals: data["Estabelecimentos Saúde Total"] = vals[-1]

    return data

def extract_sanitation(text):
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        # Busca por padrões de porcentagem ou valores absolutos
        if "abastecimento de água" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Domicílios com Água (%)"] = vals[-1]

        if "esgotamento sanitário" in line_lower or "rede de esgoto" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Domicílios com Esgoto (%)"] = vals[-1]

        if "coleta de lixo" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Domicílios com Coleta de Lixo (%)"] = vals[-1]

    return data

# --- NOVAS FUNÇÕES V8 ---

def extract_finances(text):
    """Extrai dados de Finanças Públicas (Receitas, Despesas, FPM, ICMS)"""
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        # Regex captura o último valor monetário da linha
        matches = re.findall(REGEX_MONEY, line)
        val = sanitize_number(matches[-1]) if matches else None

        if not val: continue

        if "receitas orçamentárias" in line_lower:
            data["Finanças - Receita Total (R$)"] = val
        elif "despesas orçamentárias" in line_lower:
            data["Finanças - Despesa Total (R$)"] = val
        elif "fpm" in line_lower or "fundo de participação" in line_lower:
            data["Finanças - FPM (R$)"] = val
        elif "icms" in line_lower and "cota-parte" in line_lower:
            data["Finanças - Cota Parte ICMS (R$)"] = val
        elif "receita tributária" in line_lower:
            data["Finanças - Receita Tributária (R$)"] = val

    return data

def extract_agriculture(text):
    """Extrai dados de Agropecuária (Rebanhos e Produção)"""
    data = {}
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        # Rebanhos (Geralmente números inteiros no final da linha)
        # Ex: "Bovinos 10.000"
        if "bovino" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Agro - Rebanho Bovino (cabeças)"] = vals[-1]

        elif "suíno" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Agro - Rebanho Suíno (cabeças)"] = vals[-1]

        elif "galináceos" in line_lower or "aves" in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Agro - Aves (cabeças)"] = vals[-1]

        # Produção Agrícola (Geralmente Toneladas)
        # Ex: "Soja 50.000"
        elif "soja" in line_lower and "tonelada" not in line_lower: # Evita pegar cabeçalho
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Agro - Produção Soja (ton)"] = vals[-1]

        elif "milho" in line_lower and "tonelada" not in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Agro - Produção Milho (ton)"] = vals[-1]

        elif "arroz" in line_lower and "tonelada" not in line_lower:
            parts = line.split()
            vals = [sanitize_number(p) for p in parts if sanitize_number(p)]
            if vals: data["Agro - Produção Arroz (ton)"] = vals[-1]

    return data

# ==============================================================================
# CONTROLADOR PRINCIPAL
# ==============================================================================

def map_pages(pdf):
    """Identifica quais páginas pertencem a quais capítulos."""
    mapping = {k: [] for k in PAGE_KEYWORDS.keys()}

    for i, page in enumerate(pdf.pages):
        text = extract_text_from_page(page).lower()
        for chapter, keywords in PAGE_KEYWORDS.items():
            # Se encontrar QUALQUER palavra-chave do capítulo na página
            if any(k in text for k in keywords):
                mapping[chapter].append(i)

    return mapping

def process_municipio(pdf_path):
    """Processa um único PDF e retorna um dicionário plano de dados."""
    filename = os.path.basename(pdf_path)
    municipio_name = filename.replace("_perfil_2024pdf.pdf", "").replace("_", " ").title()

    full_data = {"Municipio_Arquivo": municipio_name}

    with pdfplumber.open(pdf_path) as pdf:
        # 1. Mapear onde estão os dados
        page_map = map_pages(pdf)

        # 2. Extrair dados por capítulo
        # Demografia
        for page_idx in page_map["demography"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_demography(text))

        # IDH
        for page_idx in page_map["idh"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_idh(text))

        # Economia
        for page_idx in page_map["economy"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_economy(text))

        # Educação
        for page_idx in page_map["education"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_education(text))

        # Saúde
        for page_idx in page_map["health"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_health(text))

        # Saneamento
        for page_idx in page_map["sanitation"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_sanitation(text))

        # Finanças (V8)
        for page_idx in page_map["finance"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_finances(text))

        # Agropecuária (V8)
        for page_idx in page_map["agriculture"]:
            text = extract_text_from_page(pdf.pages[page_idx])
            full_data.update(extract_agriculture(text))

    return full_data

def batch_process(pdf_folder_path, output_excel="BASE_DADOS_TOCANTINS_V03_BETA.xlsx"):
    """Processa todos os PDFs de uma pasta."""
    all_data = []
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]

    print(f"Iniciando processamento de {len(pdf_files)} arquivos...")

    start_time = time.time()

    for i, pdf_file in enumerate(pdf_files):
        pdf_path = os.path.join(pdf_folder_path, pdf_file)
        print(f"[{i+1}/{len(pdf_files)}] Processando {pdf_file}...")

        try:
            data = process_municipio(pdf_path)
            all_data.append(data)
        except Exception as e:
            print(f"ERRO em {pdf_file}: {e}")

    df = pd.DataFrame(all_data)

    # Ordenar colunas para ficar bonito
    cols = sorted(list(df.columns))
    # Mover 'Municipio_Arquivo' para primeira posição
    if 'Municipio_Arquivo' in cols:
        cols.insert(0, cols.pop(cols.index('Municipio_Arquivo')))
    df = df[cols]

    df.to_excel(output_excel, index=False)
    print(f"\nConcluído! Dados salvos em {output_excel}")
    print(f"Tempo total: {time.time() - start_time:.2f} segundos")

    # Exibir estatísticas
    print(f"\n=== ESTATÍSTICAS ===")
    print(f"Total de municípios: {len(df)}")
    print(f"Total de indicadores: {len(df.columns) - 1}")  # -1 para excluir coluna município
    print(f"Indicadores por município (média): {df.notna().sum(axis=1).mean():.1f}")

    return df

# ==============================================================================
# EXECUÇÃO (DEBUG / TESTE)
# ==============================================================================
if __name__ == "__main__":
    # Para teste rápido, aponte para a pasta onde salvou os PDFs de amostra
    # Substitua pelo caminho real na sua máquina ou colab

    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "."

    # Se houver PDFs na pasta atual, roda o teste
    if any(f.endswith(".pdf") for f in os.listdir(folder_path)):
        batch_process(folder_path)
    else:
        print("Nenhum arquivo PDF encontrado na pasta atual para teste.")
