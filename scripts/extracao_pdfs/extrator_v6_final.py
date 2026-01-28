#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator de Indicadores - Versão 6 (Final Completa)
Extrai TODOS os indicadores dos Perfis SEPLAN-TO

Autor: Manus AI
Data: 27/01/2026
"""

import pdfplumber
import re
import json
from typing import Dict, List, Optional
from pathlib import Path


class ExtratadorPerfilSEPLANv6:
    """
    Extrator completo e final para todos os capítulos dos Perfis SEPLAN-TO
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.dados = {
            "municipio": "",
            "codigo_ibge": "",
            "fonte": "SEPLAN-TO - Perfil Socioeconômico 2024 (8ª Edição)",
            "indicadores": {}
        }

    def extrair_texto_pagina(self, pagina_num: int) -> str:
        """Extrai texto de uma página específica"""
        with pdfplumber.open(self.pdf_path) as pdf:
            if pagina_num < 0 or pagina_num >= len(pdf.pages):
                return ""
            pagina = pdf.pages[pagina_num]
            return pagina.extract_text() or ""

    def limpar_numero(self, numero_str: str) -> Optional[float]:
        """
        Converte string numérica para float, tratando formato brasileiro
        """
        if not numero_str:
            return None

        # Remover % se houver
        numero_str = numero_str.replace('%', '').strip()

        # Verificar se tem vírgula (indica decimal no formato BR)
        if ',' in numero_str:
            # Se tem ponto E vírgula, o ponto é separador de milhar
            if '.' in numero_str:
                numero_str = numero_str.replace('.', '')
            # Trocar vírgula por ponto
            numero_str = numero_str.replace(',', '.')
        else:
            # Se tem apenas pontos, verificar se é separador de milhar ou decimal
            if numero_str.count('.') > 1:
                numero_str = numero_str.replace('.', '')
            elif '.' in numero_str:
                partes = numero_str.split('.')
                if len(partes[-1]) == 3 and len(partes) == 2:
                    numero_str = numero_str.replace('.', '')

        try:
            return float(numero_str)
        except ValueError:
            return None

    def extrair_linha_com_valores(
        self,
        texto: str,
        palavra_chave: str,
        anos_esperados: List[int],
        prefixo: str
    ) -> Dict[str, float]:
        """
        Extrai valores de uma linha que contém a palavra-chave e os valores

        Estrutura esperada:
        Indicador 1991 2000 2010 2022
        População (número de pessoas) 24.334 137.355 228.332 302.692
        """
        linhas = texto.split('\n')
        resultado = {}

        # Encontrar a linha com a palavra-chave E que tenha valores (não apenas anos)
        for linha in linhas:
            if palavra_chave.lower() in linha.lower():
                # Extrair todos os números da linha
                numeros_brutos = re.findall(r'\d+(?:\.\d+)*(?:,\d+)?%?', linha)

                # Verificar se a linha tem valores (não apenas anos e números pequenos)
                # A linha correta deve ter pelo menos len(anos_esperados) números
                if len(numeros_brutos) < len(anos_esperados):
                    continue

                # Filtrar para remover anos e manter apenas valores
                valores = []
                for num in numeros_brutos:
                    # Verificar se não é um ano
                    try:
                        num_int = int(num.replace('.', '').replace(',', ''))
                        if num_int < 1900 or num_int > 2100:
                            # Não é um ano, é um valor
                            valor = self.limpar_numero(num)
                            if valor is not None:
                                valores.append(valor)
                    except:
                        # Se não conseguir converter, tentar como valor normal
                        valor = self.limpar_numero(num)
                        if valor is not None:
                            valores.append(valor)

                # Se encontrou valores suficientes, mapear aos anos
                if len(valores) >= len(anos_esperados):
                    for i, ano in enumerate(anos_esperados):
                        if i < len(valores):
                            chave = f"{prefixo}_{ano}"
                            resultado[chave] = valores[i]
                    break

        return resultado

    def extrair_demografia(self) -> Dict:
        """Extrai indicadores demográficos (Capítulo 3, Página 19)"""
        texto = self.extrair_texto_pagina(18)
        indicadores = {}
        anos = [1991, 2000, 2010, 2022]

        # População
        indicadores.update(self.extrair_linha_com_valores(
            texto, "população (número de pessoas)", anos, "pop"
        ))

        # Densidade Demográfica
        indicadores.update(self.extrair_linha_com_valores(
            texto, "densidade demográfica", anos, "densidade"
        ))

        # Taxa de Urbanização
        indicadores.update(self.extrair_linha_com_valores(
            texto, "taxa de urbanização", anos, "taxa_urbanizacao"
        ))

        return indicadores

    def extrair_idh(self) -> Dict:
        """Extrai IDH (Capítulo 4, Página 27)"""
        texto = self.extrair_texto_pagina(26)
        indicadores = {}
        anos = [1991, 2000, 2010]

        # IDH-M
        indicadores.update(self.extrair_linha_com_valores(
            texto, "idh-m", anos, "idhm"
        ))

        # IDH-M Longevidade
        indicadores.update(self.extrair_linha_com_valores(
            texto, "idh-m longevidade", anos, "idhm_longevidade"
        ))

        # IDH-M Educação
        indicadores.update(self.extrair_linha_com_valores(
            texto, "idh-m educação", anos, "idhm_educacao"
        ))

        # IDH-M Renda
        indicadores.update(self.extrair_linha_com_valores(
            texto, "idh-m renda", anos, "idhm_renda"
        ))

        return indicadores

    def extrair_economia(self) -> Dict:
        """Extrai economia (Capítulo 5, Página 31)"""
        texto = self.extrair_texto_pagina(30)
        indicadores = {}

        # Estrutura diferente: cada linha tem Ano, PIB, PIB per capita
        linhas = texto.split('\n')
        anos_pib = [2017, 2018, 2019, 2020, 2021]

        for linha in linhas:
            # Procurar linhas que começam com ano
            for ano in anos_pib:
                if linha.strip().startswith(str(ano)):
                    # Extrair números da linha
                    numeros = re.findall(r'\d+(?:\.\d+)*(?:,\d+)?', linha)
                    if len(numeros) >= 3:
                        # Primeiro número é o ano, segundo é PIB, terceiro é PIB per capita
                        pib_total = self.limpar_numero(numeros[1])
                        pib_per_capita = self.limpar_numero(numeros[2])

                        if pib_total:
                            indicadores[f"pib_total_{ano}"] = pib_total
                        if pib_per_capita:
                            indicadores[f"pib_per_capita_{ano}"] = pib_per_capita
                    break

        return indicadores

    def extrair_educacao(self) -> Dict:
        """Extrai educação (Capítulo 6, Páginas 46-51)"""
        indicadores = {}

        # Taxa de Alfabetização (Página 46)
        texto_p46 = self.extrair_texto_pagina(45)
        anos_alfab = [2000, 2010, 2022]
        indicadores.update(self.extrair_linha_com_valores(
            texto_p46, "total", anos_alfab, "taxa_alfabetizacao"
        ))

        # IDEB Anos Finais - Municipal (Página 50)
        texto_p50 = self.extrair_texto_pagina(49)
        anos_ideb = [2013, 2015, 2017, 2019, 2021, 2023]
        indicadores.update(self.extrair_linha_com_valores(
            texto_p50, "municipal", anos_ideb, "ideb_anos_finais"
        ))

        return indicadores

    def extrair_saneamento(self) -> Dict:
        """Extrai saneamento (Capítulo 8, Páginas 60-62)"""
        indicadores = {}
        anos = [1991, 2000, 2010, 2022]

        # Abastecimento de Água (Página 60)
        texto_p60 = self.extrair_texto_pagina(59)
        indicadores.update(self.extrair_linha_com_valores(
            texto_p60, "rede geral de distribuição", anos, "agua_rede_geral"
        ))

        # Esgotamento Sanitário (Página 61)
        texto_p61 = self.extrair_texto_pagina(60)
        indicadores.update(self.extrair_linha_com_valores(
            texto_p61, "rede geral de esgoto", anos, "esgoto_rede_geral"
        ))

        # Coleta de Lixo (Página 62)
        texto_p62 = self.extrair_texto_pagina(61)
        indicadores.update(self.extrair_linha_com_valores(
            texto_p62, "coletado", anos, "lixo_coletado"
        ))

        return indicadores

    def extrair_todos_indicadores(self) -> Dict:
        """Extrai todos os indicadores do PDF"""
        print("🔍 Iniciando extração (Versão 6 - Final Completa)...")

        print("📊 Demografia...")
        self.dados["indicadores"].update(self.extrair_demografia())

        print("📊 IDH...")
        self.dados["indicadores"].update(self.extrair_idh())

        print("📊 Economia...")
        self.dados["indicadores"].update(self.extrair_economia())

        print("📊 Educação...")
        self.dados["indicadores"].update(self.extrair_educacao())

        print("📊 Saneamento...")
        self.dados["indicadores"].update(self.extrair_saneamento())

        total = len(self.dados["indicadores"])
        print(f"✅ {total} indicadores extraídos")

        return self.dados

    def salvar_json(self, caminho_saida: str):
        """Salva os dados extraídos em JSON"""
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=4)
        print(f"💾 Salvo em: {caminho_saida}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Uso: python extrator_v6_final.py <pdf_entrada> <json_saida>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    json_path = sys.argv[2]

    extrator = ExtratadorPerfilSEPLANv6(pdf_path)
    extrator.extrair_todos_indicadores()
    extrator.salvar_json(json_path)
