# PROMPT PARA GERAÇÃO DE FICHA MUNICIPAL CONDENSADA (VOLUME 2)

## CONTEXTO

Você receberá a **Ficha Municipal Completa** de um município do Tocantins em formato Markdown. Este documento foi gerado a partir do Perfil Socioeconômico Municipal da SEPLAN-TO (2024) e contém uma análise socioeconômica detalhada de 15-20 páginas, com dados de 9 dimensões, análise SWOT, diagnóstico integrado e diretrizes estratégicas.

Este documento faz parte do **Caderno Tocantins 2026** — um sistema de inteligência territorial do estado do Tocantins desenvolvido com a metodologia **IA-Collab-OS v1.0** (colaboração humano-IA).

## OBJETIVO

Criar uma **FICHA MUNICIPAL CONDENSADA** de 5-7 páginas (~250-350 linhas), preservando a essência analítica e propositiva da ficha completa, mas com foco estratégico e leitura mais ágil.

A ficha condensada deve:

1. **Preservar TODOS os indicadores-chave** listados na estrutura obrigatória abaixo
2. **Condensar** as análises qualitativas em 2-3 frases por dimensão, mantendo a substância
3. **Manter a SWOT**, reduzindo de 5 para 3 itens por quadrante, com dados de suporte
4. **Preservar o diagnóstico integrado** com paradoxo e cadeia causal
5. **Manter as 4 diretrizes estratégicas**, cada uma com 2 ações-chave e 1 indicador
6. **Condensar os alertas** em tabela de semáforo (2 itens por nível)
7. **Incluir o perfil do eleitorado** em tabela compacta dentro da Dimensão 1 (dado estratégico para inteligência territorial)
8. **Eliminar** seções de baixo valor estratégico (tipos de domicílio, acidentes com animais, comércio exterior zerado, produtos de origem animal por ano, agenda de implementação, recomendações para estudos)
9. **NÃO inventar dados** — usar exclusivamente o que consta na ficha completa

## ESTRUTURA OBRIGATÓRIA DO DOCUMENTO

