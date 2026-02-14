# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não Lançado]

### Próxima Fase (Ciclo 4 ou Pós-Qualificação)
- ⏳ **Validação territorial** com atores locais (Etapa 3 do Plano de Fortalecimento)
- ⏳ **Teste de compreensibilidade** com gestores públicos
- ⏳ **Revisão colaborativa** com equipe de campanha/gabinete
- ⏳ **Eventual atualização** com dados de 2026 (Censo IBGE)
- ⏳ **Volume 1 v2.0** — consolidação ascendente com base nas 139 fichas municipais
- 📋 Planejamento detalhado em `PLANEJAMENTO-FASES-FINAIS.md` e `RESUMO-PLANEJAMENTO.md`

## [2.1.0] - 2026-02-13

### Incorporação do CLAUDE.md e Revisão de Documentos de Referência
- ✅ **CLAUDE.md incorporado** ao repositório (origem: `doutorado/temp-claude-md-files/`)
  - Contexto acadêmico da pesquisa-ação (Ciclo 3)
  - Instruções obrigatórias para agentes IA
  - Mapa de documentos de referência local e externo
  - Relação com repositórios `doutorado`, `ia-collab-os`, `tocantins-integrado`, `framework-v6-mvp`
  - Lacunas acadêmicas conhecidas documentadas
  - Convenções de produção e reflexão (proporção 90/10)
- ✅ **README.md atualizado**
  - Contexto acadêmico adicionado (doutorado em Ciência Política, pesquisa-ação)
  - Referência ao CLAUDE.md incluída
  - Seção "Repositórios Relacionados" adicionada (4 repositórios do ecossistema)
  - Referência ao framework IA-Collab-OS v2.2 atualizada
  - Árvore de estrutura do repositório atualizada com CLAUDE.md
- ✅ **CHANGELOG.md reestruturado**
  - Entrada [2.0.0] adicionada para marco dos 9 volumes finalizados (08/02/2026)
  - Seção "Não Lançado" atualizada para refletir fases futuras reais
  - Documentação de sessão (06-08/02/2026) registrada
- ✅ **.governance/README.md atualizado**
  - Histórico de entregas completo (9 volumes + todas as microrregiões)
  - Referência ao framework IA-Collab-OS v2.2
  - Contexto acadêmico integrado
- ✅ **HANDOFF-PROXIMA-SESSAO.md e RESUMO-PLANEJAMENTO.md** — notas de status adicionadas

## [2.0.0] - 2026-02-08

### ✅ TODOS OS 9 VOLUMES FINALIZADOS E PUBLICADOS

#### Marco Principal
- 🎉 **9 VOLUMES COMPLETOS** — ~1.150 páginas de análise territorial
- 🎉 **139 municípios** do Tocantins cobertos integralmente
- 🎉 **8 microrregiões** com volumes dedicados
- 🎉 **213 agentes IA orquestrados** em uma única sessão (dado central para OE3)

#### Volumes 2-9 — Fichas Municipais por Microrregião (08/02/2026)
- ✅ **Volume 2 — Porto Nacional** (11 municípios, 248 KB)
- ✅ **Volume 3 — Araguaína** (17 municípios, 358 KB)
- ✅ **Volume 4 — Bico do Papagaio** (25 municípios, 484 KB)
- ✅ **Volume 5 — Miracema do Tocantins** (24 municípios, 498 KB)
- ✅ **Volume 6 — Gurupi** (14 municípios, 331 KB)
- ✅ **Volume 7 — Dianópolis** (20 municípios, 419 KB)
- ✅ **Volume 8 — Jalapão** (15 municípios, 319 KB)
- ✅ **Volume 9 — Rio Formoso** (13 municípios, 250 KB)
- Todos < 500 KB (compatíveis com Google Docs)
- Localização: `volumes-finalizados/volume-{2..9}-*/`

#### 139 Fichas Municipais V2 Condensadas (07/02/2026)
- ✅ **139 fichas condensadas** (~5-7 páginas cada, ~250-350 linhas)
- Estrutura: Dados Fundamentais → Resumo Executivo → SWOT → 8 Dimensões → Diagnóstico → Diretrizes → Alertas
- ~45 indicadores por ficha com dados atuais e variação temporal
- 61 labels de microrregião corrigidos
- Localização: `parte-iii-fichas-municipais/fichas-v2/`

