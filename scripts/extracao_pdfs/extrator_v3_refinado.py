#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator de Indicadores - Versão 3 (Refinada)
Lógica aprimorada para maior precisão na extração

MELHORIAS:
- Identifica anos no cabeçalho da tabela
- Extrai valores da linha de dados correspondente
- Mapeia posições dos anos às posições dos valores
- Melhor tratamento de números formatados (milhares, decimais)

Autor: Manus AI
Data: 27/01/2026
"""

import pdfplumber
import re
import json
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class ExtratadorPerfilSEPLANv3:
    """
    Extrator aprimorado com maior precisão na identificação de valores
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
        
        Exemplos:
        - "24.334" -> 24334.0 (milhares)
        - "10,9" -> 10.9 (decimal)
        - "97,7%" -> 97.7 (percentual)
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
            # Regra: se houver mais de um ponto, são separadores de milhar
            if numero_str.count('.') > 1:
                numero_str = numero_str.replace('.', '')
            # Se houver apenas um ponto e o número depois dele tiver 3 dígitos,
            # é separador de milhar
            elif '.' in numero_str:
                partes = numero_str.split('.')
                if len(partes[-1]) == 3 and len(partes) == 2:
                    numero_str = numero_str.replace('.', '')
        
        try:
            return float(numero_str)
        except ValueError:
            return None
    
    def extrair_serie_temporal_precisa(
        self,
        texto: str,
        palavra_chave_indicador: str,
        anos_esperados: List[int],
        prefixo: str,
        janela_busca: int = 10
    ) -> Dict[str, float]:
        """
        Extrai série temporal com alta precisão
        
        Estratégia:
        1. Encontra a linha que contém a palavra-chave do indicador
        2. Verifica se há uma linha com os anos (cabeçalho)
        3. Extrai a linha de valores IMEDIATAMENTE após a linha do indicador
        4. Mapeia valores às posições dos anos
        
        Args:
            texto: Texto da página
            palavra_chave_indicador: Palavra que identifica a linha do indicador
            anos_esperados: Lista de anos na série
            prefixo: Prefixo para nomear indicadores
            janela_busca: Número de linhas para buscar antes/depois
        
        Returns:
            Dict com indicadores extraídos
        """
        linhas = texto.split('\n')
        resultado = {}
        
        # PASSO 1: Encontrar linha com a palavra-chave
        idx_indicador = -1
        for i, linha in enumerate(linhas):
            if palavra_chave_indicador.lower() in linha.lower():
                idx_indicador = i
                break
        
        if idx_indicador == -1:
            return {}
        
        # PASSO 2: Procurar linha com anos (cabeçalho da tabela)
        idx_anos = -1
        linha_anos = ""
        
        # Buscar para trás (acima da linha do indicador)
        for i in range(max(0, idx_indicador - janela_busca), idx_indicador):
            linha = linhas[i]
            # Verificar se a linha contém anos
            anos_encontrados = re.findall(r'\b(19\d{2}|20\d{2})\b', linha)
            if len(anos_encontrados) >= 2:  # Pelo menos 2 anos = cabeçalho
                idx_anos = i
                linha_anos = linha
                break
        
        # Se não encontrou acima, buscar na própria linha ou abaixo
        if idx_anos == -1:
            for i in range(idx_indicador, min(len(linhas), idx_indicador + 3)):
                linha = linhas[i]
                anos_encontrados = re.findall(r'\b(19\d{2}|20\d{2})\b', linha)
                if len(anos_encontrados) >= 2:
                    idx_anos = i
                    linha_anos = linha
                    break
        
        if idx_anos == -1:
            # Sem linha de anos, tentar extração simples
            return self._extrair_fallback(linhas, idx_indicador, anos_esperados, prefixo)
        
        # PASSO 3: Identificar posições dos anos na linha de cabeçalho
        posicoes_anos = {}
        for ano in anos_esperados:
            match = re.search(rf'\b{ano}\b', linha_anos)
            if match:
                posicoes_anos[ano] = match.start()
        
        # PASSO 4: Extrair linha de valores (logo após a linha do indicador)
        idx_valores = idx_indicador + 1
        if idx_valores >= len(linhas):
            return {}
        
        linha_valores = linhas[idx_valores]
        
        # PASSO 5: Extrair todos os números da linha de valores
        # Regex que captura números com pontos e vírgulas
        numeros_brutos = re.findall(r'\d+(?:\.\d+)*(?:,\d+)?%?', linha_valores)
        
        # PASSO 6: Limpar e converter números
        numeros_limpos = []
        for num in numeros_brutos:
            valor = self.limpar_numero(num)
            if valor is not None:
                numeros_limpos.append(valor)
        
        # PASSO 7: Mapear valores aos anos
        # Se temos o mesmo número de valores e anos, mapeamento direto
        if len(numeros_limpos) == len(anos_esperados):
            for i, ano in enumerate(anos_esperados):
                chave = f"{prefixo}_{ano}"
                resultado[chave] = numeros_limpos[i]
        # Senão, tentar mapear por posição no texto
        else:
            # Extrair posições dos números na linha
            posicoes_numeros = []
            for num in numeros_brutos:
                match = re.search(re.escape(num), linha_valores)
                if match:
                    posicoes_numeros.append((match.start(), self.limpar_numero(num)))
            
            # Mapear cada ano ao número mais próximo
            for ano, pos_ano in posicoes_anos.items():
                # Encontrar número mais próximo à direita da posição do ano
                melhor_num = None
                menor_dist = float('inf')
                
                for pos_num, valor in posicoes_numeros:
                    dist = abs(pos_num - pos_ano)
                    if dist < menor_dist:
                        menor_dist = dist
                        melhor_num = valor
                
                if melhor_num is not None:
                    chave = f"{prefixo}_{ano}"
                    resultado[chave] = melhor_num
        
        return resultado
    
    def _extrair_fallback(
        self, 
        linhas: List[str], 
        idx_indicador: int, 
        anos: List[int],
        prefixo: str
    ) -> Dict[str, float]:
        """
        Método de fallback: extração simples quando não há cabeçalho claro
        """
        resultado = {}
        
        # Verificar linha do indicador e próximas 3 linhas
        for i in range(idx_indicador, min(len(linhas), idx_indicador + 4)):
            linha = linhas[i]
            
            # Extrair anos e números da mesma linha
            anos_linha = re.findall(r'\b(19\d{2}|20\d{2})\b', linha)
            numeros_brutos = re.findall(r'\d+(?:\.\d+)*(?:,\d+)?%?', linha)
            
            # Filtrar números que não são anos
            numeros = []
            for num in numeros_brutos:
                if num not in anos_linha:
                    valor = self.limpar_numero(num)
                    if valor is not None:
                        numeros.append(valor)
            
            # Se encontrou anos e números, mapear
            if anos_linha and numeros:
                for j, ano_str in enumerate(anos_linha):
                    ano = int(ano_str)
                    if ano in anos and j < len(numeros):
                        chave = f"{prefixo}_{ano}"
                        resultado[chave] = numeros[j]
        
        return resultado
    
    # ===== FUNÇÕES DE EXTRAÇÃO POR CAPÍTULO =====
    
    def extrair_demografia(self) -> Dict:
        """Extrai indicadores demográficos (Capítulo 3, Página 19)"""
        texto = self.extrair_texto_pagina(18)
        indicadores = {}
        anos = [1991, 2000, 2010, 2022]
        
        # População
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto, "população (número de pessoas)", anos, "pop"
        ))
        
        # Densidade Demográfica
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto, "densidade demográfica", anos, "densidade"
        ))
        
        # Taxa de Urbanização
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto, "taxa de urbanização", anos, "taxa_urbanizacao"
        ))
        
        return indicadores
    
    def extrair_idh(self) -> Dict:
        """Extrai IDH (Capítulo 4, Página 25)"""
        texto = self.extrair_texto_pagina(24)
        indicadores = {}
        anos = [1991, 2000, 2010]
        
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto, "idhm", anos, "idh"
        ))
        
        return indicadores
    
    def extrair_economia(self) -> Dict:
        """Extrai economia (Capítulo 5)"""
        indicadores = {}
        anos_pib = [2017, 2018, 2019, 2020, 2021]
        
        # PIB
        texto_p30 = self.extrair_texto_pagina(29)
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto_p30, "pib", anos_pib, "pib_total"
        ))
        
        # VAB
        texto_p31 = self.extrair_texto_pagina(30)
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto_p31, "agropecuária", anos_pib, "vab_agropecuaria"
        ))
        
        return indicadores
    
    def extrair_educacao(self) -> Dict:
        """Extrai educação (Capítulo 6)"""
        indicadores = {}
        
        # IDEB
        texto_p45 = self.extrair_texto_pagina(44)
        anos_ideb = [2013, 2015, 2017, 2019, 2021, 2023]
        
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto_p45, "anos iniciais", anos_ideb, "ideb_anos_iniciais"
        ))
        
        return indicadores
    
    def extrair_saneamento(self) -> Dict:
        """Extrai saneamento (Capítulo 8)"""
        indicadores = {}
        anos = [1991, 2000, 2010, 2021]
        
        texto_p59 = self.extrair_texto_pagina(58)
        indicadores.update(self.extrair_serie_temporal_precisa(
            texto_p59, "rede geral", anos, "agua_rede_geral"
        ))
        
        return indicadores
    
    def extrair_todos_indicadores(self) -> Dict:
        """Extrai todos os indicadores"""
        print("🔍 Iniciando extração com método aprimorado...")
        
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
        
        print(f"✅ {len(self.dados['indicadores'])} indicadores extraídos")
        
        return self.dados
    
    def salvar_json(self, arquivo_saida: str):
        """Salva dados em JSON"""
        Path(arquivo_saida).parent.mkdir(parents=True, exist_ok=True)
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=2)
        print(f"💾 Salvo em: {arquivo_saida}")


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python extrator_v3_refinado.py <pdf> [saida.json]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    saida = sys.argv[2] if len(sys.argv) > 2 else "dados_extraidos_v3.json"
    
    extrator = ExtratadorPerfilSEPLANv3(pdf_path)
    extrator.extrair_todos_indicadores()
    extrator.salvar_json(saida)


if __name__ == "__main__":
    main()