```markdown
# [NOME DO MUNICÍPIO] — Ficha Municipal

**Código IBGE**: XXXXXXX | **Microrregião**: XXXXXXX | **Área**: X.XXX km² | **Bioma**: Cerrado

---

## Dados Fundamentais

| Indicador | Valor | Contexto |
|-----------|-------|----------|
| População (2022) | X.XXX hab | Variação 2010-2022: +/-X,X% |
| Densidade demográfica | X,X hab/km² | — |
| PIB total (2021) | R$ X.XXX mil | Xª posição no estado |
| PIB per capita (2021) | R$ XX.XXX | TO: R$ 29.619 / BR: R$ 43.460 |
| IDHM (2010) | 0,XXX | Classificação: [Muito Baixo/Baixo/Médio/Alto/Muito Alto] |
| Taxa de urbanização (2022) | XX,X% | — |
| Dependência de transferências | XX,X% | [Cálculo: (FPM + FUNDEB) / Total transferências, ou estimativa sobre receita] |
| Emprego formal (2022-2023) | X.XXX postos | Saldo: +/-XXX |

---

## Resumo Executivo

[UM parágrafo de 100-150 palavras que:
- Abre com o paradoxo central do município entre aspas (ex: "crescimento sem inclusão", "infraestrutura avançando com capital humano regredindo")
- Apresenta 3-4 dados-chave que sustentam o diagnóstico
- Fecha com a principal oportunidade estratégica
- DEVE ser específico para este município — evite frases genéricas aplicáveis a qualquer cidade]

---

## Síntese Estratégica

| Forças | Fraquezas |
|--------|-----------|
| [Item com dado numérico de suporte] | [Item com dado numérico de suporte] |
| [Item com dado numérico de suporte] | [Item com dado numérico de suporte] |
| [Item com dado numérico de suporte] | [Item com dado numérico de suporte] |

| Oportunidades | Ameaças |
|---------------|---------|
| [Item com dado numérico de suporte] | [Item com dado numérico de suporte] |
| [Item com dado numérico de suporte] | [Item com dado numérico de suporte] |
| [Item com dado numérico de suporte] | [Item com dado numérico de suporte] |

---

## Dimensão 1: Perfil Demográfico e Social

| Indicador | Valor | Referência |
|-----------|-------|-----------|
| População (2022) | X.XXX hab | 2010: X.XXX (var. XX%) |
| Pop. urbana / rural | XX% / XX% | X.XXX / X.XXX hab |
| Faixa 0-14 / 15-64 / 65+ | XX% / XX% / XX% | Razão de dependência: XX,X |
| IDHM Geral (2010) | 0,XXX | [classificação] |
| IDHM Longevidade | 0,XXX | — |
| IDHM Educação | 0,XXX | — |
| IDHM Renda | 0,XXX | — |
| Famílias em extrema pobreza (2010) | XX% | XXX famílias |
| Famílias em pobreza (2010) | XX% | XXX famílias |
| Bolsa Família (2023) | XXX famílias | XX% do total, média R$ XXX |

**Perfil do Eleitorado (2024)**:

| Indicador | Valor |
|-----------|-------|
| Total de eleitores | X.XXX |
| Sexo | Homens XX,X% / Mulheres XX,X% |
| Faixa etária predominante | XX-XX anos (XX%) |
| Jovens (16-29 anos) | XX,X% |
| Idosos (60+ anos) | XX,X% |
| Ensino Médio completo ou superior | XX,X% |
| Analfabetos | XX,X% |

**Análise**: [2-3 frases sobre: tendência demográfica (crescimento/declínio), perfil de envelhecimento, situação de pobreza e desigualdade. Incluir 1 frase sobre o perfil do eleitorado e suas implicações para políticas públicas.]

---

## Dimensão 2: Economia e Produção

| Indicador | Valor | Referência |
|-----------|-------|-----------|
| PIB total (2021) | R$ X.XXX mil | var. 2017-2021: +XX% |
| PIB per capita (2021) | R$ XX.XXX | var. 2017-2021: +XX% |
| VAB Agropecuária (2021) | R$ X.XXX mil (XX%) | — |
| VAB Indústria (2021) | R$ X.XXX mil (XX%) | — |
| VAB Serviços (2021) | R$ X.XXX mil (XX%) | — |
| Emprego formal (2022/2023) | X.XXX postos | Saldo: +/-XXX |
| Principal setor empregador (2022) | [nome] | XX% dos empregos formais |
| MEIs (2023) | XXX | var. 2019-2023: +XX% |
| Empresas ativas (2024) | XXX | [principais setores] |

**Análise**: [2-3 frases sobre: estrutura econômica (qual setor domina o VAB vs. qual domina o emprego), dinâmica do mercado de trabalho, diversificação ou concentração.]

---

## Dimensão 3: Educação

| Indicador | Valor | Referência |
|-----------|-------|-----------|
| Alfabetização (2022) | XX,X% | 2010: XX,X% |
| IDEB Anos Iniciais (2023) | X,X | Meta nacional: 6,0 |
| IDEB Anos Finais (2023) | X,X | — |
| IDEB Ensino Médio (2023) | X,X | — |
| Matrículas totais (2023) | X.XXX | [distribuição por nível] |
| Distorção idade-série EM | XX,X% | — |
| Ensino superior | [Sim: X IES / Não] | — |

**Análise**: [2-3 frases sobre: evolução do IDEB, qualidade do fluxo escolar (distorção, reprovação), acesso ao ensino superior. Se IDEB não disponível para algum nível, informar.]

---

## Dimensão 4: Saúde

| Indicador | Valor | Referência |
|-----------|-------|-----------|
| UBS (2023) | XX unidades | — |
| Estabelecimentos hospitalares / Leitos | XX / XX | (ou 0 se ausentes) |
| Profissionais de saúde (2023) | XX | Médicos: XX |
| Mortalidade infantil (mais recente) | XX,X‰ | TO: ~13,4‰ |
| Cobertura vacinal BCG (2022) | XX,X% | Meta OMS: 95% |
| Casos de dengue (2023) | XXX | [tendência: crescente/estável/decrescente] |

**Análise**: [2-3 frases sobre: capacidade da rede de saúde (leitos, profissionais), indicadores vitais (mortalidade, vacinação), vulnerabilidades (doenças de notificação).]

---

## Dimensão 5: Saneamento e Infraestrutura

| Indicador | Valor |
|-----------|-------|
| Água via rede geral (2022) | XX,X% dos domicílios |
| Esgoto via rede geral (2022) | XX,X% dos domicílios |
| Fossa rudimentar (2022) | XX,X% dos domicílios |
| Coleta de lixo (2022) | XX,X% dos domicílios |
| Destino final dos resíduos | [Aterro sanitário / Aterro controlado / Lixão] |
| Cobertura 4G (2024) | ~XX% da população |
| Banda larga fixa (2023) | XXX acessos |
| Agências bancárias | XX (ou 0) |

**Análise**: [2-3 frases sobre: contraste entre cobertura de água e esgoto, situação do manejo de resíduos, nível de conectividade digital e acesso a serviços financeiros.]

---

## Dimensão 6: Agropecuária e Desenvolvimento Rural

| Indicador | Valor | Variação |
|-----------|-------|----------|
| VAB Agropecuária (2021) | R$ X.XXX mil | var. 2017-2021 |
| Rebanho bovino (2023) | XX.XXX cabeças | var. 2019-2023 |
| Principal cultura | [nome] | XXX t (2023) |
| Segunda cultura | [nome] | XXX t (2023) |
| Estabelecimentos agropecuários (2017) | XXX | var. 2006-2017 |
| Crédito rural (2023) | R$ X,XX milhões | var. 2019-2023 |
| Concentração fundiária | [dado mais relevante] | — |

**Análise**: [2-3 frases sobre: vocação produtiva principal (pecuária vs. lavoura), tendências do setor (expansão/retração), potencial de agregação de valor, situação fundiária.]

---

## Dimensão 7: Finanças Públicas

| Transferência | 2019 | 2023 | Variação |
|---------------|------|------|----------|
| FPM | R$ X,XX mi | R$ X,XX mi | +XX% |
| ICMS | R$ X,XX mi | R$ X,XX mi | +XX% |
| FUNDEB | R$ X,XX mi | R$ X,XX mi | +XX% |
| IPVA | R$ XXX mil | R$ XXX mil | +XX% |
| ITR | R$ XX mil | R$ XX mil | +XX% |
| **Total** | **R$ X,XX mi** | **R$ X,XX mi** | **+XX%** |

**Análise**: [2-3 frases sobre: grau de dependência de transferências, principal fonte de receita, evolução da base fiscal, capacidade de investimento próprio.]

---

## Dimensão 8: Meio Ambiente

| Indicador | Valor |
|-----------|-------|
| Focos de queimadas (2023) | XX |
| Tendência de queimadas (2014-2023) | [Crescente / Estável / Decrescente] |
| Manejo de resíduos | [Aterro sanitário / Lixão] |
| Coleta seletiva | [Sim / Não] |
| Matas preservadas (2017) | XX.XXX ha [var. 2006-2017 se disponível] |

**Análise**: [1-2 frases sobre: riscos ambientais (queimadas, poluição), gestão de resíduos, preservação.]

---

## Diagnóstico Integrado

**Paradoxo central**: *"[Frase entre aspas que sintetiza a contradição fundamental do município — deve ser original e específica, não genérica]"*

**Cadeia causal**:
1. [Causa raiz] → [Consequência imediata]
2. [Consequência] → [Próximo efeito]
3. [Efeito] → [Impacto seguinte]
4. [Impacto] → [Consequência final]
5. [Consequência final] → [Retorno à causa raiz, fechando o ciclo]

**Comparação com referências**:

| Indicador | Município | Tocantins | Brasil |
|-----------|-----------|-----------|--------|
| IDHM (2010) | 0,XXX | 0,699 | 0,727 |
| PIB per capita (2021) | R$ XX.XXX | R$ 29.619 | R$ 43.460 |
| Alfabetização (2022) | XX,X% | ~90% | ~93% |
| Esgoto rede geral | XX,X% | ~30% | ~55% |

---

## Diretrizes Estratégicas

**Prioridade 1: [Título curto e objetivo]**
- Objetivo: [frase com meta mensurável]
- Ação 1.1: [ação concreta e viável para o porte do município]
- Ação 1.2: [ação concreta]
- Indicador: [métrica + meta + prazo]

**Prioridade 2: [Título]**
- Objetivo: [meta mensurável]
- Ação 2.1: [ação concreta]
- Ação 2.2: [ação concreta]
- Indicador: [métrica + meta + prazo]

**Prioridade 3: [Título]**
- Objetivo: [meta mensurável]
- Ação 3.1: [ação concreta]
- Ação 3.2: [ação concreta]
- Indicador: [métrica + meta + prazo]

**Prioridade 4: [Título]**
- Objetivo: [meta mensurável]
- Ação 4.1: [ação concreta]
- Ação 4.2: [ação concreta]
- Indicador: [métrica + meta + prazo]

---

## Alertas

| Nível | Alerta | Justificativa |
|-------|--------|---------------|
| VERMELHO | [Situação de urgência 1] | [dado de suporte] |
| VERMELHO | [Situação de urgência 2] | [dado de suporte] |
| AMARELO | [Atenção necessária 1] | [dado de suporte] |
| AMARELO | [Atenção necessária 2] | [dado de suporte] |
| VERDE | [Oportunidade 1] | [dado de suporte] |
| VERDE | [Oportunidade 2] | [dado de suporte] |

---

**Fonte primária**: SEPLAN/TO — Perfil Socioeconômico Municipal [Nome do Município] (2024)
**Dados complementares**: IBGE, INEP/MEC, DATASUS, RAIS/CAGED, ANATEL, INPE, BACEN, CONAB
**Elaboração**: Caderno Tocantins 2026 — Metodologia IA-Collab-OS v1.0
```