#### 139 Fichas Municipais Completas (06/02/2026)
- ✅ **139 fichas completas** (15+ páginas por município, ~2.085 páginas total)
- Geradas via Deepseek V3 a partir dos Perfis Socioeconômicos SEPLAN-TO
- Estrutura padronizada: Resumo Executivo, Dados Fundamentais, SWOT, 9 Dimensões, Diagnóstico Integrado, Diretrizes, Alertas
- Localização: `parte-iii-fichas-municipais/deepseek-v3/fichas-completas/`

#### Documentação de Sessão (06-08/02/2026)
- ✅ **Planejamento estratégico** — 6 fases definidas (`PLANEJAMENTO-FASES-FINAIS.md`, 40+ páginas)
- ✅ **Resumo executivo** — (`RESUMO-PLANEJAMENTO.md`, 5 páginas)
- ✅ **Handoff de sessão** — (`HANDOFF-PROXIMA-SESSAO.md`)
- ✅ **Reflexão de pesquisa-ação** — (`REFLEXAO-PESQUISA-ACAO-SESSION-01RiFRbB4LEyeb9tvvFBdhpF.md`)
- ✅ **Caminho percorrido** — (`CAMINHO-PERCORRIDO-SESSION-01RiFRbB4LEyeb9tvvFBdhpF.md`)
- ✅ **Relato de orquestração de 213 agentes** — contribuição central para OE3
- ✅ **Plano de fortalecimento metodológico** — encerramento da sessão de produção

#### 6 Fichas Microrregionais Revisadas (07/02/2026)
- ✅ 11 municípios ausentes integrados às fichas microrregionais
- ✅ Contagens e análises revisadas
- Localização: `analises/fase-1-1-agregacao-municipal/`

### Adicionado (03/02/2026)
- ✅ **Dicionário de Dados de Referência Criado**
  - Arquivo: `parte-iii-fichas-municipais/deepseek-v3/csv-indicadores/DICIONARIO-DADOS-ABREULANDIA.csv`
  - Estrutura simplificada: 8 colunas × 824 indicadores
  - Documenta todos os indicadores do CSV com metadados completos
  - Serve como referência para todos os 139 municípios
  - Tamanho: 120 KB
  - Categorias cobertas:
    * Demografia e população (séries 1991-2024)
    * IDHM e componentes (1991, 2000, 2010)
    * Educação (matrículas, docentes, IDEB, taxas)
    * Saúde (estabelecimentos, profissionais, mortalidade, vacinação, doenças)
    * Economia (PIB, VAB, empresas, empregos por setor)
    * Finanças públicas (receitas, despesas, transferências)
    * Agricultura (produção, pecuária, aquicultura)
    * Crédito rural (contratos, valores)
    * Infraestrutura (energia, telecomunicações, transportes, saneamento)
    * Meio ambiente (uso da terra, queimadas, resíduos)
    * Indicadores sociais (pobreza, desigualdade, programas sociais)

### Adicionado (31/01/2026)
- 📁 Estrutura `parte-iii-fichas-municipais/deepseek-v3/` criada
- 📄 Prompt completo para geração de fichas municipais (15+ páginas cada)
- 📄 Prompt para extração de indicadores em formato CSV
- 📄 Prompt para geração de dicionário de dados
- 📋 README estratégico com fluxo de trabalho detalhado
- ✅ Análise de 4 protótipos Deepseek como base metodológica
- 📊 Padrões de qualidade definidos para aprovação de entregas

## [1.1.0] - 2026-01-31

### ✅ VOLUME 1 FINALIZADO E PUBLICADO

#### Documento Consolidado
- **CADERNO TOCANTINS 2026 - Vol.1 - V1.1.md** - Documento principal consolidado
  - 282 KB de conteúdo (6.965 linhas)
  - ~100-110 páginas estimadas
  - Integração completa das Partes I e II
  - Ficha técnica, índice e sumário executivo
  - Status: ✅ 100% FINALIZADO

#### Conteúdo do Volume 1

**Parte I - Visão Estadual do Tocantins**
- 9 dimensões de análise consolidadas
- 35+ indicadores estaduais compilados
- ~50-55 páginas de análise substantiva
- Análise multidimensional com matriz SWOT
- 8 mensagens-chave para campanha
- 4 pilares estratégicos 2026-2030
- Narrativa unificadora criada
- Base de dados CSV estruturada

