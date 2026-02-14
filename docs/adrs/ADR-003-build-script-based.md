# ADR-003: Construção Script-Based do Volume 1 v2.0

**Status:** ✅ Aceita
**Data:** 2026-02-07
**Responsável:** Henrique Marques Ribeiro
**Session:** 0e16a195-e9a6-4564-b12e-016b43def69a
**Fase:** Fase 2 - Consolidar e Publicar Volume 1 v2.0

---

## Contexto

Ao final da Fase 1.2, tínhamos:
- **PARTE-I-COMPLETA.md:** Visão estadual (v1.0, 1.395 linhas)
- **PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md:** Panorama microrregional (v2.0, 455 linhas)
- **8 Fichas Regionais Revisadas:** FICHA-01 a FICHA-08 (total ~450 KB)

O Volume 1 v2.0 deveria integrar todos esses componentes em um documento único consolidado.

**Problema:** Como construir Volume 1 v2.0 de forma reprodutível e manutenível?

**Complexidade:**
- Volume 1 v1.1 tinha 6.965 linhas (282 KB)
- Volume 1 v2.0 teria ~12.000+ linhas (estimativa)
- Estrutura: Seção I (extraída de v1.1) + Seção II (panorama + 8 fichas)

**Restrições:**
- Necessidade de atualizar metadados de versão (1.1 → 2.0)
- Possibilidade de correções futuras nos componentes (fichas, panorama)
- Exigência de processo rastreável e documentado

---

## Decisão

**Decidimos usar script shell (`build_volume1_v2.sh`) para compilação automatizada.**

**Processo do Script:**
1. Extrair linhas 1-1980 de `CADERNO TOCANTINS 2026 - Vol.1 - V1.1.md` (Seção I - Visão Estadual)
2. Atualizar metadados de versão: `sed 's/V1.1/V2.0/' e 's/Versão: 1.1/Versão: 2.0/'`
3. Adicionar Seção II com header "ANÁLISE POR MICRORREGIÃO"
4. Concatenar `PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md` (tail -n +3 para pular header)
5. Adicionar separador "FICHAS REGIONAIS DETALHADAS"
6. Concatenar 8 fichas revisadas sequencialmente (FICHA-01 a FICHA-08)
7. Adicionar rodapé com ficha técnica v2.0

**Resultado:** `CADERNO-TOCANTINS-2026-Vol1-V2.0.md` (579 KB, 12.572 linhas)

---

## Alternativas Consideradas

### Alternativa 1: Montagem Manual (Copy-Paste)

- **Descrição:** Abrir todos os arquivos, copiar e colar seções manualmente em novo documento
- **Prós:**
  - Controle total sobre formatação
  - Possibilidade de ajustes ad-hoc durante cópia
  - Não requer conhecimento de shell scripting
- **Contras:**
  - Extremamente propenso a erros (esquecer arquivos, ordem errada)
  - Não reprodutível (próxima versão requer refazer tudo)
  - Não rastreável (não documenta processo)
  - Edições manuais no Volume 1 v2.0 serão perdidas na próxima build
- **Por que foi rejeitada:** Erro-prone, não reprodutível, não documenta processo.

### Alternativa 2: Pipeline de CI/CD (GitHub Actions)

- **Descrição:** Configurar GitHub Actions para compilar Volume 1 v2.0 automaticamente a cada commit em componentes
- **Prós:**
  - Totalmente automatizado (zero intervenção humana)
  - Build sempre atualizado com últimas versões dos componentes
  - Integração contínua de atualizações
- **Contras:**
  - Complexidade excessiva para projeto de pesquisa (não é software production)
  - Requer configuração de YAML, workflows, triggers
  - Dificulta debugging (logs remotos vs. output local)
  - Volume 1 v2.0 seria reconstruído em cada commit menor (overkill)
- **Por que foi rejeitada:** Complexidade desnecessária. Pipeline CI/CD é mais adequado para software em produção com deploys frequentes.

### Alternativa 3: Makefile (Ferramenta Make)

- **Descrição:** Usar Makefile para definir regras de build do Volume 1 v2.0
- **Prós:**
  - Padrão estabelecido para build automation
  - Suporta dependências entre arquivos (rebuild apenas se componentes mudaram)
  - Linguagem declarativa (define "o quê", não "como")
- **Contras:**
  - Curva de aprendizado (sintaxe de Makefile é peculiar)
  - Overkill para build simples (concatenação sequencial)
  - Menos legível que shell script para iniciantes
- **Por que foi rejeitada:** Shell script é mais legível e suficiente para este caso.

---

## Consequências

### Positivas

- ✅ **Reprodutibilidade:** Volume 1 v2.0 pode ser reconstruído executando `./build_volume1_v2.sh`
- ✅ **Rastreabilidade:** Processo documentado em código (script é documentação executável)
- ✅ **Eficiência:** Build completo em ~10 segundos
- ✅ **Facilita atualizações:** Corrigir componente (ficha) → executar script → Volume 1 v2.0 atualizado
- ✅ **Documentação como código:** Script explica processo (comentários, estrutura clara)
- ✅ **Versionamento:** Script também é versionado no git

