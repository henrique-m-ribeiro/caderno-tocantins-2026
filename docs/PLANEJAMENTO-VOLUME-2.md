# PLANEJAMENTO DO VOLUME 2 - CADERNO TOCANTINS 2026

**Data**: 07 de fevereiro de 2026
**Status**: Proposta para revisão
**Sessão**: claude/review-handoff-docs-lZ6Qi

---

## 1. OBJETIVO

Produzir o **Volume 2 do Caderno Tocantins 2026**: um compêndio de 139 fichas municipais que ofereça, para cada município do estado, um diagnóstico socioeconômico completo com análise estratégica e diretrizes propositivas.

---

## 2. DIAGNÓSTICO: O QUE TEMOS HOJE

### 2.1 Fichas Completas (Deepseek V3) — 140 arquivos

Localizadas em `parte-iii-fichas-municipais/deepseek-v3/fichas-completas/`.

**Pontos fortes:**
- Cobertura de 100% dos municípios (139 + README)
- Estrutura padronizada com 12 seções e 9 dimensões de análise
- ~50 indicadores com séries históricas (2019-2023)
- SWOT detalhada, diagnóstico integrado, diretrizes estratégicas
- Cada arquivo: 26-47 KB, 550-710 linhas (~15-20 páginas impressas)

**Limitações para uso direto como Volume 2:**
- Extensão excessiva: 139 × ~18 páginas = ~2.500 páginas (inviável para publicação)
- Redundância de dados (mesmos indicadores repetidos em seções diferentes)
- Séries históricas longas que diluem a mensagem central
- Formatação heterogênea entre arquivos (alguns com escape de caracteres markdown)
- Análise às vezes genérica — mesmos "pontos de alavancagem" em municípios diferentes

### 2.2 Fichas Resumidas (modelo anterior) — 139 arquivos

Localizadas em `parte-iii-fichas-municipais/fichas/`.

**Pontos fortes:**
- Estrutura compacta e padronizada (~160 linhas, 2 páginas)
- 6 dimensões bem definidas
- Dados quantitativos em tabelas limpas

**Limitações críticas:**
- Quase toda análise é placeholder `[A DEFINIR]` — sem valor analítico
- Apenas ~32 indicadores pontuais (sem séries históricas)
- Ausência de: resumo executivo, SWOT, diagnóstico integrado, alertas
- Dimensão "Agropecuária" com apenas 2 indicadores (VAB 2017 e 2021)
- Sem dados de pobreza, programas sociais, estrutura etária, mercado de trabalho

### 2.3 Extração de Dados — Estado Atual

- **135/139 municípios** com dados extraídos dos PDFs (~97%)
- **4 municípios sem PDF**: Bandeirantes do Tocantins, Barra do Ouro, Bernardo Sayão, Muricilândia
- **1 outlier grave**: Novo Acordo (27/110 indicadores extraídos — 24,5%)
- **CSV de indicadores**: apenas 3/139 gerados (Abreulândia, Aguiarnópolis + README)
- **Base V01**: 38 colunas, com lacunas severas (IDEB, saneamento, agropecuária = 0%)
- **Base V03**: script pronto (`consolidar_base_v03.py`) mas não executado

---

## 3. PROPOSTA: NOVO MODELO DE FICHA MUNICIPAL

### 3.1 Princípios de Design

| Aspecto | Resumida (anterior) | Completa (Deepseek) | **Novo Modelo (proposto)** |
|---------|---------------------|---------------------|---------------------------|
| Extensão | ~2 páginas (160 linhas) | ~15-20 páginas (550-710 linhas) | **~5-7 páginas (~250-350 linhas)** |
| Dimensões | 6 | 9 | **8 (agrupamento estratégico)** |
| Indicadores | ~32 (pontuais) | ~50+ (séries completas) | **~45 (pontuais + variação)** |
| Análise qualitativa | Nenhuma (placeholders) | Extensa (às vezes verbosa) | **Concisa e propositiva** |
| SWOT | Ausente | 5 itens/quadrante detalhados | **3 itens/quadrante, objetivos** |
| Diagnóstico | Ausente | Paradoxo + cadeia causal | **Paradoxo + cadeia causal (compacta)** |
| Diretrizes | Placeholder genérico | 4 prioridades detalhadas | **4 prioridades com ações-chave** |
| Alertas | Ausente | 3 níveis × 3 itens | **3 níveis × 2 itens** |
| Comparações | Ausente | Presentes | **Tabela comparativa (município/TO/BR)** |

