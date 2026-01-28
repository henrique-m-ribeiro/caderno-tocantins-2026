#!/usr/bin/env python3
"""
Atualiza as fichas municipais com análises geradas automaticamente.
Substitui os placeholders [A DEFINIR] pelas análises contextualizadas.
"""

import re
from pathlib import Path
from analisar_municipio import AnalisadorMunicipal


def atualizar_ficha_municipal(ficha_path: Path, analises: dict) -> bool:
    """Atualiza uma ficha municipal com as análises geradas."""
    try:
        # Ler ficha existente
        with open(ficha_path, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # === SÍNTESE ESTRATÉGICA ===

        # Pontos Fortes
        pontos_fortes_texto = "\n".join([f"- {pf}" for pf in analises['sintese_estrategica']['pontos_fortes']])
        conteudo = re.sub(
            r'- \[A DEFINIR: Análise dos principais ativos do município\]\n- \[A DEFINIR: Vantagens competitivas identificadas\]\n- \[A DEFINIR: Recursos e potencialidades destacadas\]',
            pontos_fortes_texto,
            conteudo
        )

        # Desafios
        desafios_texto = "\n".join([f"- {d}" for d in analises['sintese_estrategica']['desafios']])
        conteudo = re.sub(
            r'- \[A DEFINIR: Principais gargalos identificados\]\n- \[A DEFINIR: Problemas estruturais evidentes\]\n- \[A DEFINIR: Áreas que demandam atenção\]',
            desafios_texto,
            conteudo
        )

        # Oportunidades
        oportunidades_texto = "\n".join([f"- {o}" for o in analises['sintese_estrategica']['oportunidades']])
        conteudo = re.sub(
            r'- \[A DEFINIR: Potenciais de desenvolvimento\]\n- \[A DEFINIR: Áreas para investimento\]\n- \[A DEFINIR: Parcerias estratégicas possíveis\]',
            oportunidades_texto,
            conteudo
        )

        # === ANÁLISES POR DIMENSÃO ===

        # Dimensão 1: Dados Sociais
        conteudo = re.sub(
            r'\[A DEFINIR: Análise contextualizada dos dados sociais e demográficos, explicando tendências de crescimento populacional, perfil urbano/rural, e implicações para políticas públicas\]',
            analises['analise_social'],
            conteudo
        )

        # Dimensão 2: Economia
        conteudo = re.sub(
            r'\[A DEFINIR: Análise da estrutura econômica do município, destacando setores dinâmicos, dependências, e potencial de diversificação econômica\]',
            analises['analise_economica'],
            conteudo
        )

        # Dimensão 3: Educação
        conteudo = re.sub(
            r'\[A DEFINIR: Análise do cenário educacional, identificando avanços, desafios em infraestrutura escolar, qualidade do ensino, e propostas de melhoria\]',
            analises['analise_educacao'],
            conteudo
        )

        # Dimensão 4: Saúde e Saneamento (vários formatos possíveis)
        conteudo = re.sub(
            r'\[A DEFINIR: Análise da infraestrutura de saúde e saneamento, identificando coberturas, déficits e prioridades de investimento\]',
            analises['analise_saude'],
            conteudo
        )
        conteudo = re.sub(
            r'\[A DEFINIR: Análise da infraestrutura de saúde e saneamento, capacidade de atendimento, e necessidades de investimento no setor\]',
            analises['analise_saude'],
            conteudo
        )

        # Dimensão 5: Agropecuária (vários formatos possíveis)
        conteudo = re.sub(
            r'\[A DEFINIR: Análise do setor agropecuário, destacando principais atividades, evolução e potencialidades\]',
            analises['analise_agropecuaria'],
            conteudo
        )
        conteudo = re.sub(
            r'\[A DEFINIR: Análise do setor agropecuário, destacando vocações produtivas, tecnologias utilizadas, e oportunidades de agregação de valor\]',
            analises['analise_agropecuaria'],
            conteudo
        )

        # Dimensão 6: Finanças Públicas (vários formatos possíveis)
        conteudo = re.sub(
            r'\[A DEFINIR: Análise da estrutura de receitas municipais, dependência de transferências e capacidade de investimento\]',
            analises['analise_financas'],
            conteudo
        )
        conteudo = re.sub(
            r'\[A DEFINIR: Análise da dependência de transferências, autonomia fiscal, evolução das receitas, e capacidade de investimento do município\]',
            analises['analise_financas'],
            conteudo
        )

        # === DIAGNÓSTICO INTEGRADO === (vários formatos possíveis)
        conteudo = re.sub(
            r'\[A DEFINIR: Síntese dos principais achados, integrando as dimensões analisadas e identificando eixos estratégicos prioritários para o desenvolvimento municipal. Deve conectar os desafios identificados com as oportunidades de intervenção do governo estadual, considerando as especificidades locais e o potencial de cada município no contexto regional.\]',
            analises['diagnostico_integrado'],
            conteudo
        )

        # Formato alternativo do diagnóstico (2 seções separadas)
        # Precisa substituir todo o bloco incluindo os headers
        conteudo = re.sub(
            r'### Diagnóstico Integrado\n\n\[A DEFINIR: Parágrafo explicando como as diferentes dimensões se conectam para explicar a realidade do município\. Por exemplo: como a estrutura econômica impacta a arrecadação municipal, como a infraestrutura logística afeta o escoamento da produção agropecuária, etc\.\]\n\n### Diretrizes para o Plano de Governo\n\n\[A DEFINIR: Parágrafo com sugestões de ações e políticas públicas estaduais, focando em parcerias Estado-Município-União, investimentos prioritários, e oportunidades de desenvolvimento sustentável\]',
            analises['diagnostico_integrado'],
            conteudo
        )

        # Salvar ficha atualizada
        with open(ficha_path, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        return True

    except Exception as e:
        print(f"Erro ao atualizar {ficha_path.name}: {e}")
        return False


def atualizar_todas_fichas(fichas_dir='parte-iii-fichas-municipais/fichas'):
    """Atualiza todas as fichas municipais com análises."""
    fichas_dir = Path(fichas_dir)
    analisador = AnalisadorMunicipal()

    # Listar fichas
    fichas = sorted(fichas_dir.glob('FICHA-MUNICIPAL-*.md'))

    print(f"📊 Atualizando {len(fichas)} fichas municipais com análises...\n")

    sucesso = []
    erros = []

    for i, ficha_path in enumerate(fichas, 1):
        # Extrair nome do município do arquivo
        nome_arquivo = ficha_path.stem.replace('FICHA-MUNICIPAL-', '')
        municipio = nome_arquivo.replace('-', ' ').title()

        # Correções específicas
        municipio = municipio.replace(' Do ', ' do ').replace(' Da ', ' da ').replace(' De ', ' de ')
        municipio = municipio.replace(" D'Arco", " D'Arco")  # Pau D'Arco

        print(f"[{i:3d}/{len(fichas)}] Processando: {municipio}")

        # Gerar análises
        analises = analisador.gerar_analises_completas(municipio)

        if analises:
            # Atualizar ficha
            if atualizar_ficha_municipal(ficha_path, analises):
                sucesso.append(municipio)
                print(f"             ✅ Análises inseridas com sucesso")
            else:
                erros.append((municipio, "Erro ao atualizar arquivo"))
                print(f"             ❌ Erro ao atualizar arquivo")
        else:
            erros.append((municipio, "JSON não encontrado"))
            print(f"             ⚠️  JSON não encontrado")

    # Relatório final
    print(f"\n{'='*70}")
    print(f"📊 RELATÓRIO DE ATUALIZAÇÃO DE ANÁLISES")
    print(f"{'='*70}")
    print(f"✅ Fichas atualizadas com sucesso: {len(sucesso)}/{len(fichas)}")
    print(f"❌ Fichas com erro: {len(erros)}/{len(fichas)}")

    if erros:
        print(f"\n⚠️  FICHAS COM ERRO:")
        for municipio, erro in erros:
            print(f"   - {municipio}: {erro}")

    print(f"\n{'='*70}")
    print(f"✨ Atualização concluída!")
    print(f"{'='*70}\n")

    return len(sucesso), len(erros)


if __name__ == '__main__':
    atualizar_todas_fichas()
