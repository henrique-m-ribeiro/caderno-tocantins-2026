# PLANEJAMENTO: PLANILHAS CONSOLIDADAS DE DADOS
## Caderno Tocantins 2026

**Data:** 23 de janeiro de 2026
**Versão:** 1.0
**Status:** Planejamento

---

## 📋 SUMÁRIO

1. [Visão Geral](#1-visão-geral)
2. [Divisão Territorial do Tocantins](#2-divisão-territorial-do-tocantins)
3. [Planilha 1: Dados Consolidados](#3-planilha-1-dados-consolidados)
4. [Planilha 2: Metadados (Dicionário de Dados)](#4-planilha-2-metadados-dicionário-de-dados)
5. [Dimensões de Análise e Indicadores](#5-dimensões-de-análise-e-indicadores)
6. [Especificação Técnica](#6-especificação-técnica)
7. [Cronograma de Implementação](#7-cronograma-de-implementação)

---

## 1. VISÃO GERAL

### 1.1 Objetivo

Criar duas planilhas interligadas:

1. **Planilha de Dados Consolidados** - Reunindo todos os dados territoriais dos 139 municípios do Tocantins, organizados por mesorregiões e microrregiões
2. **Planilha de Metadados** - Dicionário de dados completo explicando cada variável/indicador

### 1.2 Princípios

- ✅ **Rigor:** Apenas dados já coletados serão incluídos (sem estimativas ou preenchimentos)
- ✅ **Rastreabilidade:** Todas as fontes e datas de coleta documentadas
- ✅ **Escalabilidade:** Estrutura preparada para expansão para outros estados
- ✅ **Transparência:** Lacunas explicitamente marcadas
- ✅ **Padrão:** Nomenclatura padronizada com prefixos por dimensão

---

## 2. DIVISÃO TERRITORIAL DO TOCANTINS

### 2.1 Estrutura Hierárquica (IBGE 1989-2017)

```
Estado do Tocantins (139 municípios)
│
├── Mesorregião OCIDENTAL (94 municípios)
│   ├── Microrregião de Araguaína (17 municípios)
│   ├── Microrregião do Bico do Papagaio (25 municípios)
│   ├── Microrregião de Gurupi (15 municípios)
│   ├── Microrregião de Miracema do Tocantins (23 municípios)
│   └── Microrregião de Rio Formoso (14 municípios)
│
└── Mesorregião ORIENTAL (45 municípios)
    ├── Microrregião de Dianópolis (18 municípios)
    ├── Microrregião do Jalapão (15 municípios)
    └── Microrregião de Porto Nacional (12 municípios)
```

### 2.2 Observação Importante

A divisão em mesorregiões e microrregiões foi utilizada pelo IBGE entre **1989 e 2017**. Em 2017, o IBGE criou uma nova divisão regional (Regiões Geográficas Intermediárias e Imediatas). No entanto, para fins de análise política e territorial, **utilizaremos a divisão anterior** conforme solicitado.

**Fonte:** [Wikiwand - Lista de mesorregiões e microrregiões do Tocantins](https://www.wikiwand.com/pt/Lista_de_mesorregi%C3%B5es_e_microrregi%C3%B5es_do_Tocantins)

---

## 3. PLANILHA 1: DADOS CONSOLIDADOS

### 3.1 Estrutura Geral

**Nome do arquivo:** `dados-consolidados-tocantins-v01.csv`

**Formato:** CSV (vírgula como separador)

**Encoding:** UTF-8

### 3.2 Organização das Linhas

A planilha terá a seguinte sequência de linhas:

1. **Linha 1:** Cabeçalho com códigos dos campos
2. **Linhas 2-N:** Municípios organizados hierarquicamente:
   - Agrupados por mesorregião
   - Dentro de cada mesorregião, agrupados por microrregião
   - Ordenação alfabética dentro de cada microrregião
   - Após cada microrregião: **linha consolidada da microrregião**
   - Após cada mesorregião: **linha consolidada da mesorregião**
3. **Última linha:** **Dados consolidados do Estado do Tocantins**

#### 3.2.1 Exemplo de Estrutura

```
[CABEÇALHO]
--- MESORREGIÃO OCIDENTAL ---
  --- MICRORREGIÃO DE ARAGUAÍNA ---
  Município 1
  Município 2
  ...
  Município 17
  [CONSOLIDADO MICRORREGIÃO ARAGUAÍNA]

  --- MICRORREGIÃO DO BICO DO PAPAGAIO ---
  Município 1
  Município 2
  ...
  Município 25
  [CONSOLIDADO MICRORREGIÃO BICO DO PAPAGAIO]

  ... (demais microrregiões)

  [CONSOLIDADO MESORREGIÃO OCIDENTAL]

--- MESORREGIÃO ORIENTAL ---
  ... (estrutura similar)
  [CONSOLIDADO MESORREGIÃO ORIENTAL]

[CONSOLIDADO ESTADO DO TOCANTINS]
```

### 3.3 Estrutura de Colunas

#### 3.3.1 Colunas de Identificação Territorial (1-6)

| Ordem | Código | Nome Completo | Tipo | Exemplo |
|-------|--------|---------------|------|---------|
| 1 | `territorio_nome` | Nome do Território | Texto | "Palmas" |
| 2 | `territorio_cod_ibge` | Código IBGE | Numérico (7 dígitos) | 1721000 |
| 3 | `territorio_uf` | Sigla da UF | Texto (2 chars) | "TO" |
| 4 | `territorio_mesorregiao` | Nome da Mesorregião | Texto | "Oriental" |
| 5 | `territorio_microrregiao` | Nome da Microrregião | Texto | "Porto Nacional" |
| 6 | `territorio_tipo` | Tipo de Território | Texto | "município", "microrregião", "mesorregião", "estado" |

#### 3.3.2 Colunas de Dados - Demografia (7-13)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 7 | `demo_pop_2010` | População 2010 | Numérico | habitantes |
| 8 | `demo_pop_2022` | População 2022 | Numérico | habitantes |
| 9 | `demo_pop_2025_est` | População 2025 (estimativa) | Numérico | habitantes |
| 10 | `demo_cresc_2010_2022_perc` | Crescimento 2010-2022 | Numérico | % |
| 11 | `demo_area_km2` | Área Territorial | Numérico | km² |
| 12 | `demo_densidade` | Densidade Demográfica | Numérico | hab/km² |
| 13 | `demo_urbanizacao_perc` | Taxa de Urbanização | Numérico | % |

#### 3.3.3 Colunas de Dados - Economia (14-19)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 14 | `econ_pib_total_milhoes` | PIB Total | Numérico | milhões R$ |
| 15 | `econ_pib_pc` | PIB per capita | Numérico | R$ |
| 16 | `econ_pib_ano_ref` | Ano referência PIB | Numérico | ano |
| 17 | `econ_vab_agro_perc` | VAB Agropecuária | Numérico | % |
| 18 | `econ_vab_ind_perc` | VAB Indústria | Numérico | % |
| 19 | `econ_vab_serv_perc` | VAB Serviços | Numérico | % |

#### 3.3.4 Colunas de Dados - Desenvolvimento Humano (20-21)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 20 | `desenv_idhm` | IDHM | Numérico | 0-1 |
| 21 | `desenv_idhm_ano_ref` | Ano referência IDHM | Numérico | ano |

#### 3.3.5 Colunas de Dados - Educação (22-27)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 22 | `edu_escol_6_14_perc` | Taxa Escolarização 6-14 anos | Numérico | % |
| 23 | `edu_ideb_ai_2023` | IDEB Anos Iniciais 2023 | Numérico | 0-10 |
| 24 | `edu_ideb_af_2023` | IDEB Anos Finais 2023 | Numérico | 0-10 |
| 25 | `edu_ideb_ai_2021` | IDEB Anos Iniciais 2021 | Numérico | 0-10 |
| 26 | `edu_ideb_af_2021` | IDEB Anos Finais 2021 | Numérico | 0-10 |
| 27 | `edu_analfab_15mais_perc` | Taxa Analfabetismo 15+ | Numérico | % |

#### 3.3.6 Colunas de Dados - Saúde (28-32)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 28 | `saude_mort_inf` | Mortalidade Infantil | Numérico | óbitos/1000 nascidos |
| 29 | `saude_mort_inf_ano_ref` | Ano ref. Mortalidade Infantil | Numérico | ano |
| 30 | `saude_cobert_esf_perc` | Cobertura ESF | Numérico | % |
| 31 | `saude_leitos_1000hab` | Leitos por 1000 hab | Numérico | leitos |
| 32 | `saude_medicos_1000hab` | Médicos por 1000 hab | Numérico | médicos |

#### 3.3.7 Colunas de Dados - Saneamento (33-38)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 33 | `san_agua_perc` | Abastecimento Água | Numérico | % |
| 34 | `san_esgoto_coleta_perc` | Coleta Esgoto | Numérico | % |
| 35 | `san_esgoto_trat_perc` | Tratamento Esgoto | Numérico | % |
| 36 | `san_residuos_coleta_perc` | Coleta Resíduos | Numérico | % |
| 37 | `san_ano_ref` | Ano referência SNIS | Numérico | ano |
| 38 | `san_fonte` | Fonte dados saneamento | Texto | ex: "SNIS 2023" |

#### 3.3.8 Colunas de Dados - Agropecuária (39-47)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 39 | `agro_vbp_milhoes` | VBP Agropecuário | Numérico | milhões R$ |
| 40 | `agro_vbp_ano_ref` | Ano ref. VBP | Numérico | ano |
| 41 | `agro_area_plantada_ha` | Área Plantada Total | Numérico | hectares |
| 42 | `agro_rebanho_bovino` | Rebanho Bovino | Numérico | cabeças |
| 43 | `agro_cultura_princ_1` | Cultura Principal 1 | Texto | ex: "soja" |
| 44 | `agro_cultura_princ_2` | Cultura Principal 2 | Texto | ex: "milho" |
| 45 | `agro_cultura_princ_3` | Cultura Principal 3 | Texto | ex: "arroz" |
| 46 | `agro_prod_1_ton` | Produção Cultura 1 | Numérico | toneladas |
| 47 | `agro_prod_2_ton` | Produção Cultura 2 | Numérico | toneladas |

#### 3.3.9 Colunas Especiais - Turismo (48-51)

| Ordem | Código | Nome Completo | Tipo | Unidade |
|-------|--------|---------------|------|---------|
| 48 | `tur_visitantes_ano` | Visitantes/ano | Numérico | visitantes |
| 49 | `tur_receita_milhoes` | Receita Turismo | Numérico | milhões R$ |
| 50 | `tur_atrativos` | Principais Atrativos | Texto | lista |
| 51 | `tur_ano_ref` | Ano referência | Numérico | ano |

#### 3.3.10 Coluna de Observações (52)

| Ordem | Código | Nome Completo | Tipo | Conteúdo |
|-------|--------|---------------|------|----------|
| 52 | `obs` | Observações | Texto | Contexto, alertas, destaques |

### 3.4 Convenções para Dados Faltantes

- **Células vazias:** Dados não coletados
- **"nd":** Não disponível (mesmo após tentativa de coleta)
- **"nc":** Não se aplica (ex: área plantada em município 100% urbano)
- **Linhas consolidadas:** Para indicadores não agregáveis (ex: IDHM), usar "nc"

### 3.5 Total de Linhas Esperadas

- Municípios: 139
- Consolidados de Microrregiões: 8
- Consolidados de Mesorregiões: 2
- Consolidado Estadual: 1
- **Total:** 150 linhas (+ 1 cabeçalho = 151 linhas)

---

## 4. PLANILHA 2: METADADOS (DICIONÁRIO DE DADOS)

### 4.1 Estrutura Geral

**Nome do arquivo:** `metadados-consolidados-tocantins-v01.csv`

**Formato:** CSV (vírgula como separador)

**Encoding:** UTF-8

### 4.2 Estrutura de Colunas

#### Linha 1: Cabeçalho

```csv
codigo,nome_curto,descricao_curta,data_referencia,fonte_primaria,data_coleta,metodo_coleta,caminho_atualizacao,tipo_dado,unidade,agregavel,formula_agregacao,observacoes,limitacoes
```

#### Linhas 2-53: Uma linha por coluna da Planilha 1

Cada linha da planilha de metadados corresponde a uma coluna da planilha de dados.

### 4.3 Especificação das Colunas de Metadados

| # | Código | Nome Completo | Descrição | Exemplo |
|---|--------|---------------|-----------|---------|
| 1 | `codigo` | Código da variável | Mesmo código usado no cabeçalho da Planilha 1 | "demo_pop_2022" |
| 2 | `nome_curto` | Nome curto | Nome resumido da variável | "População 2022" |
| 3 | `descricao_curta` | Descrição curta | Explicação breve do indicador | "População residente segundo Censo IBGE 2022" |
| 4 | `data_referencia` | Data de referência | Data/período a que se referem os dados | "2022" ou "2021-2023" |
| 5 | `fonte_primaria` | Fonte primária | Instituição/sistema fonte | "IBGE - Censo Demográfico" |
| 6 | `data_coleta` | Data da coleta | Quando os dados foram coletados | "2026-01-22" |
| 7 | `metodo_coleta` | Método de coleta | Como foram obtidos | "Download PDF Censo 2022" ou "API IBGE Cidades" |
| 8 | `caminho_atualizacao` | Caminho para atualização | URL, API endpoint ou caminho para atualizar | "https://cidades.ibge.gov.br/" |
| 9 | `tipo_dado` | Tipo de dado | Numérico, Texto, Data, etc. | "Numérico inteiro" |
| 10 | `unidade` | Unidade de medida | Unidade do indicador | "habitantes", "km²", "%", "R$" |
| 11 | `agregavel` | Agregável? | Se pode ser agregado (soma, média) | "Sim (soma)" ou "Não" |
| 12 | `formula_agregacao` | Fórmula de agregação | Como agregar para níveis superiores | "SOMA(municípios)" ou "MÉDIA PONDERADA POP" |
| 13 | `observacoes` | Observações | Informações adicionais importantes | "Dados preliminares sujeitos a revisão" |
| 14 | `limitacoes` | Limitações | Restrições, lacunas, problemas | "Não disponível para todos os municípios" |

### 4.4 Exemplo de Linha de Metadados

```csv
demo_pop_2022,"População 2022","População residente segundo Censo IBGE 2022","2022","IBGE - Censo Demográfico","2026-01-22","Download PDF Censo 2022 e consulta IBGE Cidades","https://cidades.ibge.gov.br/","Numérico inteiro","habitantes","Sim (soma)","SOMA(municípios da microrregião/mesorregião/estado)","Dados oficiais do Censo 2022","Completo para todos os 139 municípios"
```

### 4.5 Total de Linhas Esperadas

- Cabeçalho: 1
- Variáveis documentadas: 52
- **Total:** 53 linhas

---

## 5. DIMENSÕES DE ANÁLISE E INDICADORES

### 5.1 Demografia (7 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `demo_pop_2010` | População 2010 | ✅ 100% coletado (139 municípios) |
| `demo_pop_2022` | População 2022 | ✅ 100% coletado (139 municípios) |
| `demo_pop_2025_est` | População 2025 (est.) | ⚠️ ~35% coletado |
| `demo_cresc_2010_2022_perc` | Crescimento 2010-2022 | ✅ Calculável (100%) |
| `demo_area_km2` | Área Territorial | ⚠️ ~35% coletado |
| `demo_densidade` | Densidade Demográfica | ⚠️ ~35% coletado |
| `demo_urbanizacao_perc` | Taxa de Urbanização | ❌ 0% coletado |

**Fontes:**
- IBGE Censo 2010
- IBGE Censo 2022
- IBGE Estimativas Populacionais
- IBGE Cidades

### 5.2 Economia (6 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `econ_pib_total_milhoes` | PIB Total | ⚠️ ~35% coletado |
| `econ_pib_pc` | PIB per capita | ⚠️ ~35% coletado |
| `econ_pib_ano_ref` | Ano ref. PIB | ⚠️ ~35% coletado |
| `econ_vab_agro_perc` | VAB Agropecuária | ❌ 0% coletado |
| `econ_vab_ind_perc` | VAB Indústria | ❌ 0% coletado |
| `econ_vab_serv_perc` | VAB Serviços | ❌ 0% coletado |

**Fontes:**
- IBGE - PIB Municipal
- IBGE - Contas Regionais

### 5.3 Desenvolvimento Humano (2 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `desenv_idhm` | IDHM | ⚠️ ~35% coletado |
| `desenv_idhm_ano_ref` | Ano ref. IDHM | ⚠️ ~35% coletado (sempre 2010) |

**Fontes:**
- PNUD - Atlas do Desenvolvimento Humano no Brasil

### 5.4 Educação (6 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `edu_escol_6_14_perc` | Taxa Escolarização 6-14 | ⚠️ ~35% coletado |
| `edu_ideb_ai_2023` | IDEB Anos Iniciais 2023 | ❌ 0% coletado |
| `edu_ideb_af_2023` | IDEB Anos Finais 2023 | ❌ 0% coletado |
| `edu_ideb_ai_2021` | IDEB Anos Iniciais 2021 | ❌ 0% coletado |
| `edu_ideb_af_2021` | IDEB Anos Finais 2021 | ❌ 0% coletado |
| `edu_analfab_15mais_perc` | Taxa Analfabetismo 15+ | ❌ 0% coletado |

**Fontes:**
- INEP - IDEB
- QEdu
- IBGE Cidades

### 5.5 Saúde (5 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `saude_mort_inf` | Mortalidade Infantil | ⚠️ ~32% coletado |
| `saude_mort_inf_ano_ref` | Ano ref. Mort. Infantil | ⚠️ ~32% coletado |
| `saude_cobert_esf_perc` | Cobertura ESF | ❌ 0% coletado |
| `saude_leitos_1000hab` | Leitos por 1000 hab | ❌ 0% coletado |
| `saude_medicos_1000hab` | Médicos por 1000 hab | ❌ 0% coletado |

**Fontes:**
- DATASUS - TabNet
- CNES (Cadastro Nacional de Estabelecimentos de Saúde)
- CNESNet

### 5.6 Saneamento (6 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `san_agua_perc` | Abastecimento Água | ❌ 0% coletado |
| `san_esgoto_coleta_perc` | Coleta Esgoto | ❌ 0% coletado |
| `san_esgoto_trat_perc` | Tratamento Esgoto | ❌ 0% coletado |
| `san_residuos_coleta_perc` | Coleta Resíduos | ❌ 0% coletado |
| `san_ano_ref` | Ano referência SNIS | ❌ 0% coletado |
| `san_fonte` | Fonte dados saneamento | ❌ 0% coletado |

**Fontes:**
- SNIS - Sistema Nacional de Informações sobre Saneamento
- http://www.snis.gov.br/

### 5.7 Agropecuária (9 indicadores)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `agro_vbp_milhoes` | VBP Agropecuário | ❌ 0% coletado |
| `agro_vbp_ano_ref` | Ano ref. VBP | ❌ 0% coletado |
| `agro_area_plantada_ha` | Área Plantada Total | ❌ 0% coletado |
| `agro_rebanho_bovino` | Rebanho Bovino | ❌ 0% coletado |
| `agro_cultura_princ_1` | Cultura Principal 1 | ❌ 0% coletado |
| `agro_cultura_princ_2` | Cultura Principal 2 | ❌ 0% coletado |
| `agro_cultura_princ_3` | Cultura Principal 3 | ❌ 0% coletado |
| `agro_prod_1_ton` | Produção Cultura 1 | ❌ 0% coletado |
| `agro_prod_2_ton` | Produção Cultura 2 | ❌ 0% coletado |

**Fontes:**
- IBGE - PAM (Produção Agrícola Municipal)
- IBGE - PPM (Pesquisa Pecuária Municipal)
- IBGE SIDRA

### 5.8 Turismo (4 indicadores - específicos para algumas regiões)

| Código | Nome | Status Atual |
|--------|------|--------------|
| `tur_visitantes_ano` | Visitantes/ano | ❌ 0% coletado |
| `tur_receita_milhoes` | Receita Turismo | ❌ 0% coletado |
| `tur_atrativos` | Principais Atrativos | ⚠️ Dados qualitativos disponíveis |
| `tur_ano_ref` | Ano referência | ❌ 0% coletado |

**Fontes:**
- NATURATINS (Parque Estadual do Jalapão)
- Secretaria de Turismo do Tocantins
- Observatório do Turismo TO

---

## 6. ESPECIFICAÇÃO TÉCNICA

### 6.1 Formato dos Arquivos

- **Formato:** CSV (Comma-Separated Values)
- **Separador:** Vírgula (,)
- **Encoding:** UTF-8 (com BOM para compatibilidade Excel)
- **Quebra de linha:** LF (\n) ou CRLF (\r\n)
- **Aspas:** Campos de texto com vírgulas devem estar entre aspas duplas

### 6.2 Convenções de Nomenclatura

#### 6.2.1 Prefixos por Dimensão

- `territorio_` - Identificação territorial
- `demo_` - Demografia
- `econ_` - Economia
- `desenv_` - Desenvolvimento Humano
- `edu_` - Educação
- `saude_` - Saúde
- `san_` - Saneamento
- `agro_` - Agropecuária
- `tur_` - Turismo
- `obs` - Observações (sem prefixo)

#### 6.2.2 Sufixos Comuns

- `_perc` - Percentual
- `_milhoes` - Valores em milhões
- `_km2` - Área em km²
- `_ano_ref` - Ano de referência
- `_pc` - Per capita
- `_1000hab` - Por 1000 habitantes

### 6.3 Validações

#### 6.3.1 Validações de Integridade

- Códigos IBGE devem ter 7 dígitos
- UF deve ser "TO"
- Percentuais devem estar entre 0 e 100
- Valores negativos não são permitidos (exceto em crescimento populacional)
- Datas devem estar no formato ISO (YYYY-MM-DD) quando aplicável

#### 6.3.2 Validações de Consistência

- Soma de VAB (agro + ind + serv) deve ser ~100%
- População 2022 >= População 2010 (ou negativo se declínio)
- Densidade = População / Área
- Taxa de tratamento de esgoto <= Taxa de coleta de esgoto

### 6.4 Consolidações

#### 6.4.1 Indicadores Agregáveis por SOMA

- `demo_pop_*` - População
- `demo_area_km2` - Área
- `econ_pib_total_milhoes` - PIB Total
- `agro_rebanho_bovino` - Rebanho
- `agro_area_plantada_ha` - Área plantada
- `agro_prod_*_ton` - Produção agrícola

#### 6.4.2 Indicadores Agregáveis por MÉDIA PONDERADA (População)

- `econ_pib_pc` - PIB per capita (soma PIB total / soma população)
- `demo_densidade` - Densidade (soma população / soma área)
- `edu_escol_6_14_perc` - Taxa escolarização (média ponderada)
- `san_agua_perc` - Saneamento (média ponderada)
- `saude_mort_inf` - Mortalidade infantil (média ponderada por nascidos vivos)

#### 6.4.3 Indicadores NÃO Agregáveis

- `desenv_idhm` - IDHM (específico do território, não agregável)
- `edu_ideb_*` - IDEB (média complexa, requer dados detalhados)
- `agro_cultura_princ_*` - Culturas principais (lista qualitativa)
- `tur_atrativos` - Atrativos turísticos (lista qualitativa)

---

## 7. CRONOGRAMA DE IMPLEMENTAÇÃO

### 7.1 Fase 1: Preparação (24/01/2026)

**Atividades:**
- [ ] Mapear completo de municípios por mesorregião/microrregião
- [ ] Obter códigos IBGE de todos os 139 municípios
- [ ] Validar ordenação alfabética dentro de cada microrregião
- [ ] Criar template da Planilha 1 (cabeçalho + estrutura de linhas)
- [ ] Criar template da Planilha 2 (metadados)

**Entregável:** Templates vazios prontos para preenchimento

### 7.2 Fase 2: Preenchimento com Dados Existentes (25-26/01/2026)

**Atividades:**
- [ ] Consolidar dados das 8 planilhas de microrregiões
- [ ] Preencher indicadores já coletados:
  - População 2010, 2022
  - Área territorial (quando disponível)
  - PIB per capita (quando disponível)
  - IDHM (quando disponível)
  - Taxa de escolarização (quando disponível)
  - Mortalidade infantil (quando disponível)
- [ ] Calcular indicadores derivados (crescimento populacional, densidade)
- [ ] Calcular consolidados de microrregiões
- [ ] Calcular consolidados de mesorregiões
- [ ] Calcular consolidado estadual

**Entregável:** Planilha 1 com dados parciais preenchidos

### 7.3 Fase 3: Documentação de Metadados (27/01/2026)

**Atividades:**
- [ ] Preencher Planilha 2 (metadados) para cada variável
- [ ] Documentar fontes, datas de coleta, métodos
- [ ] Documentar fórmulas de agregação
- [ ] Documentar limitações conhecidas
- [ ] Adicionar caminhos para atualização (URLs, APIs)

**Entregável:** Planilha 2 completa

### 7.4 Fase 4: Validação e Revisão (28/01/2026)

**Atividades:**
- [ ] Validar integridade dos dados (códigos IBGE, percentuais, etc.)
- [ ] Validar consistência (somas, agregações)
- [ ] Revisar consolidados calculados
- [ ] Verificar lacunas documentadas
- [ ] Testar abertura em Excel, Google Sheets, LibreOffice

**Entregável:** Planilhas validadas e aprovadas

### 7.5 Fase 5: Coleta de Dados Faltantes (29/01 - 05/02/2026)

**Atividades (conforme planejamento de coleta):**
- [ ] Coleta IDEB 2023 (139 municípios)
- [ ] Coleta Saneamento - SNIS (139 municípios)
- [ ] Coleta Agropecuária - PAM/PPM (139 municípios)
- [ ] Coleta dados demográficos complementares (91 municípios)
- [ ] Coleta dados de turismo (Jalapão)
- [ ] Atualização da Planilha 1 com novos dados
- [ ] Atualização da Planilha 2 com novos metadados

**Entregável:** Planilhas V2.0 com cobertura completa

---

## 8. OBSERVAÇÕES FINAIS

### 8.1 Versionamento

- **V0.1:** Template inicial (estrutura vazia)
- **V1.0:** Dados já coletados preenchidos
- **V2.0:** Dados complementares coletados (IDEB, Saneamento, Agropecuária)
- **V3.0:** Dados de turismo e indicadores especiais

### 8.2 Arquivos a Serem Gerados

1. `dados-consolidados-tocantins-v01.csv` - Planilha de dados
2. `metadados-consolidados-tocantins-v01.csv` - Dicionário de dados
3. `LEIAME-PLANILHAS-CONSOLIDADAS.md` - Guia de uso das planilhas

### 8.3 Integração com Google Drive

Após criação das planilhas, sincronizar com:
- **Google Drive:** `Projetos/caderno-tocantins-2026/dados/consolidados/`
- **GitHub:** `/dados/consolidados/`

### 8.4 Usos Previstos

As planilhas consolidadas servirão de base para:
1. Elaboração da Parte I do Caderno (Visão Geral do Estado)
2. Atualização das fichas regionais (V2.0)
3. Elaboração das fichas municipais (Parte III)
4. Análises comparativas entre territórios
5. Identificação de padrões e tendências estaduais
6. Visualizações e dashboards

---

**Elaborado em:** 23 de janeiro de 2026
**Responsável:** Sistema de Inteligência Territorial - Caderno Tocantins 2026
**Status:** Planejamento Aprovado - Pronto para Implementação

**Fontes Consultadas:**
- [Wikiwand - Lista de mesorregiões e microrregiões do Tocantins](https://www.wikiwand.com/pt/Lista_de_mesorregi%C3%B5es_e_microrregi%C3%B5es_do_Tocantins)
- [Redalyc - Desenvolvimento Municipal das Microrregiões do Estado do Tocantins](https://www.redalyc.org/journal/752/75257033004/html/)
- Relatórios de Coleta de Dados (Gurupi, Dianópolis, Jalapão, Rio Formoso)
- Planilhas existentes das 8 microrregiões