### 3.2 Estrutura Proposta

```
FICHA MUNICIPAL — [NOME DO MUNICÍPIO]
├── Cabeçalho (código IBGE, microrregião, área, bioma)
├── Dados Fundamentais (tabela: 8 indicadores-chave)
├── Resumo Executivo (1 parágrafo — paradoxo central)
├── Síntese Estratégica (SWOT: 3 itens por quadrante)
├── Dimensão 1: Perfil Demográfico e Social
├── Dimensão 2: Economia e Produção
├── Dimensão 3: Educação
├── Dimensão 4: Saúde
├── Dimensão 5: Saneamento e Infraestrutura
├── Dimensão 6: Agropecuária e Desenvolvimento Rural
├── Dimensão 7: Finanças Públicas
├── Dimensão 8: Meio Ambiente
├── Diagnóstico Integrado (paradoxo + cadeia causal + comparações)
├── Diretrizes Estratégicas (4 prioridades com ações)
├── Alertas (semáforo: vermelho / amarelo / verde)
└── Fontes
```

### 3.3 Modelo Detalhado — Especificação por Seção

---

#### CABEÇALHO

```markdown
# [NOME DO MUNICÍPIO] — Ficha Municipal

**Código IBGE**: XXXXXXX | **Microrregião**: XXXXXXX | **Área**: X.XXX km² | **Bioma**: Cerrado
```

---

#### DADOS FUNDAMENTAIS

Tabela compacta com os indicadores de identidade do município.

| Indicador | Valor | Contexto |
|-----------|-------|----------|
| População (2022) | X.XXX hab | Variação 2010-2022: +/-X,X% |
| Densidade demográfica | X,X hab/km² | — |
| PIB total (2021) | R$ X.XXX mil | Xª posição no estado |
| PIB per capita (2021) | R$ XX.XXX | TO: R$ 29.619 / BR: R$ 43.460 |
| IDHM (2010) | 0,XXX | Classificação: Baixo/Médio/Alto |
| Taxa de urbanização (2022) | XX,X% | — |
| Dependência de transferências | XX,X% | FPM + FUNDEB / receita total |
| Emprego formal (2022-2023) | X.XXX postos | — |

---

#### RESUMO EXECUTIVO

Um parágrafo (100-150 palavras) que:
- Identifica o **paradoxo central** do município
- Apresenta 2-3 dados-chave que sustentam o diagnóstico
- Indica a principal oportunidade estratégica

*Exemplo (Aguiarnópolis):*
> Aguiarnópolis apresenta um cenário de "enclave desenvolvimentista em retração demográfica". Enquanto indicadores de infraestrutura básica avançam (86,3% com água encanada, cobertura 4G para 87% da população), a população encolheu 12,9% entre 2010-2022 e o IDEB do ensino médio estagnou em 3,8. Com 4.497 habitantes e economia dependente de transferências governamentais (FPM+FUNDEB = 99,2% das transferências), o município precisa converter sua pecuária bovina em expansão (18.715 cabeças, +85% desde 2019) em cadeia produtiva geradora de empregos qualificados para reter jovens e reverter o declínio demográfico.

---

#### SÍNTESE ESTRATÉGICA (SWOT)

| Forças | Fraquezas |
|--------|-----------|
| • [Item 1 com dado de suporte] | • [Item 1 com dado de suporte] |
| • [Item 2 com dado de suporte] | • [Item 2 com dado de suporte] |
| • [Item 3 com dado de suporte] | • [Item 3 com dado de suporte] |

| Oportunidades | Ameaças |
|---------------|---------|
| • [Item 1 com dado de suporte] | • [Item 1 com dado de suporte] |
| • [Item 2 com dado de suporte] | • [Item 2 com dado de suporte] |
| • [Item 3 com dado de suporte] | • [Item 3 com dado de suporte] |

Cada item deve ser uma frase curta com um dado numérico de suporte.

---

#### DIMENSÃO 1: PERFIL DEMOGRÁFICO E SOCIAL

**Indicadores:**

