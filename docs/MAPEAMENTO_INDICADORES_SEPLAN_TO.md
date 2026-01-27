# Mapeamento de Indicadores: SEPLAN-TO → Estrutura V02

**Projeto:** Caderno Tocantins 2026 - Refatoração V02
**Fase:** Fase 1 - Análise de Viabilidade
**Data:** 27 de janeiro de 2026
**Fonte:** Perfis Socioeconômicos Municipais SEPLAN-TO (8ª Ed, Dez/2024)

---

## 📋 Objetivo

Este documento mapeia cada indicador da **Estrutura V02 planejada** para sua localização exata nos **PDFs SEPLAN-TO**, facilitando o desenvolvimento dos scripts de extração.

**Formato:**
- **Indicador V02:** Nome da coluna na planilha consolidada
- **Indicador SEPLAN:** Nome exato como aparece no PDF
- **Localização:** Capítulo e páginas aproximadas
- **Formato:** Como o dado está apresentado (tabela, texto, gráfico)
- **Observações:** Particularidades, anos de referência, cálculos necessários

---

## 🗂️ Mapeamento por Dimensão

### 1. IDENTIFICAÇÃO TERRITORIAL (11 colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 1 | `territorio_nome` | Nome do Município | Cap. 1, p.1 (capa) | Texto | Título principal |
| 2 | `territorio_cod_ibge` | Código IBGE | Cap. 1, p.12 | Texto/Tabela | 7 dígitos |
| 3 | `territorio_uf` | Estado | Cap. 1, p.1 | Texto | Fixo: "TO" ou "Tocantins" |
| 4 | `territorio_tipo` | - | - | - | **FIXO:** "Município" |
| 5 | `territorio_mesorregiao_ibge_1989` | Mesorregião | Cap. 1, p.13 | Texto | Class. antiga IBGE |
| 6 | `territorio_microrregiao_ibge_1989` | Microrregião | Cap. 1, p.13 | Texto | Class. antiga IBGE |
| 7 | `territorio_regiao_intermediaria_ibge_2017` | - | - | - | **NÃO PRESENTE** - pesquisar IBGE |
| 8 | `territorio_regiao_imediata_ibge_2017` | - | - | - | **NÃO PRESENTE** - pesquisar IBGE |
| 9 | `territorio_regiao_planejamento_seplan_2024` | Região de Planejamento | Cap. 1, p.14 | Texto | Portaria 91/2024 |
| 10 | `territorio_macrorregiao_seplan_2024` | Macrorregião | Cap. 1, p.14 | Texto | Norte/Central/Sul |
| 11 | `territorio_observacoes` | - | - | - | Campo livre para notas |

**Ações necessárias:**
- ⚠️ `regiao_intermediaria/imediata_ibge_2017`: Buscar em fonte externa (IBGE)
- ✅ Demais campos: Extrair dos PDFs SEPLAN-TO

---

### 2. DEMOGRAFIA (12 colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 12 | `demo_pop_2010` | População Total - 2010 | Cap. 2, p.16-17 | Tabela | Censo 2010 |
| 13 | `demo_pop_2010_ano_ref` | - | - | - | **FIXO:** 2010 |
| 14 | `demo_pop_2022` | População Total - 2022 | Cap. 2, p.16-17 | Tabela | Censo 2022 |
| 15 | `demo_pop_2022_ano_ref` | - | - | - | **FIXO:** 2022 |
| 16 | `demo_pop_2025_est` | População Estimada - 2025 | Cap. 2, p.16-17 | Tabela | Projeção IBGE |
| 17 | `demo_pop_2025_est_ano_ref` | - | - | - | **FIXO:** 2025 |
| 18 | `demo_cresc_2010_2022_pct` | - | - | Calculado | **(pop_2022 - pop_2010) / pop_2010 × 100** |
| 19 | `demo_area_km2` | Área Territorial (km²) | Cap. 1, p.12 | Tabela/Texto | Valor único |
| 20 | `demo_area_km2_ano_ref` | - | - | - | Ano da medição (geralmente 2021) |
| 21 | `demo_dens_dem_hab_km2` | Densidade Demográfica | Cap. 2, p.19 | Tabela | Ou calcular: pop_2022 / área |
| 22 | `demo_tx_urban_pct` | Taxa de Urbanização (%) | Cap. 2, p.20 | Tabela | Percentual |
| 23 | `demo_tx_urban_ano_ref` | - | - | - | Verificar ano (geralmente 2010 ou 2022) |

