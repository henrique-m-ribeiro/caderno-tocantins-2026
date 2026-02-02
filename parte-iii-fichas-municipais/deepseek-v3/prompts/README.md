# Prompts para Deepseek V3 - Volume 2

Esta pasta contém **3 prompts completos** para geração do Volume 2 do Caderno Tocantins 2026.

---

## 📄 PROMPTS DISPONÍVEIS

### 1. PROMPT-FICHA-MUNICIPAL-COMPLETA.md
**Objetivo:** Gerar análise socioeconômica completa e aprofundada de um município

**Entrada:** PDF do Perfil Socioeconômico (SEPLAN-TO)
**Saída:** Ficha municipal em Markdown (15+ páginas)

**Conteúdo da Ficha:**
- Resumo Executivo
- Dados Fundamentais
- Análise SWOT (5+ pontos em cada quadrante)
- 9 Dimensões de Análise:
  1. Informações Gerais e Aspectos Físicos
  2. Demografia e Desenvolvimento Social
  3. Economia e Produção
  4. Finanças Públicas
  5. Educação
  6. Saúde
  7. Saneamento Básico
  8. Infraestrutura e Serviços Urbanos
  9. Meio Ambiente
- Diagnóstico Integrado (cadeias causais)
- Diretrizes Estratégicas (4+ prioridades)
- Agenda de Implementação
- Alertas e Riscos
- Recomendações para estudos futuros

**Características:**
- ✅ Análise aprofundada (não apenas descritiva)
- ✅ SEM limite de páginas
- ✅ Extração de TODOS os indicadores
- ✅ Conexões entre dimensões
- ✅ Propostas concretas e viáveis

---

### 2. PROMPT-CSV-INDICADORES-MUNICIPAIS.md
**Objetivo:** Extrair todos os indicadores do município em formato CSV estruturado

**Entrada:** PDF do Perfil Socioeconômico (SEPLAN-TO)
**Saída:** CSV com 900+ colunas de indicadores

**Estrutura do CSV:**
- **Separador:** `;` (ponto e vírgula)
- **Decimal:** `.` (ponto)
- **Linha 1:** Cabeçalho com 900+ colunas
- **Linha 2:** Dados do município

**Categorias de Indicadores:**
- Informações Gerais e Aspectos Físicos
- Demografia (séries 1991-2022)
- Indicadores Sociais (IDHM, pobreza, programas)
- Economia (PIB, VAB, empresas, empregos, comércio)
- Agropecuária (produção agrícola, pecuária, aquicultura)
- Finanças Públicas (transferências 2019-2023)
- Educação (matrículas, IDEB, fluxo escolar)
- Saúde (infraestrutura, indicadores vitais, doenças)
- Saneamento (água, esgoto, lixo - séries 1991-2021)
- Infraestrutura (conectividade, energia, veículos)
- Meio Ambiente (queimadas, resíduos)

**Características:**
- ✅ Cobertura completa (900+ indicadores)
- ✅ Formatação padronizada
- ✅ Séries históricas completas
- ✅ Pronto para consolidação

---

### 3. PROMPT-DICIONARIO-DADOS.md
**Objetivo:** Documentar cada indicador com metadados completos

**Entrada:** PDF do Perfil Socioeconômico (SEPLAN-TO)
**Saída:** CSV com dicionário de dados (900+ linhas)

**Estrutura do Dicionário:**
Cada linha documenta uma coluna da planilha de indicadores.

**Colunas do Dicionário (16):**
1. **ROTULO_COLUNA** - Nome exato da coluna na planilha
2. **NOME_CURTO** - Nome legível para humanos
3. **DESCRICAO_COMPLETA** - Explicação detalhada do indicador
4. **TIPO_DADO** - INTEGER, DECIMAL, PERCENTAGE, TEXT, CODE
5. **UNIDADE** - habitantes, reais, km², %, pontos, etc.
6. **ANO_REFERENCIA** - Ano ou período dos dados
7. **FONTE_PRIMARIA** - IBGE, INEP, DATASUS, etc.
8. **FONTE_SECUNDARIA** - Censo, PNAD, pesquisa específica
9. **SECAO_PDF** - Seção do PDF onde aparece
10. **PAGINA_PDF** - Página no PDF
11. **TABELA_PDF** - Identificação da tabela
12. **OBSERVACOES** - Informações importantes
13. **FORMULA_CALCULO** - Como é calculado (se aplicável)
14. **PERIODICIDADE_ATUALIZACAO** - Frequência de atualização
15. **LIMITACOES** - Limitações conhecidas
16. **CONTEXTO_USO** - Para que é usado

**Características:**
- ✅ Documentação completa de cada indicador
- ✅ Rastreabilidade até a fonte original
- ✅ Informações para atualização futura
- ✅ Contexto de uso para analistas

---

## 🔄 ORDEM DE EXECUÇÃO RECOMENDADA

Para cada um dos 139 municípios:

### PASSO 1: Gerar Ficha Municipal
1. Abrir Deepseek V3
2. Fazer upload do PDF do município
3. Copiar e colar `PROMPT-FICHA-MUNICIPAL-COMPLETA.md`
4. Aguardar geração completa
5. Salvar em `../fichas-completas/FICHA-MUNICIPAL-[NOME]-COMPLETA.md`
6. Validar usando checklist do prompt