| Indicador | Valor | Variação / Referência |
|-----------|-------|-----------------------|
| População (2022) | X.XXX | var. 2010-2022 |
| Pop. urbana / rural (2022) | XX% / XX% | — |
| Faixa 0-14 / 15-64 / 65+ | XX% / XX% / XX% | Razão de dependência: XX,X |
| IDHM Geral (2010) | 0,XXX | Classificação |
| IDHM Longevidade | 0,XXX | — |
| IDHM Educação | 0,XXX | — |
| IDHM Renda | 0,XXX | — |
| Famílias em extrema pobreza (2010) | XX% | XX famílias |
| Bolsa Família (2023) | XXX famílias | XX% do total |

**Análise** (2-3 frases): tendência demográfica, perfil de envelhecimento, situação de pobreza e desigualdade.

---

#### DIMENSÃO 2: ECONOMIA E PRODUÇÃO

**Indicadores:**

| Indicador | Valor | Variação / Referência |
|-----------|-------|-----------------------|
| PIB total (2021) | R$ X.XXX mil | var. 2017-2021 |
| PIB per capita (2021) | R$ XX.XXX | var. 2017-2021 |
| VAB Agropecuária (2021) | R$ X.XXX mil (XX%) | — |
| VAB Indústria (2021) | R$ X.XXX mil (XX%) | — |
| VAB Serviços (2021) | R$ X.XXX mil (XX%) | — |
| Emprego formal (2022/2023) | X.XXX postos | Saldo: +/-XXX |
| Principal setor empregador | XXXXX | XX% dos empregos |
| MEIs (2023) | XXX | var. 2019-2023 |

**Análise** (2-3 frases): estrutura econômica, dinâmica do mercado de trabalho, diversificação.

---

#### DIMENSÃO 3: EDUCAÇÃO

**Indicadores:**

| Indicador | Valor | Referência |
|-----------|-------|-----------|
| Alfabetização (2022) | XX,X% | 2010: XX,X% |
| IDEB Anos Iniciais (2023) | X,X | Meta nacional: 6,0 |
| IDEB Anos Finais (2023) | X,X | — |
| IDEB Ensino Médio (2023) | X,X | — |
| Matrículas totais (2023) | X.XXX | — |
| Distorção idade-série EM (2023) | XX,X% | — |
| Ensino superior | Sim/Não | Nº de IES |

**Análise** (2-3 frases): evolução do IDEB, qualidade do fluxo escolar, acesso ao ensino superior.

---

#### DIMENSÃO 4: SAÚDE

**Indicadores:**

| Indicador | Valor | Referência |
|-----------|-------|-----------|
| UBS (2023) | XX unidades | — |
| Estabelecimentos hospitalares | XX / 0 | Leitos: XX / 0 |
| Profissionais de saúde (2023) | XX | Médicos: XX |
| Mortalidade infantil (mais recente) | XX,X‰ | TO: 13,4‰ |
| Cobertura vacinal BCG (2022) | XX,X% | Meta: 95% |
| Casos de dengue (2023) | XXX | — |

**Análise** (2-3 frases): capacidade da rede, indicadores vitais, vulnerabilidades.

---

#### DIMENSÃO 5: SANEAMENTO E INFRAESTRUTURA

**Indicadores:**

| Indicador | Valor |
|-----------|-------|
| Água via rede geral (2022) | XX,X% dos domicílios |
| Esgoto via rede geral (2022) | XX,X% dos domicílios |
| Coleta de lixo (2022) | XX,X% dos domicílios |
| Destino final dos resíduos | Aterro / Lixão |
| Cobertura 4G (2024) | XX% da população |
| Banda larga fixa (2023) | XXX acessos |
| Agências bancárias | XX |

**Análise** (2-3 frases): déficits de saneamento, nível de conectividade, acesso a serviços.

---

#### DIMENSÃO 6: AGROPECUÁRIA E DESENVOLVIMENTO RURAL

**Indicadores:**

| Indicador | Valor | Variação |
|-----------|-------|----------|
| VAB Agropecuária (2021) | R$ X.XXX mil | var. 2017-2021 |
| Rebanho bovino (2023) | XX.XXX cabeças | var. 2019-2023 |
| Principal cultura | XXXXX | XXX t (2023) |
| Segunda cultura | XXXXX | XXX t (2023) |
| Estabelecimentos agropecuários (2017) | XXX | var. 2006-2017 |
| Crédito rural (2023) | R$ X,XX milhões | var. 2019-2023 |
| Concentração fundiária | XX% da área em estab. > 200ha | — |

**Análise** (2-3 frases): vocação produtiva, tendências, potencial de agregação de valor.

