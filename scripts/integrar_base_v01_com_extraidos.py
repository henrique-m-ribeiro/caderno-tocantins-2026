#!/usr/bin/env python3
"""
Script para integrar dados extraídos dos PDFs na Base V01_REVISADA existente.
Mantém todas as colunas da V01 e adiciona os novos indicadores.

Autor: Claude Code
Data: 2026-01-28
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime
import re

def normalizar_nome_municipio(nome):
    """Normaliza nome de município para matching."""
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
    # Remover hífens, underscores e espaços extras
    nome = nome.replace('-', ' ').replace('_', ' ')
    nome = ' '.join(nome.split())
    return nome

def integrar_base_v01_com_extraidos():
    """Integra dados extraídos na base V01."""

    print("=" * 80)
    print("INTEGRAÇÃO BASE V01 + DADOS EXTRAÍDOS DOS PDFs")
    print("=" * 80)

    # 1. Carregar base V01
    print("\n📁 Carregando Base V01_REVISADA...")
    v01 = pd.read_excel('dados/finais/BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx')
    print(f"  ✅ {v01.shape[0]} municípios × {v01.shape[1]} colunas")

    # 2. Carregar dados extraídos (JSONs)
    print("\n📁 Carregando dados extraídos dos JSONs v9...")
    json_dir = Path("dados/brutos/extraidos-perfis")
    json_files = sorted(json_dir.glob("*_v9.json"))

    # Consolidar JSONs em DataFrame
    dados_extraidos = []
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            row = {'municipio_pdf': json_file.stem.replace('_v9', '')}
            row.update(data.get('indicadores', {}))
            dados_extraidos.append(row)

    df_extraidos = pd.DataFrame(dados_extraidos)
    print(f"  ✅ {len(df_extraidos)} municípios × {len(df_extraidos.columns)} colunas")

    # 3. Normalizar nomes para matching
    print("\n🔄 Normalizando nomes de municípios...")
    v01['nome_normalizado'] = v01['terr_nome'].apply(normalizar_nome_municipio)
    df_extraidos['nome_normalizado'] = df_extraidos['municipio_pdf'].apply(normalizar_nome_municipio)

    # 4. Fazer merge (left join para manter todos os municípios da V01)
    print("\n🔗 Fazendo merge dos dados...")
    df_integrado = v01.merge(
        df_extraidos.drop(columns=['municipio_pdf']),
        on='nome_normalizado',
        how='left'
    )

    # Remover coluna auxiliar
    df_integrado = df_integrado.drop(columns=['nome_normalizado'])

    print(f"  ✅ Base integrada: {df_integrado.shape[0]} municípios × {df_integrado.shape[1]} colunas")

    # 5. Estatísticas de integração
    print("\n📊 ESTATÍSTICAS DA INTEGRAÇÃO:")

    # Quantos municípios da V01 receberam dados dos PDFs
    novos_indicadores = [col for col in df_integrado.columns if col not in v01.columns]
    print(f"  Total de colunas na V01: {len(v01.columns)}")
    print(f"  Novos indicadores adicionados: {len(novos_indicadores)}")
    print(f"  Total de colunas na base integrada: {len(df_integrado.columns)}")

    # Contar municípios com dados
    municipios_com_dados = df_integrado[novos_indicadores].notna().any(axis=1).sum()
    print(f"\n  Municípios com dados dos PDFs: {municipios_com_dados}/{len(df_integrado)}")
    print(f"  Municípios sem dados dos PDFs: {len(df_integrado) - municipios_com_dados}")

    # Indicadores por município (apenas novos)
    ind_por_mun = df_integrado[novos_indicadores].notna().sum(axis=1)
    print(f"\n  Novos indicadores por município:")
    print(f"    Média: {ind_por_mun[ind_por_mun > 0].mean():.1f}")
    print(f"    Mediana: {ind_por_mun[ind_por_mun > 0].median():.0f}")
    print(f"    Mínimo: {ind_por_mun[ind_por_mun > 0].min():.0f}")
    print(f"    Máximo: {ind_por_mun.max():.0f}")

    # 6. Identificar municípios sem dados
    municipios_sem_dados = df_integrado[ind_por_mun == 0]['terr_nome'].tolist()
    if municipios_sem_dados:
        print(f"\n⚠️  MUNICÍPIOS SEM DADOS DOS PDFs ({len(municipios_sem_dados)}):")
        for mun in municipios_sem_dados:
            print(f"    - {mun}")

    # 7. Salvar base integrada
    print("\n💾 Salvando base integrada...")

    # CSV
    output_csv = Path("dados/finais/BASE_DADOS_TOCANTINS_V02.csv")
    df_integrado.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"  ✅ CSV: {output_csv}")

    # Excel
    output_excel = Path("dados/finais/BASE_DADOS_TOCANTINS_V02.xlsx")
    df_integrado.to_excel(output_excel, index=False, engine='openpyxl')
    print(f"  ✅ Excel: {output_excel}")

    # 8. Gerar novos metadados
    print("\n📝 Gerando metadados dos novos indicadores...")

    # Carregar metadados existentes
    metadados_v01 = pd.read_excel('dados/finais/METADADOS_BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx')

    # Criar metadados para novos indicadores
    novos_metadados = []

    # Categorizar indicadores
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
    }

    for indicador in novos_indicadores:
        # Identificar categoria
        categoria = None
        for key, info in categorias.items():
            if key in indicador.lower():
                categoria = info
                break

        if not categoria:
            categoria = {'dimensao': 'Outros', 'fonte': 'SEPLAN-TO', 'unidade': 'N/A'}

        # Extrair ano do nome do indicador
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

    # Criar DataFrame com novos metadados
    df_novos_metadados = pd.DataFrame(novos_metadados)

    # Concatenar com metadados existentes
    metadados_integrados = pd.concat([metadados_v01, df_novos_metadados], ignore_index=True)

    # Salvar metadados integrados
    output_metadados = Path("dados/finais/METADADOS_BASE_DADOS_TOCANTINS_V02.xlsx")
    metadados_integrados.to_excel(output_metadados, index=False, engine='openpyxl')
    print(f"  ✅ Metadados integrados: {output_metadados}")
    print(f"     Total de indicadores documentados: {len(metadados_integrados)}")
    print(f"     Novos indicadores documentados: {len(df_novos_metadados)}")

    # 9. Resumo final
    print("\n" + "=" * 80)
    print("\n✅ INTEGRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("\n📊 RESUMO:")
    print(f"  Base V01 (original):       {v01.shape[0]} municípios × {v01.shape[1]} indicadores")
    print(f"  Novos indicadores:         +{len(novos_indicadores)} indicadores")
    print(f"  Base V02 (integrada):      {df_integrado.shape[0]} municípios × {df_integrado.shape[1]} indicadores")
    print(f"  Metadados V02:             {len(metadados_integrados)} indicadores documentados")

    print("\n📁 ARQUIVOS GERADOS:")
    print(f"  ✅ {output_csv}")
    print(f"  ✅ {output_excel}")
    print(f"  ✅ {output_metadados}")

    print("\n" + "=" * 80)

    return df_integrado, metadados_integrados

if __name__ == "__main__":
    df_integrado, metadados = integrar_base_v01_com_extraidos()