### PASSO 2: Extrair CSV de Indicadores
1. Usar o MESMO PDF do Passo 1
2. Copiar e colar `PROMPT-CSV-INDICADORES-MUNICIPAIS.md`
3. Aguardar extração completa
4. Salvar em `../csv-indicadores/INDICADORES-[NOME]-COMPLETO.csv`
5. Validar formatação (`;`, `.`, 900+ colunas)

### PASSO 3: Gerar Dicionário de Dados
1. Usar o MESMO PDF dos passos anteriores
2. Copiar e colar `PROMPT-DICIONARIO-DADOS.md`
3. Aguardar documentação completa
4. Salvar em `../csv-indicadores/DICIONARIO-DADOS-[NOME].csv`
5. Validar cobertura (900+ linhas)

**Tempo estimado por município:** 25-30 minutos (3 prompts)

---

## 📊 CONSOLIDAÇÃO APÓS 139 MUNICÍPIOS

### Consolidar CSVs de Indicadores

```python
import pandas as pd
import glob

# Consolidar todos os CSVs de indicadores
csv_files = glob.glob('../csv-indicadores/INDICADORES-*.csv')
dfs = [pd.read_csv(f, sep=';', encoding='utf-8') for f in csv_files]
base_consolidada = pd.concat(dfs, ignore_index=True)
base_consolidada.to_csv('BASE-DADOS-TOCANTINS-V02-COMPLETA.csv', sep=';', index=False, encoding='utf-8')
print(f"Base consolidada: {len(base_consolidada)} municípios × {len(base_consolidada.columns)} indicadores")
```

### Consolidar Dicionários de Dados

```python
# Todos os dicionários devem ser iguais (mesmas colunas)
# Basta usar o de um município e validar com os demais
dicionario = pd.read_csv('../csv-indicadores/DICIONARIO-DADOS-PALMAS.csv', sep=';', encoding='utf-8')
dicionario.to_csv('DICIONARIO-DADOS-COMPLETO.csv', sep=';', index=False, encoding='utf-8')
print(f"Dicionário: {len(dicionario)} indicadores documentados")
```

---

## ✅ PADRÕES DE QUALIDADE

### Para Fichas Municipais

**APROVADA:**
- ✅ 15+ páginas de análise substantiva
- ✅ Todas as 9 dimensões presentes
- ✅ SWOT com 5+ pontos em cada quadrante
- ✅ Diagnóstico integrado conectando 3+ dimensões
- ✅ Prioridades estratégicas específicas e viáveis

**REQUER REVISÃO:**
- ⚠️ 12-15 páginas (pode estar incompleto)
- ⚠️ SWOT genérico sem dados
- ⚠️ Poucas conexões entre dimensões

**REJEITADA:**
- ❌ Menos de 10 páginas
- ❌ Apenas lista de dados (sem análise)
- ❌ Estrutura diferente do template

### Para CSV de Indicadores

**APROVADO:**
- ✅ 900+ colunas
- ✅ Formatação correta (`;` e `.`)
- ✅ Séries históricas completas
- ✅ Valores ausentes como vazio ou `NA`

**REQUER REVISÃO:**
- ⚠️ 700-900 colunas (faltando indicadores)
- ⚠️ Séries históricas incompletas

**REJEITADO:**
- ❌ Menos de 700 colunas
- ❌ Formatação errada

### Para Dicionário de Dados

**APROVADO:**
- ✅ 900+ linhas (uma por indicador)
- ✅ Campos obrigatórios preenchidos
- ✅ Descrições claras e úteis
- ✅ Fontes identificadas

**REQUER REVISÃO:**
- ⚠️ Descrições muito curtas ou genéricas
- ⚠️ Campos obrigatórios vazios

**REJEITADO:**
- ❌ Menos de 700 linhas
- ❌ Descrições inventadas ou incorretas

---

## 🔧 FERRAMENTAS DE VALIDAÇÃO

### Validar Ficha Municipal

```bash
# Contar páginas aproximadas
wc -l FICHA-MUNICIPAL-*.md

# Verificar seções
grep -c "^## " FICHA-MUNICIPAL-*.md

# Deve retornar 10+ (seções principais)
```

### Validar CSV de Indicadores

```bash
# Contar colunas
head -1 INDICADORES-*.csv | tr ';' '\n' | wc -l

# Deve retornar 900+
```

### Validar Dicionário

```bash
# Contar linhas (excluindo cabeçalho)
tail -n +2 DICIONARIO-DADOS-*.csv | wc -l

# Deve retornar 900+
```

---

## 📚 REFERÊNCIAS

- **Perfis Socioeconômicos SEPLAN-TO:** `/Perfil Municipios Tocantins/`
- **Protótipos analisados:** `parte-iii-fichas-municipais/prototipos/`
- **Estratégia completa:** `../README.md`

---

## 📞 SUPORTE

Para dúvidas sobre os prompts:
- **Estrutura do Volume 2:** `../README.md`
- **Framework IA-Collab-OS:** `/.governance/README.md`
- **Repositório:** https://github.com/henrique-m-ribeiro/caderno-tocantins-2026

---

**Última atualização:** 02 de Fevereiro de 2026
**Versão dos prompts:** 1.0
**Status:** Prontos para uso