---

## INSTRUÇÕES PARA A IA

### 1. SOBRE O DOCUMENTO DE ENTRADA

- **Leia TODA a ficha municipal completa** antes de iniciar a condensação
- **Identifique os indicadores que correspondem** à estrutura obrigatória acima
- **Se um indicador não existir** na ficha completa, use `—` (travessão) na célula da tabela e NÃO invente valores
- **Se a ficha completa tiver formatação inconsistente** (escapes markdown como `\-`, `\*`), corrija na saída

### 2. SOBRE A CONDENSAÇÃO

A condensação NÃO é um resumo mecânico. Siga estas regras:

- **Análises qualitativas**: Condense de parágrafos longos para 2-3 frases que preservem: (a) o dado-chave, (b) a tendência, (c) a implicação estratégica
- **SWOT**: Selecione os 3 itens mais relevantes de cada quadrante. Critério: maior impacto no desenvolvimento do município. Reformule cada item como uma frase curta com dado numérico de suporte
- **Diagnóstico integrado**: Preserve o paradoxo central. Reduza a cadeia causal para 5 elos. Mantenha a tabela comparativa
- **Diretrizes**: Preserve as 4 prioridades. Reduza de 3 para 2 ações por prioridade (as mais impactantes). Mantenha 1 indicador com meta
- **Alertas**: Selecione os 2 mais urgentes de cada nível (vermelho/amarelo/verde). Reformule como linha de tabela compacta

