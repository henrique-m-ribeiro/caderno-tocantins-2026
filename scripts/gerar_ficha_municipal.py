#!/usr/bin/env python3
"""
Script para gerar fichas municipais de 2 páginas baseadas na análise direta dos PDFs SEPLAN-TO.

Autor: Claude Code
Data: 2026-01-28
Versão: 1.0
"""

import pdfplumber
import pandas as pd
import json
from pathlib import Path
import re
from datetime import datetime


class GeradorFichaMunicipal:
    """Gera fichas municipais a partir da análise direta dos PDFs SEPLAN-TO."""

    def __init__(self, pdf_dir='Perfil Municipios Tocantins', base_dados_path='dados/finais/BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx', json_dir='dados/brutos/extraidos-perfis'):
        self.pdf_dir = Path(pdf_dir)
        self.base_dados_path = Path(base_dados_path)
        self.json_dir = Path(json_dir)

        # Carregar base de dados para metadados territoriais
        print(f"Carregando base de dados de {base_dados_path}...")
        self.df_base = pd.read_excel(base_dados_path)
        print(f"✅ Base carregada: {self.df_base.shape[0]} municípios")

    def localizar_json(self, municipio):
        """Localiza o JSON v9 do município."""
        nome_normalizado = municipio.lower().replace(' ', '_')
        nome_normalizado = self._remover_acentos(nome_normalizado)

        # Tentar várias variações
        variacoes = [
            f"{nome_normalizado}_v9.json",
            f"{nome_normalizado}_perfil_v9.json",
        ]

        for variacao in variacoes:
            json_path = self.json_dir / variacao
            if json_path.exists():
                return json_path

        # Busca case-insensitive
        for json_file in self.json_dir.glob("*_v9.json"):
            if nome_normalizado in json_file.stem.lower():
                return json_file

        print(f"⚠️ JSON v9 não encontrado para {municipio}")
        return None

    def carregar_json_v9(self, json_path):
        """Carrega dados do JSON v9."""
        if json_path is None or not json_path.exists():
            return {}

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return data.get('indicadores', {})

    def localizar_pdf(self, municipio):
        """Localiza o PDF do município."""
        # Normalizar nome do município
        nome_normalizado = municipio.lower().replace(' ', '_')
        nome_normalizado = self._remover_acentos(nome_normalizado)

        # Tentar várias variações de nome
        variacoes = [
            f"{nome_normalizado}_perfil_2024pdf.pdf",
            f"{nome_normalizado}_2024pdf.pdf",
            f"{nome_normalizado}.pdf",
        ]

        for variacao in variacoes:
            pdf_path = self.pdf_dir / variacao
            if pdf_path.exists():
                return pdf_path

        # Se não encontrou, tentar busca case-insensitive
        for pdf_file in self.pdf_dir.glob("*.pdf"):
            if nome_normalizado in pdf_file.stem.lower():
                return pdf_file

        raise FileNotFoundError(f"PDF não encontrado para {municipio}. Tentou: {variacoes}")

    def _remover_acentos(self, texto):
        """Remove acentos de um texto."""
        acentos = {
            'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i',
            'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u',
            'ç': 'c'
        }
        for a, b in acentos.items():
            texto = texto.replace(a, b)
        return texto

    def extrair_texto_pdf(self, pdf_path):
        """Extrai todo o texto de um PDF."""
        print(f"Extraindo texto de {pdf_path.name}...")
        texto_completo = []

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                texto = page.extract_text()
                if texto:
                    texto_completo.append(texto)

        print(f"✅ {len(texto_completo)} páginas extraídas")
        return "\n\n".join(texto_completo)

    def obter_metadados_territoriais(self, municipio):
        """Obtém metadados territoriais da base de dados."""
        municipio_data = self.df_base[self.df_base['terr_nome'] == municipio]

        if len(municipio_data) == 0:
            print(f"⚠️ Município {municipio} não encontrado na base de dados - usando valores padrão")
            return {
                'nome': municipio,
                'codigo_ibge': 'N/D',
                'microrregiao': 'N/D',
                'mesorregiao': 'N/D',
                'area_km2': 'N/D',
            }

        municipio_data = municipio_data.iloc[0]

        return {
            'nome': municipio,
            'codigo_ibge': municipio_data.get('terr_codigo_ibge', 'N/D'),
            'microrregiao': municipio_data.get('terr_microrregiao', 'N/D'),
            'mesorregiao': municipio_data.get('terr_mesorregiao', 'N/D'),
            'area_km2': municipio_data.get('terr_area_km2', 'N/D'),
        }

    def analisar_pdf(self, texto_pdf, metadados, indicadores_json=None):
        """Analisa o conteúdo do PDF e extrai informações estruturadas."""
        if indicadores_json is None:
            indicadores_json = {}

        analise = {
            'metadados': metadados,
            'indicadores': indicadores_json,  # Usar dados do JSON v9
            'texto_original': texto_pdf
        }

        return analise

    def gerar_ficha_markdown(self, analise, output_path):
        """Gera a ficha municipal em formato Markdown (2 páginas)."""
        metadados = analise['metadados']
        ind = analise['indicadores']  # Dados do JSON v9

        # Função auxiliar para formatar números
        def fmt_num(valor, formato='int', sufixo=''):
            if valor is None or pd.isna(valor):
                return None  # Retorna None em vez de 'N/D'
            try:
                if formato == 'int':
                    return f"{int(valor):,}".replace(',', '.') + sufixo
                elif formato == 'float':
                    return f"{float(valor):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') + sufixo
                else:
                    return str(valor) + sufixo
            except:
                return None

        # Função para gerar linha de tabela (oculta se valor é None)
        def linha_tabela(label, valor, obs='-'):
            if valor is None:
                return None
            return f"| {label} | {valor} | {obs} |"

        # Função para gerar linha de tabela dupla (com 2 valores)
        def linha_tabela_dupla(label, valor1, valor2, obs='-'):
            if valor1 is None and valor2 is None:
                return None
            v1 = valor1 if valor1 is not None else 'N/D'
            v2 = valor2 if valor2 is not None else 'N/D'
            return f"| {label} | {v1} | {v2} | {obs} |"

        # Template da ficha (estrutura de 2 páginas)
        ficha = f"""# {metadados['nome'].upper()} - FICHA MUNICIPAL

**Código IBGE**: {metadados['codigo_ibge']} | **Microrregião**: {metadados['microrregiao']} | **Área**: {fmt_num(metadados['area_km2'], 'float')} km²

---

## PÁGINA 1

### 📊 Dados Básicos

| Indicador | Valor |
|-----------|-------|
{chr(10).join(filter(None, [
    f"| **População (2022)** | {v} |" if (v := fmt_num(ind.get('pop_2022'), 'int', ' hab')) else None,
    f"| **PIB Total (2021)** | R$ {v} |" if (v := fmt_num(ind.get('pib_total_2021'), 'float', ' mil')) else None,
    f"| **PIB per capita (2021)** | R$ {v} |" if (v := fmt_num(ind.get('pib_per_capita_2021'), 'float')) else None,
    f"| **IDHM (2010)** | {v} |" if (v := fmt_num(ind.get('idhm_2010'), 'float')) else None,
    f"| **Área Territorial** | {v} km² |" if (v := fmt_num(metadados['area_km2'], 'float')) else None,
    f"| **Microrregião** | {metadados['microrregiao']} |" if metadados['microrregiao'] != 'N/D' else None
]))}


---

### 🎯 Síntese Estratégica

#### Pontos Fortes
- [A DEFINIR: Análise dos principais ativos do município]
- [A DEFINIR: Vantagens competitivas identificadas]
- [A DEFINIR: Recursos e potencialidades destacadas]

#### Desafios Prioritários
- [A DEFINIR: Principais gargalos identificados]
- [A DEFINIR: Problemas estruturais evidentes]
- [A DEFINIR: Áreas que demandam atenção]

#### Oportunidades
- [A DEFINIR: Potenciais de desenvolvimento]
- [A DEFINIR: Áreas para investimento]
- [A DEFINIR: Parcerias estratégicas possíveis]

---

### 1️⃣ Dimensão: Dados Sociais e Demográficos

**Indicadores-Chave**:

| Indicador | Valor | Observação |
|-----------|-------|------------|
{chr(10).join(filter(None, [
    linha_tabela('População 2022', fmt_num(ind.get('pop_2022'), 'int', ' hab')),
    linha_tabela('População 2010', fmt_num(ind.get('pop_2010'), 'int', ' hab')),
    linha_tabela('IDHM 2010', fmt_num(ind.get('idhm_2010'), 'float')),
    linha_tabela('IDHM Renda 2010', fmt_num(ind.get('idhm_renda_2010'), 'float')),
    linha_tabela('IDHM Longevidade 2010', fmt_num(ind.get('idhm_longevidade_2010'), 'float')),
    linha_tabela('IDHM Educação 2010', fmt_num(ind.get('idhm_educacao_2010'), 'float')),
    linha_tabela('Densidade demográfica 2022', fmt_num(ind.get('densidade_2022'), 'float', ' hab/km²')),
    linha_tabela('Taxa de urbanização 2022', fmt_num(ind.get('taxa_urbanizacao_2022'), 'float', '%'))
]))}

**Análise**:

[A DEFINIR: Análise contextualizada dos dados sociais e demográficos, explicando tendências de crescimento populacional, perfil urbano/rural, e implicações para políticas públicas]

---

### 2️⃣ Dimensão: Economia

**Indicadores-Chave**:

| Indicador | Valor (2021) | Observação |
|-----------|--------------|------------|
{chr(10).join(filter(None, [
    linha_tabela('PIB Total', 'R$ ' + v if (v := fmt_num(ind.get('pib_total_2021'), 'float', ' mil')) else None),
    linha_tabela('PIB per capita', 'R$ ' + v if (v := fmt_num(ind.get('pib_per_capita_2021'), 'float')) else None),
    linha_tabela('VAB Agropecuária', 'R$ ' + v if (v := fmt_num(ind.get('vab_agropecuaria_2021'), 'float', ' mil')) else None),
    linha_tabela('VAB Indústria', 'R$ ' + v if (v := fmt_num(ind.get('vab_industria_2021'), 'float', ' mil')) else None),
    linha_tabela('VAB Serviços', 'R$ ' + v if (v := fmt_num(ind.get('vab_servicos_2021'), 'float', ' mil')) else None),
    linha_tabela('Emprego Formal (2023)', fmt_num(ind.get('emprego_formal_estoque_2023'), 'int', ' postos'))
]))}

**Análise**:

[A DEFINIR: Análise da estrutura econômica do município, destacando setores dinâmicos, dependências, e potencial de diversificação econômica]

---

### 3️⃣ Dimensão: Educação

**Indicadores-Chave**:

| Indicador | Valor | Observação |
|-----------|-------|------------|
{chr(10).join(filter(None, [
    linha_tabela('Taxa de alfabetização 2022', fmt_num(ind.get('taxa_alfabetizacao_2022'), 'float', '%')),
    linha_tabela('Taxa de alfabetização 2010', fmt_num(ind.get('taxa_alfabetizacao_2010'), 'float', '%')),
    linha_tabela('IDEB Anos Finais 2023', fmt_num(ind.get('ideb_anos_finais_2023'), 'float')),
    linha_tabela('IDEB Anos Finais 2021', fmt_num(ind.get('ideb_anos_finais_2021'), 'float')),
    linha_tabela('IDEB Anos Finais 2019', fmt_num(ind.get('ideb_anos_finais_2019'), 'float'))
]))}

**Análise**:

[A DEFINIR: Análise do cenário educacional, identificando avanços, desafios em infraestrutura escolar, qualidade do ensino, e propostas de melhoria]

---

### 4️⃣ Dimensão: Saúde e Saneamento

**Indicadores-Chave**:

| Indicador | Valor | Observação |
|-----------|-------|------------|
{chr(10).join(filter(None, [
    linha_tabela('Estabelecimentos UBS (2023)', fmt_num(ind.get('estabelecimentos_ubs_2023'), 'int', ' unidades')),
    linha_tabela('Estabelecimentos Hospitalares (2023)', fmt_num(ind.get('estabelecimentos_hospital_2023'), 'int', ' unidades')),
    linha_tabela('Domicílios c/ água rede geral (2022)', fmt_num(ind.get('agua_rede_geral_2022'), 'int', ' domicílios')),
    linha_tabela('Domicílios c/ esgoto rede geral (2022)', fmt_num(ind.get('esgoto_rede_geral_2022'), 'int', ' domicílios')),
    linha_tabela('Domicílios c/ lixo coletado (2022)', fmt_num(ind.get('lixo_coletado_2022'), 'int', ' domicílios'))
]))}

**Análise**:

[A DEFINIR: Análise da infraestrutura de saúde e saneamento, capacidade de atendimento, e necessidades de investimento no setor]

---

## PÁGINA 2

### 5️⃣ Dimensão: Agropecuária e Desenvolvimento Rural

**Indicadores-Chave**:

| Indicador | Valor (2021) | Observação |
|-----------|--------------|------------|
{chr(10).join(filter(None, [
    linha_tabela('VAB Agropecuária', 'R$ ' + v if (v := fmt_num(ind.get('vab_agropecuaria_2021'), 'float', ' mil')) else None),
    linha_tabela('VAB Agropecuária 2017', 'R$ ' + v if (v := fmt_num(ind.get('vab_agropecuaria_2017'), 'float', ' mil')) else None, 'Comparação histórica')
]))}

**Análise**:

[A DEFINIR: Análise do setor agropecuário, destacando vocações produtivas, tecnologias utilizadas, e oportunidades de agregação de valor]

---

### 6️⃣ Dimensão: Finanças Públicas

**Indicadores-Chave**:

| Indicador | Valor (2023) | Valor (2019) | Variação |
|-----------|--------------|--------------|----------|
{chr(10).join(filter(None, [
    linha_tabela_dupla('Transferências totais', 'R$ ' + v if (v := fmt_num(ind.get('transferencias_total_2023'), 'float', ' mil')) else None, 'R$ ' + v if (v := fmt_num(ind.get('transferencias_total_2019'), 'float', ' mil')) else None),
    linha_tabela_dupla('FPM', 'R$ ' + v if (v := fmt_num(ind.get('fpm_2023'), 'float', ' mil')) else None, 'R$ ' + v if (v := fmt_num(ind.get('fpm_2019'), 'float', ' mil')) else None),
    linha_tabela_dupla('ICMS', 'R$ ' + v if (v := fmt_num(ind.get('icms_2023'), 'float', ' mil')) else None, 'R$ ' + v if (v := fmt_num(ind.get('icms_2019'), 'float', ' mil')) else None),
    linha_tabela_dupla('IPVA', 'R$ ' + v if (v := fmt_num(ind.get('ipva_2023'), 'float', ' mil')) else None, 'R$ ' + v if (v := fmt_num(ind.get('ipva_2019'), 'float', ' mil')) else None),
    linha_tabela_dupla('FUNDEB', 'R$ ' + v if (v := fmt_num(ind.get('fundeb_2023'), 'float', ' mil')) else None, 'R$ ' + v if (v := fmt_num(ind.get('fundeb_2019'), 'float', ' mil')) else None),
    linha_tabela_dupla('ITR', 'R$ ' + v if (v := fmt_num(ind.get('itr_2023'), 'float', ' mil')) else None, 'R$ ' + v if (v := fmt_num(ind.get('itr_2019'), 'float', ' mil')) else None)
]))}

**Análise**:

[A DEFINIR: Análise da dependência de transferências, autonomia fiscal, evolução das receitas, e capacidade de investimento do município]

---

## 🔗 Análise Integrada e Propositiva

### Diagnóstico Integrado

[A DEFINIR: Parágrafo explicando como as diferentes dimensões se conectam para explicar a realidade do município. Por exemplo: como a estrutura econômica impacta a arrecadação municipal, como a infraestrutura logística afeta o escoamento da produção agropecuária, etc.]

### Diretrizes para o Plano de Governo

[A DEFINIR: Parágrafo com sugestões de ações e políticas públicas estaduais, focando em parcerias Estado-Município-União, investimentos prioritários, e oportunidades de desenvolvimento sustentável]

---
"""

        # Salvar ficha
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(ficha)

        print(f"✅ Ficha gerada: {output_path}")
        return output_path

    def gerar_ficha(self, municipio, output_dir='parte-iii-fichas-municipais/prototipos'):
        """Gera ficha completa para um município."""
        print("\n" + "=" * 80)
        print(f"GERANDO FICHA MUNICIPAL: {municipio.upper()}")
        print("=" * 80)

        try:
            # 1. Localizar e carregar JSON v9
            json_path = self.localizar_json(municipio)
            indicadores_json = self.carregar_json_v9(json_path)
            if json_path:
                print(f"✅ JSON v9 localizado: {json_path.name} ({len(indicadores_json)} indicadores)")

            # 2. Localizar PDF
            pdf_path = self.localizar_pdf(municipio)
            print(f"✅ PDF localizado: {pdf_path.name}")

            # 3. Extrair texto do PDF
            texto_pdf = self.extrair_texto_pdf(pdf_path)

            # 4. Obter metadados territoriais
            metadados = self.obter_metadados_territoriais(municipio)

            # 5. Analisar PDF (agora com dados do JSON)
            analise = self.analisar_pdf(texto_pdf, metadados, indicadores_json)

            # 6. Gerar ficha Markdown
            nome_arquivo = f"FICHA-MUNICIPAL-{municipio.upper().replace(' ', '-')}.md"
            output_path = Path(output_dir) / nome_arquivo
            self.gerar_ficha_markdown(analise, output_path)

            print("=" * 80)
            print(f"✅ FICHA GERADA COM SUCESSO: {municipio}")
            print("=" * 80)

            return output_path

        except Exception as e:
            print(f"❌ Erro ao gerar ficha de {municipio}: {e}")
            raise


def main():
    """Função principal."""
    import sys

    if len(sys.argv) < 2:
        print("Uso: python gerar_ficha_municipal.py <nome_municipio>")
        print("Exemplo: python gerar_ficha_municipal.py Palmas")
        sys.exit(1)

    municipio = ' '.join(sys.argv[1:])

    gerador = GeradorFichaMunicipal()
    gerador.gerar_ficha(municipio)


if __name__ == '__main__':
    main()
