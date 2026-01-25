# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não Lançado]

### Em Desenvolvimento
- Coleta de dados complementares (IDEB 2023, Saneamento, Agropecuária)
- Cálculo de consolidações de microrregiões, mesorregiões e estado
- Atualização para V02 com dados completos
- Planejamento e implementação da Parte III (139 municípios)

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
**Última Atualização:** 2026-01-23
