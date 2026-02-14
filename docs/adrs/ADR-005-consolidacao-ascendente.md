# ADR-005: Consolidação Ascendente (Bottom-Up)

**Status:** ✅ Aceita
**Data:** 2026-01-20
**Responsável:** Henrique Marques Ribeiro
**Session:** Múltiplas sessões (Fase 1.0 - 1.2)
**Fase:** Fase 1.0 - Consolidação Ascendente

---

## Contexto

No início do projeto Caderno Tocantins 2026, precisávamos decidir a **direção de consolidação** dos dados territoriais.

**Estrutura do Tocantins:**
- **139 municípios** (nível mais granular)
- **8 microrregiões** (IBGE) - agrupamento intermediário
- **1 estado** (nível mais agregado)

**Problema:** Como consolidar dados de 139 municípios em análise estadual?

**Duas abordagens possíveis:**
1. **Top-down (Estado → Microrregião → Município):** Começar com análise estadual, depois detalhar microrregiões, depois municípios
2. **Bottom-up (Município → Microrregião → Estado):** Começar com dados municipais, agregar em microrregiões, depois consolidar estado

**Contexto histórico:**
- Fase 0 já havia gerado 139 fichas municipais (Deepseek V3, 15-25 páginas cada)
- Dados estruturados (CSV, JSON) já coletados no nível municipal (37-76 indicadores)
- Necessidade de criar fichas regionais para Volume 1

---

## Decisão

**Decidimos usar consolidação ascendente (bottom-up): Município → Microrregião → Estado.**

**Processo:**
1. **Fase 1.0:** Coletar dados de 139 municípios (fichas municipais Deepseek V3 + extração de indicadores)
2. **Fase 1.1:** Agregar dados municipais em 8 fichas regionais (por microrregião IBGE)
3. **Fase 1.2:** Consolidar dados regionais em panorama estadual
4. **Fase 2:** Compilar tudo em Volume 1 v2.0 (estadual + regional + municipal)

**Característica:** Preserva granularidade municipal em toda a cadeia de consolidação.

---

## Alternativas Consideradas

### Alternativa 1: Consolidação Descendente (Top-Down)

- **Descrição:** Começar com análise estadual (Parte I), depois criar fichas regionais derivadas da análise estadual, depois municípios
- **Prós:**
  - Visão estratégica estabelecida primeiro (contexto estadual antes de detalhes)
  - Mais alinhada com planejamento governamental tradicional (estado → município)
  - Narrativa "de cima para baixo" pode ser mais fácil de comunicar
- **Contras:**
  - Risco de generalizações prematuras (estadual sem conhecer realidades municipais)
  - Difícil capturar singularidades territoriais (municípios vistos como "médias")
  - Padrões emergentes (ex: 3 realidades econômico-sociais) podem ser invisíveis
  - Dados municipais já coletados ficariam subutilizados
- **Por que foi rejeitada:** Dados municipais já existiam (Fase 0). Abordagem top-down ignoraria riqueza dos dados granulares.

### Alternativa 2: Consolidação Simultânea (Paralela)

- **Descrição:** Trabalhar simultaneamente nos 3 níveis (estadual, regional, municipal)
- **Prós:**
  - Flexibilidade para ajustar narrativas em todos os níveis
  - Possibilidade de feedback loops (municipal informa estadual, estadual informa municipal)
- **Contras:**
  - Risco de inconsistências entre níveis (dados divergentes)
  - Complexidade de coordenação (qual nível é "fonte da verdade"?)
  - Dificulta rastreabilidade (origem dos dados não clara)
  - Mais trabalhoso (ajustes em cascata em todos os níveis)
- **Por que foi rejeitada:** Complexidade excessiva e risco de inconsistências.

---

## Consequências

### Positivas

- ✅ **Preserva granularidade:** Dados municipais mantidos intactos em toda a cadeia
- ✅ **Identificação de padrões emergentes:** 3 realidades econômico-sociais emergiram da agregação (não seriam visíveis top-down)
- ✅ **Rastreabilidade de dados:** Cada dado regional/estadual rastreável até município de origem
- ✅ **Validação por stakeholders facilitada:** Gestores municipais podem validar dados de seus municípios
- ✅ **Utiliza dados existentes:** 139 fichas municipais (Deepseek V3) são base, não descartadas
- ✅ **Narrativas territoriais autênticas:** Microrregiões "contam suas próprias histórias" através dos dados

### Negativas

- ⚠️ **Mais trabalhoso:** Consolidar 139 municípios → 8 microrregiões → 1 estado é mais demorado que estado → regiões → municípios
- ⚠️ **Complexidade inicial maior:** Lidar com 139 fichas municipais antes de ter visão estadual
- ⚠️ **Risco de "perder-se nos detalhes":** Possível foco excessivo em particularidades municipais vs. visão estratégica

