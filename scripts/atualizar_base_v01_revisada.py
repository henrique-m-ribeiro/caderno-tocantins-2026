#!/usr/bin/env python3
"""
Script para ATUALIZAR a base V01_REVISADA existente com dados extraídos dos PDFs.
Sobrescreve os arquivos originais mantendo sua estrutura.

Autor: Claude Code
Data: 2026-01-28
"""

import pandas as pd
import json
from pathlib import Path
import re

# Mapeamento manual para casos problemáticos
MAPEAMENTO_NOMES = {
    # Casos com sufixo "do Tocantins" - PDFs incluem o sufixo
    'Aliança do Tocantins': 'alianca_do_tocantins',
    'Aurora do Tocantins': 'aurora_do_tocantins',
    'Axixá do Tocantins': 'axixa_do_tocantins',
    'Bom Jesus do Tocantins': 'bom_jesus_do_tocantins',
    'Brasilândia do Tocantins': 'brasilandia_do_tocantins',
    'Buriti do Tocantins': 'buriti_do_tocantins',
    'Cariri do Tocantins': 'cariri_do_tocantins',
    'Jaú do Tocantins': 'jau_do_tocantins',
    'Palmeiras do Tocantins': 'palmeiras_do_tocantins',
    'Paraíso do Tocantins': 'paraiso_do_tocantins',
    'Porto Alegre do Tocantins': 'porto_alegre_do_tocantins',
    'Santa Maria do Tocantins': 'santa_maria_do_tocantins',
    'Santa Rita do Tocantins': 'santa_rita_do_tocantins',
    'Santa Rosa do Tocantins': 'santa_rosa_do_tocantins',
    'Santa Tereza do Tocantins': 'santa_tereza_do_tocantins',
    'São Bento do Tocantins': 'sao_bento_do_tocantins',
    'São Félix do Tocantins': 'sao_felix_do_tocantins',
    'São Miguel do Tocantins': 'sao_miguel_do_tocantins',
    'São Salvador do Tocantins': 'sao_salvador_do_tocantins',
    'São Sebastião do Tocantins': 'sao_sebastiao_do_tocantins',
    'Sítio Novo do Tocantins': 'sitio_novo_do_tocantins',
    'Taipas do Tocantins': 'taipas_do_tocantins',

    'Santa Terezinha do Tocantins': 'santa_terezinha_do_tocantins',
    'São Valério': 'sao_valerio_da_natividade',

    # PDFs com nome de arquivo diferente
    'Bandeirantes do Tocantins': 'bandeirantes_do_tocantins',
    'Barra do Ouro': 'barra_do_ouro',
    'Bernardo Sayão': 'bernardo_sayao',
    'Muricilândia': 'muricilandia_perfeil',
    
    # Casos especiais
    'Lagoa do Tocantins': 'lagoa_do_tocantins',
    'Ponte Alta do Tocantins': 'ponte_alta_do_tocantins',

    # Casos com apóstrofo no nome
    "Pau D'Arco": 'pau_d_arco',

    # Casos sem PDF
    'Cachoeirinha': None,
    'Tocantins': None,
}

def normalizar_nome(nome):
    """Normaliza nome removendo acentos e convertendo para minúsculas."""
    nome = str(nome).lower().strip()

    # Remover acentos
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c'
    }
    for a, b in acentos.items():
        nome = nome.replace(a, b)

    # Remover sufixo "do tocantins" e variações
    nome = re.sub(r'\s+do\s+tocantins$', '', nome)
    nome = re.sub(r'\s+da\s+tocantins$', '', nome)

    # Remover hífens e normalizar espaços
    nome = nome.replace('-', ' ')
    nome = ' '.join(nome.split())

    # Converter para formato de arquivo (underscores)
    nome = nome.replace(' ', '_')

    return nome