---

#### DIMENSÃO 7: FINANÇAS PÚBLICAS

**Indicadores:**

| Transferência | 2019 | 2023 | Variação |
|---------------|------|------|----------|
| FPM | R$ X,XX mi | R$ X,XX mi | +XX% |
| ICMS | R$ X,XX mi | R$ X,XX mi | +XX% |
| FUNDEB | R$ X,XX mi | R$ X,XX mi | +XX% |
| IPVA | R$ XXX mil | R$ XXX mil | +XX% |
| ITR | R$ XX mil | R$ XX mil | +XX% |
| **Total** | R$ X,XX mi | R$ X,XX mi | +XX% |

**Análise** (2-3 frases): grau de dependência, evolução da base fiscal, capacidade de investimento.

---

#### DIMENSÃO 8: MEIO AMBIENTE

**Indicadores:**

| Indicador | Valor |
|-----------|-------|
| Focos de queimadas (2023) | XX |
| Tendência de queimadas (2014-2023) | Crescente / Estável / Decrescente |
| Manejo de resíduos | Aterro sanitário / Lixão |
| Coleta seletiva | Sim / Não |

**Análise** (1-2 frases): riscos ambientais, gestão de resíduos.

---

#### DIAGNÓSTICO INTEGRADO

**Paradoxo central:** Uma frase que sintetiza a contradição fundamental do município.

**Cadeia causal:** 4-5 elos numerados mostrando o ciclo de causa-efeito.

**Comparação com referências:**

| Indicador | Município | Tocantins | Brasil |
|-----------|-----------|-----------|--------|
| IDHM (2010) | 0,XXX | 0,699 | 0,727 |
| PIB per capita (2021) | R$ XX.XXX | R$ 29.619 | R$ 43.460 |
| Alfabetização (2022) | XX,X% | ~90% | ~93% |
| Esgoto rede geral | XX,X% | ~XX% | ~XX% |

---

#### DIRETRIZES ESTRATÉGICAS

Para cada uma das 4 prioridades:

**Prioridade X: [Título]**
- Objetivo: [frase com meta mensurável]
- Ação X.1: [ação concreta]
- Ação X.2: [ação concreta]
- Indicador: [métrica de acompanhamento com meta]

---

#### ALERTAS

| Nível | Alerta | Justificativa |
|-------|--------|---------------|
| VERMELHO | [Situação de urgência 1] | [dado de suporte] |
| VERMELHO | [Situação de urgência 2] | [dado de suporte] |
| AMARELO | [Atenção necessária 1] | [dado de suporte] |
| AMARELO | [Atenção necessária 2] | [dado de suporte] |
| VERDE | [Oportunidade 1] | [dado de suporte] |
| VERDE | [Oportunidade 2] | [dado de suporte] |

---

#### FONTES

```
Fonte primária: SEPLAN/TO - Perfil Socioeconômico Municipal (2024)
Dados complementares: IBGE, INEP/MEC, DATASUS, RAIS/CAGED, ANATEL, INPE, BACEN
```

---

## 4. GANHOS DO NOVO MODELO EM RELAÇÃO AOS ANTERIORES

### Vs. Ficha Resumida (2 páginas)

| Aspecto | Antes | Agora |
|---------|-------|-------|
| Análise qualitativa | Placeholder genérico | Texto analítico concreto |
| SWOT | Ausente | Presente com dados de suporte |
| Diagnóstico integrado | Placeholder | Paradoxo + cadeia causal |
| Indicadores | 32 pontuais | ~45 com variação temporal |
| Agropecuária | 2 indicadores (VAB apenas) | 7 indicadores (culturas, rebanho, crédito, fundiário) |
| Saúde | 5 indicadores básicos | + mortalidade, vacinação, doenças |
| Pobreza/desigualdade | Ausente | Presente |
| Alertas | Ausente | Semáforo vermelho/amarelo/verde |
| Diretrizes | Placeholder | 4 prioridades com ações concretas |

### Vs. Ficha Completa (15-20 páginas)