**Script de extração:**
```python
# Capítulo 2: Demografia (páginas 16-25)
def extrair_demografia(pdf):
    page = pdf.pages[15]  # Página 16 (índice 15)
    tables = page.extract_tables()

    # Primeira tabela geralmente contém população histórica
    pop_table = tables[0]
    # Processar linhas para extrair pop_2010, pop_2022, pop_2025_est
```

---

### 3. ECONOMIA (14+ colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 24 | `econ_pib_total_mil_reais` | PIB Total (mil reais) | Cap. 3, p.27-28 | Tabela | Valor mais recente (2020-2021) |
| 25 | `econ_pib_total_ano_ref` | - | - | - | Verificar ano na tabela |
| 26 | `econ_pib_per_capita_reais` | PIB per capita (reais) | Cap. 3, p.27-28 | Tabela | Mesmo ano que PIB total |
| 27 | `econ_pib_per_capita_ano_ref` | - | - | - | Mesmo que linha 25 |
| 28 | `econ_vab_agro_pct` | VAB Agropecuária (%) | Cap. 3, p.29-30 | Tabela/Gráfico | Percentual do VAB total |
| 29 | `econ_vab_agro_ano_ref` | - | - | - | Verificar ano (geralmente 2020-2021) |
| 30 | `econ_vab_industria_pct` | VAB Indústria (%) | Cap. 3, p.29-30 | Tabela/Gráfico | Percentual do VAB total |
| 31 | `econ_vab_industria_ano_ref` | - | - | - | Mesmo que linha 29 |
| 32 | `econ_vab_servicos_pct` | VAB Serviços (%) | Cap. 3, p.29-30 | Tabela/Gráfico | Percentual do VAB total |
| 33 | `econ_vab_servicos_ano_ref` | - | - | - | Mesmo que linha 29 |

**Validação importante:**
```python
# VAB setorial deve somar ~100% (tolerância ±2%)
assert abs(vab_agro + vab_industria + vab_servicos - 100) <= 2
```

---

### 4. DESENVOLVIMENTO HUMANO (10 colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 34 | `dev_idhm_2010` | IDHM 2010 | Cap. 7, p.66-67 | Tabela | Índice (0-1) |
| 35 | `dev_idhm_ano_ref` | - | - | - | **FIXO:** 2010 |
| 36 | `dev_idhm_renda_2010` | IDHM Renda 2010 | Cap. 7, p.66-67 | Tabela | Componente (0-1) |
| 37 | `dev_idhm_renda_ano_ref` | - | - | - | **FIXO:** 2010 |
| 38 | `dev_idhm_longevidade_2010` | IDHM Longevidade 2010 | Cap. 7, p.66-67 | Tabela | Componente (0-1) |
| 39 | `dev_idhm_longevidade_ano_ref` | - | - | - | **FIXO:** 2010 |
| 40 | `dev_idhm_educacao_2010` | IDHM Educação 2010 | Cap. 7, p.66-67 | Tabela | Componente (0-1) |
| 41 | `dev_idhm_educacao_ano_ref` | - | - | - | **FIXO:** 2010 |

**Validação:**
```python
# IDHM é a média geométrica dos 3 componentes
import numpy as np
idhm_calculado = np.power(idhm_renda * idhm_long * idhm_educ, 1/3)
assert abs(idhm_calculado - dev_idhm_2010) <= 0.001
```

---

### 5. EDUCAÇÃO (12+ colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 42 | `edu_ideb_anos_iniciais_2021` | IDEB Anos Iniciais 2021 | Cap. 4, p.42-43 | Tabela | Nota (0-10) |
| 43 | `edu_ideb_anos_iniciais_ano_ref` | - | - | - | Verificar ano (2021 ou 2023) |
| 44 | `edu_ideb_anos_finais_2021` | IDEB Anos Finais 2021 | Cap. 4, p.42-43 | Tabela | Nota (0-10) |
| 45 | `edu_ideb_anos_finais_ano_ref` | - | - | - | Mesmo que linha 43 |
| 46 | `edu_ideb_ensino_medio_2021` | IDEB Ensino Médio 2021 | Cap. 4, p.42-43 | Tabela | Nota (0-10) - pode ser N/A |
| 47 | `edu_ideb_ensino_medio_ano_ref` | - | - | - | Mesmo que linha 43 |
| 48 | `edu_tx_analfabetismo_pct` | Taxa de Analfabetismo (%) | Cap. 4, p.44 | Tabela | Percentual (pop 15+ anos) |
| 49 | `edu_tx_analfabetismo_ano_ref` | - | - | - | Verificar ano (Censo 2010/2022) |

