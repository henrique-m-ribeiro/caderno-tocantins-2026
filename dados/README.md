# Dados do Projeto

Esta pasta contém todos os dados coletados para o projeto Caderno Tocantins 2026.

## Estrutura

### `/finais/`
Datasets consolidados das 8 microrregiões do Tocantins.

**Arquivos CSV:**
- `dados-microrregiao-porto-nacional-v01.csv` (11 municípios)
- `dados-microrregiao-araguaina-v01.csv` (17 municípios)
- `dados-microrregiao-bico-do-papagaio-v01.csv` (25 municípios)
- `dados-microrregiao-miracema-v01.csv` (23 municípios)
- `dados-microrregiao-gurupi-v01.csv` (15 municípios)
- `dados-microrregiao-dianopolis-v01.csv` (18 municípios)
- `dados-microrregiao-jalapao-v01.csv` (15 municípios)
- `dados-microrregiao-rio-formoso-v01.csv` (13 municípios)

**Relatórios de Coleta:**
- Documentação do processo de coleta de dados
- Fontes utilizadas
- Limitações e lacunas identificadas

## Indicadores Disponíveis

### Cobertura Completa (139 municípios)
- População 2010 e 2022

### Cobertura Parcial
- Área territorial (35%)
- PIB per capita (35%)
- IDHM (35%)
- Taxa de escolarização (35%)
- Mortalidade infantil (32%)

### Pendentes
- IDEB 2023
- Saneamento (água, esgoto, tratamento)
- Agropecuária (VBP, culturas, rebanho)

## Formato dos Dados

Os arquivos CSV seguem o padrão:

```csv
municipio,populacao_2010,populacao_2022,area_km2,pib_per_capita,idhm,taxa_escolarizacao,mortalidade_infantil
```

## Fontes de Dados

- IBGE (Instituto Brasileiro de Geografia e Estatística)
- INEP (Instituto Nacional de Estudos e Pesquisas Educacionais)
- DATASUS (Departamento de Informática do SUS)
- SNIS (Sistema Nacional de Informações sobre Saneamento)
- PNUD (Programa das Nações Unidas para o Desenvolvimento)

## Versionamento

- **V01**: Versão inicial com dados básicos
- **V02**: Planejada - inclusão de IDEB, Saneamento e Agropecuária

## Atualização

Última atualização: 23 de janeiro de 2026
