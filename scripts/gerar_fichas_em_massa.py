#!/usr/bin/env python3
"""
Script para gerar fichas municipais em massa para todos os 139 municípios do Tocantins.

Autor: Claude Code
Data: 2026-01-28
"""

import pandas as pd
from pathlib import Path
import sys
import time

# Importar o gerador de fichas
sys.path.insert(0, str(Path(__file__).parent))
from gerar_ficha_municipal import GeradorFichaMunicipal


def gerar_fichas_em_massa(output_dir='parte-iii-fichas-municipais/fichas'):
    """Gera fichas para todos os municípios do Tocantins."""

    print("=" * 80)
    print("GERAÇÃO EM MASSA DE FICHAS MUNICIPAIS - TOCANTINS 2026")
    print("=" * 80)
    print()

    # Inicializar gerador
    gerador = GeradorFichaMunicipal()

    # Obter lista de todos os municípios da base
    municipios = gerador.df_base['terr_nome'].tolist()

    # Filtrar "Tocantins" (consolidação estadual, não município)
    municipios = [m for m in municipios if m != 'Tocantins']

    print(f"📋 Total de municípios a processar: {len(municipios)}")
    print(f"📁 Diretório de saída: {output_dir}")
    print()

    # Criar diretório de saída
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Estatísticas
    sucesso = []
    erros = []
    tempo_inicio = time.time()

    # Gerar fichas
    for i, municipio in enumerate(municipios, 1):
        try:
            print(f"\n[{i}/{len(municipios)}] Processando: {municipio}")
            gerador.gerar_ficha(municipio, output_dir=output_dir)
            sucesso.append(municipio)
            print(f"✅ {municipio} - OK")

        except Exception as e:
            erros.append((municipio, str(e)))
            print(f"❌ {municipio} - ERRO: {e}")
            continue

    tempo_total = time.time() - tempo_inicio

    # Relatório final
    print("\n" + "=" * 80)
    print("RELATÓRIO FINAL DA GERAÇÃO EM MASSA")
    print("=" * 80)
    print(f"\n✅ Fichas geradas com sucesso: {len(sucesso)}/{len(municipios)}")
    print(f"❌ Erros: {len(erros)}/{len(municipios)}")
    print(f"⏱️  Tempo total: {tempo_total:.1f} segundos")
    print(f"⚡ Média: {tempo_total/len(municipios):.1f} seg/município")

    if erros:
        print(f"\n❌ Municípios com erro:")
        for municipio, erro in erros:
            print(f"   - {municipio}: {erro}")

    print("\n" + "=" * 80)
    print(f"📁 Fichas geradas em: {output_dir}/")
    print("=" * 80)

    return sucesso, erros


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Gerar fichas municipais em massa')
    parser.add_argument('--output', '-o', default='parte-iii-fichas-municipais/fichas',
                      help='Diretório de saída das fichas')

    args = parser.parse_args()

    gerar_fichas_em_massa(output_dir=args.output)