### 3. SEÇÕES A ELIMINAR DA FICHA COMPLETA

NÃO inclua na ficha condensada:
- Histórico do município e localização geográfica detalhada
- Composição por cor/raça
- Detalhes de domicílio (tipo, moradores por domicílio)
- Detalhes de admissões/desligamentos/saldo por ano
- Empregos por escolaridade e faixa etária
- Comércio exterior (zero na grande maioria dos municípios)
- Utilização detalhada das terras
- Produção agrícola com séries históricas completas (manter apenas o mais recente)
- Pecuária detalhada por espécie (manter apenas bovinos e principal produção)
- Produtos de origem animal por ano
- Aquicultura (exceto se relevante)
- Detalhes de equipamentos de saúde
- Indicadores vitais (nascidos vivos, óbitos) — manter apenas mortalidade infantil
- Causas de morte detalhadas
- Doenças de notificação compulsória detalhadas (manter apenas dengue)
- Acidentes com animais peçonhentos
- Cobertura vacinal detalhada (manter apenas BCG como indicador-sentinela)
- Séries históricas de saneamento (1991, 2000, 2010) — manter apenas dado mais recente
- Detalhes de banheiros
- Energia elétrica por classe de consumidor
- Frota de veículos
- Transferências SUS e CIDE (manter apenas FPM, ICMS, FUNDEB, IPVA, ITR)
- Agenda de implementação (curto/médio/longo prazo)
- Recomendações para estudos complementares
- Seção de referências e fontes detalhadas

