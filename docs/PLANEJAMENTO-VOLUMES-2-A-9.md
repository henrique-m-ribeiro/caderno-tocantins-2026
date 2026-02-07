# PLANEJAMENTO — REFATORAÇÃO DO VOLUME 2 EM 8 VOLUMES (2 a 9)

**Data**: 07 de fevereiro de 2026
**Status**: Proposta para revisão
**Sessão**: claude/review-handoff-docs-lZ6Qi

---

## 1. CONTEXTO E MOTIVAÇÃO

O Volume 2 consolidado (CADERNO-TOCANTINS-2026-Vol2-V1.0.md) ficou com **35.880 linhas / ~1.000 páginas / 2,2 MB**, o que:
- Excede o limite de upload do Google Docs
- Torna a navegação e consulta impraticáveis
- Dificulta o uso em campo (reuniões com prefeitos, eventos regionais)

**Solução**: Dividir em **8 volumes regionais** (Vol. 2 a 9), um por microrregião, cada qual com ~90-175 páginas — tamanho compatível com Google Docs, impressão e consulta rápida.

---

## 2. ESTRUTURA DOS 8 NOVOS VOLUMES

### 2.1 Mapeamento Volume ↔ Microrregião

| Volume | Microrregião | Municípios | Páginas est. |
|--------|-------------|------------|-------------|
| **Vol. 2** | Porto Nacional | 11 | ~90 |
| **Vol. 3** | Araguaína | 17 | ~130 |
| **Vol. 4** | Bico do Papagaio | 25 | ~175 |
| **Vol. 5** | Miracema do Tocantins | 24 | ~170 |
| **Vol. 6** | Gurupi | 14 | ~110 |
| **Vol. 7** | Dianópolis | 20 | ~145 |
| **Vol. 8** | Jalapão | 15 | ~115 |
| **Vol. 9** | Rio Formoso | 13 | ~105 |
| | **TOTAL** | **139** | **~1.040** |

### 2.2 Estrutura Interna de Cada Volume

```
CADERNO TOCANTINS 2026 — Volume X: Microrregião de [NOME]
├── CAPA
├── FICHA TÉCNICA
├── ÍNDICE
├── APRESENTAÇÃO (contextualização da microrregião)
├── SUMÁRIO EXECUTIVO (padrões e alertas da microrregião)
├── FICHA DA MICRORREGIÃO (revisada — da pasta fase-1-1)
├── FICHAS MUNICIPAIS (em ordem alfabética)
│   ├── Município A — Ficha V2
│   ├── Município B — Ficha V2
│   └── ...
└── FONTES E METODOLOGIA
```

---

## 3. DIAGNÓSTICO: PROBLEMAS A RESOLVER ANTES DA PRODUÇÃO

### 3.1 Os 11 Municípios Ausentes das Fichas Microrregionais

As fichas microrregionais revisadas (fase-1-1) somam apenas **128 municípios** — faltam 11. A tabela abaixo identifica cada um e sua microrregião correta (baseada na contagem canônica do Volume 1):

| Município ausente | Microrregião correta | Label no V2 | Observação |
|---|---|---|---|
| Colinas do Tocantins | **Araguaína** | Porto Nacional | Label V2 incorreto |
| Pau d'Arco | **Araguaína** | Araguaína | Label V2 correto |
| Maurilândia do Tocantins | **Bico do Papagaio** | Bico do Papagaio | Label V2 correto |
| Divinópolis do Tocantins | **Miracema** | Miracema do Tocantins | Label V2 correto |
| Dois Irmãos do Tocantins | **Miracema** | Porto Nacional | Label V2 incorreto |
| Itaporã do Tocantins | **Miracema** | Porto Nacional | Label V2 incorreto |
| Marianópolis do Tocantins | **Miracema** | Porto Nacional | Label V2 incorreto |
| Monte Santo do Tocantins | **Miracema** | [Não especificada] | Label V2 ausente |
| Crixás do Tocantins | **Gurupi** | Gurupi | Label V2 correto |
| Conceição do Tocantins | **Dianópolis** | Dianópolis | Label V2 correto |
| Pindorama do Tocantins | **Dianópolis** | Dianópolis | Label V2 correto |

**Verificação da contagem (Vol. 1 canônico vs. fichas fase-1-1):**

