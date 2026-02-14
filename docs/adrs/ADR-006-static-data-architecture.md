# ADR-006: Arquitetura de Dados Estáticos (Static Data Architecture)

**Status:** ✅ Aceita
**Data:** 2026-01-15
**Responsável:** Henrique Marques Ribeiro
**Session:** Múltiplas sessões (Fase 0 - Fase 2)
**Fase:** Fase 0 - Planejamento Arquitetural

---

## Contexto

No início do projeto Caderno Tocantins 2026, precisávamos decidir a **arquitetura de armazenamento e distribuição de dados** territoriais.

**Requisitos:**
- Armazenar dados de 139 municípios (37-76 indicadores cada)
- Produzir fichas regionais e municipais (documentos markdown)
- Possibilitar visualização (dashboard web)
- Facilitar iteração e atualizações
- Permitir versionamento e rastreabilidade

**Contexto do projeto:**
- Projeto de pesquisa-ação (não software de produção)
- Equipe pequena (pesquisador + IA)
- Necessidade de velocidade de iteração
- Dados relativamente estáticos (atualizações anuais, não em tempo real)
- Prazo limitado (campanha eleitoral 2026)

---

## Decisão

**Decidimos usar arquitetura de dados estáticos: CSV + JSON + Markdown (sem database/backend tradicional).**

**Componentes:**

1. **CSV (Planilhas Consolidadas)**
   - `BASE_DADOS_TOCANTINS_V01.csv`: 52 colunas planejadas (37 implementadas)
   - `METADADOS_BASE_DADOS_TOCANTINS_V01.csv`: 14 campos de metadados por variável
   - Formato: Município, Microrregião, Mesorregião, [Indicadores]

2. **JSON (Dados Estruturados)**
   - `dados-municipais-completos-deepseek-v3.json`: 139 municípios com dados estruturados
   - Versões: v6 (55 indicadores), v7 (76 indicadores), v9 (validado)
   - Formato hierárquico: { município: { demografia, economia, educação, saúde, ... } }

3. **Markdown (Documentos de Análise)**
   - Fichas municipais (139 arquivos, 15-25 páginas cada)
   - Fichas regionais (8 arquivos, 50-70 KB cada)
   - Volume 1 v2.0 (579 KB, 12.572 linhas)

4. **Shell Scripts (Build Automation)**
   - `build_volume1_v2.sh`: Compilação automatizada de componentes
   - Python extractors: Extração de indicadores de PDFs/JSON

**Ausentes (intencionalmente):**
- ❌ Banco de dados relacional (PostgreSQL, MySQL)
- ❌ Backend API (Node.js, Python/FastAPI)
- ❌ ORM (Prisma, SQLAlchemy)
- ❌ Infraestrutura de deploy (AWS, Azure, Heroku)

---

## Alternativas Consideradas

### Alternativa 1: PostgreSQL + API REST + Frontend

- **Descrição:** Arquitetura tradicional web: PostgreSQL (dados) → Node.js/Python API (backend) → Next.js (frontend)
- **Prós:**
  - Padrão estabelecido para aplicações web
  - Queries complexas facilitadas (SQL)
  - Escalabilidade (suporta milhões de registros)
  - Atualizações em tempo real possíveis
- **Contras:**
  - Complexidade excessiva para 139 municípios (PostgreSQL é overkill)
  - Infraestrutura de deploy necessária (servidor, banco, CI/CD)
  - Tempo de setup (configuração de DB, migrations, ORM)
  - Dificulta iteração (mudanças no schema requerem migrations)
  - Custo de manutenção (servidor rodando 24/7)
- **Por que foi rejeitada:** Complexidade desnecessária para escala do projeto (139 municípios, não 139 milhões).

### Alternativa 2: Planilhas Google Sheets como "Backend"

- **Descrição:** Usar Google Sheets como banco de dados (via API), frontend lê diretamente de Sheets
- **Prós:**
  - Interface familiar (planilhas)
  - Colaboração facilitada (múltiplos editores)
  - Zero setup de infraestrutura
