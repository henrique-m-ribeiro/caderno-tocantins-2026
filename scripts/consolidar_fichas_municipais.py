#!/usr/bin/env python3
"""
Script para consolidar as fichas municipais em um documento único com:
- Capa
- Apresentação
- Índice alfabético com números de página
- Todas as fichas municipais (139)
- Fontes e elaboração

Autor: Claude Code
Data: 2026-01-28
"""

import pandas as pd
from pathlib import Path
import re
from datetime import datetime


def gerar_capa():
    """Gera a capa do documento."""
    return """---
title: "Caderno Tocantins 2026 - Parte III"
subtitle: "Fichas Municipais"
author: "Sistema de Inteligência Territorial"
date: "Janeiro de 2026"
---

<div style="text-align: center; margin-top: 30vh;">

# CADERNO TOCANTINS 2026

## PARTE III
## FICHAS MUNICIPAIS

### 139 Municípios do Estado do Tocantins

---

**Sistema de Inteligência Territorial**
**Janeiro de 2026**

</div>

\\newpage

"""


def gerar_apresentacao():
    """Gera a apresentação do documento."""
    return """# APRESENTAÇÃO

Este documento constitui a **Parte III** do **Caderno Tocantins 2026**, apresentando fichas detalhadas de cada um dos **139 municípios** do Estado do Tocantins.

## Objetivo

As fichas municipais foram elaboradas para subsidiar com informações precisas e análises contextualizadas a campanha da Senadora Dorinha Seabra ao governo do Estado do Tocantins. Cada ficha oferece uma visão integrada do município em múltiplas dimensões, facilitando:

- **Preparação para eventos locais**: Dados essenciais para discursos e entrevistas
- **Elaboração de propostas territorializadas**: Diretrizes específicas para cada realidade municipal
- **Compreensão das prioridades locais**: Desafios e oportunidades identificados
- **Articulação política**: Pontos fortes e parcerias estratégicas

## Estrutura das Fichas

Cada ficha municipal possui **2 páginas** organizadas da seguinte forma:

**PÁGINA 1 - Visão Geral e Dimensões Prioritárias:**
- **Dados Básicos**: População, PIB, IDHM, Área territorial
- **Síntese Estratégica**: Pontos fortes, desafios prioritários e oportunidades
- **Dimensão 1 - Dados Sociais e Demográficos**: População, IDHM e componentes, densidade, urbanização
- **Dimensão 2 - Economia**: PIB, VAB setorial, emprego formal
- **Dimensão 3 - Educação**: Taxa de alfabetização, IDEB
- **Dimensão 4 - Saúde e Saneamento**: Estabelecimentos de saúde, infraestrutura de saneamento

**PÁGINA 2 - Dimensões Complementares e Análise Integrada:**
- **Dimensão 5 - Agropecuária e Desenvolvimento Rural**: VAB agropecuária, vocações produtivas
- **Dimensão 6 - Finanças Públicas**: Transferências, FPM, ICMS, IPVA, FUNDEB, ITR
- **Análise Integrada**: Diagnóstico sistêmico conectando as dimensões
- **Diretrizes para o Plano de Governo**: Ações e políticas públicas estaduais

## Fontes de Dados

Os indicadores apresentados nas fichas municipais foram extraídos de fontes oficiais:

- **SEPLAN-TO**: Perfil Socioeconômico dos Municípios do Tocantins 2024 (8ª Edição)
- **IBGE**: Instituto Brasileiro de Geografia e Estatística
- **INEP**: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira
- **DATASUS**: Departamento de Informática do Sistema Único de Saúde
- **Tesouro Nacional**: Sistema de Informações Contábeis e Fiscais do Setor Público Brasileiro

## Como Utilizar Este Documento

1. **Consulta Rápida**: Use o índice alfabético para localizar rapidamente qualquer município
2. **Preparação para Eventos**: Leia a Síntese Estratégica para mensagens-chave
3. **Aprofundamento**: Analise as dimensões específicas conforme o tema do evento
4. **Elaboração de Propostas**: Consulte as Diretrizes para o Plano de Governo

## Atualização

Este documento reflete dados disponíveis até janeiro de 2026. Para informações mais recentes ou complementares, consulte as fontes oficiais listadas.

---

**Elaboração**: Caderno Tocantins 2026 - Sistema de Inteligência Territorial
**Data**: Janeiro de 2026

\\newpage

"""


def gerar_indice(fichas_paths, pagina_inicial=5):
    """Gera o índice alfabético com números de página."""

    # Extrair nomes dos municípios dos arquivos
    municipios = []
    for path in sorted(fichas_paths):
        # Extrair nome do arquivo FICHA-MUNICIPAL-NOME.md
        nome = path.stem.replace('FICHA-MUNICIPAL-', '').replace('-', ' ').title()
        municipios.append(nome)

    # Calcular páginas (cada ficha tem 2 páginas)
    indice_md = """# ÍNDICE ALFABÉTICO DOS MUNICÍPIOS

"""

    pagina_atual = pagina_inicial
    for i, municipio in enumerate(sorted(municipios), 1):
        indice_md += f"{i:3d}. {municipio:<50s} .................... pág. {pagina_atual}\n"
        pagina_atual += 2  # Cada ficha tem 2 páginas

    indice_md += "\n\\newpage\n\n"

    return indice_md


