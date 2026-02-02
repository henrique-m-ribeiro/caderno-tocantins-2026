# Estratégia Deepseek V3 para Fichas Municipais

## 📋 CONTEXTO

Esta pasta contém a estratégia e os materiais para geração do **Volume 2 do Caderno Tocantins 2026**, composto pelas **139 Fichas Municipais completas** e a **Base de Dados Expandida** do estado.

**Decisão Técnica:** Após testes com Claude Code e Manus AI, constatou-se que o **Deepseek V3** apresenta capacidade superior para processar os PDFs extensos (~40 MB) dos Perfis Socioeconômicos da SEPLAN-TO e gerar análises completas e estruturadas.

---

## 🎯 OBJETIVO

Criar 139 fichas municipais completas, bases de dados estruturadas e documentação completa, seguindo os princípios do framework **IA-Collab-OS**:

1. **Completude:** Extrair TODOS os indicadores dos Perfis Socioeconômicos
2. **Qualidade Analítica:** Análises aprofundadas, não apenas descritivas
3. **Estrutura Consistente:** Todas as fichas seguem o mesmo template
4. **Utilidade Estratégica:** Diagnósticos integrados e diretrizes concretas
5. **Rastreabilidade:** Dados vinculados às fontes oficiais
6. **Documentação:** Metadados completos para cada indicador

---

## 📁 ESTRUTURA DE DIRETÓRIOS

```
deepseek-v3/
│
├── README.md                         ← Este arquivo
│
├── prompts/                          ← Prompts para Deepseek
│   ├── PROMPT-FICHA-MUNICIPAL-COMPLETA.md
│   ├── PROMPT-CSV-INDICADORES-MUNICIPAIS.md
│   ├── PROMPT-DICIONARIO-DADOS.md
│   └── README.md
│
├── fichas-completas/                 ← Fichas geradas (139 arquivos)
│   ├── FICHA-MUNICIPAL-ABREULANDIA-COMPLETA.md
│   ├── FICHA-MUNICIPAL-AGUIARNOPOLIS-COMPLETA.md
│   └── ... (137 outras)
│
└── csv-indicadores/                  ← CSVs gerados (139 arquivos)
    ├── INDICADORES-ABREULANDIA-COMPLETO.csv
    ├── INDICADORES-AGUIARNOPOLIS-COMPLETO.csv
    └── ... (137 outros)
```

---

## 🔄 FLUXO DE TRABALHO

### FASE 1: GERAÇÃO DAS FICHAS MUNICIPAIS

**Para cada um dos 139 municípios:**

1. **Preparar o PDF:**
   - Localizar o Perfil Socioeconômico do município em `/Perfil Municipios Tocantins/`
   - Verificar que o arquivo está completo e legível

2. **Executar o prompt:**
   - Abrir o Deepseek V3
   - Fazer upload do PDF do Perfil Socioeconômico
   - Copiar e colar o conteúdo de `prompts/PROMPT-FICHA-MUNICIPAL-COMPLETA.md`
   - Aguardar a geração da análise completa

3. **Revisar e salvar:**
   - Verificar se a estrutura está completa (todas as seções presentes)
   - Verificar se há dados suficientes em cada dimensão
   - Salvar em `fichas-completas/FICHA-MUNICIPAL-[NOME]-COMPLETA.md`

4. **Controle de qualidade:**
   - [ ] Resumo executivo presente e sintético?
   - [ ] Análise SWOT completa (5+ pontos em cada quadrante)?
   - [ ] Todas as 9 dimensões analisadas?
   - [ ] Diagnóstico integrado presente?
   - [ ] Pelo menos 4 prioridades estratégicas?
   - [ ] Ações concretas e viáveis?
   - [ ] Documento com 15+ páginas?

### FASE 2: EXTRAÇÃO DOS INDICADORES PARA CSV

**Para cada um dos 139 municípios:**

1. **Executar o prompt:**
   - Abrir o Deepseek V3
   - Fazer upload do MESMO PDF usado na Fase 1
   - Copiar e colar o conteúdo de `prompts/PROMPT-CSV-INDICADORES-MUNICIPAIS.md`
   - Aguardar a extração de todos os indicadores

