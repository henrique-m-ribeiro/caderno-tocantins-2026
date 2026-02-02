# Base de Dados Consolidada - Volume 2

Esta pasta armazenará a **base de dados consolidada** do Tocantins com todos os 139 municípios e 900+ indicadores.

## 📊 Arquivos Esperados

### 1. BASE-DADOS-TOCANTINS-V02-COMPLETA.csv
- **Formato:** CSV com separador `;`
- **Estrutura:** 139 linhas (municípios) × 900+ colunas (indicadores)
- **Codificação:** UTF-8
- **Tamanho estimado:** ~50-100 MB

### 2. BASE-DADOS-TOCANTINS-V02-COMPLETA.xlsx
- **Formato:** Excel (.xlsx)
- **Estrutura:** Planilha formatada com múltiplas abas
- **Abas sugeridas:**
  - `Todos_Indicadores` - Base completa
  - `Demografia` - Indicadores demográficos
  - `Economia` - PIB, VAB, empregos
  - `Educacao` - Matrículas, IDEB, alfabetização
  - `Saude` - Infraestrutura, indicadores vitais
  - `Agropecuaria` - Produção agrícola e pecuária
  - `Financas` - Transferências e arrecadação
  - `Saneamento` - Água, esgoto, lixo
  - `Infraestrutura` - Energia, conectividade
  - `Meio_Ambiente` - Queimadas, resíduos

### 3. DICIONARIO-DADOS-V02.md
- **Conteúdo:** Descrição de cada uma das 900+ colunas
- **Informações:** Nome, descrição, unidade, fonte, ano de referência

### 4. METADADOS-COMPLETO.md
- **Conteúdo:** Metadados completos da base
- **Informações:**
  - Data de geração
  - Fonte dos dados (SEPLAN-TO)
  - Metodologia de extração (Deepseek V3)
  - Limitações conhecidas
  - Changelog de versões

## 🔄 Origem dos Dados

Os dados são consolidados a partir de:
- **Fonte primária:** 139 CSVs individuais em `parte-iii-fichas-municipais/deepseek-v3/csv-indicadores/`
- **Fonte original:** Perfis Socioeconômicos SEPLAN-TO 2024 (139 PDFs)

## 📈 Cobertura de Indicadores

A base V02 representa um **salto qualitativo** em relação à V01:

| Versão | Colunas | Cobertura | Origem |
|--------|---------|-----------|--------|
| V01 | 38 | ~35% | Extração manual/scripts |
| V02 | 900+ | ~85%+ | Deepseek V3 + PDFs SEPLAN |

## ✅ Validação da Base

Antes de considerar a base pronta, verificar:
- [ ] 139 municípios presentes (100% do Tocantins)
- [ ] 900+ colunas com dados
- [ ] Séries históricas completas (1991-2023 onde aplicável)
- [ ] Códigos IBGE corretos (7 dígitos)
- [ ] Sem valores claramente incorretos
- [ ] Formatação consistente
- [ ] Dicionário de dados completo

## 📊 Status

- **CSVs individuais gerados:** 0/139
- **Base consolidada:** ❌ Pendente
- **Planilha Excel:** ❌ Pendente
- **Dicionário de dados:** ❌ Pendente
- **Metadados:** ❌ Pendente

---

**Esta pasta será preenchida após a geração dos 139 CSVs individuais!**
