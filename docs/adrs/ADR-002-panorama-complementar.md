# ADR-002: Panorama Complementar vs. Edição Direta

**Status:** ✅ Aceita
**Data:** 2026-02-07
**Responsável:** Henrique Marques Ribeiro
**Session:** 0e16a195-e9a6-4564-b12e-016b43def69a
**Fase:** Fase 1.2 - Revisar Panorama Estadual com Dados Consolidados

---

## Contexto

Após completar a revisão das 8 fichas regionais (Fase 1.1), precisávamos criar um **panorama consolidado** que sintetizasse dados das microrregiões. Este panorama serviria como ponte entre:
- **Parte I (Visão Estadual):** Análise top-down com dados agregados do estado
- **Parte II (Fichas Regionais):** Análise bottom-up com dados detalhados de 128 municípios

**Situação encontrada:**
- `parte-i-visao-estadual/docs/PARTE-I-COMPLETA.md` já existia (versão 1.0, Janeiro 2026)
- PARTE-I era documento robusto (1.395 linhas, 9 dimensões de análise)
- PARTE-I **não incluía** síntese das microrregiões (foi escrita antes da consolidação das fichas)

**Problema:** Como integrar panorama microrregional à PARTE-I sem comprometer documento existente?

**Restrições:**
- PARTE-I v1.0 já validada e em uso
- Risco de quebrar referências/links se modificar estrutura
- Necessidade de rastreabilidade de versões (v1.0 estadual, v2.0 microrregional)

---

## Decisão

**Decidimos criar documento complementar separado: `PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md`**

**Características:**
- Documento independente na mesma pasta (`parte-i-visao-estadual/docs/`)
- 455 linhas com síntese das 8 microrregiões
- Seções incluídas:
  1. Síntese demográfica (tabela comparativa)
  2. Perfis econômicos por microrregião
  3. Rankings de municípios (PIB per capita, IDHM)
  4. Consolidação agrícola
  5. Três realidades econômico-sociais identificadas
  6. Oportunidades estratégicas por microrregião
  7. Recomendações transversais
  8. Metodologia e fontes

**Referenciação:** Volume 1 v2.0 referencia AMBOS os documentos sequencialmente.

---

## Alternativas Consideradas

### Alternativa 1: Editar PARTE-I-COMPLETA.md Diretamente

- **Descrição:** Inserir nova seção "Panorama Microrregional" dentro do arquivo PARTE-I-COMPLETA.md (após seção 9)
- **Prós:**
  - Documento único e consolidado
  - Não requer referenciação cruzada
  - Usuários encontram tudo em um lugar
- **Contras:**
  - Modifica documento v1.0 já validado
  - Perde rastreabilidade de versões (qual conteúdo é v1.0, qual é v2.0?)
  - Risco de quebrar referências existentes
  - Dificulta uso modular (panorama pode ser útil independentemente)
- **Por que foi rejeitada:** Violaria princípio de **preservação de versão original** e dificultaria rastreabilidade.

### Alternativa 2: Criar Parte I v2.0 Completamente Nova

- **Descrição:** Criar novo arquivo PARTE-I-V2-COMPLETA.md que incorpora PARTE-I v1.0 + panorama microrregional
- **Prós:**
  - Versionamento semântico claro (v1.0, v2.0)
  - Documento único para usuários da v2.0
  - Preserva v1.0 original intacta
- **Contras:**
  - Duplicação massiva de conteúdo (v1.0 tem 1.395 linhas)
  - Manutenção duplicada (correções precisam ser aplicadas em ambos)
  - Uso de espaço excessivo (~100 KB extras)
- **Por que foi rejeitada:** Duplicação desnecessária. Panorama complementar pode ser **referenciado** sem duplicação.

### Alternativa 3: Criar Parte II Separada (Somente Panorama)

- **Descrição:** Criar documento "PARTE-II-PANORAMA-MICRORREGIONAL.md" como documento totalmente novo, não vinculado à PARTE-I
- **Prós:**
  - Separação clara de conteúdos
  - Permite evolução independente
- **Contras:**
  - Usuários podem não entender relação com PARTE-I
  - Nomenclatura confusa ("Parte II" já usada para fichas regionais)
  - Não deixa claro que complementa PARTE-I
- **Por que foi rejeitada:** Nome "COMPLEMENTO" é mais claro que "Parte II".

---

## Consequências

### Positivas

- ✅ **Preservação da versão original:** PARTE-I v1.0 permanece intacta e rastreável
- ✅ **Rastreabilidade de versões:** Claro que v1.0 = estadual, v2.0 = estadual + microrregional
- ✅ **Modularidade:** Panorama pode ser usado independentemente (ex: apresentações focadas em microrregiões)
- ✅ **Manutenção facilitada:** Correções na PARTE-I não afetam panorama e vice-versa
- ✅ **Clareza de versionamento:** Usuários entendem que "COMPLEMENTO" expande "COMPLETA"

