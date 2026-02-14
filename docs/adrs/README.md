# Architecture Decision Records (ADRs)

Registro de decisões arquiteturais significativas tomadas durante o projeto Caderno Tocantins 2026.

## O que são ADRs?

Architecture Decision Records (ADRs) são documentos que capturam decisões arquiteturais importantes, incluindo:
- **Contexto** que motivou a decisão
- **Decisão** tomada
- **Alternativas** consideradas e rejeitadas
- **Consequências** positivas e negativas

ADRs promovem **rastreabilidade** e **transparência** nas decisões técnicas, permitindo que futuros colaboradores entendam o "porquê" de escolhas passadas.

---

## Formato

Cada ADR segue o template padrão (`ADR-000-template.md`):

- **Status:** Proposta | Aceita | Rejeitada | Substituída
- **Contexto:** Situação que motivou a decisão
- **Decisão:** O que foi decidido
- **Alternativas Consideradas:** Opções rejeitadas e por quê
- **Consequências:** Impactos positivos e negativos
- **Referências:** Links para handoffs, session logs, commits

---

## Índice de ADRs

| # | Título | Status | Data | Fase |
|---|--------|--------|------|------|
| [ADR-001](./ADR-001-template-based-approach.md) | Template-Based Approach para Fichas Regionais | ✅ Aceita | 2026-02-07 | Fase 1.1 |
| [ADR-002](./ADR-002-panorama-complementar.md) | Panorama Complementar vs. Edição Direta | ✅ Aceita | 2026-02-07 | Fase 1.2 |
| [ADR-003](./ADR-003-build-script-based.md) | Construção Script-Based do Volume 1 v2.0 | ✅ Aceita | 2026-02-07 | Fase 2 |
| [ADR-004](./ADR-004-enfase-agua-sustentabilidade.md) | Ênfase em Água/Sustentabilidade (FICHA 08) | ✅ Aceita | 2026-02-07 | Fase 1.1 |
| [ADR-005](./ADR-005-consolidacao-ascendente.md) | Consolidação Ascendente (Bottom-Up) | ✅ Aceita | 2026-01-20 | Fase 1.0 |
| [ADR-006](./ADR-006-static-data-architecture.md) | Arquitetura de Dados Estáticos | ✅ Aceita | 2026-01-15 | Fase 0 |

---

## Como Criar um Novo ADR

1. Copie o template de `ADR-000-template.md`
2. Renomeie para `ADR-XXX-titulo-decisao.md` (use o próximo número disponível)
3. Preencha todas as seções do template
4. Adicione ao índice acima (tabela)
5. Commit com mensagem: `docs: adicionar ADR-XXX sobre [título]`

---

## Referências

### Handoffs Relacionados
- [HANDOFF-SESSION-0e16a195.md](../handoffs/HANDOFF-SESSION-0e16a195.md) - Decisões Arquiteturais Principais (Seção 9)

### Session Logs
- [SESSION-LOG-0e16a195.md](../session-logs/SESSION-LOG-0e16a195.md) - Timeline e Estatísticas

### Reflexões de Pesquisa-Ação
- [REFLEXAO-PESQUISA-ACAO-0e16a195.md](../reflexoes/REFLEXAO-PESQUISA-ACAO-0e16a195.md) - Seção 4: Reflexão Crítica

---

## Sobre ADRs no Ecossistema

Este repositório (`caderno-tocantins-2026`) documenta decisões relacionadas à **produção de conteúdo e dados**.

**ADRs relacionados a outros repositórios:**
- **tocantins-integrado** (dashboard): ADR-006 (arquitetura de dados estáticos) afeta ambos os repos
- **doutorado** (governança acadêmica): Versões centralizadas de ADRs para análise de tese

---

**Última atualização:** 2026-02-14
**Responsável:** Henrique Marques Ribeiro
**Framework:** IA-Collab-OS v1.0
