#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de consolidação de dados das microrregiões do Tocantins
Consolida dados de 8 planilhas de microrregiões na planilha BASE_DADOS_TOCANTINS_V01.csv
"""

import csv
import os
from typing import Dict, List, Optional

# Diretório base
BASE_DIR = "/home/user/caderno-tocantins-2026/dados/finais"

# Arquivos de entrada
ARQUIVOS_MICRORREGIOES = {
    "Bico do Papagaio": f"{BASE_DIR}/dados-microrregiao-bico-do-papagaio-v01.csv",
    "Araguaína": f"{BASE_DIR}/dados-microrregiao-araguaina-v01.csv",
    "Miracema do Tocantins": f"{BASE_DIR}/dados-microrregiao-miracema-v01.csv",
    "Rio Formoso": f"{BASE_DIR}/dados-microrregiao-rio-formoso-v01.csv",
    "Gurupi": f"{BASE_DIR}/dados-microrregiao-gurupi-v01.csv",
    "Porto Nacional": f"{BASE_DIR}/dados-microrregiao-porto-nacional-v01.csv",
    "Jalapão": f"{BASE_DIR}/dados-microrregiao-jalapao-v01.csv",
    "Dianópolis": f"{BASE_DIR}/dados-microrregiao-dianopolis-v01.csv"
}

# Arquivo de saída
ARQUIVO_CONSOLIDADO = f"{BASE_DIR}/BASE_DADOS_TOCANTINS_V01.csv"

def limpar_valor(valor: str) -> Optional[str]:
    """Limpa e valida um valor, retornando None para valores vazios ou 'nd'"""
    if not valor or valor.strip().lower() in ['nd', 'n/d', '', 'nan']:
        return ""
    return valor.strip()

def ler_planilha_porto_nacional() -> Dict[str, Dict]:
    """Lê a planilha de Porto Nacional que está em formato pivotado"""
    arquivo = ARQUIVOS_MICRORREGIOES["Porto Nacional"]
    municipios = {}

    with open(arquivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            municipio = row['Município'].strip()
            indicador = row['Indicador'].strip()
            valor = limpar_valor(row['Valor'])

            if municipio not in municipios:
                municipios[municipio] = {}

            # Mapeamento dos indicadores
            if indicador == 'População Censo':
                municipios[municipio]['pop_2022'] = valor
            elif indicador == 'População Estimada':
                municipios[municipio]['pop_2025_est'] = valor
            elif indicador == 'Área Territorial (km²)':
                municipios[municipio]['area_km2'] = valor
            elif indicador == 'Densidade Demográfica (hab/km²)':
                municipios[municipio]['densidade'] = valor
            elif indicador == 'PIB per capita (R$)':
                municipios[municipio]['pib_pc'] = valor
            elif indicador == 'IDHM':
                municipios[municipio]['idhm'] = valor
            elif indicador == 'Taxa de Escolarização 6-14 anos (%)':
                municipios[municipio]['escol_6_14'] = valor
            elif indicador == 'Mortalidade Infantil (por mil)':
                municipios[municipio]['mort_inf'] = valor

    return municipios

def ler_planilha_tabular(arquivo: str) -> List[Dict]:
    """Lê planilhas em formato tabular"""
    municipios = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get('municipio'):
                continue
            municipio = row['municipio'].strip()
            # Ignorar linhas de totais e legendas
            if municipio.upper().startswith('TOTAIS') or municipio.upper().startswith('LEGENDAS') or not municipio:
                continue
            municipios.append(row)
    return municipios

def calcular_crescimento(pop_2010: Optional[str], pop_2022: Optional[str]) -> str:
    """Calcula o crescimento percentual entre 2010 e 2022"""
    if not pop_2010 or not pop_2022:
        return ""
    try:
        p_2010 = float(pop_2010)
        p_2022 = float(pop_2022)
        if p_2010 > 0:
            crescimento = ((p_2022 - p_2010) / p_2010) * 100
            return f"{crescimento:.2f}"
    except (ValueError, ZeroDivisionError):
        pass
    return ""

def calcular_densidade(pop_2022: Optional[str], area: Optional[str]) -> str:
    """Calcula a densidade demográfica"""
    if not pop_2022 or not area:
        return ""
    try:
        p = float(pop_2022)
        a = float(area)
        if a > 0:
            densidade = p / a
            return f"{densidade:.2f}"
    except (ValueError, ZeroDivisionError):
        pass
    return ""

def ler_base_consolidada() -> tuple[List[str], List[Dict]]:
    """Lê a planilha consolidada existente"""
    linhas = []
    with open(ARQUIVO_CONSOLIDADO, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        colunas = reader.fieldnames
        for row in reader:
            linhas.append(row)
    return colunas, linhas

def processar_municipios():
    """Processa todos os municípios e retorna um dicionário com os dados"""
    dados_municipios = {}

    # Processar Porto Nacional (formato pivotado)
    print("Processando Porto Nacional...")
    municipios_porto = ler_planilha_porto_nacional()
    for municipio, dados in municipios_porto.items():
        nome_completo = municipio
        dados_municipios[nome_completo] = {
            'demo_pop_2010': "",
            'demo_pop_2022': limpar_valor(dados.get('pop_2022', '')),
            'demo_pop_2025_est': limpar_valor(dados.get('pop_2025_est', '')),
            'terr_area_km2': limpar_valor(dados.get('area_km2', '')),
            'demo_dens_dem_hab_km2': limpar_valor(dados.get('densidade', '')),
            'econ_pib_per_capita_reais': limpar_valor(dados.get('pib_pc', '')),
            'idh_idhm_2010': limpar_valor(dados.get('idhm', '')),
            'educ_tx_escolar_6_14_pct': limpar_valor(dados.get('escol_6_14', '')),
            'saude_mort_inf_por_mil': limpar_valor(dados.get('mort_inf', '')),
            'demo_cresc_2010_2022_pct': ""
        }

    # Processar as outras 7 microrregiões
    for nome_micro, arquivo in ARQUIVOS_MICRORREGIOES.items():
        if nome_micro == "Porto Nacional":
            continue

        print(f"Processando {nome_micro}...")
        municipios = ler_planilha_tabular(arquivo)

        for mun in municipios:
            municipio = mun.get('municipio', '').strip()
            if not municipio:
                continue

            pop_2010 = limpar_valor(mun.get('pop_2010', ''))
            pop_2022 = limpar_valor(mun.get('pop_2022', ''))
            area_km2 = limpar_valor(mun.get('area_km2', ''))
            densidade = limpar_valor(mun.get('densidade', ''))

            # Calcular crescimento se tivermos pop_2010 e pop_2022
            crescimento = calcular_crescimento(pop_2010, pop_2022)

            # Calcular densidade se não disponível mas tivermos pop e área
            if not densidade and pop_2022 and area_km2:
                densidade = calcular_densidade(pop_2022, area_km2)

            dados_municipios[municipio] = {
                'demo_pop_2010': pop_2010,
                'demo_pop_2022': pop_2022,
                'demo_pop_2025_est': limpar_valor(mun.get('pop_2025_est', '')),
                'terr_area_km2': area_km2,
                'demo_dens_dem_hab_km2': densidade,
                'econ_pib_per_capita_reais': limpar_valor(mun.get('pib_pc', '')),
                'idh_idhm_2010': limpar_valor(mun.get('idhm', '')),
                'educ_tx_escolar_6_14_pct': limpar_valor(mun.get('escol_6_14', '') or mun.get('escol', '')),
                'saude_mort_inf_por_mil': limpar_valor(mun.get('mort_inf', '')),
                'demo_cresc_2010_2022_pct': crescimento
            }

    return dados_municipios

def atualizar_planilha_consolidada(dados_municipios: Dict):
    """Atualiza a planilha consolidada com os dados processados"""
    colunas, linhas = ler_base_consolidada()

    # Atualizar cada linha
    linhas_atualizadas = []
    for linha in linhas:
        nome_municipio = linha['terr_nome'].strip()

        # Se for um consolidado, pular por enquanto
        if '[CONSOLIDADO]' in nome_municipio:
            linhas_atualizadas.append(linha)
            continue

        # Se tivermos dados para este município, atualizar
        if nome_municipio in dados_municipios:
            dados = dados_municipios[nome_municipio]
            for campo, valor in dados.items():
                if campo in linha:
                    linha[campo] = valor

        linhas_atualizadas.append(linha)

    # Escrever arquivo atualizado
    with open(ARQUIVO_CONSOLIDADO, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(linhas_atualizadas)

    print(f"\n✓ Planilha consolidada atualizada: {ARQUIVO_CONSOLIDADO}")
    print(f"  Total de municípios processados: {len(dados_municipios)}")

def calcular_consolidados():
    """Calcula os valores consolidados por microrregião"""
    colunas, linhas = ler_base_consolidada()

    # Agrupar municípios por microrregião
    microrregioes = {}
    linhas_consolidadas = {}

    for linha in linhas:
        nome = linha['terr_nome'].strip()
        microrregiao = linha['terr_microrregiao'].strip()

        if '[CONSOLIDADO]' in nome:
            # Guardar a linha de consolidado para atualizar depois
            linhas_consolidadas[microrregiao] = linha
            continue

        if not microrregiao:
            continue

        if microrregiao not in microrregioes:
            microrregioes[microrregiao] = []

        microrregioes[microrregiao].append(linha)

    # Calcular consolidados
    for microrregiao, municipios in microrregioes.items():
        if microrregiao not in linhas_consolidadas:
            continue

        linha_consolid = linhas_consolidadas[microrregiao]

        # Somas
        total_pop_2010 = 0
        total_pop_2022 = 0
        total_pop_2025 = 0
        total_area = 0

        # Para médias ponderadas
        soma_idhm_pop = 0
        soma_escol_pop = 0
        soma_mort_pop = 0
        pop_com_idhm = 0
        pop_com_escol = 0
        pop_com_mort = 0

        for mun in municipios:
            # População
            try:
                if mun['demo_pop_2010']:
                    total_pop_2010 += float(mun['demo_pop_2010'])
            except (ValueError, KeyError):
                pass

            try:
                if mun['demo_pop_2022']:
                    pop_2022 = float(mun['demo_pop_2022'])
                    total_pop_2022 += pop_2022

                    # IDHM ponderado pela população
                    if mun['idh_idhm_2010']:
                        idhm = float(mun['idh_idhm_2010'])
                        soma_idhm_pop += idhm * pop_2022
                        pop_com_idhm += pop_2022

                    # Escolarização ponderada
                    if mun['educ_tx_escolar_6_14_pct']:
                        escol = float(mun['educ_tx_escolar_6_14_pct'])
                        soma_escol_pop += escol * pop_2022
                        pop_com_escol += pop_2022

                    # Mortalidade ponderada
                    if mun['saude_mort_inf_por_mil']:
                        mort = float(mun['saude_mort_inf_por_mil'])
                        soma_mort_pop += mort * pop_2022
                        pop_com_mort += pop_2022
            except (ValueError, KeyError):
                pass

            try:
                if mun['demo_pop_2025_est']:
                    total_pop_2025 += float(mun['demo_pop_2025_est'])
            except (ValueError, KeyError):
                pass

            try:
                if mun['terr_area_km2']:
                    total_area += float(mun['terr_area_km2'])
            except (ValueError, KeyError):
                pass

        # Atualizar consolidado
        if total_pop_2010 > 0:
            linha_consolid['demo_pop_2010'] = str(int(total_pop_2010))

        if total_pop_2022 > 0:
            linha_consolid['demo_pop_2022'] = str(int(total_pop_2022))

            # Calcular crescimento
            if total_pop_2010 > 0:
                cresc = ((total_pop_2022 - total_pop_2010) / total_pop_2010) * 100
                linha_consolid['demo_cresc_2010_2022_pct'] = f"{cresc:.2f}"

        if total_pop_2025 > 0:
            linha_consolid['demo_pop_2025_est'] = str(int(total_pop_2025))

        if total_area > 0:
            linha_consolid['terr_area_km2'] = f"{total_area:.2f}"

            # Calcular densidade
            if total_pop_2022 > 0:
                dens = total_pop_2022 / total_area
                linha_consolid['demo_dens_dem_hab_km2'] = f"{dens:.2f}"

        # Médias ponderadas
        if pop_com_idhm > 0:
            idhm_medio = soma_idhm_pop / pop_com_idhm
            linha_consolid['idh_idhm_2010'] = f"{idhm_medio:.3f}"

        if pop_com_escol > 0:
            escol_media = soma_escol_pop / pop_com_escol
            linha_consolid['educ_tx_escolar_6_14_pct'] = f"{escol_media:.2f}"

        if pop_com_mort > 0:
            mort_media = soma_mort_pop / pop_com_mort
            linha_consolid['saude_mort_inf_por_mil'] = f"{mort_media:.2f}"

    # Escrever arquivo atualizado
    with open(ARQUIVO_CONSOLIDADO, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(linhas)

    print(f"\n✓ Consolidados calculados para {len(microrregioes)} microrregiões")

def main():
    print("=" * 70)
    print("CONSOLIDAÇÃO DE DADOS DO TOCANTINS")
    print("=" * 70)

    # Processar dados de todas as microrregiões
    print("\n1. Processando dados das microrregiões...")
    dados_municipios = processar_municipios()

    # Atualizar planilha consolidada
    print("\n2. Atualizando planilha consolidada...")
    atualizar_planilha_consolidada(dados_municipios)

    # Calcular consolidados
    print("\n3. Calculando consolidados de microrregiões...")
    calcular_consolidados()

    print("\n" + "=" * 70)
    print("CONSOLIDAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 70)

    # Estatísticas
    print(f"\nESTATÍSTICAS:")
    print(f"  - Total de municípios processados: {len(dados_municipios)}")
    print(f"  - Arquivo consolidado: {ARQUIVO_CONSOLIDADO}")

    # Contar dados por indicador
    contadores = {
        'pop_2010': 0,
        'pop_2022': 0,
        'area': 0,
        'pib': 0,
        'idhm': 0,
        'escol': 0,
        'mort': 0
    }

    for dados in dados_municipios.values():
        if dados['demo_pop_2010']:
            contadores['pop_2010'] += 1
        if dados['demo_pop_2022']:
            contadores['pop_2022'] += 1
        if dados['terr_area_km2']:
            contadores['area'] += 1
        if dados['econ_pib_per_capita_reais']:
            contadores['pib'] += 1
        if dados['idh_idhm_2010']:
            contadores['idhm'] += 1
        if dados['educ_tx_escolar_6_14_pct']:
            contadores['escol'] += 1
        if dados['saude_mort_inf_por_mil']:
            contadores['mort'] += 1

    print(f"\n  Cobertura de dados:")
    print(f"    - População 2010: {contadores['pop_2010']} municípios")
    print(f"    - População 2022: {contadores['pop_2022']} municípios")
    print(f"    - Área territorial: {contadores['area']} municípios")
    print(f"    - PIB per capita: {contadores['pib']} municípios")
    print(f"    - IDHM: {contadores['idhm']} municípios")
    print(f"    - Taxa escolarização: {contadores['escol']} municípios")
    print(f"    - Mortalidade infantil: {contadores['mort']} municípios")
    print()

if __name__ == "__main__":
    main()
