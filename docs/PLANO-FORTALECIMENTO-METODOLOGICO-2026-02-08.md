# Plano de Fortalecimento Metodológico — Caderno Tocantins 2026 / Doutorado

**Data:** 08 de Fevereiro de 2026
**Sessao:** session_01Hj1yX6KsVL4QbAqunMSRQv (continuacao)
**Autor:** Henrique M. Ribeiro, com suporte de Claude Code (Opus 4.6)
**Contexto:** Pos-avaliacao critica da atuacao no processo de pesquisa

---

## Contexto

Apos sessao intensiva de producao (9 volumes, 139 municipios, ~1.150 paginas), avaliacao honesta identificou 6 lacunas que precisam ser enderecadas antes de avancar para novos artefatos (dashboard, sistema multi-agentes). Este plano organiza o trabalho em etapas sequenciais com dependencias claras.

## Lacunas Identificadas

1. **Ferramenta conduzindo pesquisa** — Claude Code como driver em vez de questoes de pesquisa
2. **Ciclos PA nao formalizados** — sem perguntas pre-definidas, hipoteses, criterios por ciclo
3. **Ausencia de vozes territoriais** — producao inteiramente "de gabinete"
4. **IA-Collab-OS sem rigor suficiente** — sem criterios operacionais, metricas padronizadas, validacao externa
5. **Tensao produto pratico vs. tese** — caderno como produto politico vs. dado de pesquisa
6. **Diarios dispersos** — 3 entradas em caderno-tocantins, 0 no doutorado/diarios-sessoes/

---

## Plano em 6 Etapas

### ETAPA 1: Centralizacao e Organizacao da Base Documental (1-2 dias)

**Objetivo:** Reunir todos os artefatos dispersos no repositorio `doutorado`, criando uma base documental unica e navegavel.

**Passos:**

1.1. **Migrar diarios de pesquisa-acao** para `doutorado/02-pesquisa-acao/03-dados/diarios-sessoes/`
   - Copiar as 3 entradas existentes de `caderno-tocantins-2026/docs/DIARIO-*.md`
   - Padronizar nomenclatura: `YYYY-MM-DD-sessao-NNN.md`
   - Criar `README.md` no diretorio com indice e instrucoes

1.2. **Migrar documentos de handoff relevantes** para `doutorado/02-pesquisa-acao/03-dados/`
   - Criar subdiretorio `handoffs/` com os 8 handoffs existentes
   - Criar subdiretorio `relatorios-orquestracao/` com o relatorio de 2026-02-08
   - Manter originais nos repos de origem (sao dados primarios)

1.3. **Criar indice cronologico unificado**
   - Atualizar `doutorado/02-pesquisa-acao/04-repositorios/cronologia-real-repositorios.md`
   - Incluir sessao de 2026-02-08 com metricas (213 agentes, 9 volumes, 139 municipios)
   - Vincular cada entrada aos artefatos correspondentes

1.4. **Criar template de diario de sessao**
   - Arquivo: `doutorado/02-pesquisa-acao/03-dados/diarios-sessoes/TEMPLATE-DIARIO.md`
   - Secoes obrigatorias: Questao de pesquisa enderecada, Hipotese testada, Ciclo PA de referencia, Observacoes, Reflexao, Evidencias, Replanejamento
   - Basear-se no melhor exemplo existente (DIARIO-PESQUISA-ACAO-2026-02-08.md) mas adicionar campos formais

**Criterio de conclusao:** Diretorio `diarios-sessoes/` populado, indice cronologico atualizado, template criado.

---

### ETAPA 2: Formalizacao dos Ciclos de Pesquisa-Acao (2-3 dias)

**Objetivo:** Transformar os 5 ciclos PA definidos no projeto de doutorado em estruturas operacionais com perguntas, hipoteses e criterios de avaliacao explicitos.

**Passos:**

2.1. **Mapear ciclos existentes contra evidencias produzidas**
   - Criar documento: `doutorado/02-pesquisa-acao/01-ciclos/MAPEAMENTO-CICLOS-EVIDENCIAS.md`
   - Para cada ciclo (0-3, ja realizados):
     - Questao de pesquisa enderecada (PS1-PS5, OE1-OE6)
     - O que foi planejado vs. o que foi executado
     - Evidencias produzidas (artefatos, dados, codigo)
     - Reflexoes registradas (ou ausentes)
     - Replanejamento que ocorreu (ou deveria ter ocorrido)

2.2. **Formalizar Ciclo 4 (retomada do sistema + audiencias publicas)**
   - Criar: `doutorado/02-pesquisa-acao/01-ciclos/CICLO-04-PLANO.md`
   - Definir:
     - Pergunta-guia: Como sistemas de inteligencia territorial mediados por IA podem ser validados por atores territoriais?
     - Hipoteses testaveis (ex.: "Fichas V2 serao compreensiveis por tecnicos municipais sem explicacao adicional")
     - Criterios de sucesso/fracasso quantificaveis
     - Metodos de coleta de dados
     - Cronograma com marcos

