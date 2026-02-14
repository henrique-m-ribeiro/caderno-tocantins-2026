# Arquitetura do Ecossistema de Superinteligência Territorial

**Projeto:** Caderno Tocantins 2026
**Versão:** 1.0
**Data:** 2026-02-14
**Responsável:** Henrique Marques Ribeiro

---

## 📋 Visão Geral

O projeto de **Superinteligência Territorial do Tocantins** é composto por um **ecossistema integrado de 3 repositórios complementares**, cada um com responsabilidades específicas mas interconectadas.

**Princípio Fundamental:**
> Superinteligência territorial não é um artefato tecnológico isolado, mas um **ecossistema sociotécnico** que articula dados + análise humana + IA + validação de stakeholders + governança.

---

## 🌐 Os 3 Repositórios

### 1. 📊 caderno-tocantins-2026 (ESTE REPOSITÓRIO)

**Responsabilidade:** Produção de Conteúdo e Dados Estruturados

**Repositório:** https://github.com/henrique-m-ribeiro/caderno-tocantins-2026

**Entregas:**
- ✅ **Volume 1 v2.0** (579 KB): Análise estadual (Parte I) + Panorama microrregional + 8 fichas regionais
- ✅ **139 fichas municipais** (Deepseek V3): Análise de 15-25 páginas por município
- ✅ **Dados estruturados** (CSV, JSON): 37-76 indicadores por município
- ✅ **Documentação de pesquisa-ação:** Handoffs, session logs, reflexões, ADRs

**Tecnologias:**
- Markdown (documentos de análise)
- Shell Scripts (build automation)
- Python (extractors de dados)
- Git (versionamento e rastreabilidade)

**Status:** ✅ **Ativo** - Fase 2 concluída, Volume 1 v2.0 publicado

**Arquivos-Chave:**
```
/volumes-finalizados/volume-1/CADERNO-TOCANTINS-2026-Vol1-V2.0.md (579 KB)
/analises/fase-1-1-agregacao-municipal/FICHA-XX-REVISADA.md (8 fichas)
/parte-iii-fichas-municipais/deepseek-v3/fichas-completas/ (139 fichas)
/BASE_DADOS_TOCANTINS_V01.csv
/dados-municipais-completos-deepseek-v3.json
```

---

### 2. 🖥️ tocantins-integrado (DASHBOARD)

**Responsabilidade:** Visualização e Interface de Usuário

**Repositório:** https://github.com/henrique-m-ribeiro/tocantins-integrado

**Entregas:**
- ✅ **Dashboard web interativo** (Next.js + React)
- ✅ **Parser Node.js** (1.000+ linhas) que extrai dados dos 139 handbooks municipais
- ✅ **Arquivo JSON** (1.9 MB) com dados estruturados para visualização
- ✅ **Visualizações por município/microrregião:** Gráficos, tabelas, comparações

**Tecnologias:**
- Next.js 14 (framework React)
- Node.js (parser de dados)
- TypeScript (type safety)
- Tailwind CSS (estilização)

**Status:** ✅ **MVP Funcional** com dados estáticos

**Características:**
- Self-contained (não requer backend externo)
- Parser processa fichas markdown e extrai indicadores
- Frontend consome JSON gerado pelo parser
- Deploy estático possível (Vercel, Netlify, GitHub Pages)

**Nota Importante:**
> O dashboard **consome os dados produzidos** por este repositório (`caderno-tocantins-2026`). A arquitetura de dados estáticos (ADR-006) é compartilhada entre os dois repositórios.

---

### 3. 📚 doutorado (GOVERNANÇA ACADÊMICA)

**Responsabilidade:** Gestão de Pesquisa-Ação e Documentação de Tese

**Repositório:** https://github.com/henrique-m-ribeiro/doutorado

**Entregas:**
- ✅ **Planos de ciclos de pesquisa-ação:** Ciclo 1, Ciclo 2, Ciclo 3, Ciclo 4 (em andamento)
- ✅ **Reflexões metodológicas:** Diários de campo, notas de pesquisa
- ✅ **ADRs centralizados:** Decisões arquiteturais para análise de tese
- ✅ **Análises críticas:** Tensões, contradições, aprendizados

**Tecnologias:**
- Markdown (documentação acadêmica)
- Framework IA-Collab-OS (colaboração humano-IA estruturada)
- Git (rastreabilidade de reflexões)

**Status:** ✅ **Ativo** - Ciclo 4 em andamento

