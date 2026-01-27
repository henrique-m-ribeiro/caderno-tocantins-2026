#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator de Indicadores de Prioridade Alta - Versão 2 (Corrigida)
Sistema de Extração de Dados dos Perfis SEPLAN-TO

CORREÇÃO APLICADA:
- Implementação de lógica stateful para parsing multi-linha
- Busca palavra-chave numa linha, depois processa linhas subsequentes
- Extração de séries temporais com mapeamento de anos

Autor: Manus AI
Data: 27/01/2026
"""

import pdfplumber
import re
import json
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class ExtratadorPerfilSEPLAN:
    """
    Extrator de dados dos Perfis Socioeconômicos SEPLAN-TO
    com suporte a parsing multi-linha
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
            pagina = pdf.pages[pagina_num]
            return pagina.extract_text()
    
    def encontrar_linha_com_palavra_chave(self, texto: str, palavra_chave: str) -> Tuple[int, str]:
        """
        Encontra a primeira linha que contém a palavra-chave
        
        Returns:
            (índice_da_linha, texto_da_linha) ou (-1, "") se não encontrar
        """
        linhas = texto.split('\n')
        for i, linha in enumerate(linhas):
            if palavra_chave.lower() in linha.lower():
                return i, linha
        return -1, ""
    
    def extrair_valores_linhas_subsequentes(
        self, 
        texto: str, 
        indice_inicio: int, 
        num_linhas: int = 5,
        anos_esperados: List[int] = None
    ) -> Dict[str, float]:
        """
        Extrai valores numéricos das linhas subsequentes à palavra-chave
        
        Args:
            texto: Texto completo da página
            indice_inicio: Índice da linha onde a palavra-chave foi encontrada
            num_linhas: Número de linhas para processar após a palavra-chave
            anos_esperados: Lista de anos para mapear aos valores (ex: [1991, 2000, 2010, 2022])
        
        Returns:
            Dicionário com valores extraídos
        """
        linhas = texto.split('\n')
        valores = {}
        
        # Processar as linhas subsequentes
        for i in range(indice_inicio, min(indice_inicio + num_linhas, len(linhas))):
            linha = linhas[i]
            
            # Extrair todos os números (incluindo decimais) da linha
            numeros = re.findall(r'\d+\.?\d*(?:,\d+)?', linha)
            
            # Converter vírgula para ponto (padrão brasileiro)
            numeros = [n.replace(',', '.') for n in numeros]
            
            # Tentar identificar anos na linha
            anos_na_linha = re.findall(r'\b(19\d{2}|20\d{2})\b', linha)
            
            # Se encontrou anos e valores na mesma linha
            if anos_na_linha and numeros:
                # Filtrar apenas os números que não são anos
                valores_numericos = [float(n) for n in numeros if n not in anos_na_linha]
                
                # Mapear anos aos valores
                for j, ano in enumerate(anos_na_linha):
                    if j < len(valores_numericos):
                        valores[ano] = valores_numericos[j]
            
            # Se não encontrou anos mas tem valores e anos_esperados foi fornecido
            elif numeros and anos_esperados:
                valores_numericos = [float(n) for n in numeros]
                for j, valor in enumerate(valores_numericos):
                    if j < len(anos_esperados):
                        valores[str(anos_esperados[j])] = valor
        
        return valores
    
    def extrair_serie_temporal(
        self, 
        texto: str, 
        palavra_chave: str,
        anos: List[int],
        prefixo_indicador: str
    ) -> Dict[str, float]:
        """
        Extrai uma série temporal completa para um indicador
        
        Args:
            texto: Texto da página
            palavra_chave: Palavra-chave que identifica o indicador
            anos: Lista de anos esperados na série
            prefixo_indicador: Prefixo para nomear os indicadores (ex: 'populacao')
        
        Returns:
            Dicionário com indicadores nomeados (ex: {'populacao_1991': 24334, ...})
        """
        indice, _ = self.encontrar_linha_com_palavra_chave(texto, palavra_chave)
        
        if indice == -1:
            return {}
        
        valores = self.extrair_valores_linhas_subsequentes(texto, indice, num_linhas=10, anos_esperados=anos)
        
        # Criar dicionário com nomes padronizados
        resultado = {}
        for ano in anos:
            chave = f"{prefixo_indicador}_{ano}"
            if str(ano) in valores:
                resultado[chave] = valores[str(ano)]
        
        return resultado
    
    # ===== FUNÇÕES DE EXTRAÇÃO POR CAPÍTULO =====
    
    def extrair_demografia(self) -> Dict:
        """
        Extrai indicadores demográficos (Capítulo 3, Página 19)
        Tabelas 3.1, 3.2, 3.4, 3.5
        """
        texto = self.extrair_texto_pagina(18)  # Página 19 (índice 18)
        indicadores = {}
        anos = [1991, 2000, 2010, 2022]
        
        # Tabela 3.1 - População, Densidade, Taxa de Urbanização, Crescimento
        indicadores.update(self.extrair_serie_temporal(
            texto, "população", anos, "pop"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "densidade demográfica", anos, "densidade"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "taxa de urbanização", anos, "taxa_urbanizacao"
        ))
        
        # Taxa de crescimento (apenas 3 valores)
        indicadores.update(self.extrair_serie_temporal(
            texto, "taxa média geométrica de crescimento", 
            [1991, 2000, 2010], 
            "taxa_crescimento"
        ))
        
        # Tabela 3.2 - População por domicílio e sexo (página 19)
        indicadores.update(self.extrair_serie_temporal(
            texto, "urbana", [2022], "pop_urbana"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "rural", [2022], "pop_rural"
        ))
        
        # Adicionar extração da página 20 para Tabelas 3.4 e 3.5 se necessário
        texto_p20 = self.extrair_texto_pagina(19)  # Página 20
        
        # Longevidade e mortalidade (Tabela 3.5)
        indicadores.update(self.extrair_serie_temporal(
            texto_p20, "esperança de vida ao nascer", [1991, 2000, 2010], "esperanca_vida"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p20, "mortalidade infantil", [1991, 2000, 2010], "mortalidade_infantil"
        ))
        
        return indicadores
    
    def extrair_idh(self) -> Dict:
        """
        Extrai indicadores de IDH (Capítulo 4, Página 25)
        Tabela 4.1
        """
        texto = self.extrair_texto_pagina(24)  # Página 25
        indicadores = {}
        anos = [1991, 2000, 2010]
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "idhm", anos, "idh"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "renda", anos, "idh_renda"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "longevidade", anos, "idh_longevidade"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto, "educação", anos, "idh_educacao"
        ))
        
        return indicadores
    
    def extrair_economia(self) -> Dict:
        """
        Extrai indicadores econômicos (Capítulo 5)
        Páginas 30-31, 38, 41
        """
        indicadores = {}
        
        # Página 30 - PIB (Tabela 5.1)
        texto_p30 = self.extrair_texto_pagina(29)
        anos_pib = [2017, 2018, 2019, 2020, 2021]
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p30, "pib total", anos_pib, "pib_total"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p30, "pib per capita", anos_pib, "pib_per_capita"
        ))
        
        # Página 31 - VAB Setorial (Tabela 5.2)
        texto_p31 = self.extrair_texto_pagina(30)
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p31, "agropecuária", anos_pib, "vab_agropecuaria"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p31, "indústria", anos_pib, "vab_industria"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p31, "serviços", anos_pib, "vab_servicos"
        ))
        
        # Página 38 - Produção Agrícola (Tabela 5.14/5.15)
        texto_p38 = self.extrair_texto_pagina(37)
        anos_agro = [2019, 2020, 2021, 2022, 2023]
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p38, "soja", anos_agro, "producao_soja"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p38, "milho", anos_agro, "producao_milho"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p38, "arroz", anos_agro, "producao_arroz"
        ))
        
        # Página 41 - Rebanhos (Tabela 5.16)
        texto_p41 = self.extrair_texto_pagina(40)
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p41, "bovino", anos_agro, "rebanho_bovino"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p41, "suíno", anos_agro, "rebanho_suino"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p41, "galinhas", anos_agro, "rebanho_aves"
        ))
        
        return indicadores
    
    def extrair_educacao(self) -> Dict:
        """
        Extrai indicadores de educação (Capítulo 6)
        Páginas 45-46
        """
        indicadores = {}
        
        # Página 45 - IDEB (Tabela 6.1)
        texto_p45 = self.extrair_texto_pagina(44)
        anos_ideb = [2013, 2015, 2017, 2019, 2021, 2023]
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p45, "anos iniciais", anos_ideb, "ideb_anos_iniciais"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p45, "anos finais", anos_ideb, "ideb_anos_finais"
        ))
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p45, "ensino médio", anos_ideb, "ideb_ensino_medio"
        ))
        
        # Página 46 - Alfabetização (Tabela 6.2)
        texto_p46 = self.extrair_texto_pagina(45)
        anos_alfa = [2000, 2010, 2022]
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p46, "taxa de alfabetização", anos_alfa, "taxa_alfabetizacao"
        ))
        
        return indicadores
    
    def extrair_saneamento(self) -> Dict:
        """
        Extrai indicadores de saneamento (Capítulo 8)
        Páginas 59-61
        """
        indicadores = {}
        anos_saneamento = [1991, 2000, 2010, 2021]
        
        # Página 59 - Abastecimento de água (Tabela 8.1)
        texto_p59 = self.extrair_texto_pagina(58)
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p59, "rede geral", anos_saneamento, "agua_rede_geral"
        ))
        
        # Página 60 - Esgotamento sanitário (Tabela 8.3)
        texto_p60 = self.extrair_texto_pagina(59)
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p60, "rede geral ou pluvial", anos_saneamento, "esgoto_rede_geral"
        ))
        
        # Página 61 - Destino do lixo (Tabela 8.4)
        texto_p61 = self.extrair_texto_pagina(60)
        
        indicadores.update(self.extrair_serie_temporal(
            texto_p61, "coletado", anos_saneamento, "lixo_coletado"
        ))
        
        return indicadores
    
    # ===== ORQUESTRAÇÃO =====
    
    def extrair_todos_indicadores(self) -> Dict:
        """
        Extrai todos os indicadores de prioridade alta
        """
        print("🔍 Iniciando extração de indicadores de prioridade alta...")
        
        # Demografia
        print("📊 Extraindo demografia...")
        self.dados["indicadores"].update(self.extrair_demografia())
        
        # IDH
        print("📊 Extraindo IDH...")
        self.dados["indicadores"].update(self.extrair_idh())
        
        # Economia
        print("📊 Extraindo economia...")
        self.dados["indicadores"].update(self.extrair_economia())
        
        # Educação
        print("📊 Extraindo educação...")
        self.dados["indicadores"].update(self.extrair_educacao())
        
        # Saneamento
        print("📊 Extraindo saneamento...")
        self.dados["indicadores"].update(self.extrair_saneamento())
        
        print(f"✅ Extração concluída! {len(self.dados['indicadores'])} indicadores extraídos.")
        
        return self.dados
    
    def salvar_json(self, arquivo_saida: str):
        """Salva os dados extraídos em JSON"""
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=2)
        print(f"💾 Dados salvos em: {arquivo_saida}")


def main():
    """Função principal para testes"""
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python extrator_prioridade_alta_v2.py <caminho_pdf> [arquivo_saida.json]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    arquivo_saida = sys.argv[2] if len(sys.argv) > 2 else "dados_extraidos.json"
    
    # Criar extrator e processar
    extrator = ExtratadorPerfilSEPLAN(pdf_path)
    dados = extrator.extrair_todos_indicadores()
    
    # Salvar resultados
    extrator.salvar_json(arquivo_saida)
    
    # Mostrar resumo
    print("\n📋 RESUMO DA EXTRAÇÃO:")
    print(f"   Total de indicadores: {len(dados['indicadores'])}")
    print(f"   Arquivo de saída: {arquivo_saida}")


if __name__ == "__main__":
    main()
