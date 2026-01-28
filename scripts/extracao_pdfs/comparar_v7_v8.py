#!/usr/bin/env python3
"""
Script para comparar extrator v7 vs v8 e identificar lacunas.
Autor: Claude Code
Data: 2026-01-28
"""

import json
import pandas as pd
from pathlib import Path

def comparar_extratores():
    """Compara v7 (JSON) com v8 (Excel) e gera relatório de lacunas."""

    # Carregar dados v7 (JSON)
    v7_files = list(Path("dados/brutos/extraidos-perfis").glob("*_v7.json"))
    v7_data = {}
    for f in v7_files:
        municipio = f.stem.replace("_v7", "")
        with open(f) as file:
            data = json.load(file)
            v7_data[municipio] = set(data["indicadores"].keys())

    # Carregar dados v8 (Excel)
    v8_df = pd.read_excel("BASE_DADOS_TOCANTINS_V03_BETA.xlsx")
    v8_cols = set(v8_df.columns) - {"Municipio_Arquivo"}

    # Pegar indicadores únicos do v7 (união de todos os municípios)
    v7_all_indicators = set()
    for indicators in v7_data.values():
        v7_all_indicators.update(indicators)

    # Análise de cobertura
    print("=" * 80)
    print("COMPARAÇÃO EXTRATOR V7 vs V8")
    print("=" * 80)

    print(f"\n📊 RESUMO GERAL:")
    print(f"  V7: {len(v7_all_indicators)} indicadores únicos (66-76 por município)")
    print(f"  V8: {len(v8_cols)} indicadores")
    print(f"  Cobertura V8: {len(v8_cols)/len(v7_all_indicators)*100:.1f}%")

    # Indicadores presentes em v8
    print(f"\n✅ INDICADORES CAPTURADOS POR V8 ({len(v8_cols)}):")
    for col in sorted(v8_cols):
        # Tentar encontrar correspondência aproximada no v7
        v7_match = [ind for ind in v7_all_indicators if col.lower() in ind.lower() or ind.lower() in col.lower()]
        if v7_match:
            print(f"  ✓ {col:50s} (match v7: {v7_match[0][:40]}...)")
        else:
            print(f"  🆕 {col:50s} (NOVO no v8)")

    # Categorizar indicadores faltantes no v8
    faltantes = v7_all_indicators - {ind for ind in v7_all_indicators
                                      if any(col.lower() in ind.lower() or ind.lower() in col.lower()
                                             for col in v8_cols)}

    categorias = {
        'IDH': [],
        'Economia - PIB': [],
        'Economia - VAB': [],
        'Emprego': [],
        'Aspectos Físicos': [],
        'Serviços Urbanos': [],
        'Meio Ambiente': [],
        'Outros': []
    }

    for ind in faltantes:
        ind_lower = ind.lower()
        if 'idhm' in ind_lower:
            categorias['IDH'].append(ind)
        elif 'pib' in ind_lower:
            categorias['Economia - PIB'].append(ind)
        elif 'vab' in ind_lower or 'valor adicionado' in ind_lower:
            categorias['Economia - VAB'].append(ind)
        elif 'emprego' in ind_lower or 'estoque' in ind_lower:
            categorias['Emprego'].append(ind)
        elif 'área' in ind_lower or 'altitude' in ind_lower:
            categorias['Aspectos Físicos'].append(ind)
        elif 'agência' in ind_lower or 'lotérica' in ind_lower or 'cartório' in ind_lower:
            categorias['Serviços Urbanos'].append(ind)
        elif 'queimada' in ind_lower or 'focos' in ind_lower:
            categorias['Meio Ambiente'].append(ind)
        else:
            categorias['Outros'].append(ind)

    print(f"\n❌ LACUNAS - INDICADORES EM V7 MAS NÃO EM V8 ({len(faltantes)}):")
    for cat, inds in categorias.items():
        if inds:
            print(f"\n  📂 {cat} ({len(inds)} indicadores):")
            for ind in sorted(inds):
                print(f"    - {ind}")

    # Análise por município
    print(f"\n📍 COBERTURA POR MUNICÍPIO:")
    print(f"{'Município':15s} {'V7':>4s} {'V8':>4s} {'Dif':>5s} {'%':>6s}")
    print("-" * 40)
    for municipio, v7_inds in sorted(v7_data.items()):
        v8_count = len(v8_cols)
        diff = len(v7_inds) - v8_count
        pct = v8_count / len(v7_inds) * 100
        print(f"{municipio:15s} {len(v7_inds):4d} {v8_count:4d} {diff:5d} {pct:5.1f}%")

    # Recomendações
    print(f"\n💡 RECOMENDAÇÕES PARA APRIMORAMENTO DO V8:")
    print(f"  1. PRIORIDADE ALTA - Adicionar capítulo 'Economia':")
    print(f"     - PIB Total e PIB Per Capita")
    print(f"     - VAB por setor (15 indicadores)")
    print(f"  2. PRIORIDADE ALTA - Adicionar IDHM e componentes")
    print(f"  3. PRIORIDADE MÉDIA - Adicionar Emprego Formal (4 indicadores)")
    print(f"  4. PRIORIDADE BAIXA - Aspectos Físicos, Serviços Urbanos, Meio Ambiente")
    print(f"\n  Meta: Alcançar 95%+ de cobertura = ~{int(len(v7_all_indicators) * 0.95)} indicadores")
    print(f"  Gap atual: {len(faltantes)} indicadores ({len(faltantes)/len(v7_all_indicators)*100:.1f}%)")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    comparar_extratores()