| Microrregião | Vol. 1 (canônico) | Ficha fase-1-1 | Faltam | Municípios faltantes |
|---|---|---|---|---|
| Porto Nacional | 11 | 11 | 0 | — |
| Araguaína | 17 | 15 | **2** | Colinas do Tocantins, Pau d'Arco |
| Bico do Papagaio | 25 | 24 | **1** | Maurilândia do Tocantins |
| Miracema | 24 | 19 | **5** | Divinópolis, Dois Irmãos, Itaporã, Marianópolis, Monte Santo |
| Gurupi | 14 | 13 | **1** | Crixás do Tocantins |
| Dianópolis | 20 | 18 | **2** | Conceição, Pindorama |
| Jalapão | 15 | 15 | 0 | — |
| Rio Formoso | 13 | 13 | 0 | — |
| **Total** | **139** | **128** | **11** | |

### 3.2 Inconsistências nos Labels de Microrregião das Fichas V2

Além dos 11 municípios ausentes, a primeira análise revelou que **~20 fichas V2** possuem labels de microrregião não padronizados ou incorretos (ex: "Central", "Araguacema", "Sudoeste do Tocantins", "---"). Estas fichas precisam ter o cabeçalho corrigido para o nome canônico da microrregião antes da montagem dos volumes.

**Fichas V2 com labels problemáticos (amostra):**

| Município | Label atual na V2 | Label correto |
|---|---|---|
| Colinas do Tocantins | Porto Nacional | Araguaína |
| Dois Irmãos do Tocantins | Porto Nacional | Miracema |
| Itaporã do Tocantins | Porto Nacional | Miracema |
| Marianópolis do Tocantins | Porto Nacional | Miracema |
| Monte Santo do Tocantins | [Não especificada] | Miracema |
| Aparecida do Rio Negro | Central | Porto Nacional |
| Goianorte | Araguacema | Miracema |
| Pium | Araguaia | Rio Formoso |
| Pedro Afonso | Central do Tocantins | Porto Nacional |
| Jaú do Tocantins | Sudoeste do Tocantins | Gurupi |
| Talismã | Sul do Tocantins | Gurupi |
| Taguatinga | Região Sudeste | Dianópolis |
| São Sebastião do Tocantins | Extremo Norte | Bico do Papagaio |
| Lagoa da Confusão | Formoso do Araguaia | Rio Formoso |
| Ponte Alta do Tocantins | Região do Jalapão | Jalapão |
| Itacajá | Vale do Tocantins | Jalapão |
| Brasilândia do Tocantins | Colinas do Tocantins | Miracema |
| Cachoeirinha | --- | Bico do Papagaio |
| Novo Alegre | --- | Dianópolis |
| Recursolândia | --- | Jalapão |
| Tupiratins | --- | Miracema |

### 3.3 Revisão das Fichas Microrregionais

As fichas microrregionais (fase-1-1) foram produzidas **antes** das fichas municipais V2 e sem os dados dos 11 municípios ausentes. Portanto, precisam de revisão para:

1. **Incluir os municípios faltantes** — Dados, análises e referências aos 11 municípios
2. **Atualizar contagens** — Número de municípios, totais populacionais, somas de PIB, médias de IDEB
3. **Garantir coerência com as fichas V2** — Dados citados na ficha microrregional devem coincidir com os das fichas municipais
4. **Padronizar estrutura** — A ficha 02 (Araguaína) tem estrutura diferente das demais (sem seção DADOS GERAIS)

---

## 4. MAPEAMENTO CANÔNICO COMPLETO: 139 MUNICÍPIOS → 8 MICRORREGIÕES

### Vol. 2 — Porto Nacional (11 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Aparecida do Rio Negro | Presente |
| 2 | Bom Jesus do Tocantins | Presente |
| 3 | Ipueiras | Presente |
| 4 | Lajeado | Presente |
| 5 | Monte do Carmo | Presente |
| 6 | Palmas | Presente |
| 7 | Pedro Afonso | Presente |
| 8 | Porto Nacional | Presente |
| 9 | Santa Maria do Tocantins | Presente |
| 10 | Silvanópolis | Presente |
| 11 | Tocantínia | Presente |