def atualizar_base_v01():
    """Atualiza BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx com dados extraídos."""

    print("=" * 80)
    print("ATUALIZAÇÃO DA BASE V01_REVISADA")
    print("=" * 80)

    # 1. Carregar base V01
    print("\n📁 Carregando BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx...")
    v01_path = Path('dados/finais/BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx')
    v01 = pd.read_excel(v01_path)
    colunas_originais = v01.columns.tolist()
    print(f"  ✅ {v01.shape[0]} linhas × {v01.shape[1]} colunas originais")

    # 2. Criar índice de JSONs por nome normalizado
    print("\n📁 Indexando JSONs extraídos...")
    json_dir = Path("dados/brutos/extraidos-perfis")
    json_index = {}

    for json_file in json_dir.glob("*_v9.json"):
        nome_base = json_file.stem.replace('_v9', '')
        json_index[nome_base] = json_file

    print(f"  ✅ {len(json_index)} JSONs indexados")

    # 3. Preparar dados extraídos por município
    print("\n🔗 Associando dados aos municípios...")

    novos_indicadores_dict = {}  # {municipio: {indicador: valor}}
    todos_indicadores = set()

    municipios_processados = 0
    municipios_nao_encontrados = []

    for idx, row in v01.iterrows():
        nome_municipio = row['terr_nome']

        # Tentar mapeamento manual primeiro
        if nome_municipio in MAPEAMENTO_NOMES:
            nome_arquivo = MAPEAMENTO_NOMES[nome_municipio]
            if nome_arquivo is None:  # Estado consolidado
                continue
        else:
            # Normalizar automaticamente
            nome_arquivo = normalizar_nome(nome_municipio)

        # Buscar JSON correspondente
        json_path = json_index.get(nome_arquivo)

        if json_path and json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                indicadores = data.get('indicadores', {})
                novos_indicadores_dict[nome_municipio] = indicadores
                todos_indicadores.update(indicadores.keys())
                municipios_processados += 1
        else:
            municipios_nao_encontrados.append((nome_municipio, nome_arquivo))

    print(f"  ✅ {municipios_processados} municípios associados")
    print(f"  ✅ {len(todos_indicadores)} indicadores únicos identificados")

    if municipios_nao_encontrados:
        print(f"\n  ⚠️  {len(municipios_nao_encontrados)} municípios sem dados:")
        for mun, arquivo in municipios_nao_encontrados[:5]:
            print(f"      - {mun} (buscado: {arquivo})")
        if len(municipios_nao_encontrados) > 5:
            print(f"      ... e mais {len(municipios_nao_encontrados) - 5}")

    # 4. Adicionar colunas dos novos indicadores
    print("\n📊 Adicionando novos indicadores à base...")

    # Ordenar indicadores alfabeticamente
    novos_indicadores_ordenados = sorted(todos_indicadores)

    # Criar DataFrame com novos indicadores
    for indicador in novos_indicadores_ordenados:
        v01[indicador] = None

        # Preencher valores
        for idx, row in v01.iterrows():
            nome_municipio = row['terr_nome']
            if nome_municipio in novos_indicadores_dict:
                valor = novos_indicadores_dict[nome_municipio].get(indicador)
                if valor is not None:
                    v01.at[idx, indicador] = valor

    print(f"  ✅ {len(novos_indicadores_ordenados)} novos indicadores adicionados")
    print(f"  ✅ Base atualizada: {v01.shape[0]} linhas × {v01.shape[1]} colunas")

    # 5. Salvar base atualizada (SOBRESCREVENDO V01_REVISADA)
    print("\n💾 Salvando BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx...")
    v01.to_excel(v01_path, index=False, engine='openpyxl')
    print(f"  ✅ Arquivo atualizado: {v01_path}")

    # 6. Atualizar metadados
    print("\n📝 Atualizando METADADOS_BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx...")

    metadados_path = Path('dados/finais/METADADOS_BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx')
    metadados = pd.read_excel(metadados_path)

    # Identificar quais indicadores são novos
    codigos_existentes = set(metadados['codigo'].tolist())
    novos_indicadores_meta = [ind for ind in novos_indicadores_ordenados
                               if ind not in codigos_existentes]

    # Criar metadados para novos indicadores
    categorias = {
        'idhm': {'dimensao': 'IDH', 'fonte': 'PNUD/Atlas Brasil', 'unidade': 'Índice (0-1)'},
        'pop': {'dimensao': 'Demografia', 'fonte': 'IBGE - Censo', 'unidade': 'Habitantes'},
        'densidade': {'dimensao': 'Demografia', 'fonte': 'IBGE', 'unidade': 'hab/km²'},
        'taxa_urbanizacao': {'dimensao': 'Demografia', 'fonte': 'IBGE - Censo', 'unidade': '%'},
        'pib': {'dimensao': 'Economia', 'fonte': 'IBGE - Contas Regionais', 'unidade': 'R$ (mil)'},
        'vab': {'dimensao': 'Economia', 'fonte': 'IBGE - Contas Regionais', 'unidade': 'R$ (mil)'},
        'emprego': {'dimensao': 'Trabalho', 'fonte': 'CAGED/MTE', 'unidade': 'Vínculos'},
        'alfabetizacao': {'dimensao': 'Educação', 'fonte': 'IBGE - Censo', 'unidade': '%'},
        'ideb': {'dimensao': 'Educação', 'fonte': 'INEP', 'unidade': 'Nota (0-10)'},
        'saneamento': {'dimensao': 'Saneamento', 'fonte': 'IBGE - Censo', 'unidade': '%'},
        'agua': {'dimensao': 'Saneamento', 'fonte': 'IBGE - Censo', 'unidade': '%'},
        'esgoto': {'dimensao': 'Saneamento', 'fonte': 'IBGE - Censo', 'unidade': '%'},
        'lixo': {'dimensao': 'Saneamento', 'fonte': 'IBGE - Censo', 'unidade': '%'},
        'fpm': {'dimensao': 'Finanças Públicas', 'fonte': 'Tesouro Nacional', 'unidade': 'R$'},
        'icms': {'dimensao': 'Finanças Públicas', 'fonte': 'SEFAZ-TO', 'unidade': 'R$'},
        'ipva': {'dimensao': 'Finanças Públicas', 'fonte': 'SEFAZ-TO', 'unidade': 'R$'},
        'fundeb': {'dimensao': 'Finanças Públicas', 'fonte': 'Tesouro Nacional', 'unidade': 'R$'},
        'itr': {'dimensao': 'Finanças Públicas', 'fonte': 'Tesouro Nacional', 'unidade': 'R$'},
        'transferencias': {'dimensao': 'Finanças Públicas', 'fonte': 'Tesouro Nacional', 'unidade': 'R$'},
        'estabelecimentos': {'dimensao': 'Saúde', 'fonte': 'DATASUS/CNES', 'unidade': 'Unidades'},
        'leitos': {'dimensao': 'Saúde', 'fonte': 'DATASUS/CNES', 'unidade': 'Leitos'},
    }

    novos_metadados = []
    for indicador in novos_indicadores_meta:
        # Identificar categoria
        categoria = None
        for key, info in categorias.items():
            if key in indicador.lower():
                categoria = info
                break

        if not categoria:
            categoria = {'dimensao': 'Outros', 'fonte': 'SEPLAN-TO', 'unidade': 'N/A'}

        # Extrair ano
        ano_match = re.search(r'_(\d{4})$', indicador)
        ano = ano_match.group(1) if ano_match else '2024'

        meta = {
            'codigo': indicador,
            'nome_curto': indicador.replace('_', ' ').title(),
            'descricao': f'Indicador extraído do Perfil Socioeconômico SEPLAN-TO 2024',
            'tipo_dado': 'Numérico',
            'dimensao': categoria['dimensao'],
            'unidade': categoria['unidade'],
            'fonte': f"SEPLAN-TO - Perfil Socioeconômico 2024 (via {categoria['fonte']})",
            'ano_referencia': ano,
            'data_coleta': '2026-01-28',
            'metodo_coleta': 'Extração automatizada via pdfplumber (Extrator v9)',
            'endpoint_atualizacao': 'https://www.to.gov.br/seplan/perfis-socioeconomicos',
            'periodicidade_atualizacao': 'Anual',
            'observacoes': 'Extraído dos Perfis Socioeconômicos Municipais (8ª Edição, Dez/2024)',
            'limitacoes': 'Disponibilidade depende da presença do dado no PDF original'
        }
        novos_metadados.append(meta)

    # Adicionar novos metadados
    if novos_metadados:
        df_novos_metadados = pd.DataFrame(novos_metadados)
        metadados = pd.concat([metadados, df_novos_metadados], ignore_index=True)

        # Salvar metadados atualizados
        metadados.to_excel(metadados_path, index=False, engine='openpyxl')
        print(f"  ✅ {len(novos_metadados)} novos metadados adicionados")
        print(f"  ✅ Arquivo atualizado: {metadados_path}")

    # 7. Resumo final
    print("\n" + "=" * 80)
    print("\n✅ ATUALIZAÇÃO CONCLUÍDA COM SUCESSO!")
    print("\n📊 RESUMO:")
    print(f"  Indicadores originais (V01):    {len(colunas_originais)}")
    print(f"  Novos indicadores adicionados:  +{len(novos_indicadores_ordenados)}")
    print(f"  Total de indicadores (V01):     {len(v01.columns)}")
    print(f"  Municípios com novos dados:     {municipios_processados}/{len(v01)}")
    print(f"  Total de metadados:             {len(metadados)}")

    print("\n📁 ARQUIVOS ATUALIZADOS:")
    print(f"  ✅ BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx")
    print(f"  ✅ METADADOS_BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx")

    print("\n" + "=" * 80)

    return v01, metadados

if __name__ == "__main__":
    v01_atualizada, metadados = atualizar_base_v01()
