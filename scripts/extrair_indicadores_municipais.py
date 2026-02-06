#!/usr/bin/env python3
"""
Script para extrair indicadores municipais e agregar por microrregião
Gera tabelas comparativas em formato Markdown para revisão das fichas regionais
"""

import os
import re
import json
from collections import defaultdict
from pathlib import Path

# Diretório das fichas municipais
FICHAS_DIR = Path("/home/user/caderno-tocantins-2026/parte-iii-fichas-municipais/fichas")
OUTPUT_DIR = Path("/home/user/caderno-tocantins-2026/analises/fase-1-1-agregacao-municipal")

def extrair_valor_tabela(lines, indicador):
    """
    Extrai valor de uma tabela no formato:
    | Indicador | Valor |
    |-----------|-------|
    | Nome | 123 |
    """
    for i, line in enumerate(lines):
        if indicador in line and '|' in line:
            # Extrai o valor da linha (última coluna)
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                valor = parts[-1]
                # Limpa formatação (remove R$, mil, etc)
                valor_limpo = valor.replace('R$', '').replace('mil', '').replace(' ', '').strip()
                return valor_limpo
    return None

def extrair_microrregiao(filepath):
    """Extrai o nome da microrregião"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Microrregião' in line:
                match = re.search(r'\*\*Microrregião\*\*:\s*([^|]+)', line)
                if match:
                    return match.group(1).strip()
    return "N/D"

def extrair_indicadores(filepath):
    """Extrai todos os indicadores relevantes de uma ficha municipal"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    indicadores = {}

    # Extrai nome do município do cabeçalho
    if lines:
        match = re.match(r'#\s*([A-ZÀ-Ú\s\-]+)\s*-\s*FICHA', lines[0])
        if match:
            indicadores['nome'] = match.group(1).strip()

    # Busca por padrões de indicadores nas tabelas
    for i, line in enumerate(lines):
        # População 2022
        if 'População (2022)' in line or 'População 2022' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'População')
            if valor:
                try:
                    indicadores['populacao_2022'] = int(valor.replace('.', '').replace(',', ''))
                except:
                    indicadores['populacao_2022'] = valor

        # População 2010
        if 'População 2010' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'População 2010')
            if valor:
                try:
                    indicadores['populacao_2010'] = int(valor.replace('.', '').replace(',', ''))
                except:
                    indicadores['populacao_2010'] = valor

        # Área territorial
        if 'Área Territorial' in line or 'Área territorial' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'Área')
            if valor:
                try:
                    indicadores['area_km2'] = float(valor.replace('.', '').replace(',', '.'))
                except:
                    indicadores['area_km2'] = valor

        # PIB Total 2021
        if 'PIB Total' in line and '2021' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'PIB Total')
            if valor:
                indicadores['pib_total_2021'] = valor

        # PIB per capita 2021
        if 'PIB per capita' in line and '2021' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'PIB per capita')
            if valor:
                indicadores['pib_per_capita_2021'] = valor

        # IDHM 2010
        if 'IDHM (2010)' in line or 'IDHM 2010' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'IDHM')
            if valor:
                indicadores['idhm_2010'] = valor

        # Densidade demográfica
        if 'Densidade demográfica' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'Densidade')
            if valor:
                indicadores['densidade_2022'] = valor

        # Taxa de urbanização
        if 'Taxa de urbanização' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'urbanização')
            if valor:
                indicadores['taxa_urbanizacao_2022'] = valor

        # VAB Agropecuária 2021
        if 'VAB Agropecuária' in line and '2021' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'VAB Agropecuária')
            if valor:
                indicadores['vab_agropecuaria_2021'] = valor

        # VAB Indústria 2021
        if 'VAB Indústria' in line and '2021' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'VAB Indústria')
            if valor:
                indicadores['vab_industria_2021'] = valor

        # VAB Serviços 2021
        if 'VAB Serviços' in line and '2021' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'VAB Serviços')
            if valor:
                indicadores['vab_servicos_2021'] = valor

        # Emprego Formal 2023
        if 'Emprego Formal' in line and '2023' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'Emprego Formal')
            if valor:
                indicadores['emprego_formal_2023'] = valor

        # Taxa de alfabetização
        if 'Taxa de alfabetização 2022' in line:
            valor = extrair_valor_tabela(lines[i:i+5], 'alfabetização 2022')
            if valor:
                indicadores['taxa_alfabetizacao_2022'] = valor

    return indicadores