| Aspecto | Antes | Agora |
|---------|-------|-------|
| Extensão | 550-710 linhas | ~250-350 linhas |
| Séries históricas | 5 anos completos | Valor atual + variação |
| SWOT | 5 itens × 4 quadrantes = 20 | 3 itens × 4 quadrantes = 12 |
| Dados redundantes | Sim (VAB aparece 3x) | Eliminados |
| Dados de eleitores | Detalhados | Omitidos (fora do escopo) |
| Detalhes de domicílio | Tipo, moradores/domicílio | Omitidos (pouco estratégicos) |
| Produção animal detalhada | Ovos, mel, leite por ano | Apenas rebanho principal |
| Comércio exterior | Série completa | Omitido (zero na maioria) |
| Acidentes com animais | Presente | Omitido |
| Foco | Enciclopédico | Estratégico e propositivo |

---

## 5. PROBLEMAS A RESOLVER ANTES DA PRODUÇÃO

### 5.1 Dados Faltantes (Prioridade Alta)

| Problema | Impacto | Solução proposta |
|----------|---------|------------------|
| 4 municípios sem PDF | 4/139 fichas sem dados primários | Buscar PDFs alternativos na SEPLAN ou usar dados IBGE/INEP |
| Novo Acordo com 27/110 indicadores | 1 ficha muito incompleta | Investigar PDF original, complementar com fontes abertas |
| CSV de indicadores: 3/139 | Base estruturada indisponível | Executar extração em lote ou usar fichas completas como fonte |
| Base V03 não consolidada | Sem base unificada para geração | Executar `consolidar_base_v03.py` |

### 5.2 Qualidade e Padronização (Prioridade Média)

| Problema | Impacto | Solução proposta |
|----------|---------|------------------|
| Formatação heterogênea nas fichas completas | Alguns arquivos com escape markdown (`\-`, `\*`) | Normalizar na geração |
| Análises genéricas em alguns municípios | Recomendações repetidas entre municípios diferentes | Customizar por vocação econômica e porte |
| Indicadores com anos de referência diferentes | Dificulta comparação intermunicipal | Padronizar ano de referência por indicador |

### 5.3 Infraestrutura de Geração (Prioridade Alta)

| Necessidade | Status | Ação |
|-------------|--------|------|
| Script de geração de fichas V2 | Não existe | Criar baseado no novo modelo |
| Fonte de dados primária definida | Fichas completas (Deepseek V3) | Confirmar como fonte |
| Template markdown padronizado | Não existe | Criar com base neste documento |
| Script de consolidação em documento único | Existe (`consolidar_fichas_municipais.py`) | Adaptar para novo formato |
| Conversão PDF | Existe (`converter_para_pdf.py`) | Adaptar cabeçalhos/rodapés |

---

## 6. ESTRATÉGIA DE PRODUÇÃO

### Fase 1: Preparação de Dados (pré-requisito)
- Consolidar Base V03 (executar script existente)
- Verificar cobertura de indicadores por município
- Resolver os 4 municípios sem PDF (buscar dados alternativos)
- Investigar outlier Novo Acordo

### Fase 2: Criação do Template e Script de Geração
- Implementar template markdown do novo modelo
- Criar script Python que:
  - Lê a ficha completa (Deepseek V3) como fonte primária
  - Extrai os indicadores necessários
  - Gera o resumo executivo (pode usar IA para condensar)
  - Aplica o template
  - Gera arquivo markdown padronizado

### Fase 3: Geração em Lote
- Gerar 139 fichas no novo formato
- Revisão automatizada: verificar campos vazios, formatação, coerência

### Fase 4: Revisão e Refinamento
- Revisão por amostragem (1 município por microrregião = 8 revisões)
- Ajustes no template e script conforme necessário
- Geração final

### Fase 5: Consolidação e Publicação
- Consolidar em documento único (Volume 2)
- Gerar PDF com paginação e índice
- Revisão final

---

## 7. DECISÕES PENDENTES

1. **Fonte primária para geração**: Fichas completas (Deepseek V3) como fonte de dados E texto analítico? Ou extrair dados puros e gerar análise nova?
2. **Tratamento dos 4 municípios sem PDF**: Aceitar lacuna documentada? Buscar dados manualmente?
3. **Uso de IA na geração**: Usar Claude/Deepseek para condensar as fichas completas no novo formato? Ou abordagem puramente baseada em extração de dados?
4. **Ordem de apresentação**: Alfabética (como atual)? Por microrregião? Por IDHM?
5. **Inclusão de mapa**: Adicionar mapa de localização por município?

---

*Documento elaborado seguindo a metodologia IA-Collab-OS v1.0*
*Caderno Tocantins 2026 — Volume 2*