### Vol. 3 — Araguaína (17 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Aragominas | Presente |
| 2 | Araguaína | Presente |
| 3 | Araguanã | Presente |
| 4 | Arapoema | Presente |
| 5 | Babaçulândia | Presente |
| 6 | Bandeirantes do Tocantins | Presente |
| 7 | Carmolândia | Presente |
| 8 | **Colinas do Tocantins** | **AUSENTE — a incluir** |
| 9 | Filadélfia | Presente |
| 10 | Muricilândia | Presente |
| 11 | Nova Olinda | Presente |
| 12 | Palmeirante | Presente |
| 13 | **Pau d'Arco** | **AUSENTE — a incluir** |
| 14 | Piraquê | Presente |
| 15 | Santa Fé do Araguaia | Presente |
| 16 | Wanderlândia | Presente |
| 17 | Xambioá | Presente |

### Vol. 4 — Bico do Papagaio (25 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Aguiarnópolis | Presente |
| 2 | Ananás | Presente |
| 3 | Angico | Presente |
| 4 | Araguatins | Presente |
| 5 | Augustinópolis | Presente |
| 6 | Axixá do Tocantins | Presente |
| 7 | Buriti do Tocantins | Presente |
| 8 | Cachoeirinha | Presente |
| 9 | Carrasco Bonito | Presente |
| 10 | Darcinópolis | Presente |
| 11 | Esperantina | Presente |
| 12 | Itaguatins | Presente |
| 13 | Luzinópolis | Presente |
| 14 | **Maurilândia do Tocantins** | **AUSENTE — a incluir** |
| 15 | Nazaré | Presente |
| 16 | Palmeiras do Tocantins | Presente |
| 17 | Praia Norte | Presente |
| 18 | Riachinho | Presente |
| 19 | Sampaio | Presente |
| 20 | Santa Terezinha do Tocantins | Presente |
| 21 | São Bento do Tocantins | Presente |
| 22 | São Miguel do Tocantins | Presente |
| 23 | São Sebastião do Tocantins | Presente |
| 24 | Sítio Novo do Tocantins | Presente |
| 25 | Tocantinópolis | Presente |

### Vol. 5 — Miracema do Tocantins (24 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Abreulândia | Presente |
| 2 | Araguacema | Presente |
| 3 | Barrolândia | Presente |
| 4 | Bernardo Sayão | Presente |
| 5 | Brasilândia do Tocantins | Presente |
| 6 | Caseara | Presente |
| 7 | Colméia | Presente |
| 8 | Couto Magalhães | Presente |
| 9 | **Divinópolis do Tocantins** | **AUSENTE — a incluir** |
| 10 | **Dois Irmãos do Tocantins** | **AUSENTE — a incluir** |
| 11 | Goianorte | Presente |
| 12 | Guaraí | Presente |
| 13 | **Itaporã do Tocantins** | **AUSENTE — a incluir** |
| 14 | Juarina | Presente |
| 15 | **Marianópolis do Tocantins** | **AUSENTE — a incluir** |
| 16 | Miracema do Tocantins | Presente |
| 17 | Miranorte | Presente |
| 18 | **Monte Santo do Tocantins** | **AUSENTE — a incluir** |
| 19 | Pequizeiro | Presente |
| 20 | Presidente Kennedy | Presente |
| 21 | Rio dos Bois | Presente |
| 22 | Tabocão | Presente |
| 23 | Tupirama | Presente |
| 24 | Tupiratins | Presente |

### Vol. 6 — Gurupi (14 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Aliança do Tocantins | Presente |
| 2 | Alvorada | Presente |
| 3 | Brejinho de Nazaré | Presente |
| 4 | Cariri do Tocantins | Presente |
| 5 | **Crixás do Tocantins** | **AUSENTE — a incluir** |
| 6 | Figueirópolis | Presente |
| 7 | Gurupi | Presente |
| 8 | Jaú do Tocantins | Presente |
| 9 | Palmeirópolis | Presente |
| 10 | Peixe | Presente |
| 11 | Santa Rita do Tocantins | Presente |
| 12 | São Salvador do Tocantins | Presente |
| 13 | Sucupira | Presente |
| 14 | Talismã | Presente |

