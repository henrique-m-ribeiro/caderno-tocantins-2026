# ADR-001: Template-Based Approach para Fichas Regionais

**Status:** ✅ Aceita
**Data:** 2026-02-07
**Responsável:** Henrique Marques Ribeiro
**Session:** 0e16a195-e9a6-4564-b12e-016b43def69a
**Fase:** Fase 1.1 - Revisão de Fichas Regionais

---

## Contexto

Durante a Fase 1.1 do projeto, precisávamos criar/revisar fichas regionais para as 8 microrregiões do Tocantins. Após completar as fichas 01-04, ficou evidente que cada ficha seguia estrutura similar (12 seções padronizadas), mas com conteúdo específico de cada microrregião.

**Problema:** Como equilibrar eficiência produtiva e qualidade analítica?

**Restrições:**
- Tempo limitado para completar 8 fichas regionais
- Necessidade de consistência estrutural para comparabilidade
- Exigência de customização profunda para capturar singularidades territoriais
- Sessões de trabalho com limite de contexto (session compaction)

A FICHA-04-DIANOPOLIS havia sido revisada com estrutura robusta e bem organizada, incluindo:
- 12 seções padronizadas
- SWOT completa e contextualizada (seção 9.3)
- Considerações Finais reflexivas (seção 12)
- Referências rastreáveis (seção 13)

---

## Decisão

**Decidimos usar FICHA-04-DIANOPOLIS-REVISADA.md como template base para as fichas 05-08.**

**Processo:**
1. Copiar FICHA-04 como ponto de partida
2. Substituir sistematicamente dados gerais (nome, municípios, população, área)
3. **Customizar profundamente** seções críticas:
   - Seção 1.1: Características Gerais (narrativa da microrregião)
   - Seção 9.3: Análise SWOT (forças, fraquezas, oportunidades, ameaças específicas)
   - Seção 12: Considerações Finais (síntese reflexiva e mensagem-chave)
4. Atualizar demais seções (2-8, 10-11) com dados da tabela comparativa correspondente

**Critério de qualidade:** Seções críticas (1.1, 9.3, 12) devem ter mínimo 30-40% de reescrita para evitar homogeneização.

---

## Alternativas Consideradas

### Alternativa 1: Criar Cada Ficha do Zero

- **Descrição:** Escrever cada ficha regionalmente sem usar template, começando de documento em branco
- **Prós:**
  - Máxima singularidade (cada ficha única)
  - Zero risco de homogeneização
  - Permite experimentação estrutural
- **Contras:**
  - Muito tempo (estimativa: 3-4h por ficha × 4 fichas = 12-16h)
  - Inconsistência estrutural dificulta comparação
  - Fadiga cognitiva em decisões estruturais repetitivas
- **Por que foi rejeitada:** Inviável no tempo disponível, e inconsistência estrutural prejudicaria comparabilidade entre microrregiões.

### Alternativa 2: Usar Template Genérico (Esqueleto Vazio)

- **Descrição:** Criar template com apenas headers de seções, sem conteúdo de referência
- **Prós:**
  - Padronização estrutural
  - Zero risco de copiar conteúdo inadequado
- **Contras:**
  - Não acelera significativamente o trabalho (ainda precisa escrever tudo)
  - Não fornece referência de qualidade esperada
  - Perde oportunidade de reusar parágrafos genéricos (ex: "Metodologia")
- **Por que foi rejeitada:** Não oferece ganho significativo de eficiência vs. alternativa 1.

### Alternativa 3: Geração Automatizada por IA + Revisão Humana

- **Descrição:** Usar IA (Claude, GPT-4) para gerar fichas completas automaticamente a partir de dados, seguida de revisão humana
- **Prós:**
  - Extremamente rápido (minutos por ficha)
  - Escalável para Volume 2 (139 municípios)
- **Contras:**
  - Qualidade analítica pode ser superficial
  - Perde oportunidade de reflexão profunda durante escrita
  - Requer validação cuidadosa (pode gerar hallucinations)
- **Por que foi rejeitada:** Nesta fase, queríamos priorizar qualidade sobre velocidade. Reservada para Volume 2 (139 fichas municipais).

---

## Consequências

### Positivas

- ✅ **Eficiência produtiva:** FICHA 08 (13 municípios) criada em ~1.5h (vs. 3-4h do zero)
- ✅ **Padronização estrutural:** Todas as 8 fichas têm mesma estrutura (12 seções), facilitando comparação
- ✅ **Consistência de qualidade:** Template estabelece "barra mínima" de profundidade analítica
- ✅ **Reutilização de parágrafos genéricos:** Metodologia, fontes, disclaimers copiados sem modificação
- ✅ **Redução de fadiga cognitiva:** Decisões estruturais já tomadas, energia focada em análise de conteúdo