def processar_todos_municipios():
    """Processa todas as fichas municipais e agrupa por microrregião"""
    dados_por_microrregiao = defaultdict(list)

    for filepath in sorted(FICHAS_DIR.glob("FICHA-MUNICIPAL-*.md")):
        microrregiao = extrair_microrregiao(filepath)
        indicadores = extrair_indicadores(filepath)

        if indicadores.get('nome'):
            indicadores['microrregiao'] = microrregiao
            dados_por_microrregiao[microrregiao].append(indicadores)
            print(f"✓ Processado: {indicadores['nome']} ({microrregiao})")
        else:
            print(f"⚠ Não foi possível extrair nome de {filepath.name}")

    return dados_por_microrregiao

def gerar_tabela_comparativa(microrregiao, municipios):
    """Gera tabela markdown comparativa para uma microrregião"""

    md = f"# TABELA COMPARATIVA: MICRORREGIÃO DE {microrregiao.upper()}\n\n"
    md += f"**Total de Municípios:** {len(municipios)}\n\n"
    md += "---\n\n"

    # Tabela de dados demográficos
    md += "## 1. PERFIL DEMOGRÁFICO E TERRITORIAL\n\n"
    md += "| Município | População<br>2022 | População<br>2010 | Crescimento<br>2010-2022 | Área<br>(km²) | Densidade<br>(hab/km²) | Taxa<br>Urbanização |\n"
    md += "|-----------|-------------------|-------------------|--------------------------|---------------|------------------------|---------------------|\n"

    for mun in sorted(municipios, key=lambda x: x.get('populacao_2022', 0) if isinstance(x.get('populacao_2022'), int) else 0, reverse=True):
        nome = mun.get('nome', '-')
        pop_2022 = mun.get('populacao_2022', '-')
        pop_2010 = mun.get('populacao_2010', '-')

        # Calcula crescimento percentual
        crescimento = '-'
        if isinstance(pop_2022, int) and isinstance(pop_2010, int) and pop_2010 > 0:
            cresc_pct = ((pop_2022 - pop_2010) / pop_2010) * 100
            crescimento = f"{cresc_pct:+.1f}%"

        area = mun.get('area_km2', '-')
        densidade = mun.get('densidade_2022', '-')
        urbanizacao = mun.get('taxa_urbanizacao_2022', '-')

        # Formata valores
        if isinstance(pop_2022, int):
            pop_2022_fmt = f"{pop_2022:,}".replace(',', '.')
        else:
            pop_2022_fmt = pop_2022

        if isinstance(pop_2010, int):
            pop_2010_fmt = f"{pop_2010:,}".replace(',', '.')
        else:
            pop_2010_fmt = pop_2010

        if isinstance(area, float):
            area_fmt = f"{area:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        else:
            area_fmt = area

        md += f"| {nome} | {pop_2022_fmt} | {pop_2010_fmt} | {crescimento} | {area_fmt} | {densidade} | {urbanizacao} |\n"

    # Calcula totais/médias regionais
    md += "|**REGIONAL**|**Total/Média**|**Total**|**Variação**|-|-|-|\n"

    pop_total_2022 = sum(m.get('populacao_2022', 0) for m in municipios if isinstance(m.get('populacao_2022'), int))
    pop_total_2010 = sum(m.get('populacao_2010', 0) for m in municipios if isinstance(m.get('populacao_2010'), int))

    if pop_total_2010 > 0:
        cresc_regional = ((pop_total_2022 - pop_total_2010) / pop_total_2010) * 100
        md += f"|**{len(municipios)} municípios**|**{pop_total_2022:,}**.replace(',', '.')|**{pop_total_2010:,}**.replace(',', '.')|**{cresc_regional:+.1f}%**|-|-|-|\n"

    md += "\n---\n\n"

    # Tabela de dados econômicos
    md += "## 2. PERFIL ECONÔMICO\n\n"
    md += "| Município | PIB Total<br>2021 (R$ mil) | PIB per capita<br>2021 (R$) | IDHM<br>2010 | VAB Agro<br>(R$ mil) | VAB Indústria<br>(R$ mil) | VAB Serviços<br>(R$ mil) | Empregos<br>Formais 2023 |\n"
    md += "|-----------|----------------------------|-----------------------------|--------------|-----------------------|---------------------------|--------------------------|---------------------------|\n"

    for mun in sorted(municipios, key=lambda x: x.get('nome', '').upper()):
        nome = mun.get('nome', '-')
        pib_total = mun.get('pib_total_2021', '-')
        pib_pc = mun.get('pib_per_capita_2021', '-')
        idhm = mun.get('idhm_2010', '-')
        vab_agro = mun.get('vab_agropecuaria_2021', '-')
        vab_ind = mun.get('vab_industria_2021', '-')
        vab_serv = mun.get('vab_servicos_2021', '-')
        empregos = mun.get('emprego_formal_2023', '-')

        md += f"| {nome} | {pib_total} | {pib_pc} | {idhm} | {vab_agro} | {vab_ind} | {vab_serv} | {empregos} |\n"

    md += "\n---\n\n"

    # Tabela de educação
    md += "## 3. INDICADORES EDUCACIONAIS\n\n"
    md += "| Município | Taxa de Alfabetização<br>2022 (%) |\n"
    md += "|-----------|-----------------------------------|\n"

    for mun in sorted(municipios, key=lambda x: x.get('nome', '').upper()):
        nome = mun.get('nome', '-')
        alfab = mun.get('taxa_alfabetizacao_2022', '-')
        md += f"| {nome} | {alfab} |\n"

    md += "\n---\n\n"

    return md