**Parte II - Fichas Regionais**
- 8 microrregiões analisadas em profundidade
- 139 municípios (100% do Tocantins) cobertos
- ~50-55 páginas de análises regionais
- Versões V1.1 revisadas de todas as fichas
- Dados comparativos entre regiões
- Identificação de desafios e oportunidades regionais

#### Documentação de Entrega
- **ENTREGA-VOLUME-1-FINALIZADO.md** - Relatório oficial de conclusão
  - Especificações técnicas completas
  - Métricas de produção documentadas
  - Guia de uso para campanha
  - Cronologia de desenvolvimento
  - Próximos passos definidos

### Cobertura Territorial Completa
- ✅ **Estado do Tocantins:** Análise estadual 100%
- ✅ **8 Microrregiões IBGE:** 100% mapeadas
- ✅ **139 Municípios:** 100% incluídos nas análises regionais
- ✅ **População:** ~1.607.000 habitantes cobertos

### Destaques do Volume 1

#### Mensagens-Chave Identificadas
1. Economia: 4º maior crescimento do Brasil (7,9%)
2. Educação: 1º lugar do Norte no IDEB (6.1)
3. Social: 9º melhor Gini nacional
4. Saúde: 1º lugar nacional em vacinação infantil
5. Agropecuária: Safra recorde 8,9M ton (+16%)
6. Infraestrutura: BR-153 duplicação + Ponte Araguaia R$ 233M
7. Mineração: 7º produtor de ouro + R$ 4bi investimentos
8. Histórico: 173% expansão econômica em 21 anos

#### Análises Regionais Consolidadas
- Porto Nacional: Centro político-administrativo
- Araguaína: Capital econômica do norte
- Bico do Papagaio: Desafios sociais e oportunidades turísticas
- Miracema: Transição demográfica e potencial industrial
- Gurupi: Agronegócio forte e logística estratégica
- Dianópolis: Patrimônio histórico e turismo cultural
- Jalapão: Ecoturismo mundial e paradoxo econômico
- Rio Formoso: Potência agropecuária

### Qualidade e Governança
- ✅ 100% de fontes oficiais (IBGE, INEP, DATASUS, SNIS, CONAB, SEPLAN-TO)
- ✅ Rastreabilidade total de todas as afirmações
- ✅ Dados 2023-2024 (mais recentes disponíveis)
- ✅ Metodologia IA-Collab-OS aplicada rigorosamente
- ✅ Transparência sobre limitações e lacunas de dados

### Modificado
- Estrutura do repositório organizada com Volume 1 publicado
- Link público disponível no GitHub
- Documentação de referência atualizada

## [1.2.0-dev] - 2026-01-27

### Adicionado

#### Planejamento da Refatoração V02
- **PLANO_REFATORACAO_V02_2026-01-27.md** - Plano completo e validado
  - Contexto detalhado dos problemas identificados
  - Estrutura alvo das planilhas revisada (~65 colunas)
  - 6 planilhas de consolidação separadas por classificação
  - Estratégia de extração de PDFs SEPLAN-TO
  - 7 fases de implementação (41-61h estimadas)
  - 4 sprints de trabalho em paralelo
  - Critérios de sucesso e validação
  - 17 scripts Python planejados

#### Nova Fonte de Dados Identificada
- **Perfis Socioeconômicos Municipais SEPLAN-TO** (8ª Edição - Dezembro 2024)
  - 139 PDFs oficiais (um por município, ~40MB cada)
  - 10 capítulos estruturados por perfil
  - Cobertura de ~85-95% dos indicadores necessários
  - Dados atualizados e metodologia consistente
  - Fonte: https://www.to.gov.br/seplan/perfil-socioeconomico-municipal/

#### Classificações Regionais SEPLAN-TO 2024
- **8 Regiões de Planejamento** (Portaria nº 91 - 22/10/2024):
  - Bico do Papagaio (25), Norte (15), Meio Norte (25)
  - Vale do Araguaia (15), Central (14), Jalapão (9)
  - Sul (17), Sudeste (19)
- **3 Macrorregiões**:
  - Norte: 65 municípios
  - Central: 38 municípios
  - Sul: 36 municípios

### Decisões Técnicas Aprovadas

#### Correções de Design Não Aprovadas
- ✅ Restaurar coluna `territorio_tipo` (removida automaticamente)
- ✅ Restaurar sufixos `_ano_ref` para TODOS os indicadores (permitir análise temporal)
- ✅ Separar consolidações em planilhas independentes (6 planilhas vs linhas misturadas)
- ✅ Adicionar 6 tipos de classificações regionais (IBGE 1989, IBGE 2017, SEPLAN 2024)