def consolidar_fichas(fichas_dir='parte-iii-fichas-municipais/fichas',
                      output_path='parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.md'):
    """Consolida todas as fichas em um documento único."""

    print("=" * 80)
    print("CONSOLIDAÇÃO DAS FICHAS MUNICIPAIS")
    print("=" * 80)
    print()

    fichas_dir = Path(fichas_dir)
    output_path = Path(output_path)

    # Listar todas as fichas
    fichas_paths = sorted(fichas_dir.glob('FICHA-MUNICIPAL-*.md'))

    print(f"📁 Diretório de fichas: {fichas_dir}")
    print(f"📄 Total de fichas encontradas: {len(fichas_paths)}")
    print(f"💾 Arquivo de saída: {output_path}")
    print()

    # Iniciar documento consolidado
    documento = []

    # 1. Capa
    print("1️⃣  Gerando capa...")
    documento.append(gerar_capa())

    # 2. Apresentação
    print("2️⃣  Gerando apresentação...")
    documento.append(gerar_apresentacao())

    # 3. Índice
    print("3️⃣  Gerando índice alfabético...")
    documento.append(gerar_indice(fichas_paths))

    # 4. Fichas municipais
    print("4️⃣  Consolidando fichas municipais...")
    for i, ficha_path in enumerate(sorted(fichas_paths), 1):
        municipio = ficha_path.stem.replace('FICHA-MUNICIPAL-', '').replace('-', ' ').title()

        # Ler conteúdo da ficha
        with open(ficha_path, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Adicionar quebra de página antes de cada ficha (exceto a primeira)
        if i > 1:
            documento.append("\n\\newpage\n\n")

        documento.append(conteudo)

        if i % 10 == 0:
            print(f"   Processadas: {i}/{len(fichas_paths)} fichas...")

    print(f"   ✅ Todas as {len(fichas_paths)} fichas consolidadas")

    # 5. Rodapé final com fontes
    print("5️⃣  Adicionando fontes e elaboração...")
    rodape = f"""

\\newpage

---

# FONTES E ELABORAÇÃO

## Fontes de Dados

Este documento utilizou dados oficiais das seguintes instituições:

- **SEPLAN-TO** - Secretaria de Planejamento e Orçamento do Tocantins
  Perfil Socioeconômico dos Municípios do Tocantins 2024 (8ª Edição)

- **IBGE** - Instituto Brasileiro de Geografia e Estatística
  Censos Demográficos, Estimativas Populacionais, PIB Municipal, PNAD

- **INEP** - Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira
  Índice de Desenvolvimento da Educação Básica (IDEB)

- **DATASUS** - Departamento de Informática do Sistema Único de Saúde
  Cadastro Nacional de Estabelecimentos de Saúde (CNES)

- **Tesouro Nacional** - Ministério da Fazenda
  SICONFI - Sistema de Informações Contábeis e Fiscais do Setor Público Brasileiro

## Elaboração

**Projeto**: Caderno Tocantins 2026 - Sistema de Inteligência Territorial

**Objetivo**: Subsidiar com informações e análises a campanha da Senadora Dorinha Seabra ao governo do Estado do Tocantins

**Metodologia**:
- Extração automatizada de dados dos Perfis Socioeconômicos da SEPLAN-TO
- Integração com bases de dados oficiais (IBGE, INEP, DATASUS)
- Análise multidimensional de 139 municípios do Tocantins
- Estruturação em fichas de 2 páginas para consulta rápida

**Data de Elaboração**: Janeiro de 2026

**Atualização dos Dados**: Os indicadores refletem os dados mais recentes disponíveis nas fontes oficiais até janeiro de 2026, com séries históricas variando conforme a disponibilidade de cada indicador.

---

**Caderno Tocantins 2026**
Sistema de Inteligência Territorial
Janeiro de 2026
"""

    documento.append(rodape)

    # 6. Salvar documento consolidado
    print("6️⃣  Salvando documento consolidado...")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(documento))

    # Estatísticas
    tamanho_kb = output_path.stat().st_size / 1024
    num_linhas = len(''.join(documento).split('\n'))

    print()
    print("=" * 80)
    print("✅ CONSOLIDAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 80)
    print(f"\n📄 Arquivo gerado: {output_path}")
    print(f"📏 Tamanho: {tamanho_kb:.1f} KB")
    print(f"📝 Linhas: {num_linhas:,}")
    print(f"📑 Fichas consolidadas: {len(fichas_paths)}")
    print(f"📄 Páginas estimadas: ~{len(fichas_paths) * 2 + 5} páginas")
    print()
    print("=" * 80)

    return output_path


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Consolidar fichas municipais em documento único')
    parser.add_argument('--input', '-i', default='parte-iii-fichas-municipais/fichas',
                      help='Diretório com as fichas individuais')
    parser.add_argument('--output', '-o', default='parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.md',
                      help='Arquivo de saída do documento consolidado')

    args = parser.parse_args()

    consolidar_fichas(fichas_dir=args.input, output_path=args.output)