### Mitigações

- **Trabalho:** Automatização da extração de indicadores (scripts Python) reduz esforço manual
- **Complexidade:** Tabelas comparativas por microrregião organizam dados municipais
- **Perder-se:** Panorama consolidado (Fase 1.2) garante síntese estratégica após consolidação

---

## Trade-offs Identificados

**Trade-off: Granularidade vs. Síntese Estratégica**
- **Ganhamos:** Granularidade (dados municipais preservados, padrões emergentes identificados)
- **Perdemos:** Velocidade de síntese estratégica (visão estadual vem depois)
- **Avaliação:** Trade-off justificado. Granularidade permite síntese mais robusta.

---

## Resultados Observados

### Padrões Emergentes Identificados (Fase 1.2)

**Consolidação ascendente permitiu identificar 3 realidades econômico-sociais:**

1. **Eixo Metropolitano Consolidado (61% população)**
   - Microrregiões: Porto Nacional, Araguaína, Gurupi
   - Características: Alta densidade, IDHM elevado, economia diversificada
   - Padrão emergiu da agregação de dados de 39 municípios

2. **Fronteira Agrícola Consolidada (19% população)**
   - Microrregiões: Dianópolis, Rio Formoso, Jalapão
   - Características: Alto PIB, baixa densidade, paradoxo riqueza-desenvolvimento
   - Padrão emergiu de municípios com PIB per capita excepcional (>R$ 40k)

3. **Transição e Vulnerabilidade (20% população)**
   - Microrregiões: Bico do Papagaio, Miracema
   - Características: Desafios sociais, infraestrutura precária, transição econômica
   - Padrão emergiu de municípios com IDHM baixo (<0.700) e infraestrutura deficitária

**Estes padrões NÃO seriam visíveis em abordagem top-down** (dados estaduais agregados mascaram heterogeneidade).

---

## Implementação

**Data de Implementação:** 2026-01-15 a 2026-02-07 (Fases 1.0 - 1.2)

**Commits Relacionados:**
- Múltiplos commits ao longo de Fases 1.0, 1.1, 1.2

**Arquivos Afetados:**
- `analises/fase-1-1-agregacao-municipal/dados-municipais-completos-deepseek-v3.json` (139 municípios)
- `analises/fase-1-1-agregacao-municipal/FICHA-01-PORTO-NACIONAL-REVISADA.md` (+ 7 fichas regionais)
- `parte-i-visao-estadual/docs/PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md` (panorama consolidado)

---

## Referências

### Documentação Interna
- **Handoff:** [HANDOFF-SESSION-0e16a195.md](../handoffs/HANDOFF-SESSION-0e16a195.md) - Seção 9.1: ADR-005
- **Reflexão:** [REFLEXAO-PESQUISA-ACAO-0e16a195.md](../reflexoes/REFLEXAO-PESQUISA-ACAO-0e16a195.md) - Seção 5.1: Aprendizado 5, Insight 3

### Panorama Consolidado
- [PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md](../../parte-i-visao-estadual/docs/PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md) - Seção 5: Três Realidades Identificadas

---

## Notas Adicionais

### Aprendizado Metodológico

**Insight:** Consolidação ascendente produz conhecimento emergente.

Da REFLEXAO-PESQUISA-ACAO-0e16a195.md:
> "Análise municipal isolada não revelaria 3 realidades econômico-sociais (padrão emerge na agregação). Metodologia de consolidação (bottom-up vs. top-down) produz diferentes tipos de conhecimento. Consolidação ascendente altera epistemologia de políticas públicas territoriais."

### Princípio Epistemológico

**Bottom-up permite emergência, top-down pressupõe estrutura.**

- **Top-down:** Assume que realidade estadual é conhecida a priori → detalha em municípios
- **Bottom-up:** Descobre realidades territoriais através da agregação → padrões emergem dos dados

**Implicação para políticas públicas:** Políticas formuladas top-down podem ignorar realidades locais. Consolidação ascendente informa políticas diferenciadas por território.

### Replicabilidade

Esta abordagem pode ser replicada para:
- **Outros estados:** Consolidação ascendente de municípios em microrregiões e estado
- **Comparações interestaduais:** Agregação de estados em regiões/Brasil
- **Políticas setoriais:** Consolidação ascendente de estabelecimentos (educação, saúde) em municípios/regiões

---

## Histórico de Revisões

| Data | Autor | Mudança |
|------|-------|---------|
| 2026-02-14 | Henrique Marques Ribeiro | Criação inicial (formalização de decisão tomada em 2026-01-20) |

---

**Última atualização:** 2026-02-14
**Próxima revisão:** Após comparação com outros estados (avaliar se padrões emergentes são replicáveis)