- **Contras:**
  - Limites de API (quotas, rate limiting)
  - Latência (requisições à API do Google)
  - Dependência de serviço externo (Google)
  - Versionamento precário (histórico de versões limitado)
  - Queries complexas difíceis (não é SQL)
- **Por que foi rejeitada:** Dependência de serviço externo + limites de API + versionamento precário.

### Alternativa 3: Firebase / Supabase (Backend-as-a-Service)

- **Descrição:** Usar BaaS para armazenamento (Firebase Firestore, Supabase PostgreSQL) + autenticação + hosting
- **Prós:**
  - Infraestrutura gerenciada (zero configuração de servidores)
  - Tier gratuito robusto (Firebase free tier: 50k reads/dia)
  - Facilita desenvolvimento (SDK pronto)
- **Contras:**
  - Vendor lock-in (difícil migrar de Firebase para outro)
  - Custo em escala (além do free tier, preços sobem)
  - Complexidade de setup (configuração de regras, índices)
  - Dados não versionáveis em git (ficam no serviço)
- **Por que foi rejeitada:** Dados não versionáveis + vendor lock-in + complexidade desnecessária.

---

## Consequências

### Positivas

- ✅ **Simplicidade extrema:** Zero infraestrutura de servidor/banco/backend
- ✅ **Velocidade de iteração:** Editar CSV → commit → rebuild (segundos)
- ✅ **Reprodutibilidade total:** Clone do repo = todos os dados
- ✅ **Versionamento nativo:** Git rastreia TODAS as mudanças em CSV/JSON/Markdown
- ✅ **Rastreabilidade absoluta:** Cada alteração em dados rastreável via git log
- ✅ **Zero custo de infraestrutura:** Nenhum servidor rodando, nenhum banco hospedado
- ✅ **Portabilidade máxima:** Dados podem ser lidos por qualquer ferramenta (CSV/JSON são formatos universais)
- ✅ **Offline-first:** Trabalho não depende de conexão (dados locais)

### Negativas

- ⚠️ **Escalabilidade limitada:** Não suporta milhões de registros (CSV/JSON não são otimizados)
- ⚠️ **Queries complexas difíceis:** Sem SQL, joins/aggregations requerem código manual
- ⚠️ **Não suporta tempo real:** Atualizações exigem rebuild (não é live)
- ⚠️ **Tamanho de arquivos:** JSON de 1.9 MB pode ser lento para carregar no frontend
- ⚠️ **Concorrência limitada:** Git não resolve conflitos em CSV automaticamente

### Mitigações

- **Escalabilidade:** Para 139 municípios, CSV/JSON são suficientes. Se projeto escalar (outros estados), migrar para DB.
- **Queries complexas:** Python/Node.js podem processar CSV/JSON (pandas, lodash) para queries.
- **Tempo real:** Não é requisito (dados atualizados anualmente, não minuto a minuto).
- **Tamanho:** 1.9 MB é aceitável com compressão gzip (~200 KB). Lazy loading se necessário.
- **Concorrência:** Equipe pequena, conflitos raros. Manual merge quando ocorrer.

---

## Trade-offs Identificados

**Trade-off 1: Simplicidade vs. Escalabilidade**
- **Ganhamos:** Simplicidade (zero infraestrutura, iteração rápida)
- **Perdemos:** Escalabilidade (não suporta milhões de registros)
- **Avaliação:** Trade-off justificado. 139 municípios não exigem PostgreSQL.

**Trade-off 2: Versionamento vs. Queries Complexas**
- **Ganhamos:** Versionamento nativo (Git rastreia tudo)
- **Perdemos:** Queries complexas facilitadas (SQL não disponível)
- **Avaliação:** Trade-off justificado. Rastreabilidade é mais importante que queries complexas nesta fase.

---

## Cross-Repository Impact

**⚠️ IMPORTANTE:** Esta decisão afeta DOIS repositórios:

### 1. caderno-tocantins-2026 (ESTE REPOSITÓRIO)
**Responsabilidade:** Produção de dados estáticos