#### Nova Estratégia de Dados
- ✅ Extração automatizada de 139 PDFs (vs coleta manual via APIs)
- ✅ Geração automática de fichas municipais da Parte III
- ✅ Revisão das Partes I e II integrada ao fluxo
- ✅ Trabalho em paralelo em 4 sprints (aprovado pelo usuário)

### Estrutura Planejada

#### Planilhas de Dados (Nova Arquitetura)
1. **BASE_DADOS_TOCANTINS_V02.csv** - Planilha principal
   - 139 municípios × ~65 colunas
   - 11 colunas de identificação territorial
   - Colunas `_ano_ref` restauradas para análise temporal

2. **Planilhas de Consolidação** (6 arquivos separados):
   - `BASE_CONSOLIDACOES_MICRORREGIOES_IBGE_1989.csv` (8 linhas)
   - `BASE_CONSOLIDACOES_MESORREGIOES_IBGE_1989.csv` (2 linhas)
   - `BASE_CONSOLIDACOES_REGIOES_PLANEJAMENTO_SEPLAN_2024.csv` (8 linhas)
   - `BASE_CONSOLIDACOES_MACRORREGIOES_SEPLAN_2024.csv` (3 linhas)
   - `BASE_CONSOLIDACAO_ESTADUAL.csv` (1 linha)

3. **METADADOS_BASE_DADOS_TOCANTINS_V02.csv** - Expandido
   - ~65-70 variáveis × 14 campos de documentação

#### Scripts de Automação (17 planejados)
- `migrar_v01_para_v02.py` - Migração de dados existentes
- `mapear_regioes_planejamento.py` - Mapeamento classificações regionais
- `download_perfis_seplan_to.py` - Download de PDFs
- `extrair_tabelas_perfis_seplan.py` - Extração automatizada
- `consolidar_extraidos_perfis.py` - Consolidação e validação
- `calcular_consolidacoes.py` - Gerar planilhas de consolidação
- `gerar_fichas_municipais.py` - Geração automática Parte III

#### Documentação de Mapeamento (3 documentos)
- `MAPEAMENTO_INDICADORES_SEPLAN_TO.md` - PDFs → estrutura
- `MAPEAMENTO_REGIOES_PLANEJAMENTO_2024.md` - Municípios → Regiões
- `RELATORIO_REFATORACAO_V02.md` - Relatório de execução

### Modificado
- README.md - Atualizado com seção de Refatoração V02
  - Badges atualizados (status, Parte III, cobertura de dados)
  - Seção completa sobre Refatoração V02
  - Status do projeto atualizado com 8 fases
  - Próximos passos detalhados
- Estrutura de governança - Preparada para trabalho em paralelo

### Meta de Cobertura de Dados V02
- **Atual:** ~35% em média
- **Meta V02:** ≥85% em média
- **Fonte:** Extração dos 139 PDFs SEPLAN-TO + APIs complementares

### Melhorias Incorporadas Após Avaliação (27/01/2026 - Tarde)

**Avaliador:** Manus (CTO) - Framework IA-Collab-OS
**Avaliação:** 🟢 Excelente (4/5 princípios) | Aprovado com melhorias

#### 1. Mitigação de Riscos na Extração de PDFs
- ✅ **Fase 1 expandida:** 2-3h → 3-5h
  - Amostra aumentada de 3-5 para 10-15 PDFs
  - Amostragem estratificada: grandes, médios e pequenos municípios
  - Cobertura de todas as 8 Regiões de Planejamento
- ✅ **Novo documento:** `RELATORIO_VARIABILIDADE_PDFS_SEPLAN.md`
  - Análise de variações estruturais entre PDFs
  - Tipos de exceções encontradas
  - Estratégias de fallback para casos especiais
  - Estimativa mais precisa de taxa de sucesso

#### 2. Detalhamento do Processo de Validação de Dados
- ✅ **Script `validar_dados.py` expandido** com 4 tipos de validação:
  1. **Validação de Schema:** Tipos de dados corretos
  2. **Validação de Intervalo (Range):** Valores dentro de limites plausíveis
  3. **Validação Cruzada (Cross-field):** Consistência entre campos relacionados
  4. **Validação de Consistência Histórica:** Comparação com dados V01