### Vol. 7 — Dianópolis (20 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Almas | Presente |
| 2 | Arraias | Presente |
| 3 | Aurora do Tocantins | Presente |
| 4 | Chapada da Natividade | Presente |
| 5 | Combinado | Presente |
| 6 | **Conceição do Tocantins** | **AUSENTE — a incluir** |
| 7 | Dianópolis | Presente |
| 8 | Lavandeira | Presente |
| 9 | Natividade | Presente |
| 10 | Novo Alegre | Presente |
| 11 | Novo Jardim | Presente |
| 12 | Paranã | Presente |
| 13 | **Pindorama do Tocantins** | **AUSENTE — a incluir** |
| 14 | Ponte Alta do Bom Jesus | Presente |
| 15 | Porto Alegre do Tocantins | Presente |
| 16 | Rio da Conceição | Presente |
| 17 | Santa Rosa do Tocantins | Presente |
| 18 | São Valério da Natividade | Presente |
| 19 | Taguatinga | Presente |
| 20 | Taipas do Tocantins | Presente |

### Vol. 8 — Jalapão (15 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Barra do Ouro | Presente |
| 2 | Campos Lindos | Presente |
| 3 | Centenário | Presente |
| 4 | Goiatins | Presente |
| 5 | Itacajá | Presente |
| 6 | Itapiratins | Presente |
| 7 | Lagoa do Tocantins | Presente |
| 8 | Lizarda | Presente |
| 9 | Mateiros | Presente |
| 10 | Novo Acordo | Presente |
| 11 | Ponte Alta do Tocantins | Presente |
| 12 | Recursolândia | Presente |
| 13 | Rio Sono | Presente |
| 14 | Santa Tereza do Tocantins | Presente |
| 15 | São Félix do Tocantins | Presente |

### Vol. 9 — Rio Formoso (13 municípios)

| N.° | Município | Status na ficha microrregional |
|---|---|---|
| 1 | Araguaçu | Presente |
| 2 | Chapada de Areia | Presente |
| 3 | Cristalândia | Presente |
| 4 | Dueré | Presente |
| 5 | Fátima | Presente |
| 6 | Formoso do Araguaia | Presente |
| 7 | Lagoa da Confusão | Presente |
| 8 | Nova Rosalândia | Presente |
| 9 | Oliveira de Fátima | Presente |
| 10 | Paraíso do Tocantins | Presente |
| 11 | Pium | Presente |
| 12 | Pugmil | Presente |
| 13 | Sandolândia | Presente |

---

## 5. PLANO DE EXECUÇÃO — 5 FASES

### FASE 1: Correção dos Labels de Microrregião nas Fichas V2

**Objetivo**: Garantir que todas as 139 fichas V2 tenham o nome correto da microrregião no cabeçalho.

**Ações:**
1. Para cada uma das ~20 fichas V2 com labels incorretos ou ausentes:
   - Abrir o arquivo
   - Corrigir a linha `**Microrregião**: [nome]` para o nome canônico
2. Commit das correções

**Critério de aceite:** `grep "Microrregião" fichas-v2/*.md | sort` retorna apenas os 8 nomes canônicos.

**Estimativa:** ~30 minutos (edição automatizada)

---

### FASE 2: Revisão das 6 Fichas Microrregionais Afetadas

**Objetivo**: Atualizar as fichas microrregionais que têm municípios ausentes para incluí-los e garantir coerência com as fichas V2.

**Microrregiões a revisar (6 de 8):**

| Ficha | Municípios a incluir | Impacto estimado |
|---|---|---|
| FICHA-02-ARAGUAINA | Colinas do Tocantins, Pau d'Arco | Alto — Colinas é o 2° maior município da microrregião |
| FICHA-03-BICO-DO-PAPAGAIO | Maurilândia do Tocantins | Baixo — município pequeno |
| FICHA-04-DIANOPOLIS | Conceição do Tocantins, Pindorama | Médio — 2 municípios rurais |
| FICHA-05-GURUPI | Crixás do Tocantins | Baixo — município pequeno |
| FICHA-07-MIRACEMA | Divinópolis, Dois Irmãos, Itaporã, Marianópolis, Monte Santo | **Muito alto — 5 municípios, ~21% da microrregião** |
| FICHA-02-ARAGUAINA | Padronizar seção DADOS GERAIS (ausente) | Estrutural |

**Para cada ficha microrregional, a revisão deve:**