### Negativas

- ⚠️ **Dois documentos em vez de um:** Usuários precisam consultar ambos para visão completa
- ⚠️ **Referenciação cruzada necessária:** Volume 1 v2.0 precisa referenciar ambos os arquivos
- ⚠️ **Possível confusão:** Usuários podem não entender qual documento ler primeiro

### Mitigações

- **Dois documentos:** Criar README na pasta `parte-i-visao-estadual/` explicando relação
- **Referenciação:** Volume 1 v2.0 inclui AMBOS sequencialmente (via build script)
- **Confusão:** Nome "COMPLEMENTO" deixa claro que complementa "COMPLETA"

---

## Trade-offs Identificados

**Trade-off 1: Modularidade vs. Unificação**
- **Ganhamos:** Modularidade (panorama pode ser usado separadamente, versões rastreáveis)
- **Perdemos:** Unificação (usuários precisam consultar dois arquivos)
- **Avaliação:** Trade-off justificado. Volume 1 v2.0 unifica tudo, mas mantém componentes rastreáveis.

**Trade-off 2: Rastreabilidade vs. Simplicidade**
- **Ganhamos:** Rastreabilidade (claro que v1.0 ≠ v2.0, origem de cada conteúdo identificável)
- **Perdemos:** Simplicidade (mais arquivos no repositório)
- **Avaliação:** Trade-off justificado. Pesquisa-ação exige rastreabilidade de decisões e versões.

---

## Implementação

**Data de Implementação:** 2026-02-07

**Commits Relacionados:**
- `294eba1` - "✅ Fase 1.2: Criar Panorama Microrregional consolidado (V2.0)"

**Arquivos Criados:**
- `parte-i-visao-estadual/docs/PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md` (455 linhas, ~18 KB)

**Arquivos Preservados:**
- `parte-i-visao-estadual/docs/PARTE-I-COMPLETA.md` (v1.0, inalterado)

**Build Script:**
- `/tmp/build_volume1_v2.sh` referencia AMBOS os arquivos na ordem:
  1. PARTE-I-COMPLETA.md (v1.0)
  2. PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md (v2.0)

---

## Referências

### Documentação Interna
- **Handoff:** [HANDOFF-SESSION-0e16a195.md](../handoffs/HANDOFF-SESSION-0e16a195.md) - Seção 9.1: ADR-002
- **Session Log:** [SESSION-LOG-0e16a195.md](../session-logs/SESSION-LOG-0e16a195.md) - Bloco 3: Panorama Estadual Consolidado
- **Reflexão:** [REFLEXAO-PESQUISA-ACAO-0e16a195.md](../reflexoes/REFLEXAO-PESQUISA-ACAO-0e16a195.md) - Seção 5.1: Aprendizado 6

### Commits
- [294eba1](../../commits/294eba1) - Criação do panorama complementar

### Documentos Relacionados
- [PARTE-I-COMPLETA.md](../../parte-i-visao-estadual/docs/PARTE-I-COMPLETA.md) - v1.0 (preservado)
- [PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md](../../parte-i-visao-estadual/docs/PARTE-I-COMPLEMENTO-PANORAMA-MICRORREGIONAL-V2.md) - v2.0 (criado)

---

## Notas Adicionais

### Aprendizado Metodológico

**Insight:** Panorama complementar é melhor que edição direta.

Da REFLEXAO-PESQUISA-ACAO-0e16a195.md:
> "Preserva versão original (rastreabilidade), permite uso modular (panorama microrregional independente), facilita versionamento semântico (v1.0 estadual, v2.0 microrregional)."

### Princípio de Design

Esta decisão reflete princípio de **versionamento semântico não-destrutivo**:
- Versões anteriores (v1.0) são preservadas como artefatos históricos
- Novas versões (v2.0) são criadas como complementos ou substituições explícitas
- Usuários podem escolher versão apropriada ao seu uso

**Aplicação futura:** Volume 2 v1.0 (fichas municipais) também deve preservar versões anteriores quando houver refatoração.

---

## Histórico de Revisões

| Data | Autor | Mudança |
|------|-------|---------|
| 2026-02-14 | Henrique Marques Ribeiro | Criação inicial (formalização de decisão tomada em 2026-02-07) |

---

**Última atualização:** 2026-02-14
**Próxima revisão:** Após publicação de Volume 1 v2.0 (verificar se usuários entendem relação entre documentos)