**Arquivos:**
- `BASE_DADOS_TOCANTINS_V01.csv`
- `dados-municipais-completos-deepseek-v3.json`
- Fichas municipais/regionais (markdown)

### 2. tocantins-integrado (DASHBOARD)
**Responsabilidade:** Consumo de dados estáticos

**Repositório:** https://github.com/henrique-m-ribeiro/tocantins-integrado

**Arquivos:**
- Parser Node.js (1.000+ linhas) que lê fichas markdown e extrai dados
- JSON (1.9 MB) gerado pelo parser
- Frontend Next.js que consome JSON

**Relação:** Dashboard CONSOME dados produzidos por este repositório (static data architecture é compartilhada).

---

## Implementação

**Data de Implementação:** 2026-01-15 (decisão inicial, implementação contínua)

**Commits Relacionados:**
- Múltiplos commits ao longo do projeto

**Arquivos Criados:**
- `BASE_DADOS_TOCANTINS_V01.csv`
- `METADADOS_BASE_DADOS_TOCANTINS_V01.csv`
- `dados-municipais-completos-deepseek-v3.json` (v6, v7, v9)
- 139 fichas municipais (markdown)
- 8 fichas regionais (markdown)

---

## Referências

### Documentação Interna
- **Handoff:** [HANDOFF-SESSION-0e16a195.md](../handoffs/HANDOFF-SESSION-0e16a195.md) - Seção 3.2 (Dados Estruturados)
- **Planejamento:** [PLANEJAMENTO_PLANILHAS_CONSOLIDADAS.md](../../docs/PLANEJAMENTO_PLANILHAS_CONSOLIDADAS.md)
- **Reflexão:** [REFLEXAO-PESQUISA-ACAO-0e16a195.md](../reflexoes/REFLEXAO-PESQUISA-ACAO-0e16a195.md) - Insight 2

### Cross-Repository
- **Dashboard (tocantins-integrado):** ADR-006 (versão focada em consumo de dados)
- **Doutorado:** ADR-006 centralizado (para análise de tese)

---

## Notas Adicionais

### Aprendizado Metodológico

**Insight:** Superinteligência territorial é ecossistema sociotécnico.

Da REFLEXAO-PESQUISA-ACAO-0e16a195.md:
> "Superinteligência territorial não é artefato tecnológico isolado, mas ecossistema que articula dados + análise humana + IA + validação stakeholders + governança. Arquitetura de dados estáticos é componente desse ecossistema, não substituição de governança."

### Princípio de Design: Data as Code

Esta decisão reflete princípio de **data as code**:
- Dados versionados em git (como código)
- Mudanças rastreáveis (git log, git diff)
- Reprodutíveis (git clone = todos os dados)
- Auditáveis (quem mudou o quê, quando, por quê)

**Benefício:** Transparência total sobre origem e evolução dos dados.

### Quando Migrar para Database?

**Indicadores de que é hora de migrar:**
- Volume de dados > 10 MB (CSVs ficam lentos)
- Necessidade de queries complexas frequentes (joins, aggregations)
- Múltiplos colaboradores editando dados simultaneamente (conflitos de merge frequentes)
- Requisito de atualizações em tempo real
- Integração com sistemas externos (APIs que exigem DB)

**Para Volume 2 (139 fichas municipais):** Static data architecture ainda é adequada.

**Para expansão multi-estadual (1.000+ municípios):** Considerar migração para PostgreSQL.

---

## Histórico de Revisões

| Data | Autor | Mudança |
|------|-------|---------|
| 2026-02-14 | Henrique Marques Ribeiro | Criação inicial (formalização de decisão tomada em 2026-01-15) |

---

**Última atualização:** 2026-02-14
**Próxima revisão:** Após Volume 2 (avaliar se static data architecture ainda é adequada para 139 fichas municipais completas)

**TODO:** Criar versão de ADR-006 no repositório `tocantins-integrado` (focada em consumo de dados) e versão centralizada no repositório `doutorado` (para análise de tese).