1. **Atualizar DADOS GERAIS**: número de municípios, lista de municípios, área total, população total
2. **Incorporar dados dos municípios ausentes** nas análises dimensionais:
   - PIB agregado, estrutura econômica
   - Indicadores de educação (IDEB médio)
   - Indicadores de saúde (cobertura, mortalidade)
   - Saneamento (% esgoto, % água)
   - Agropecuária (rebanho total, produção)
3. **Revisar conclusões e recomendações** se os novos dados alterarem o diagnóstico
4. **Verificar coerência** com dados apresentados nas fichas V2 dos respectivos municípios

**Metodologia de revisão:**
- Cada agente de revisão receberá:
  - A ficha microrregional atual (fase-1-1)
  - As fichas V2 de TODOS os municípios da microrregião (incluindo os ausentes)
  - Instruções para integrar os dados faltantes sem alterar a estrutura geral

**Fichas que NÃO precisam de revisão de conteúdo (apenas verificação):**
- Porto Nacional (11/11 presentes)
- Jalapão (15/15 presentes)
- Rio Formoso (13/13 presentes)

**Estimativa:** ~3-4 horas (6 revisões paralelas via agentes)

---

### FASE 3: Produção dos 8 Volumes

**Objetivo**: Gerar os 8 documentos consolidados, cada um com a estrutura completa.

**Para cada volume (Vol. 2 a 9):**

1. **Gerar front matter** (capa, ficha técnica, índice, apresentação, sumário executivo)
   - Capa: adaptada do modelo do Vol. 1, com nome da microrregião
   - Ficha técnica: escopo territorial da microrregião (área, população, n° municípios)
   - Índice: lista alfabética dos municípios + seções da ficha microrregional
   - Apresentação: contexto da microrregião, relação com Vol. 1
   - Sumário executivo: padrões transversais, alertas, oportunidades **específicos da microrregião**

2. **Incluir ficha microrregional revisada** (da Fase 2)

3. **Incluir fichas V2 municipais** em ordem alfabética (da pasta fichas-v2, com labels corrigidos)

4. **Concatenar** tudo em um único arquivo markdown por volume

**Nomenclatura dos arquivos:**
```
CADERNO-TOCANTINS-2026-Vol2-PORTO-NACIONAL.md
CADERNO-TOCANTINS-2026-Vol3-ARAGUAINA.md
CADERNO-TOCANTINS-2026-Vol4-BICO-DO-PAPAGAIO.md
CADERNO-TOCANTINS-2026-Vol5-MIRACEMA.md
CADERNO-TOCANTINS-2026-Vol6-GURUPI.md
CADERNO-TOCANTINS-2026-Vol7-DIANOPOLIS.md
CADERNO-TOCANTINS-2026-Vol8-JALAPAO.md
CADERNO-TOCANTINS-2026-Vol9-RIO-FORMOSO.md
```

**Estimativa:** ~2-3 horas (8 montagens paralelas via agentes)

---

### FASE 4: Validação de Qualidade

**Objetivo**: Garantir coerência e integridade de todos os 8 volumes.

**Verificações automatizadas:**

| Verificação | Comando | Critério |
|---|---|---|
| Contagem de fichas por volume | `grep -c "Ficha Municipal" VolX.md` | Deve coincidir com n° de municípios |
| Perfil do Eleitorado presente | `grep -c "Perfil do Eleitorado" VolX.md` | = n° municípios |
| Paradoxo central presente | `grep -c "Paradoxo central" VolX.md` | = n° municípios |
| 4 Prioridades por ficha | `grep -c "Prioridade 4" VolX.md` | = n° municípios |
| Labels de microrregião coerentes | `grep "Microrregião" VolX.md` | Apenas o nome da microrregião do volume |
| Sem labels incorretos | grep para labels antigos | 0 ocorrências |
| Tamanho do arquivo | `wc -l`, `du -h` | < 500 KB por volume |

**Verificações manuais (por amostragem):**
- Ler 1 ficha por volume para verificar qualidade do conteúdo
- Verificar se o sumário executivo do volume reflete os dados das fichas municipais
- Confirmar que a ficha microrregional menciona todos os municípios

**Estimativa:** ~1 hora

---

### FASE 5: Commit, Push e Organização do Repositório

**Objetivo**: Publicar os 8 volumes e organizar o repositório.

