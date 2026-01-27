# Relatórios de Validação de Dados

## Descrição

Este diretório contém todos os relatórios de validação dos dados extraídos, implementando os **4 tipos de validação** especificados na recomendação Manus.

## Arquivos de Validação

### 1. RELATORIO_VALIDACAO_SCHEMA.txt
**Validação de Schema (Estrutural)**
- Verifica se tipos de dados correspondem ao esperado
- Detecta strings em campos numéricos
- Valida campos percentuais (0-100)
- **Critério de aprovação:** <5% de campos com tipos incorretos

### 2. RELATORIO_VALIDACAO_RANGES.txt
**Validação de Intervalo (Range)**
- Verifica valores dentro de limites plausíveis
- Detecta outliers e valores impossíveis
- Exemplos de ranges:
  - População TO: 500-350.000
  - IDEB: 0-10
  - IDHM: 0-1
  - Percentuais: 0-100
- **Critério de aprovação:** <10% de valores fora do range plausível

### 3. RELATORIO_VALIDACAO_CRUZADA.txt
**Validação Cruzada (Cross-field)**
- Verifica consistência entre campos relacionados
- Regras implementadas:
  - VAB setorial deve somar ~100% (tolerância 2%)
  - PIB per capita = PIB total / População (tolerância <R$100)
  - Taxa de urbanização consistente com pop. urbana/rural
  - Crescimento populacional 2010-2022 consistente
  - Densidade = População / Área
- **Critério de aprovação:** <5% de inconsistências

### 4. RELATORIO_VALIDACAO_HISTORICA.txt
**Validação de Consistência Histórica**
- Compara dados extraídos com dados V01 coletados manualmente
- Detecta divergências significativas (>5%)
- Identifica possíveis erros de extração
- **Critério de aprovação:** <10% de divergências >5%

### 5. RELATORIO_VALIDACAO_CONSOLIDADO.md
**Síntese Executiva**
- Resumo de todas as validações
- Estatísticas gerais de qualidade
- Municípios com problemas críticos
- Recomendações de ações corretivas
- Status de aprovação geral

## Formato dos Relatórios

### Relatórios TXT (1-3)
Formato estruturado para processamento automatizado:
```
=== VALIDAÇÃO DE [TIPO] ===
Data: 2026-01-XX
Total de registros: 139 municípios

--- ESTATÍSTICAS GERAIS ---
Total de campos validados: XXX
Campos válidos: XXX (XX.X%)
Campos com problemas: XXX (XX.X%)
Status: [APROVADO/REPROVADO]

--- PROBLEMAS IDENTIFICADOS ---
1. Município: [Nome]
   Código IBGE: [Código]
   Campo: [campo]
   Problema: [descrição]
   Valor encontrado: [valor]
   Valor esperado: [range ou critério]

...
```

### Relatório Consolidado (MD)
Formato markdown para leitura humana:
- Resumo executivo
- Tabelas de estatísticas
- Gráficos de qualidade (se possível)
- Lista de ações necessárias
- Assinatura digital (hash dos dados)

## Scripts Relacionados

- `scripts/validar_dados.py` - Executa todas as 4 validações
- `scripts/consolidar_extraidos_perfis.py` - Chama validações após consolidação

## Critérios de Aprovação Geral

Para aprovar os dados extraídos, TODOS os critérios devem ser atendidos:
- ✅ Schema: <5% de erros de tipo
- ✅ Ranges: <10% de valores fora do esperado
- ✅ Cruzada: <5% de inconsistências
- ✅ Histórica: <10% de divergências >5%

Se qualquer critério falhar, é necessário:
1. Revisar municípios com problemas
2. Corrigir scripts de extração
3. Re-executar extração para municípios problemáticos
4. Re-executar validações

## Fase de Criação

**Fase 3:** Desenvolvimento de Infraestrutura (3.4: Script de Validação - 3-4h)
**Fase 4:** Execução após extração em lote

## Status

- [ ] Script de validação desenvolvido
- [ ] Validação de Schema implementada
- [ ] Validação de Ranges implementada
- [ ] Validação Cruzada implementada
- [ ] Validação Histórica implementada
- [ ] Relatórios gerados
- [ ] Critérios de aprovação atendidos

---

**Última atualização:** 27 de janeiro de 2026
**Fase:** 0 (Preparação)
**Recomendação:** Manus (Framework IA-Collab-OS)
