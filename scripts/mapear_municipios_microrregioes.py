#!/usr/bin/env python3
"""
Script para mapear municípios às suas microrregiões
Extrai informações das fichas municipais e agrupa por microrregião
"""

import os
import re
from collections import defaultdict

# Diretório das fichas municipais
FICHAS_DIR = "/home/user/caderno-tocantins-2026/parte-iii-fichas-municipais/fichas"

def extrair_microrregiao(filepath):
    """Extrai o nome da microrregião de uma ficha municipal"""
    with open(filepath, 'r', encoding='utf-8') as f:
        # Ler as primeiras 10 linhas onde a informação geralmente está
        for i, line in enumerate(f):
            if i > 10:
                break
            if 'Microrregião' in line:
                # Formato: **Microrregião**: Nome | **Área**
                match = re.search(r'\*\*Microrregião\*\*:\s*([^|]+)', line)
                if match:
                    return match.group(1).strip()
    return None

def extrair_nome_municipio(filename):
    """Extrai o nome do município do nome do arquivo"""
    # Remove FICHA-MUNICIPAL- e .md
    name = filename.replace('FICHA-MUNICIPAL-', '').replace('.md', '')
    return name

def main():
    # Dicionário para agrupar municípios por microrregião
    microrregioes = defaultdict(list)

    # Processar todas as fichas
    for filename in sorted(os.listdir(FICHAS_DIR)):
        if not filename.startswith('FICHA-MUNICIPAL-') or not filename.endswith('.md'):
            continue

        filepath = os.path.join(FICHAS_DIR, filename)
        municipio = extrair_nome_municipio(filename)
        microrregiao = extrair_microrregiao(filepath)

        if microrregiao:
            microrregioes[microrregiao].append(municipio)
        else:
            print(f"AVISO: Não encontrou microrregião para {municipio}")

    # Exibir resultados agrupados
    print("=" * 80)
    print("MAPEAMENTO: MUNICÍPIOS POR MICRORREGIÃO")
    print("=" * 80)
    print()

    for i, (microrregiao, municipios) in enumerate(sorted(microrregioes.items()), 1):
        print(f"## {i}. MICRORREGIÃO: {microrregiao.upper()}")
        print(f"   Total de municípios: {len(municipios)}")
        print()
        for municipio in sorted(municipios):
            print(f"   - {municipio}")
        print()
        print("-" * 80)
        print()

    # Sumário
    print("=" * 80)
    print("SUMÁRIO")
    print("=" * 80)
    total_municipios = sum(len(m) for m in microrregioes.values())
    print(f"Total de microrregiões: {len(microrregioes)}")
    print(f"Total de municípios: {total_municipios}")
    print()

    for microrregiao, municipios in sorted(microrregioes.items()):
        print(f"  {microrregiao}: {len(municipios)} municípios")

if __name__ == '__main__':
    main()