### 4. O QUE PRESERVAR COM MÁXIMA FIDELIDADE

- **Todos os valores numéricos** presentes na estrutura obrigatória — copiar exatamente
- **O perfil do eleitorado** — incluir tabela compacta na Dimensão 1 com total, sexo, faixas etárias agregadas (jovens 16-29, idosos 60+), escolaridade agregada (EM completo ou superior, analfabetos)
- **O paradoxo central** — preservar a frase entre aspas do diagnóstico integrado
- **A cadeia causal** — preservar a lógica, condensar para 5 elos
- **Os nomes das 4 prioridades estratégicas** — preservar os títulos e reformular ações
- **Os alertas vermelhos** — preservar integralmente, são os mais críticos

### 5. REGRAS DE FORMATAÇÃO

- **NÃO use emojis** nos títulos das seções (diferente da ficha completa que usava)
- **Use markdown limpo**: sem escapes desnecessários (`\-`, `\*`, `\:`)
- **Tabelas devem ter alinhamento consistente**: usar `|` simples
- **Indicadores com valores monetários**: usar formato `R$ X,XX mi` para milhões, `R$ XXX mil` para milhares
- **Percentuais**: uma casa decimal (XX,X%)
- **Variações**: formato `+XX%` ou `-XX%`
- **Dados indisponíveis**: usar `—` (travessão), nunca deixar célula vazia
- **Negrito**: usar apenas para destaques estratégicos, não para todos os termos
- **Aspas**: usar apenas para o paradoxo central no diagnóstico integrado

### 6. CRITÉRIOS DE QUALIDADE

A ficha condensada deve:

- [ ] Ter entre 250 e 350 linhas (5-7 páginas)
- [ ] Conter TODAS as 16 tabelas da estrutura obrigatória (8 dimensões + dados fundamentais + SWOT + comparação + finanças + alertas + meio ambiente + agropecuária)
- [ ] Ter análise qualitativa em TODAS as 8 dimensões (nunca placeholder)
- [ ] Ter paradoxo central ÚNICO e ESPECÍFICO para o município
- [ ] Ter cadeia causal com EXATAMENTE 5 elos formando ciclo
- [ ] Ter 4 prioridades estratégicas com 2 ações cada
- [ ] Ter 6 alertas (2 por nível: vermelho, amarelo, verde)
- [ ] NÃO conter dados inventados
- [ ] NÃO conter seções listadas para eliminação
- [ ] Ter formatação markdown limpa e consistente

### 7. TOM E LINGUAGEM

- **Tom**: Técnico-estratégico, conciso, direto ao ponto
- **Perspectiva**: Analista que assessora gestores públicos estaduais
- **Evite**: Redundâncias, frases genéricas ("é necessário investir em educação"), obviedades
- **Valorize**: Especificidade ("o IDEB do ensino médio caiu de 4,1 para 3,8"), conexões causais, propostas mensuráveis
- **Foco**: Cada frase deve trazer informação nova — se uma frase pode ser removida sem perda de conteúdo, remova-a

### 8. EXEMPLO DE TRANSFORMAÇÃO