**Casos especiais:**
- Municípios sem escola de ensino médio: IDEB Ensino Médio = N/A
- Verificar qual edição do IDEB está presente (2021 ou 2023)

---

### 6. SAÚDE (10+ colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 50 | `saude_mort_infantil_2022` | Mortalidade Infantil (por 1.000) | Cap. 5, p.52 | Tabela | Taxa |
| 51 | `saude_mort_infantil_ano_ref` | - | - | - | Verificar ano na tabela |
| 52 | `saude_cobertura_esf_pct` | Cobertura ESF (%) | Cap. 5, p.56 | Tabela | Percentual |
| 53 | `saude_cobertura_esf_ano_ref` | - | - | - | Verificar ano |
| 54 | `saude_estabelecimentos` | Estabelecimentos de Saúde | Cap. 5, p.53-54 | Tabela | Número total |
| 55 | `saude_estabelecimentos_ano_ref` | - | - | - | Verificar ano (CNES) |
| 56 | `saude_leitos` | Leitos Hospitalares | Cap. 5, p.55 | Tabela | Número total - pode ser N/A |
| 57 | `saude_leitos_ano_ref` | - | - | - | Verificar ano |

---

### 7. SANEAMENTO (10+ colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 58 | `sane_abastec_agua_pct` | Abastecimento de Água (%) | Cap. 6, p.60-62 | Tabela | % domicílios (rede geral) |
| 59 | `sane_abastec_agua_ano_ref` | - | - | - | Verificar ano (Censo 2010/2021) |
| 60 | `sane_esgoto_sanitario_pct` | Esgotamento Sanitário (%) | Cap. 6, p.63 | Tabela | % domicílios (rede coletora) |
| 61 | `sane_esgoto_sanitario_ano_ref` | - | - | - | Mesmo que linha 59 |
| 62 | `sane_coleta_lixo_pct` | Coleta de Lixo (%) | Cap. 6, p.64-65 | Tabela | % domicílios |
| 63 | `sane_coleta_lixo_ano_ref` | - | - | - | Mesmo que linha 59 |

**Observação:** Dados de saneamento têm série histórica (1991-2021). Extrair o ano mais recente disponível.

---

### 8. AGROPECUÁRIA (8+ colunas)

| # | Indicador V02 | Indicador SEPLAN | Localização | Formato | Observações |
|---|---------------|------------------|-------------|---------|-------------|
| 64 | `agro_valor_producao_mil_reais` | Valor da Produção (mil reais) | Cap. 3, p.39-40 | Tabela | Soma PAM + PPM + PEVS |
| 65 | `agro_valor_producao_ano_ref` | - | - | - | Verificar ano (geralmente 2021-2022) |
| 66 | `agro_producao_agricola` | Produção Agrícola (PAM) | Cap. 3, p.39-40 | Tabela/Texto | Principais culturas |
| 67 | `agro_producao_pecuaria` | Produção Pecuária (PPM) | Cap. 3, p.39-40 | Tabela/Texto | Principais rebanhos |

**Observação:** Pode haver detalhamento de produtos agrícolas e rebanhos. Extrair valor total ou principais itens conforme necessidade.

---

## 📊 Resumo de Cobertura

| Dimensão | Total Colunas V02 | Presentes nos PDFs | Cobertura | Fonte Alternativa Necessária |
|----------|-------------------|--------------------|-----------|------------------------------|
| Territorial | 11 | 9 | 82% | ⚠️ 2 (IBGE 2017) |
| Demografia | 12 | 12 | 100% | ✅ Nenhuma |
| Economia | 14+ | 14+ | 100% | ✅ Nenhuma |
| Desenvolvimento | 10 | 10 | 100% | ✅ Nenhuma |
| Educação | 12+ | 11+ | ~92% | ⚠️ Verificar IDEB 2023 |
| Saúde | 10+ | 10+ | 100% | ✅ Nenhuma |
| Saneamento | 10+ | 10+ | 100% | ✅ Nenhuma |
| Agropecuária | 8+ | 8+ | 100% | ✅ Nenhuma |
| **TOTAL** | **~65 colunas** | **~60 colunas** | **~92%** | **2-3 indicadores externos** |