### Negativas

- ⚠️ **Risco de homogeneização:** Se customização for insuficiente, fichas podem parecer "copy-paste"
- ⚠️ **Viés da ficha-template:** FICHA-04 (Dianópolis) pode influenciar narrativa de outras microrregiões
- ⚠️ **Necessidade de vigilância:** Revisor deve garantir que seções críticas foram customizadas

### Mitigações

- **Homogeneização:** Estabelecemos critério de mínimo 30-40% de reescrita nas seções críticas (1.1, 9.3, 12)
- **Viés da template:** Leitura cuidadosa da tabela comparativa ANTES de editar, para capturar singularidades
- **Vigilância:** Inspeção final por seção crítica (SWOT e Considerações Finais devem ser únicas)

---

## Trade-offs Identificados

**Trade-off 1: Eficiência vs. Singularidade**
- **Ganhamos:** Velocidade de produção (1.5h vs. 3-4h por ficha)
- **Perdemos:** Parte da singularidade narrativa (estrutura padronizada)
- **Avaliação:** Trade-off justificado. Singularidade preservada nas seções críticas.

**Trade-off 2: Consistência vs. Flexibilidade**
- **Ganhamos:** Comparabilidade entre microrregiões (mesma estrutura)
- **Perdemos:** Flexibilidade para experimentar estruturas alternativas
- **Avaliação:** Trade-off justificado. Comparabilidade é essencial para panorama consolidado.

---

## Implementação

**Data de Implementação:** 2026-02-07

**Commits Relacionados:**
- `55127ec` - "✅ Fase 1.1.g: Criar FICHA 08 (Rio Formoso) com 13 municípios completos"

**Arquivos Afetados:**
- `analises/fase-1-1-agregacao-municipal/FICHA-05-GURUPI-REVISADA.md` (template-based)
- `analises/fase-1-1-agregacao-municipal/FICHA-06-JALAPAO-REVISADA.md` (template-based)
- `analises/fase-1-1-agregacao-municipal/FICHA-07-MIRACEMA-REVISADA.md` (template-based)
- `analises/fase-1-1-agregacao-municipal/FICHA-08-RIO-FORMOSO-REVISADA.md` (template-based)

**Template Base:**
- `analises/fase-1-1-agregacao-municipal/FICHA-04-DIANOPOLIS-REVISADA.md`

---

## Referências

### Documentação Interna
- **Handoff:** [HANDOFF-SESSION-0e16a195.md](../handoffs/HANDOFF-SESSION-0e16a195.md) - Seção 9.1: Decisões Arquiteturais Principais
- **Session Log:** [SESSION-LOG-0e16a195.md](../session-logs/SESSION-LOG-0e16a195.md) - Bloco 2: Criação da FICHA 08
- **Reflexão:** [REFLEXAO-PESQUISA-ACAO-0e16a195.md](../reflexoes/REFLEXAO-PESQUISA-ACAO-0e16a195.md) - Seção 4.1: Tensões e Contradições (Tensão 1)

### Commits
- [55127ec](../../commits/55127ec) - Criação da FICHA 08 usando template approach

---

## Notas Adicionais

### Aprendizado Metodológico

**Insight:** Template approach funciona se seções críticas forem customizadas.

Da REFLEXAO-PESQUISA-ACAO-0e16a195.md:
> "Template approach equilibra eficiência e qualidade: estrutura padronizada libera energia cognitiva para análise de conteúdo. Eficiência é legítima se seções reflexivas (SWOT, Considerações Finais) mantêm profundidade."

### Replicabilidade para Volume 2

Esta decisão estabelece precedente para Volume 2 (139 fichas municipais):
- Fichas municipais podem usar template-based approach com geração automatizada + curadoria seletiva
- 20-30 municípios prioritários recebem customização profunda
- Restante usa geração automatizada com validação amostral

---

## Histórico de Revisões

| Data | Autor | Mudança |
|------|-------|---------|
| 2026-02-14 | Henrique Marques Ribeiro | Criação inicial (formalização de decisão tomada em 2026-02-07) |

---

**Última atualização:** 2026-02-14
**Próxima revisão:** Após Volume 2 (avaliar se abordagem funcionou para 139 municípios)
