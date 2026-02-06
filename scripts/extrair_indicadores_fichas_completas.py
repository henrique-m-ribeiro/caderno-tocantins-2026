#!/usr/bin/env python3
"""
Script ATUALIZADO para extrair indicadores das FICHAS COMPLETAS (Deepseek V3)
Localização: parte-iii-fichas-municipais/deepseek-v3/fichas-completas/
Formato: Fichas de 15-25 páginas com análise SWOT, resumo executivo, 9 dimensões
"""

import os
import re
import json
from collections import defaultdict
from pathlib import Path

# Diretório das fichas COMPLETAS (Deepseek V3)
FICHAS_DIR = Path("/home/user/caderno-tocantins-2026/parte-iii-fichas-municipais/deepseek-v3/fichas-completas")
OUTPUT_DIR = Path("/home/user/caderno-tocantins-2026/analises/fase-1-1-agregacao-municipal")

def extrair_nome_e_codigo(filepath):
    """Extrai nome do município e código IBGE do cabeçalho"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(2000)  # Lê primeiras linhas

        # Padrão: # **ANÁLISE SOCIOECONÔMICA \- NOME DO MUNICÍPIO**
        # O hífen pode estar escapado com backslash
        match_nome = re.search(r'#\s*\*\*AN[ÁA]LISE SOCIOECON[ÔO]MICA\s*\\?[-–]\s*([A-ZÀ-Ú\s]+)\*\*', content, re.IGNORECASE)
        nome = match_nome.group(1).strip() if match_nome else None

        # Código IBGE
        match_codigo = re.search(r'C[óo]digo IBGE:\s*(\d+)', content)
        codigo_ibge = match_codigo.group(1) if match_codigo else None

        return nome, codigo_ibge

def extrair_dados_fundamentais(content):
    """Extrai tabela de dados fundamentais"""
    dados = {}

    # Encontra a seção "DADOS FUNDAMENTAIS"
    match_section = re.search(r'##\s*\*\*📊 DADOS FUNDAMENTAIS\*\*\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if not match_section:
        return dados

    tabela = match_section.group(1)

    # Extrai linhas da tabela markdown
    # Formato: | Indicador | Valor | Observação |
    for line in tabela.split('\n'):
        if '|' in line and not line.strip().startswith('|:'):  # Pula separadores
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                indicador = parts[0]
                valor = parts[1]

                # População
                if 'População' in indicador and '2022' in indicador:
                    pop_match = re.search(r'([\d.]+)', valor.replace('.', ''))
                    if pop_match:
                        dados['populacao_2022'] = int(pop_match.group(1))

                # Área
                if 'Área Territorial' in indicador or 'Área territorial' in indicador:
                    area_match = re.search(r'([\d.]+)', valor.replace('.', '').replace(',', '.'))
                    if area_match:
                        try:
                            dados['area_km2'] = float(area_match.group(1))
                        except:
                            dados['area_km2'] = valor

                # PIB Total
                if 'PIB Total' in indicador:
                    pib_match = re.search(r'R\$\s*([\d.,]+)', valor)
                    if pib_match:
                        dados['pib_total_2021'] = pib_match.group(1)

                # PIB per capita
                if 'PIB per capita' in indicador:
                    pibpc_match = re.search(r'R\$\s*([\d.,]+)', valor)
                    if pibpc_match:
                        dados['pib_per_capita_2021'] = pibpc_match.group(1)

                # IDHM
                if 'IDHM' in indicador and '2010' in indicador:
                    idhm_match = re.search(r'(0[,.]?\d+)', valor.replace(',', '.'))
                    if idhm_match:
                        dados['idhm_2010'] = idhm_match.group(1)

                # Urbanização
                if 'Taxa de Urbanização' in indicador or 'Urbanização' in indicador:
                    urb_match = re.search(r'([\d,]+)%', valor)
                    if urb_match:
                        dados['taxa_urbanizacao'] = urb_match.group(1).replace(',', '.') + '%'

    return dados

def extrair_resumo_executivo(content):
    """Extrai o resumo executivo"""
    match = re.search(r'##\s*\*\*📋 RESUMO EXECUTIVO\*\*\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if match:
        resumo = match.group(1).strip()
        # Limita a 500 caracteres para o JSON
        return resumo[:500] + '...' if len(resumo) > 500 else resumo
    return None

def extrair_swot(content):
    """Extrai análise SWOT"""
    swot = {'forcas': [], 'fraquezas': [], 'oportunidades': [], 'ameacas': []}

    # Encontra seção SWOT
    match_swot = re.search(r'##\s*\*\*🎯 AN[ÁA]LISE SWOT\*\*\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if not match_swot:
        return swot

    swot_text = match_swot.group(1)

    # Extrai Forças
    match_forcas = re.search(r'###\s*\*\*FOR[ÇC]AS.*?\*\*\s*\n(.*?)(?=\n###|\Z)', swot_text, re.DOTALL)
    if match_forcas:
        forcas_text = match_forcas.group(1)
        swot['forcas'] = [f.strip() for f in re.findall(r'\*\s+([^\*\n]+)', forcas_text)]

    # Extrai Fraquezas
    match_fraquezas = re.search(r'###\s*\*\*FRAQUEZAS.*?\*\*\s*\n(.*?)(?=\n###|\Z)', swot_text, re.DOTALL)
    if match_fraquezas:
        fraquezas_text = match_fraquezas.group(1)
        swot['fraquezas'] = [f.strip() for f in re.findall(r'\*\s+([^\*\n]+)', fraquezas_text)]

    # Extrai Oportunidades
    match_opor = re.search(r'###\s*\*\*OPORTUNIDADES.*?\*\*\s*\n(.*?)(?=\n###|\Z)', swot_text, re.DOTALL)
    if match_opor:
        opor_text = match_opor.group(1)
        swot['oportunidades'] = [f.strip() for f in re.findall(r'\*\s+([^\*\n]+)', opor_text)]

    # Extrai Ameaças
    match_ameacas = re.search(r'###\s*\*\*AMEA[ÇC]AS.*?\*\*\s*\n(.*?)(?=\n###|\Z)', swot_text, re.DOTALL)
    if match_ameacas:
        ameacas_text = match_ameacas.group(1)
        swot['ameacas'] = [f.strip() for f in re.findall(r'\*\s+([^\*\n]+)', ameacas_text)]

    return swot

def identificar_microrregiao(nome_municipio):
    """Identifica a microrregião do município"""
    # Mapeamento conhecido das microrregiões (baseado no mapeamento anterior)
    mapeamento = {
        # Porto Nacional
        'PALMAS': 'Porto Nacional',
        'PORTO NACIONAL': 'Porto Nacional',
        'PEDRO AFONSO': 'Porto Nacional',
        'MONTE DO CARMO': 'Porto Nacional',
        'LAJEADO': 'Porto Nacional',
        'TOCANTINIA': 'Porto Nacional',
        'SILVANOPOLIS': 'Porto Nacional',
        'APARECIDA DO RIO NEGRO': 'Porto Nacional',
        'BOM JESUS DO TOCANTINS': 'Porto Nacional',
        'IPUEIRAS': 'Porto Nacional',
        'SANTA MARIA DO TOCANTINS': 'Porto Nacional',

        # Araguaína
        'ARAGUAINA': 'Araguaína',
        'ARAGUANA': 'Araguaína',
        'ARAGOMINAS': 'Araguaína',
        'ARAPOEMA': 'Araguaína',
        'BABACULANDIA': 'Araguaína',
        'BANDEIRANTES DO TOCANTINS': 'Araguaína',
        'CARMOLANDIA': 'Araguaína',
        'FILADELFIA': 'Araguaína',
        'MURICILANDIA': 'Araguaína',
        'NOVA OLINDA': 'Araguaína',
        'PALMEIRANTE': 'Araguaína',
        'PAU D ARCO': 'Araguaína',
        'PIRAQUE': 'Araguaína',
        'SANTA FE DO ARAGUAIA': 'Araguaína',
        'WANDERLANDIA': 'Araguaína',
        'XAMBIOA': 'Araguaína',

        # Bico do Papagaio
        'AGUIARNOPOLIS': 'Bico do Papagaio',
        'ANANAS': 'Bico do Papagaio',
        'ANGICO': 'Bico do Papagaio',
        'ARAGUATINS': 'Bico do Papagaio',
        'AUGUSTINOPOLIS': 'Bico do Papagaio',
        'AXIXA DO TOCANTINS': 'Bico do Papagaio',
        'BURITI DO TOCANTINS': 'Bico do Papagaio',
        'CACHOEIRINHA': 'Bico do Papagaio',
        'CARRASCO BONITO': 'Bico do Papagaio',
        'DARCINOPOLIS': 'Bico do Papagaio',
        'ESPERANTINA': 'Bico do Papagaio',
        'ITAGUATINS': 'Bico do Papagaio',
        'LUZINOPOLIS': 'Bico do Papagaio',
        'NAZARE': 'Bico do Papagaio',
        'PALMEIRAS DO TOCANTINS': 'Bico do Papagaio',
        'PRAIA NORTE': 'Bico do Papagaio',
        'RIACHINHO': 'Bico do Papagaio',
        'SAMPAIO': 'Bico do Papagaio',
        'SANTA TEREZINHA DO TOCANTINS': 'Bico do Papagaio',
        'SAO BENTO DO TOCANTINS': 'Bico do Papagaio',
        'SAO MIGUEL DO TOCANTINS': 'Bico do Papagaio',
        'SAO SEBASTIAO DO TOCANTINS': 'Bico do Papagaio',
        'SITIO NOVO DO TOCANTINS': 'Bico do Papagaio',
        'TOCANTINOPOLIS': 'Bico do Papagaio',

        # Gurupi
        'GURUPI': 'Gurupi',
        'ALIANCA DO TOCANTINS': 'Gurupi',
        'ALVORADA': 'Gurupi',
        'BREJINHO DE NAZARE': 'Gurupi',
        'CARIRI DO TOCANTINS': 'Gurupi',
        'FIGUEIROPOLIS': 'Gurupi',
        'JAU DO TOCANTINS': 'Gurupi',
        'PALMEIROPOLIS': 'Gurupi',
        'PEIXE': 'Gurupi',
        'SANTA RITA DO TOCANTINS': 'Gurupi',
        'SUCUPIRA': 'Gurupi',
        'SAO SALVADOR DO TOCANTINS': 'Gurupi',
        'TALISMA': 'Gurupi',

        # Miracema do Tocantins
        'MIRACEMA DO TOCANTINS': 'Miracema do Tocantins',
        'ABREULANDIA': 'Miracema do Tocantins',
        'ARAGUACEMA': 'Miracema do Tocantins',
        'BARROLANDIA': 'Miracema do Tocantins',
        'BERNARDO SAYAO': 'Miracema do Tocantins',
        'BRASILANDIA DO TOCANTINS': 'Miracema do Tocantins',
        'CASEARA': 'Miracema do Tocantins',
        'COLMEIA': 'Miracema do Tocantins',
        'COUTO MAGALHAES': 'Miracema do Tocantins',
        'GOIANORTE': 'Miracema do Tocantins',
        'GUARAI': 'Miracema do Tocantins',
        'JUARINA': 'Miracema do Tocantins',
        'MIRANORTE': 'Miracema do Tocantins',
        'PEQUIZEIRO': 'Miracema do Tocantins',
        'PRESIDENTE KENNEDY': 'Miracema do Tocantins',
        'RIO DOS BOIS': 'Miracema do Tocantins',
        'TABOCAO': 'Miracema do Tocantins',
        'TUPIRAMA': 'Miracema do Tocantins',
        'TUPIRATINS': 'Miracema do Tocantins',

        # Dianópolis
        'DIANOPOLIS': 'Dianópolis',
        'ALMAS': 'Dianópolis',
        'ARRAIAS': 'Dianópolis',
        'AURORA DO TOCANTINS': 'Dianópolis',
        'CHAPADA DA NATIVIDADE': 'Dianópolis',
        'COMBINADO': 'Dianópolis',
        'LAVANDEIRA': 'Dianópolis',
        'NATIVIDADE': 'Dianópolis',
        'NOVO ALEGRE': 'Dianópolis',
        'NOVO JARDIM': 'Dianópolis',
        'PARANA': 'Dianópolis',
        'PONTE ALTA DO BOM JESUS': 'Dianópolis',
        'PORTO ALEGRE DO TOCANTINS': 'Dianópolis',
        'RIO DA CONCEICAO': 'Dianópolis',
        'SANTA ROSA DO TOCANTINS': 'Dianópolis',
        'SAO VALERIO DA NATIVIDADE': 'Dianópolis',
        'TAGUATINGA': 'Dianópolis',
        'TAIPAS DO TOCANTINS': 'Dianópolis',

        # Jalapão
        'BARRA DO OURO': 'Jalapão',
        'CAMPOS LINDOS': 'Jalapão',
        'CENTENARIO': 'Jalapão',
        'GOIATINS': 'Jalapão',
        'ITACAJA': 'Jalapão',
        'ITAPIRATINS': 'Jalapão',
        'LAGOA DO TOCANTINS': 'Jalapão',
        'LIZARDA': 'Jalapão',
        'MATEIROS': 'Jalapão',
        'NOVO ACORDO': 'Jalapão',
        'PONTE ALTA DO TOCANTINS': 'Jalapão',
        'RECURSOLANDIA': 'Jalapão',
        'RIO SONO': 'Jalapão',
        'SANTA TEREZA DO TOCANTINS': 'Jalapão',
        'SAO FELIX DO TOCANTINS': 'Jalapão',

        # Rio Formoso
        'ARAGUACU': 'Rio Formoso',
        'CHAPADA DE AREIA': 'Rio Formoso',
        'CRISTALANDIA': 'Rio Formoso',
        'DUERE': 'Rio Formoso',
        'FORMOSO DO ARAGUAIA': 'Rio Formoso',
        'FATIMA': 'Rio Formoso',
        'LAGOA DA CONFUSAO': 'Rio Formoso',
        'NOVA ROSALANDIA': 'Rio Formoso',
        'OLIVEIRA DE FATIMA': 'Rio Formoso',
        'PARAISO DO TOCANTINS': 'Rio Formoso',
        'PIUM': 'Rio Formoso',
        'PUGMIL': 'Rio Formoso',
        'SANDOLANDIA': 'Rio Formoso',
    }

    # Normaliza nome para busca
    nome_norm = nome_municipio.upper().strip()
    return mapeamento.get(nome_norm, 'N/D')

def processar_ficha_completa(filepath):
    """Processa uma ficha completa do Deepseek V3"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extrai informações básicas
        nome, codigo_ibge = extrair_nome_e_codigo(filepath)
        if not nome:
            return None

        # Identifica microrregião
        microrregiao = identificar_microrregiao(nome)

        # Extrai dados
        dados = {
            'nome': nome,
            'codigo_ibge': codigo_ibge,
            'microrregiao': microrregiao,
            'arquivo_fonte': filepath.name
        }

        # Dados fundamentais
        dados.update(extrair_dados_fundamentais(content))

        # Resumo executivo
        dados['resumo_executivo'] = extrair_resumo_executivo(content)

        # SWOT
        dados['swot'] = extrair_swot(content)

        # Contagem de caracteres/linhas (indicador de extensão da análise)
        dados['tamanho_analise_linhas'] = content.count('\n')
        dados['tamanho_analise_caracteres'] = len(content)

        return dados

    except Exception as e:
        print(f"⚠️  Erro ao processar {filepath.name}: {e}")
        return None