**Foco Acadêmico:**
- Pesquisa-ação participativa
- IA como parceiro epistêmico
- Superinteligência territorial como governança (não tecnocracia)
- Documentação como infraestrutura epistêmica

---

## 🔄 Fluxo de Dados

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  [caderno-tocantins-2026] - PRODUÇÃO DE DADOS              │
│                                                             │
│  ► Fichas municipais (139 × 15-25 páginas)                 │
│  ► Fichas regionais (8 microrregiões)                      │
│  ► Volume 1 v2.0 (579 KB consolidado)                      │
│  ► CSV: BASE_DADOS_TOCANTINS_V01.csv                       │
│  ► JSON: dados-municipais-completos-deepseek-v3.json       │
│                                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼ (CSV, JSON, Markdown)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [tocantins-integrado] - CONSUMO E VISUALIZAÇÃO             │
│                                                              │
│  ► Parser Node.js lê fichas markdown                        │
│  ► Extrai indicadores → JSON (1.9 MB)                       │
│  ► Dashboard Next.js consome JSON                           │
│  ► Visualizações interativas (gráficos, tabelas, mapas)     │
│                                                              │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ▼ (Dashboard Web)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [USUÁRIOS FINAIS]                                          │
│                                                              │
│  ► Gestores públicos (SEPLAN-TO, prefeituras)              │
│  ► Candidatos e equipes de campanha                         │
│  ► Pesquisadores e universidades                            │
│  ► Jornalistas e sociedade civil                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘

                       │
                       ▼ (Feedback, Validação)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [doutorado] - GOVERNANÇA E REFLEXÃO                        │
│                                                              │
│  ► Ciclos de pesquisa-ação (planejamento)                  │
│  ► Validação com stakeholders                                │
│  ► Reflexões metodológicas (diários, notas)                 │
│  ► ADRs centralizados (decisões para tese)                  │
│  ► Análise de impacto (formulação de políticas)            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🔗 Referências Cruzadas

### ADRs Compartilhados

**ADR-006: Arquitetura de Dados Estáticos**
- **Decisão:** CSV + JSON + Markdown (sem database/backend tradicional)
- **Afeta:**
  - `caderno-tocantins-2026`: Produção de dados em formatos estáticos
  - `tocantins-integrado`: Consumo de dados estáticos via parser
- **Localização:**
  - [ADR-006 (caderno-tocantins-2026)](./adrs/ADR-006-static-data-architecture.md)
  - ADR-006 (tocantins-integrado) - versão focada em consumo
  - ADR-006 (doutorado) - versão centralizada para análise de tese

### Handoffs Relacionados

**HANDOFF-SESSION-0e16a195**
- **Repositório:** caderno-tocantins-2026
- **Documenta:** Consolidação do Volume 1 v2.0 (Fase 2)
- **Relação com dashboard:** Menciona dashboard como "médio prazo", mas dashboard já foi implementado em paralelo no `tocantins-integrado`
- **Localização:** [docs/handoffs/HANDOFF-SESSION-0e16a195.md](./handoffs/HANDOFF-SESSION-0e16a195.md)

---

## 📐 Princípios Arquiteturais

### 1. Separation of Concerns (Separação de Responsabilidades)

**Cada repositório tem responsabilidade clara:**
- `caderno-tocantins-2026`: **Produção** de dados e análises
- `tocantins-integrado`: **Visualização** de dados
- `doutorado`: **Governança** e reflexão metodológica

**Benefício:** Mudanças em um repositório não quebram os outros (baixo acoplamento).

### 2. Data as Source of Truth (Dados como Fonte Primária)

**Repositório `caderno-tocantins-2026` é fonte primária de dados.**

**Implicação:** Correções/atualizações de dados devem ser feitas em `caderno-tocantins-2026`, não no dashboard.

**Fluxo de atualização:**
1. Corrigir dado em `caderno-tocantins-2026` (CSV/JSON/ficha)
2. Commit e push
3. Dashboard re-executa parser (extrai novos dados)
4. Visualizações atualizadas automaticamente

### 3. Static Data Architecture (Arquitetura de Dados Estáticos)

**Decisão compartilhada (ADR-006):**
- Sem banco de dados relacional (PostgreSQL, MySQL)
- Sem backend API (Node.js/Express, Python/FastAPI)
- Dados em arquivos versionados (CSV, JSON, Markdown)