- ✅ **Critérios de aprovação objetivos:**
  - Schema: <5% de erros de tipo
  - Range: <10% de valores fora do esperado
  - Cruzada: <5% de inconsistências
  - Histórica: <10% de divergências >5%
- ✅ **5 relatórios de validação:**
  - `RELATORIO_VALIDACAO_SCHEMA.txt`
  - `RELATORIO_VALIDACAO_RANGES.txt`
  - `RELATORIO_VALIDACAO_CRUZADA.txt`
  - `RELATORIO_VALIDACAO_HISTORICA.txt`
  - `RELATORIO_VALIDACAO_CONSOLIDADO.md`

#### 3. Aprofundamento da Reflexão e Melhoria Contínua
- ✅ **Nova seção no HANDOFF:** "Análise da Causa Raiz das Divergências da V01"
  - Análise detalhada de 4 divergências da implementação anterior
  - Identificação do padrão raiz: otimização prematura
  - Estratégias de prevenção para futuras colaborações
  - Checklist de validação pré-implementação
  - Lições para futuras colaborações IA-Humano

#### Impacto nas Estimativas
- **Documentação:** 3 → 4 documentos (+1 Relatório Variabilidade)
- **Scripts:** 17 → 18 scripts (+1 validar_dados.py detalhado)
- **Fase 1:** 2-3h → 3-5h (+1-2h)
- **Fase 3:** 10-15h → 12-18h (+2-3h)
- **Esforço total:** 41-61h → 44-66h (+3-5h)
- **Duração total:** 7-10 dias → 8-11 dias úteis (6h/dia)

#### Avaliação Framework IA-Collab-OS
| Princípio | Antes | Depois |
|-----------|-------|--------|
| 1. Humano no Comando | 🟢 Excelente | 🟢 Excelente |
| 2. Colaboração Explícita | 🟢 Excelente | 🟢 Excelente |
| 3. Documentação como Código | 🟢 Excelente | 🟢 Excelente |
| 4. Execução Incremental | 🟢 Excelente | 🟢 Excelente |
| 5. Reflexão e Melhoria | 🟡 Bom | 🟢 Excelente |

**Status:** ✅ Plano refinado e aprovado para implementação

### Estimativas (Atualizadas)
- **Esforço:** 44-66 horas de trabalho (+3-5h de melhorias)
- **Duração:** 8-11 dias úteis (com 6h/dia) OU 11-16 dias úteis (com 4h/dia)
- **Estratégia:** 4 sprints de trabalho em paralelo
- **Status:** ✅ Planejamento completo e refinado | ⏳ Aguardando implementação

## [1.1.0] - 2026-01-23

### Adicionado

#### Infraestrutura de Dados Consolidados
- **BASE_DADOS_TOCANTINS_V01.csv** - Planilha consolidada (151 linhas × 37 colunas)
  - 139 municípios + 8 microrregiões + 2 mesorregiões + 1 estado
  - 8 dimensões de análise (territorial, demográfica, econômica, desenvolvimento, educação, saúde, saneamento, agropecuária)
  - Nomenclatura padronizada com prefixos (terr_, demo_, econ_, etc.)
- **METADADOS_BASE_DADOS_TOCANTINS_V01.csv** - Dicionário de dados completo
  - 38 variáveis × 14 campos de documentação
  - Rastreabilidade completa (fonte, método, limitações, endpoints de atualização)
- **Script consolidar_dados.py** - Automação de consolidação
  - Processa 8 arquivos de microrregiões com formatos heterogêneos
  - Calcula indicadores derivados (crescimento, densidade)
  - Computa consolidações de microrregiões

#### Documentação de Planejamento e Análise
- **PLANEJAMENTO_PLANILHAS_CONSOLIDADAS.md** (13.000+ palavras)
  - Especificação completa da estrutura de dados
  - 8 dimensões detalhadas
  - Fórmulas de agregação e consolidação
  - Timeline e prioridades de coleta
- **ANALISE_PLANILHAS_CONSOLIDADAS.md** (8.000+ palavras)
  - Avaliação detalhada: 9.8/10
  - Análise de pontos fortes e áreas de atenção
  - Recomendações para próximas etapas
- **MAPEAMENTO_MUNICIPIOS_TO.md**
  - Mapeamento completo dos 139 municípios
  - Organização por mesorregião e microrregião
  - Códigos IBGE validados
  - Identificação de duplicações para validação