---

## 🛠️ Estratégia de Extração por Capítulo

### Capítulo 1: Localização e Aspectos Físicos (p. 1-15)
```python
def extrair_cap1_territorial(pdf):
    """Extrai dados territoriais"""
    return {
        'territorio_nome': extrair_titulo_capa(pdf.pages[0]),
        'territorio_cod_ibge': extrair_codigo_ibge(pdf.pages[11]),
        'territorio_mesorregiao_ibge_1989': extrair_mesorregiao(pdf.pages[12]),
        'demo_area_km2': extrair_area_territorial(pdf.pages[11]),
    }
```

### Capítulo 2: Demografia (p. 16-25)
```python
def extrair_cap2_demografia(pdf):
    """Extrai todos os indicadores demográficos"""
    # Página 16-17: População histórica
    pop_table = pdf.pages[15].extract_tables()[0]

    return {
        'demo_pop_2010': extrair_valor(pop_table, '2010'),
        'demo_pop_2022': extrair_valor(pop_table, '2022'),
        'demo_pop_2025_est': extrair_valor(pop_table, '2025'),
        'demo_tx_urban_pct': extrair_urbanizacao(pdf.pages[19]),
    }
```

### Capítulo 3: Economia (p. 26-40)
```python
def extrair_cap3_economia(pdf):
    """Extrai indicadores econômicos"""
    # Páginas 27-28: PIB
    pib_page = pdf.pages[26]
    pib_table = pib_page.extract_tables()[0]

    # Páginas 29-30: VAB setorial
    vab_page = pdf.pages[28]
    vab_data = extrair_vab_setorial(vab_page)

    return {**pib_data, **vab_data}
```

### Capítulos 4-10: Similar
Seguir o mesmo padrão de extração para os demais capítulos.

---

## 🔄 Tratamento de Valores Ausentes

### Padrões Identificados

| Representação no PDF | Tratamento | Valor no CSV |
|---------------------|------------|--------------|
| `-` | Dado inexistente | `NULL` ou `None` |
| `x` | Dado não divulgado (sigilo) | `NULL` ou `None` |
| Célula vazia | Dado ausente | `NULL` ou `None` |
| `ND` ou `N/D` | Não disponível | `NULL` ou `None` |

### Script de Tratamento

```python
def tratar_valor_ausente(valor):
    """Padroniza valores ausentes"""
    if valor is None:
        return None

    valor_str = str(valor).strip()

    if valor_str in ['-', 'x', '', 'ND', 'N/D', 'N.D.', '...']:
        return None

    return valor
```

---

## 📋 Checklist de Validação por Município

Após extração, validar:

- [ ] Código IBGE tem 7 dígitos
- [ ] População 2022 > População 2010 (ou justificar decréscimo)
- [ ] VAB setorial soma ~100% (tolerância ±2%)
- [ ] IDHM está entre 0 e 1
- [ ] IDEB está entre 0 e 10
- [ ] Taxas de saneamento estão entre 0% e 100%
- [ ] PIB per capita = PIB total / População (tolerância ±R$100)
- [ ] Todos os `_ano_ref` estão preenchidos

---

## 🚀 Próximos Passos

### Fase 2: PoC (Prova de Conceito) - 2-3h

1. ✅ Criar `scripts/poc_extracao_demografia.py`
2. ✅ Implementar extração do Capítulo 2 (Demografia) apenas
3. ✅ Testar em Palmas.pdf
4. ✅ Validar resultados contra valores conhecidos
5. ✅ Documentar taxa de sucesso e problemas

### Fase 3: Extrator Completo - 8-12h

1. Expandir para todos os 10 capítulos
2. Criar funções especializadas por dimensão
3. Implementar validação inline
4. Testar em municípios de diferentes portes

### Fase 4: Extração em Lote - 4-6h

1. Processar 139 municípios
2. Gerar relatórios de cobertura
3. Executar 4 tipos de validação

---

**Elaborado em:** 27 de janeiro de 2026
**Sessão:** claude/integracao-caderno-tocantins-bSEfU
**Fase:** Fase 1 - Análise de Viabilidade
**Status:** ✅ CONCLUÍDO
**Próxima Fase:** Fase 2 - PoC com pdfplumber

---

**FIM DO MAPEAMENTO**