**Benefícios:**
- ✅ Zero infraestrutura (sem servidor/banco)
- ✅ Versionamento nativo (Git rastreia tudo)
- ✅ Reprodutibilidade (clone do repo = todos os dados)
- ✅ Portabilidade (formatos universais: CSV/JSON)

**Trade-off:**
- ⚠️ Escalabilidade limitada (não suporta milhões de registros)
- ⚠️ Queries complexas difíceis (sem SQL)

### 4. Documentation as Code (Documentação como Código)

**Documentação é artefato de primeira classe:**
- ADRs formais (decisões arquiteturais rastreáveis)
- Handoffs estruturados (transferência de contexto entre sessões)
- Session logs (rastreabilidade de atividades)
- Reflexões de pesquisa-ação (aprendizados metódicos)

**Benefício:** Conhecimento acumulativo, rastreável e auditável.

---

## 🛠️ Tecnologias por Repositório

| Tecnologia | caderno-tocantins-2026 | tocantins-integrado | doutorado |
|------------|------------------------|---------------------|-----------|
| **Markdown** | ✅ Documentos de análise | ❌ | ✅ Reflexões acadêmicas |
| **CSV** | ✅ Dados tabulares | ❌ | ❌ |
| **JSON** | ✅ Dados estruturados | ✅ Consumo | ❌ |
| **Next.js** | ❌ | ✅ Frontend | ❌ |
| **Node.js** | ❌ | ✅ Parser | ❌ |
| **Python** | ✅ Extractors | ❌ | ❌ |
| **Shell Scripts** | ✅ Build automation | ❌ | ❌ |
| **TypeScript** | ❌ | ✅ Type safety | ❌ |
| **Git** | ✅ Versionamento | ✅ Versionamento | ✅ Versionamento |

---

## 🚀 Roadmap Integrado

### Imediato (Fevereiro 2026)

**caderno-tocantins-2026:**
- ✅ Volume 1 v2.0 publicado
- ⏳ Adequação de documentação (este documento)
- ⏳ ADRs formalizados

**tocantins-integrado:**
- ✅ MVP funcional com dados estáticos
- ⏳ Atualizar README (status "pausado" → "MVP ativo")
- ⏳ Deploy em produção (Vercel/Netlify)

**doutorado:**
- ⏳ Revisar Ciclo 4 (refletir pivô para MVP)
- ⏳ Centralizar ADR-006 (para análise de tese)

### Curto Prazo (Março-Abril 2026)

**caderno-tocantins-2026:**
- ⏳ Refatoração V02 (38 → 65 indicadores)
- ⏳ Volume 2: Fichas municipais individuais (139 municípios)
- ⏳ Validação com stakeholders (SEPLAN-TO, prefeituras)

**tocantins-integrado:**
- ⏳ Novas visualizações (mapas, comparações regionais)
- ⏳ Filtros e buscas avançadas
- ⏳ Exportação de dados (PDF, CSV)

**doutorado:**
- ⏳ Diários de sessão detalhados (implementação do MVP)
- ⏳ Análise de impacto (uso do dashboard por stakeholders)

### Médio Prazo (Maio-Agosto 2026)

**Integração entre repositórios:**
- ⏳ **API REST:** Ponte entre `caderno-tocantins-2026` (dados) e `tocantins-integrado` (visualização)
- ⏳ **Atualização automática:** Dashboard re-processa dados quando `caderno-tocantins-2026` atualiza
- ⏳ **Sistema de feedback:** Usuários do dashboard podem sugerir correções de dados

**caderno-tocantins-2026:**
- ⏳ Volume 3: Análises setoriais (educação, saúde, agronegócio)
- ⏳ Sistema de atualização contínua (refresh periódico de dados)

**tocantins-integrado:**
- ⏳ Painel de administração (gestão de conteúdo)
- ⏳ Análises preditivas (IA para projeções)

**doutorado:**
- ⏳ Capítulo de tese (metodologia)
- ⏳ Publicações acadêmicas (artigos, conferências)

### Longo Prazo (2027+)

**Expansão geográfica:**
- ⏳ Replicação para outros estados (Goiás, Mato Grosso)
- ⏳ Rede de inteligência territorial nacional

**Institucionalização:**
- ⏳ Integração com SEPLAN-TO (uso institucional)
- ⏳ Parcerias com universidades (UFT, UnB)
- ⏳ Governança democrática (conselho gestor, comitê técnico)

---

## 📞 Contatos e Links

### Repositórios