**Ações:**
1. Criar diretório `volumes-finalizados/` (se não existir) com subdiretórios por volume
2. Mover/copiar cada volume para o diretório adequado
3. Commit com mensagem descritiva
4. Push para `origin/claude/review-handoff-docs-lZ6Qi`
5. Atualizar README se necessário

**Estrutura proposta do repositório:**
```
volumes-finalizados/
├── volume-1/
│   └── CADERNO-TOCANTINS-2026-Vol1-V2.0.md
├── volume-2-porto-nacional/
│   └── CADERNO-TOCANTINS-2026-Vol2-PORTO-NACIONAL.md
├── volume-3-araguaina/
│   └── CADERNO-TOCANTINS-2026-Vol3-ARAGUAINA.md
├── volume-4-bico-do-papagaio/
│   └── CADERNO-TOCANTINS-2026-Vol4-BICO-DO-PAPAGAIO.md
├── volume-5-miracema/
│   └── CADERNO-TOCANTINS-2026-Vol5-MIRACEMA.md
├── volume-6-gurupi/
│   └── CADERNO-TOCANTINS-2026-Vol6-GURUPI.md
├── volume-7-dianopolis/
│   └── CADERNO-TOCANTINS-2026-Vol7-DIANOPOLIS.md
├── volume-8-jalapao/
│   └── CADERNO-TOCANTINS-2026-Vol8-JALAPAO.md
└── volume-9-rio-formoso/
    └── CADERNO-TOCANTINS-2026-Vol9-RIO-FORMOSO.md
```

**Estimativa:** ~30 minutos

---

## 6. RISCOS E MITIGAÇÕES

| Risco | Impacto | Mitigação |
|---|---|---|
| Dados inconsistentes entre ficha microrregional e fichas V2 | Alto — documento parece incoerente | Revisão automatizada cruzando dados-chave (PIB, população, IDEB) |
| Agentes gerarem revisões de baixa qualidade | Médio — retrabalho | Fornecer instruções detalhadas + ficha V2 completa como referência |
| Labels de microrregião ainda incorretos após correção | Baixo — afeta índice | Validação automatizada via grep |
| Volume muito grande para Google Docs | Baixo — max ~175 pp | Todos os volumes ficam < 500 KB |
| Ficha de Miracema com 5 municípios novos altera diagnóstico | Alto — análise pode mudar | Revisão dedicada com mais contexto para esta microrregião |

---

## 7. DECISÕES PENDENTES

1. **Ordem dos volumes**: A proposta usa Porto Nacional como Vol. 2 (seguindo a numeração do Vol. 1, onde Porto Nacional é Ficha 01). Confirmar se prefere outra ordem.

2. **Destino do Volume 2 consolidado**: O arquivo `CADERNO-TOCANTINS-2026-Vol2-V1.0.md` (versão anterior com todas as 139 fichas) deve ser mantido como backup, movido para arquivo morto, ou deletado?

3. **Profundidade da revisão microrregional**: Revisão leve (incluir os municípios ausentes nas listas e atualizar contagens) ou revisão profunda (reescrever análises dimensionais, recalcular médias, atualizar conclusões)?

4. **Sumário executivo por volume**: Genérico (mesmo texto adaptado) ou específico (análise única dos padrões de cada microrregião baseada nas fichas V2)?

---

## 8. CRONOGRAMA ESTIMADO

| Fase | Ação | Tempo est. | Dependência |
|---|---|---|---|
| **1** | Correção de labels nas fichas V2 | 30 min | — |
| **2** | Revisão das 6 fichas microrregionais | 3-4 h | Fase 1 |
| **3** | Produção dos 8 volumes | 2-3 h | Fases 1 e 2 |
| **4** | Validação de qualidade | 1 h | Fase 3 |
| **5** | Commit, push, organização | 30 min | Fase 4 |
| | **TOTAL** | **~7-9 h** | |

**Nota**: As fases 2 e 3 podem ser parcialmente paralelizadas — volumes de microrregiões sem alteração (Porto Nacional, Jalapão, Rio Formoso) podem ser montados enquanto as revisões das outras 5 fichas microrregionais estão em andamento.

---

*Documento elaborado seguindo a metodologia IA-Collab-OS v1.0*
*Caderno Tocantins 2026 — Planejamento Volumes 2-9*