2. **Validar o CSV:**
   - Verificar número de colunas (deve ser 900+)
   - Verificar formatação (ponto e vírgula, ponto decimal)
   - Verificar séries históricas completas
   - Salvar em `csv-indicadores/INDICADORES-[NOME]-COMPLETO.csv`

3. **Controle de qualidade:**
   - [ ] Cabeçalho completo presente?
   - [ ] Linha de dados corresponde ao cabeçalho?
   - [ ] Números formatados corretamente?
   - [ ] Séries históricas completas (2019-2023)?
   - [ ] Valores ausentes marcados como vazio ou NA?

### FASE 2.5: GERAÇÃO DO DICIONÁRIO DE DADOS

**Para cada um dos 139 municípios (ou apenas 1 representativo):**

1. **Executar o prompt:**
   - Abrir o Deepseek V3
   - Fazer upload do MESMO PDF usado nas Fases 1 e 2
   - Copiar e colar o conteúdo de `prompts/PROMPT-DICIONARIO-DADOS.md`
   - Aguardar a documentação completa de todos os indicadores

2. **Validar o Dicionário:**
   - Verificar número de linhas (deve ser 900+, uma por indicador)
   - Verificar se campos obrigatórios estão preenchidos
   - Verificar descrições claras e úteis
   - Salvar em `csv-indicadores/DICIONARIO-DADOS-[NOME].csv`

3. **Controle de qualidade:**
   - [ ] 900+ linhas presentes (uma por coluna da planilha)?
   - [ ] Campos obrigatórios preenchidos (ROTULO_COLUNA, NOME_CURTO, DESCRICAO_COMPLETA, TIPO_DADO, ANO_REFERENCIA, FONTE_PRIMARIA)?
   - [ ] Descrições claras e não genéricas?
   - [ ] Fontes identificadas corretamente?
   - [ ] Tipos de dados apropriados?

**Nota:** Como o dicionário documenta a estrutura da planilha (não os dados específicos de cada município), você pode gerar apenas um dicionário e usá-lo para todos os 139 municípios, ou gerar um para cada município como backup. Recomenda-se gerar para pelo menos 3-5 municípios diferentes e comparar para garantir consistência.

### FASE 3: CONSOLIDAÇÃO DA BASE DE DADOS

**Após gerar os 139 CSVs individuais:**

1. **Consolidar em uma única base:**
   - Usar script Python para concatenar todos os CSVs
   - Gerar `BASE-DADOS-TOCANTINS-V02-COMPLETA.csv`
   - Validar consistência (139 linhas + cabeçalho)

2. **Gerar planilha Excel:**
   - Converter para formato `.xlsx`
   - Adicionar formatação condicional
   - Criar abas por dimensão (Demografia, Economia, Educação, etc.)

3. **Gerar metadados:**
   - Criar dicionário de dados completo
   - Documentar fonte de cada indicador
   - Registrar ano de referência de cada dado

### FASE 4: ORGANIZAÇÃO DO VOLUME 2

**Estrutura do Volume 2:**

```
volumes-finalizados/
└── volume-2/
    ├── CADERNO-TOCANTINS-2026-VOLUME-2-FICHAS-MUNICIPAIS.md
    ├── README.md
    ├── ENTREGA-VOLUME-2-FINALIZADO.md
    │
    ├── fichas-por-microrregiao/
    │   ├── 01-PORTO-NACIONAL/           (11 municípios)
    │   ├── 02-ARAGUAINA/                (17 municípios)
    │   ├── 03-BICO-DO-PAPAGAIO/         (25 municípios)
    │   ├── 04-MIRACEMA-DO-TOCANTINS/    (23 municípios)
    │   ├── 05-GURUPI/                   (15 municípios)
    │   ├── 06-DIANOPOLIS/               (18 municípios)
    │   ├── 07-JALAPAO/                  (15 municípios)
    │   └── 08-RIO-FORMOSO/              (15 municípios)
    │
    └── base-dados/
        ├── BASE-DADOS-TOCANTINS-V02-COMPLETA.csv
        ├── BASE-DADOS-TOCANTINS-V02-COMPLETA.xlsx
        ├── DICIONARIO-DADOS-V02.md
        └── METADADOS-COMPLETO.md
```