2.3. **Formalizar Ciclo 5 (analise + defesa)**
   - Criar: `doutorado/02-pesquisa-acao/01-ciclos/CICLO-05-PLANO.md`
   - Mesma estrutura do Ciclo 4
   - Incluir: analise cruzada dos ciclos, triangulacao de dados, preparacao da tese

2.4. **Criar protocolo de registro por sessao**
   - Cada sessao de trabalho com Claude deve:
     - Comecar declarando qual ciclo PA e qual questao de pesquisa esta sendo enderecada
     - Registrar no CLAUDE.md do repo correspondente
     - Produzir diario ao final usando o template da Etapa 1

**Criterio de conclusao:** Ciclos 0-3 mapeados retroativamente, Ciclos 4-5 formalizados com hipoteses e criterios, protocolo de registro definido.

---

### ETAPA 3: Integracao de Vozes Territoriais (planejamento: 1-2 dias; execucao: continua)

**Objetivo:** Planejar a inclusao de perspectivas de atores territoriais reais, transformando o trabalho "de gabinete" em pesquisa-acao participativa.

**Passos:**

3.1. **Definir estrategia de validacao territorial**
   - Criar: `doutorado/02-pesquisa-acao/02-campo/ESTRATEGIA-VALIDACAO-TERRITORIAL.md`
   - Identificar 3 niveis de validacao:
     a. **Tecnica:** Especialistas em politicas publicas/gestao municipal revisam fichas
     b. **Politica:** Equipe do senador/pre-candidato avalia utilidade pratica
     c. **Territorial:** Atores locais (prefeitos, secretarios, liderancas) reagem ao conteudo
   - Para cada nivel, definir: quem, como, quando, que dados coletar

3.2. **Desenhar protocolo de audiencias/consultas**
   - Criar roteiro semi-estruturado para apresentacao dos volumes a atores locais
   - Definir instrumento de coleta (questionario, grupo focal, entrevista)
   - Prever registro sistematico das reacoes e criticas
   - Submeter ao comite de etica se necessario

3.3. **Planejar piloto com 2-3 municipios**
   - Selecionar municipios de diferentes portes e microrregioes
   - Identificar interlocutores locais
   - Preparar versao do volume relevante para apresentacao
   - Definir cronograma do piloto

3.4. **Integrar feedback ao ciclo PA**
   - Definir como os dados das audiencias alimentam o Ciclo 4
   - Prever mecanismo de revisao das fichas a partir do feedback
   - Documentar aprendizados metodologicos

**Criterio de conclusao:** Estrategia documentada, protocolo de coleta desenhado, piloto planejado com cronograma.

---

### ETAPA 4: Fortalecimento do IA-Collab-OS (2-3 dias)

**Objetivo:** Elevar o framework de colaboracao humano-IA de "pratica documentada" para "metodologia com criterios operacionais validaveis".

**Passos:**

4.1. **Definir metricas operacionais para cada principio**
   - Para cada um dos 5 principios, criar criterios mensuraveis:
     - "Documentation is Contract" → % de sessoes com handoff completo, % de decisoes registradas em ADR
     - "Limited Scope" → media de tarefas por sessao, % concluidas
     - "Explicit Decisions" → contagem de decisoes implicitas vs. explicitas por sessao
     - "CEO as Orchestrator" → taxonomia de intervencoes do orquestrador
     - "Complete Handoffs" → checklist de completude (secoes presentes, perguntas abertas documentadas)

4.2. **Criar template de retrospectiva de sessao**
   - Adicionar a `ia-collab-os/templates/RETROSPECTIVE.md`
   - Secoes: O que funcionou, O que nao funcionou, Metricas da sessao, Padroes observados, Ajustes para proxima sessao
   - Vincular aos principios do framework

4.3. **Documentar modos de falha conhecidos**
   - Criar `ia-collab-os/docs/FAILURE-MODES.md`
   - Baseado nas licoes aprendidas reais:
     - Agentes monoliticos (contexto estourado)
     - Labels inconsistentes (propagacao silenciosa de erros)
     - Estimativas incorretas de escopo
     - Vies de producao sobre reflexao
   - Para cada modo: descricao, sintomas, mitigacao, exemplo real

4.4. **Conectar IA-Collab-OS a pesquisa-acao**
   - Criar secao em `ia-collab-os/METHODOLOGY.md` sobre integracao com PA
   - Definir como sessoes IA-Collab-OS mapeiam para ciclos PA
   - Explicitar que o framework e simultaneamente ferramenta e objeto de pesquisa

4.5. **Avaliar viabilidade de validacao externa**
   - Identificar 1-2 pesquisadores ou praticantes que possam revisar o framework
   - Preparar versao resumida para revisao por pares
   - Documentar feedback recebido

**Criterio de conclusao:** Metricas definidas para os 5 principios, template de retrospectiva criado, modos de falha documentados, conexao PA-framework explicitada.

---

### ETAPA 5: Resolucao da Tensao Produto-Tese (1-2 dias)

**Objetivo:** Explicitar e documentar a relacao entre o Caderno Tocantins (produto pratico) e a tese (contribuicao academica), evitando que um substitua o outro.