**FICHA COMPLETA (entrada) — seção Educação:**
> **Alfabetização:**
> - Taxa de alfabetização (15+ anos): 76,1% (2000), 82,9% (2010), 90,3% (2022)
> - Taxa por sexo (2022): Homens 89,7%, Mulheres 91,0%
> - Taxa por faixa etária (2022): 15-19 anos 97,9%, 20-29 anos 99,3%, 30-39 anos 96,9%, 40-49 anos 94,2%, 50-59 anos 84,6%, 60+ anos 65,5%
>
> **Rede Escolar:**
> - Matrículas por dependência administrativa (2018-2023): [série completa]
> - Matrículas por tipo de ensino (2023): Creche 77, Pré-escola 152, Fundamental 794, Médio 269, EJA 28, Educação Especial 65
> - Docentes por tipo e dependência (2023): Total 95 (Estadual 25, Municipal 70)
> - Estabelecimentos por tipo e dependência (2023): Total 6 (Estadual 2, Municipal 4)
>
> **IDEB:**
> - Anos Iniciais (2013-2023): 3,8 (2013), 3,9 (2015), 4,4 (2017), 4,8 (2019), 4,3 (2021), 4,4 (2023)
> - Anos Finais (2018-2023): 3,7 (2018), 3,9 (2019), 4,8 (2021), 4,7 (2023)
> - Ensino Médio (2018-2023): 4,1 (2019), 3,8 (2023)
>
> **Indicadores de Fluxo Escolar (2023):**
> - Taxa de abandono: [detalhes por nível e dependência]
> - Taxa de aprovação: [detalhes]
> - Taxa de reprovação: [detalhes]
> - Distorção idade-série: Fund. Iniciais 5,8%, Fund. Finais 14,4%, Médio 27,1%
>
> **Ensino Superior:** Nenhuma instituição

**FICHA CONDENSADA (saída) — mesma seção:**

> ## Dimensão 3: Educação
>
> | Indicador | Valor | Referência |
> |-----------|-------|-----------|
> | Alfabetização (2022) | 90,3% | 2010: 82,9% (+7,4 p.p.) |
> | IDEB Anos Iniciais (2023) | 4,4 | Estagnado desde 2017 |
> | IDEB Anos Finais (2023) | 4,7 | 2019: 3,9 (+0,8) |
> | IDEB Ensino Médio (2023) | 3,8 | Meta nacional: 4,2 |
> | Matrículas totais (2023) | 1.385 | Médio: 269, Fund.: 794 |
> | Distorção idade-série EM | 27,1% | — |
> | Ensino superior | Ausente | Nenhuma IES no município |
>
> **Análise**: Avanços significativos na alfabetização (+7,4 p.p. em 12 anos), mas IDEB do ensino médio (3,8) fica abaixo da meta nacional e apresenta distorção idade-série alarmante de 27,1%. A rede é 100% pública (6 estabelecimentos, 95 docentes) e não há ensino superior no município.

---

## NOME DO ARQUIVO DE SAÍDA

`FICHA-MUNICIPAL-[NOME-DO-MUNICIPIO]-V2.md`

Exemplo: `FICHA-MUNICIPAL-AGUIARNOPOLIS-V2.md`

---

## MODO DE USO

### Opção A: Condensação individual

Forneça à IA o conteúdo completo de UMA ficha municipal e este prompt.

**Entrada**: Conteúdo de `FICHA-MUNICIPAL-AGUIARNOPOLIS-COMPLETA.md`
**Saída**: `FICHA-MUNICIPAL-AGUIARNOPOLIS-V2.md`

### Opção B: Condensação em lote

Forneça à IA múltiplas fichas completas com a instrução:

> "Aplique o PROMPT-FICHA-MUNICIPAL-CONDENSADA.md a cada uma das fichas completas a seguir. Gere um arquivo de saída para cada município."

---

## CHECKLIST FINAL ANTES DE ENTREGAR

- [ ] A ficha tem entre 250 e 350 linhas?
- [ ] Todas as 8 dimensões têm tabela de indicadores E análise qualitativa?
- [ ] A SWOT tem exatamente 3 itens por quadrante, cada um com dado numérico?
- [ ] O resumo executivo tem 100-150 palavras com paradoxo identificado?
- [ ] O diagnóstico integrado tem paradoxo + cadeia causal (5 elos) + tabela comparativa?
- [ ] Há 4 prioridades estratégicas com 2 ações e 1 indicador cada?
- [ ] A tabela de alertas tem 6 linhas (2 vermelho + 2 amarelo + 2 verde)?
- [ ] Nenhum dado foi inventado?
- [ ] A formatação markdown está limpa (sem escapes, sem emojis nos títulos)?
- [ ] O arquivo foi nomeado corretamente (FICHA-MUNICIPAL-[NOME]-V2.md)?