| Repositório | URL | Status |
|-------------|-----|--------|
| **caderno-tocantins-2026** | https://github.com/henrique-m-ribeiro/caderno-tocantins-2026 | ✅ Ativo |
| **tocantins-integrado** | https://github.com/henrique-m-ribeiro/tocantins-integrado | ✅ MVP Funcional |
| **doutorado** | https://github.com/henrique-m-ribeiro/doutorado | ✅ Ativo |

### Documentação-Chave

| Documento | Repositório | Descrição |
|-----------|-------------|-----------|
| [Volume 1 v2.0](../volumes-finalizados/volume-1/CADERNO-TOCANTINS-2026-Vol1-V2.0.md) | caderno-tocantins-2026 | Documento consolidado (579 KB) |
| [README-V2.0](../volumes-finalizados/volume-1/README-V2.0.md) | caderno-tocantins-2026 | Guia de uso do Volume 1 |
| [ADRs](./adrs/README.md) | caderno-tocantins-2026 | Decisões arquiteturais formalizadas |
| [HANDOFF-SESSION-0e16a195](./handoffs/HANDOFF-SESSION-0e16a195.md) | caderno-tocantins-2026 | Contexto da Fase 2 |
| Dashboard README | tocantins-integrado | Documentação do MVP (atualizar status) |
| Ciclo 4 | doutorado | Plano de pesquisa-ação (revisar) |

---

## ❓ Perguntas Frequentes

### 1. Por que 3 repositórios separados em vez de um monorepo?

**Razão:** Separation of concerns + governança acadêmica.

- `caderno-tocantins-2026`: Produção de dados (pode ser usado sem dashboard)
- `tocantins-integrado`: Visualização (pode consumir dados de outras fontes no futuro)
- `doutorado`: Governança acadêmica (escopo maior que apenas Tocantins)

**Benefício:** Cada repositório pode evoluir independentemente.

### 2. Como os repositórios se comunicam?

**Atualmente:** Compartilhamento de arquivos (CSV, JSON, Markdown).

**Futuro:** API REST para integração mais robusta.

**Fluxo:**
1. `caderno-tocantins-2026` produz CSV/JSON
2. `tocantins-integrado` clona/baixa arquivos e processa com parser
3. Dashboard exibe visualizações

### 3. O que acontece se dados forem atualizados?

**Fluxo de atualização:**
1. Corrigir dado em `caderno-tocantins-2026` (fonte primária)
2. Commit e push
3. `tocantins-integrado` re-executa parser (manual ou automatizado)
4. Dashboard atualizado com novos dados

**Importante:** Nunca editar dados diretamente no dashboard. Sempre corrigir na fonte (`caderno-tocantins-2026`).

### 4. Quem pode contribuir com os repositórios?

**caderno-tocantins-2026 e tocantins-integrado:**
- Henrique Marques Ribeiro (responsável principal)
- Colaboradores convidados (via pull requests)
- Stakeholders (via issues/feedback)

**doutorado:**
- Henrique Marques Ribeiro (pesquisador)
- Orientadores (feedback acadêmico)

### 5. Como validar dados antes de publicar?

**Processo de validação:**
1. **Validação automática:** Scripts Python verificam consistência (ex: soma de populações municipais = população regional)
2. **Validação por pares:** Revisar com especialistas locais (SEPLAN-TO, universidades)
3. **Validação com stakeholders:** Apresentar para gestores municipais (validam dados de seus municípios)
4. **Validação pública:** Publicar no dashboard, coletar feedback via issues

---

## 📚 Referências Adicionais

### Frameworks e Metodologias

- **IA-Collab-OS:** https://github.com/henrique-m-ribeiro/ia-collab-os
  - Framework de colaboração humano-IA estruturada
  - Handoffs, ADRs, session logs como artefatos de primeira classe

- **Pesquisa-Ação Participativa:** Método de pesquisa com stakeholders

- **Data as Code:** Princípio de versionamento de dados como código

### Inspirações Arquiteturais

- **Jamstack Architecture:** Static site generation + API layer
- **Git-based CMS:** Dados versionados em Git (ex: Netlify CMS, Forestry)
- **Static Data Architecture:** Alternativa a backends tradicionais para projetos de escala média

---

**Última atualização:** 2026-02-14
**Responsável:** Henrique Marques Ribeiro
**Versão:** 1.0

---

<div align="center">

**🌐 Ecossistema de Superinteligência Territorial**

**Dados** (`caderno-tocantins-2026`) + **Visualização** (`tocantins-integrado`) + **Governança** (`doutorado`)

</div>