def processar_todos_municipios():
    """Processa todas as fichas completas"""
    dados_por_microrregiao = defaultdict(list)
    total_processados = 0
    total_erros = 0

    fichas = sorted(FICHAS_DIR.glob("FICHA-MUNICIPAL-*-COMPLETA.md"))
    total_fichas = len(fichas)

    print(f"Processando {total_fichas} fichas completas...")
    print()

    for filepath in fichas:
        dados = processar_ficha_completa(filepath)

        if dados:
            microrregiao = dados['microrregiao']
            dados_por_microrregiao[microrregiao].append(dados)
            total_processados += 1
            print(f"✓ {dados['nome']} → {microrregiao}")
        else:
            total_erros += 1
            print(f"✗ Erro: {filepath.name}")

    print()
    print(f"Total: {total_processados} fichas processadas, {total_erros} erros")
    print()

    return dados_por_microrregiao

def gerar_tabela_comparativa(microrregiao, municipios):
    """Gera tabela markdown comparativa para uma microrregião"""

    md = f"# TABELA COMPARATIVA DETALHADA: MICRORREGIÃO DE {microrregiao.upper()}\n\n"
    md += f"**Total de Municípios:** {len(municipios)}\n"
    md += f"**Fonte:** Fichas Completas Deepseek V3 (15-25 páginas cada)\n\n"
    md += "---\n\n"

    # Tabela 1: Perfil Geral
    md += "## 1. PERFIL GERAL\n\n"
    md += "| Município | População<br>2022 | Área<br>(km²) | PIB Total<br>2021 (R$ mil) | PIB per capita<br>2021 (R$) | IDHM<br>2010 |\n"
    md += "|-----------|-------------------|---------------|----------------------------|-----------------------------|--------------|\n"

    for mun in sorted(municipios, key=lambda x: x.get('populacao_2022', 0), reverse=True):
        nome = mun.get('nome', '-')
        pop = mun.get('populacao_2022', '-')
        area = mun.get('area_km2', '-')
        pib = mun.get('pib_total_2021', '-')
        pibpc = mun.get('pib_per_capita_2021', '-')
        idhm = mun.get('idhm_2010', '-')

        # Formata população
        if isinstance(pop, int):
            pop_fmt = f"{pop:,}".replace(',', '.')
        else:
            pop_fmt = pop

        md += f"| {nome} | {pop_fmt} | {area} | {pib} | {pibpc} | {idhm} |\n"

    md += "\n---\n\n"

    # Tabela 2: Análise SWOT Consolidada
    md += "## 2. SWOT CONSOLIDADO DA MICRORREGIÃO\n\n"
    md += "### Principais Forças Identificadas (por município)\n\n"

    for mun in municipios:
        if mun.get('swot', {}).get('forcas'):
            md += f"**{mun['nome']}:**\n"
            for forca in mun['swot']['forcas'][:3]:  # Top 3
                md += f"- {forca[:200]}...\n" if len(forca) > 200 else f"- {forca}\n"
            md += "\n"

    md += "### Principais Fraquezas Identificadas\n\n"

    for mun in municipios:
        if mun.get('swot', {}).get('fraquezas'):
            md += f"**{mun['nome']}:**\n"
            for fraqueza in mun['swot']['fraquezas'][:3]:  # Top 3
                md += f"- {fraqueza[:200]}...\n" if len(fraqueza) > 200 else f"- {fraqueza}\n"
            md += "\n"

    md += "\n---\n\n"

    # Estatísticas
    md += "## 3. ESTATÍSTICAS DA MICRORREGIÃO\n\n"

    pop_total = sum(m.get('populacao_2022', 0) for m in municipios if isinstance(m.get('populacao_2022'), int))
    area_total = sum(float(m.get('area_km2', 0)) for m in municipios if isinstance(m.get('area_km2'), (int, float)))

    md += f"- **População Total:** {pop_total:,} habitantes\n".replace(',', '.')
    md += f"- **Área Total:** {area_total:,.2f} km²\n".replace(',', 'X').replace('.', ',').replace('X', '.')
    if pop_total > 0 and area_total > 0:
        densidade = pop_total / area_total
        md += f"- **Densidade Média:** {densidade:.2f} hab/km²\n"
    md += f"- **Número de Municípios:** {len(municipios)}\n"

    # Município maior e menor
    if municipios:
        maior = max(municipios, key=lambda x: x.get('populacao_2022', 0) if isinstance(x.get('populacao_2022'), int) else 0)
        menor = min((m for m in municipios if isinstance(m.get('populacao_2022'), int)),
                   key=lambda x: x.get('populacao_2022', 0), default=None)

        if maior:
            md += f"- **Município Mais Populoso:** {maior['nome']} ({maior.get('populacao_2022', 0):,} hab)\n".replace(',', '.')
        if menor:
            md += f"- **Município Menos Populoso:** {menor['nome']} ({menor.get('populacao_2022', 0):,} hab)\n".replace(',', '.')

    md += "\n---\n\n"

    return md