**Nota:** A organização segue as **8 microrregiões do Volume 1**, mantendo a consistência metodológica do projeto.

---

## 📊 MÉTRICAS DE PROGRESSO

**Meta:** 139 municípios × 3 entregas (ficha + CSV + dicionário*) = **278-417 documentos**

*Dicionário pode ser único para todos ou um por município

**Status Atual:**

| Fase | Meta | Concluído | % |
|------|------|-----------|---|
| Fichas Municipais | 139 | 0 | 0% |
| CSVs de Indicadores | 139 | 0 | 0% |
| Dicionários de Dados | 1-139 | 0 | 0% |
| Base Consolidada | 1 | 0 | 0% |
| Dicionário Consolidado | 1 | 0 | 0% |
| Volume 2 Organizado | 1 | 0 | 0% |

**Atualizar esta tabela conforme o progresso!**

---

## 🎯 PADRÕES DE QUALIDADE

### Para Fichas Municipais

**APROVADA se:**
- ✅ Estrutura completa (todas as seções obrigatórias presentes)
- ✅ Análise SWOT com 5+ pontos em cada quadrante
- ✅ Todas as 9 dimensões analisadas com dados
- ✅ Diagnóstico integrado conecta pelo menos 3 dimensões
- ✅ Prioridades estratégicas são específicas e viáveis
- ✅ Documento tem 15+ páginas de análise substantiva

**REQUER REVISÃO se:**
- ⚠️ Alguma seção faltando ou muito curta (<1 página)
- ⚠️ SWOT genérico (frases vagas sem dados)
- ⚠️ Menos de 4 prioridades estratégicas
- ⚠️ Ações genéricas ("melhorar", "investir mais")
- ⚠️ Documento com menos de 12 páginas

**REJEITADA se:**
- ❌ Estrutura completamente diferente do template
- ❌ Dados claramente incorretos ou inventados
- ❌ Falta de análise (apenas lista de dados)
- ❌ Documento com menos de 8 páginas

### Para CSVs de Indicadores

**APROVADO se:**
- ✅ 900+ colunas presentes
- ✅ Formatação correta (`;` separador, `.` decimal)
- ✅ Séries históricas completas
- ✅ Valores ausentes marcados apropriadamente
- ✅ Sem dados claramente incorretos

**REQUER REVISÃO se:**
- ⚠️ Menos de 800 colunas (muitos dados faltando)
- ⚠️ Formatação inconsistente
- ⚠️ Séries históricas incompletas
- ⚠️ Muitos valores como 0 (pode indicar erro)

**REJEITADO se:**
- ❌ Menos de 500 colunas
- ❌ Formatação completamente errada
- ❌ Dados claramente inventados
- ❌ Arquivo vazio ou corrompido

---

## 🔧 FERRAMENTAS DE APOIO

### Script de Validação de Fichas

```bash
# Contar páginas aproximadas de uma ficha
wc -l fichas-completas/FICHA-MUNICIPAL-*.md

# Verificar se todas as seções estão presentes
grep -c "^##" fichas-completas/FICHA-MUNICIPAL-*.md
```

### Script de Validação de CSVs

```bash
# Contar colunas de um CSV
head -1 csv-indicadores/INDICADORES-*.csv | tr ';' '\n' | wc -l

# Verificar formatação
head -2 csv-indicadores/INDICADORES-*.csv
```

### Script de Consolidação

```python
import pandas as pd
import glob

# Consolidar todos os CSVs
csv_files = glob.glob('csv-indicadores/INDICADORES-*.csv')
dfs = [pd.read_csv(f, sep=';', encoding='utf-8') for f in csv_files]
base_consolidada = pd.concat(dfs, ignore_index=True)
base_consolidada.to_csv('BASE-DADOS-TOCANTINS-V02-COMPLETA.csv', sep=';', index=False, encoding='utf-8')
print(f"Base consolidada: {len(base_consolidada)} municípios")
```

---

## 📅 CRONOGRAMA ESTIMADO

**Premissas:**
- Deepseek V3 processa 1 município completo em ~15-20 minutos
- 139 municípios × 20 min = ~46 horas de processamento
- Revisões e ajustes: ~10-15 horas adicionais
- **Total estimado:** 55-60 horas de trabalho