def main():
    """Função principal"""
    print("=" * 80)
    print("EXTRAÇÃO DE INDICADORES MUNICIPAIS POR MICRORREGIÃO")
    print("=" * 80)
    print()

    # Cria diretório de saída
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Processa todos os municípios
    print("Processando fichas municipais...")
    print()
    dados = processar_todos_municipios()

    print()
    print("=" * 80)
    print(f"Total de microrregiões processadas: {len(dados)}")
    print()

    # Gera tabelas comparativas por microrregião
    for microrregiao, municipios in sorted(dados.items()):
        print(f"Gerando tabela comparativa: {microrregiao} ({len(municipios)} municípios)")

        # Gera markdown
        tabela_md = gerar_tabela_comparativa(microrregiao, municipios)

        # Salva arquivo (sanitiza nome removendo caracteres inválidos)
        nome_safe = microrregiao.upper().replace(' ', '-').replace('/', '-').replace('\\', '-')
        nome_arquivo = f"TABELA-COMPARATIVA-{nome_safe}.md"
        output_path = OUTPUT_DIR / nome_arquivo

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(tabela_md)

        print(f"  ✓ Salvo: {output_path}")

    # Salva também dados brutos em JSON para processamento posterior
    dados_json = {}
    for microrregiao, municipios in dados.items():
        dados_json[microrregiao] = municipios

    json_path = OUTPUT_DIR / "dados-municipais-agregados.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dados_json, f, ensure_ascii=False, indent=2)

    print()
    print(f"✓ Dados brutos salvos em: {json_path}")
    print()
    print("=" * 80)
    print("PROCESSAMENTO CONCLUÍDO!")
    print(f"Arquivos gerados em: {OUTPUT_DIR}")
    print("=" * 80)

if __name__ == '__main__':
    main()