**Passos:**

5.1. **Criar matriz de dupla leitura**
   - Documento: `doutorado/02-pesquisa-acao/00-projeto/MATRIZ-PRODUTO-TESE.md`
   - Para cada artefato produzido, explicitar:
     - Valor como produto pratico (para o senador/candidato)
     - Valor como dado de pesquisa (para a tese)
     - Lacuna que o artefato NAO cobre no ambito academico
   - Exemplos: volumes sao produto excelente, mas nao demonstram sozinhos como IA transforma politica publica

5.2. **Mapear contribuicoes academicas ja realizadas**
   - Listar contribuicoes concretas para cada objetivo especifico (OE1-OE6):
     - OE1 (Desenvolver framework): IA-Collab-OS v1.0 ✓
     - OE2 (Aplicar em contexto real): Caderno Tocantins ✓
     - OE3 (Avaliar impacto): Pendente (precisa de vozes territoriais)
     - OE4 (Documentar processo): Parcial (diarios dispersos, agora centralizando)
     - OE5 (Produzir guia metodologico): Pendente
     - OE6 (Formular recomendacoes): Pendente

5.3. **Definir artefatos academicos faltantes**
   - Para cada OE pendente, listar o que precisa ser produzido
   - Priorizar por dependencia (OE3 depende de campo, OE5 depende de OE3-4)
   - Criar cronograma realista

5.4. **Estabelecer "regra de ouro" para proximas sessoes**
   - Cada sessao de producao de artefatos deve ser acompanhada de registro reflexivo
   - Proporcao sugerida: 70% producao, 30% reflexao/documentacao
   - Registrar em CLAUDE.md como instrucao permanente

**Criterio de conclusao:** Matriz produto-tese criada, OEs mapeados com lacunas, cronograma de artefatos academicos, regra de ouro registrada.

---

### ETAPA 6: Preparacao para Retomada de Producao (1 dia)

**Objetivo:** Criar as condicoes para retomar a producao de novos artefatos (dashboard, sistema multi-agentes) com base metodologica solida.

**Passos:**

6.1. **Atualizar CLAUDE.md de todos os repos**
   - Incluir referencia ao ciclo PA ativo
   - Incluir questao de pesquisa em foco
   - Incluir instrucao sobre registro reflexivo obrigatorio
   - Incluir referencia ao template de diario

6.2. **Criar checklist pre-sessao**
   - Antes de iniciar qualquer sessao de producao:
     - [ ] Qual ciclo PA estou enderecando?
     - [ ] Qual questao de pesquisa (PS1-PS5) esta em foco?
     - [ ] Qual hipotese estou testando?
     - [ ] Quais dados vou coletar?
     - [ ] O handoff anterior foi revisado?

6.3. **Planejar proximos artefatos com dupla leitura**
   - Dashboard: valor pratico (visualizacao para equipe) + valor academico (demonstracao de OE2)
   - Sistema multi-agentes: valor pratico (automacao) + valor academico (dados para OE1, OE4)
   - Para cada um, definir que dados de pesquisa serao coletados durante a producao

6.4. **Merge e limpeza do repositorio caderno-tocantins-2026**
   - Decidir: squash merge vs. merge normal da branch atual
   - Limpar artefatos intermediarios (front-matter-vol*.md)
   - Organizar scripts em diretorio dedicado
   - Remover duplicatas (root vs. volumes-finalizados/)

**Criterio de conclusao:** CLAUDE.md atualizado, checklist criada, proximos artefatos planejados com dupla leitura, repo limpo e mergeado.

---

## Sequencia e Dependencias

```
ETAPA 1 (base documental) ──→ ETAPA 2 (ciclos PA)
         │                            │
         │                            ↓
         │                     ETAPA 3 (vozes territoriais)
         │                            │
         ↓                            │
ETAPA 4 (IA-Collab-OS) ──────→ ETAPA 5 (produto-tese)
                                      │
                                      ↓
                               ETAPA 6 (retomada)
```

- Etapas 1 e 4 podem ser parcialmente paralelas (nao dependem uma da outra)
- Etapa 2 depende de Etapa 1 (precisa dos diarios centralizados)
- Etapa 3 depende de Etapa 2 (precisa dos ciclos formalizados para saber o que validar)
- Etapa 5 depende de Etapas 2 e 4 (precisa dos ciclos e do framework fortalecido)
- Etapa 6 depende de todas as anteriores

## Estimativa Total

- **Trabalho com Claude Code:** ~8-12 sessoes focadas (Etapas 1, 2, 4, 5, 6)
- **Trabalho autonomo do pesquisador:** Continuo (Etapa 3 especialmente)
- **Prazo sugerido:** 3-4 semanas para Etapas 1-5, Etapa 6 marca a transicao

## Principio Orientador

> "Desacelerar para acelerar" — investir agora em organizacao metodologica para que toda producao futura seja simultaneamente artefato pratico e dado de pesquisa, eliminando retrabalho e fortalecendo a tese.