**Divisão Sugerida:**

| Semana | Atividade | Municípios | Horas |
|--------|-----------|------------|-------|
| 1 | Gerar fichas (lote 1) | 35 | 12h |
| 2 | Gerar fichas (lote 2) | 35 | 12h |
| 3 | Gerar fichas (lote 3) | 35 | 12h |
| 4 | Gerar fichas (lote 4) | 34 | 12h |
| 5 | Gerar CSVs (todos) | 139 | 10h |
| 6 | Consolidação e revisão | - | 10h |

**Total:** 6 semanas

---

## 🚨 PROBLEMAS CONHECIDOS E SOLUÇÕES

### Problema 1: PDF Corrompido ou Ilegível

**Solução:**
1. Baixar novamente do site da SEPLAN-TO
2. Se persistir, marcar município como "pendente"
3. Contatar SEPLAN-TO se necessário

### Problema 2: Deepseek Trunca a Resposta

**Solução:**
1. Dividir o prompt em partes (Dimensões 1-3, 4-6, 7-9)
2. Gerar em múltiplas interações
3. Consolidar manualmente

### Problema 3: Dados Ausentes no PDF

**Solução:**
1. Marcar como `NA` no CSV
2. Documentar no README do município
3. Buscar fonte alternativa se crítico

### Problema 4: Inconsistências entre Fichas

**Solução:**
1. Revisar com checklist de qualidade
2. Ajustar manualmente se necessário
3. Documentar padrão correto para próximas

---

## 📚 REFERÊNCIAS

### Protótipos Analisados

Os seguintes protótipos foram gerados pelo Deepseek V3 e serviram de base para os prompts:

1. `parte-iii-fichas-municipais/prototipos/Ficha_Abreulândia.md`
2. `parte-iii-fichas-municipais/prototipos/Ficha_Aguiarnópolis.md`
3. `parte-iii-fichas-municipais/prototipos/Ficha_Aliança do Tocantins.md`
4. `parte-iii-fichas-municipais/prototipos/Ficha_Almas.md`

### Estrutura dos Perfis Socioeconômicos SEPLAN-TO

Os Perfis Socioeconômicos seguem esta estrutura:

1. Informações Gerais (histórico, limites)
2. Aspectos Físicos (área, altitude, bioma, pedologia, relevo, uso da terra)
3. Aspectos Demográficos (população, densidade, urbanização, estrutura etária, eleitores)
4. Indicadores Sociais (IDHM, pobreza, Bolsa Família)
5. Aspectos Econômicos (PIB, VAB, empresas, empregos, comércio exterior, agropecuária)
6. Educação (alfabetização, matrículas, IDEB, fluxo escolar)
7. Saúde (estabelecimentos, profissionais, leitos, indicadores vitais, doenças)
8. Saneamento Básico (água, esgoto, lixo)
9. Serviços e Equipamentos Urbanos (bancos, conectividade, energia, veículos)
10. Meio Ambiente (queimadas, resíduos sólidos)

### Framework IA-Collab-OS

Documentação completa: [`/.governance/README.md`](../../.governance/README.md)

Princípios aplicados:
- Transparência e rastreabilidade
- Qualidade baseada em critérios objetivos
- Iteração e melhoria contínua
- Colaboração humano-IA

---

## 🤝 CONTRIBUIÇÃO

Este trabalho segue a metodologia do **Caderno Tocantins 2026** e os princípios do **IA-Collab-OS**.

**Responsável Técnico:** Henrique Marques Ribeiro
**Framework:** https://github.com/henrique-m-ribeiro/ia-collab-os
**Data de Criação:** 31 de Janeiro de 2026
**Última Atualização:** 31 de Janeiro de 2026

---

## 📞 CONTATO

Para dúvidas sobre esta estratégia ou sobre o Caderno Tocantins 2026:

- **Repositório:** https://github.com/henrique-m-ribeiro/caderno-tocantins-2026
- **Framework:** https://github.com/henrique-m-ribeiro/ia-collab-os
- **SEPLAN-TO:** (63) 3212-4475 | http://www.to.gov.br/seplan

---

**VOLUME 2 EM CONSTRUÇÃO** 🚧

Status: Estratégia definida | Prompts criados | Aguardando execução