### Negativas

- ⚠️ **Edições manuais no Volume 1 v2.0 são sobrescritas:** Próximo rebuild perde edições manuais
- ⚠️ **Dependência do script:** Se script for perdido (/tmp limpo), processo precisa ser reconstruído
- ⚠️ **Requer conhecimento de shell:** Futuros colaboradores precisam entender bash

### Mitigações

- **Edições sobrescritas:** Volume 1 v2.0 é **artefato derivado**, não fonte primária. Edições devem ser feitas em componentes.
- **Dependência:** Mover script de /tmp para `docs/scripts/build_volume1_v2.sh` (versionado no git)
- **Conhecimento de shell:** Script é simples (~100 linhas) e bem comentado. Pode ser convertido para Python se necessário.

---

## Trade-offs Identificados

**Trade-off 1: Automação vs. Controle Manual**
- **Ganhamos:** Reprodutibilidade, velocidade, rastreabilidade
- **Perdemos:** Controle sobre ajustes ad-hoc durante montagem
- **Avaliação:** Trade-off justificado. Ajustes devem ser feitos em componentes, não no artefato final.

**Trade-off 2: Simplicidade vs. Sofisticação**
- **Ganhamos:** Simplicidade (shell script de 100 linhas vs. CI/CD pipeline complexo)
- **Perdemos:** Sofisticação (sem build incremental, sem caching, sem triggers automáticos)
- **Avaliação:** Trade-off justificado. Simplicidade facilita manutenção e debug.

---

## Implementação

**Data de Implementação:** 2026-02-07

**Commits Relacionados:**
- `a37f1a1` - "✅ Fase 2: Volume 1 v2.0 - Consolidação completa com fichas revisadas"

**Arquivos Criados:**
- `/tmp/build_volume1_v2.sh` (script de build, ~100 linhas)
- `volumes-finalizados/volume-1/CADERNO-TOCANTINS-2026-Vol1-V2.0.md` (artefato final, 579 KB)

**Arquivos Fonte (Input):**
- `volumes-finalizados/volume-1/CADERNO TOCANTINS 2026 - Vol.1 - V1.1.md` (Seção I)
- `parte-i-visao-estadual/docs/PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md`
- `analises/fase-1-1-agregacao-municipal/FICHA-01-PORTO-NACIONAL-REVISADA.md` (+ FICHA-02 a 08)

---

## Referências

### Documentação Interna
- **Handoff:** [HANDOFF-SESSION-0e16a195.md](../handoffs/HANDOFF-SESSION-0e16a195.md) - Seção 9.1: ADR-003
- **Session Log:** [SESSION-LOG-0e16a195.md](../session-logs/SESSION-LOG-0e16a195.md) - Bloco 4: Construção do Volume 1 v2.0
- **Reflexão:** [REFLEXAO-PESQUISA-ACAO-0e16a195.md](../reflexoes/REFLEXAO-PESQUISA-ACAO-0e16a195.md) - Seção 5.1: Aprendizado 2

### Commits
- [a37f1a1](../../commits/a37f1a1) - Commit do Volume 1 v2.0 compilado

### Script de Build
- Original: `/tmp/build_volume1_v2.sh` (pode estar perdido se /tmp foi limpo)
- **TODO:** Mover para `docs/scripts/build_volume1_v2.sh` e versionar no git

---

## Notas Adicionais

### Aprendizado Metodológico

**Insight:** Build scripts transformam iteração.

Da REFLEXAO-PESQUISA-ACAO-0e16a195.md:
> "Script de 100 linhas compila documento de 579 KB em segundos. Permite correções em componentes individuais + rebuild instantâneo. Documentação do processo como código."

### Princípio de Design: Separation of Concerns

Esta decisão reflete princípio de **separação entre fontes e artefatos derivados**:
- **Fontes:** Componentes individuais (fichas, panorama) - editáveis
- **Artefatos Derivados:** Volume 1 v2.0 - gerado automaticamente, não editável

**Benefício:** Correções em componentes propagam automaticamente para artefato final.

### Replicabilidade para Futuro

Este padrão pode ser replicado para:
- **Volume 2 v1.0:** Compilar 139 fichas municipais
- **Volume 3:** Consolidar Volumes 1 + 2 + análises adicionais
- **Versões futuras:** v2.1, v2.2, v3.0 (rebuild com componentes atualizados)

---

## Histórico de Revisões

| Data | Autor | Mudança |
|------|-------|---------|
| 2026-02-14 | Henrique Marques Ribeiro | Criação inicial (formalização de decisão tomada em 2026-02-07) |

---

**Última atualização:** 2026-02-14
**Próxima revisão:** Após Volume 2 (avaliar se script approach escalou bem para 139 municípios)

**TODO Crítico:** Mover `/tmp/build_volume1_v2.sh` para `docs/scripts/` antes que /tmp seja limpo.