#### Integração da Parte I - Visão Estadual
- Diretório completo `/parte-i-visao-estadual/`
  - 9 documentos dimensionais (~50-55 páginas)
  - Documento consolidado (84 KB, 1.395 linhas)
  - Sumário executivo
  - Base de dados CSV com 35+ indicadores estaduais
  - Análise SWOT completa
- **README_PARTE_I.md** - Documentação completa da Parte I

#### Documentação de Sessão (Metodologia IA Collab OS)
- **HANDOFF-SESSION-2026-01-23.md** (18.000+ palavras)
  - Contexto completo e entregas
  - Próximos passos com estratégias detalhadas
  - Riscos e bloqueios identificados
  - Checklist para continuidade
- **SESSION-LOG-2026-01-23.md** (8.000+ palavras)
  - Registro cronológico de atividades
  - Decisões técnicas documentadas
  - Commits e branches
- **DIARIO-PESQUISA-ACAO-2026-01-23.md** (13.000+ palavras)
  - Reflexão meticulosa sobre metodologia
  - 5 ciclos de ação-reflexão
  - Aprendizados e contribuições metodológicas
  - Autoavaliação crítica

### Cobertura de Dados Atualizada
- **População 2022:** 95.7% (133/139 municípios)
- **População 2010:** 59.0% (82/139 municípios)
- **Área territorial:** 38.8% (54/139 municípios)
- **PIB per capita:** 29.5% (41/139 municípios)
- **IDHM 2010:** 27.3% (38/139 municípios)
- **Taxa escolarização:** 25.9% (36/139 municípios)
- **Mortalidade infantil:** 16.5% (23/139 municípios)
- **Cobertura média geral:** ~35%

### Pendente
- IDEB 2023: 0% (prioridade máxima)
- Saneamento (SNIS): 0% (prioridade alta)
- Agropecuária (PAM/PPM/VBP): 0% (prioridade alta)
- Consolidações de microrregiões/mesorregiões/estado: 0%
- Resolução de duplicações municipais

## [1.0.0] - 2026-01-23

### Adicionado
- Estrutura inicial do repositório GitHub
- README.md principal com visão geral completa do projeto
- .gitignore para proteção de arquivos sensíveis
- Estrutura de diretórios:
  - `.governance/` - Governança e metodologia
  - `dados/` - Datasets das microrregiões
  - `parte-ii-fichas-regionais/` - Fichas regionais
  - `docs/` - Documentação do projeto
- README.md em subpastas principais:
  - `dados/README.md`
  - `parte-ii-fichas-regionais/README.md`
  - `.governance/README.md`
- CHANGELOG.md para rastreamento de mudanças
- Relatório completo do projeto em `docs/RELATORIO_COMPLETO_PROJETO.md`

### Parte II - Fichas Regionais (V1.0)
- ✅ Ficha 05: Microrregião de Gurupi (9.5/10)
- ✅ Ficha 06: Microrregião de Dianópolis (9.2/10)
- ✅ Ficha 07: Microrregião do Jalapão (9.5/10)
- ✅ Ficha 08: Microrregião de Rio Formoso (9.8/10)

### Dados Coletados
- 8 datasets CSV (v01) das microrregiões
- 4 relatórios de coleta de dados:
  - `RELATORIO-COLETA-GURUPI.md`
  - `RELATORIO-COLETA-DIANOPOLIS.md`
  - `RELATORIO-COLETA-JALAPAO.md`
  - `RELATORIO-COLETA-RIO-FORMOSO.md`

### Cobertura de Dados
- População 2010 e 2022: 139 municípios (100%)
- Área territorial: 48 municípios (35%)
- PIB per capita: 48 municípios (35%)
- IDHM: 48 municípios (35%)
- Taxa de escolarização: 48 municípios (35%)
- Mortalidade infantil: 45 municípios (32%)

## [0.1.0] - 2026-01-XX

### Adicionado
- Criação do repositório
- Primeiras 4 fichas regionais (Porto Nacional, Araguaína, Bico do Papagaio, Miracema)
- Estrutura inicial de governança
- Metodologia IA Collab OS

---

## Legenda de Tipos de Mudança

- `Adicionado` - para novas funcionalidades
- `Modificado` - para mudanças em funcionalidades existentes
- `Descontinuado` - para funcionalidades que serão removidas
- `Removido` - para funcionalidades removidas
- `Corrigido` - para correção de bugs
- `Segurança` - para vulnerabilidades

---

**Formato de Data:** AAAA-MM-DD
**Última Atualização:** 2026-02-13