def main():
    """Função principal"""
    print("=" * 80)
    print("EXTRAÇÃO DE INDICADORES DAS FICHAS COMPLETAS (DEEPSEEK V3)")
    print("=" * 80)
    print()

    # Cria diretório de saída
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Processa todas as fichas
    dados = processar_todos_municipios()

    print("=" * 80)
    print(f"Total de microrregiões: {len(dados)}")
    print()

    # Gera tabelas comparativas
    for microrregiao, municipios in sorted(dados.items()):
        print(f"Gerando tabela: {microrregiao} ({len(municipios)} municípios)")

        # Gera markdown
        tabela_md = gerar_tabela_comparativa(microrregiao, municipios)

        # Salva arquivo
        nome_safe = microrregiao.upper().replace(' ', '-').replace('/', '-').replace('\\', '-')
        nome_arquivo = f"TABELA-COMPARATIVA-{nome_safe}-V2.md"
        output_path = OUTPUT_DIR / nome_arquivo

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(tabela_md)

        print(f"  ✓ Salvo: {output_path}")

    # Salva JSON
    json_path = OUTPUT_DIR / "dados-municipais-completos-deepseek-v3.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dict(dados), f, ensure_ascii=False, indent=2)

    print()
    print(f"✓ Dados JSON: {json_path}")
    print()
    print("=" * 80)
    print("PROCESSAMENTO CONCLUÍDO!")
    print("=" * 80)

if __name__ == '__main__':
    main()
