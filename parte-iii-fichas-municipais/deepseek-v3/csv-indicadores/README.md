# CSVs de Indicadores Municipais - Deepseek V3

Esta pasta armazena os **139 arquivos CSV** com todos os indicadores de cada município extraídos pelo Deepseek V3, além do **dicionário de dados** que documenta cada indicador.

## 📄 Conteúdo

### CSVs de Indicadores
Cada CSV segue o padrão:
- **Nome:** `INDICADORES-[NOME-DO-MUNICIPIO]-COMPLETO.csv`
- **Estrutura:** 824 colunas conforme `../prompts/PROMPT-CSV-INDICADORES-MUNICIPAIS.md`
- **Formato:** Separador `;` (ponto e vírgula), decimal `.` (ponto)

### Dicionário de Dados
- **Nome:** `DICIONARIO-DADOS-ABREULANDIA.csv` (referência para todos os municípios)
- **Estrutura:** 8 colunas × 824 indicadores (uma linha por indicador)
- **Colunas:** ROTULO_COLUNA, NOME_CURTO, DESCRICAO_COMPLETA, TIPO_DADO, UNIDADE, ANO_REFERENCIA, FONTE_PRIMARIA, FONTE_SECUNDARIA
- **Tamanho:** 120 KB
- **Criado:** 03 de Fevereiro de 2026

## 📊 Status

**CSVs de Indicadores:**
- **Meta:** 139 CSVs
- **Concluídos:** 1 (Abreulândia)
- **Progresso:** 0.7%

**Dicionários de Dados:**
- **Meta:** 1 dicionário de referência
- **Concluídos:** 1 (Abreulândia - serve para todos os municípios)
- **Progresso:** 100%

## ✅ Padrões de Qualidade

Cada CSV deve conter:
- [ ] Cabeçalho completo (900+ colunas)
- [ ] Linha de dados correspondente ao município
- [ ] Formatação correta (`;` separador, `.` decimal)
- [ ] Séries históricas completas (2019-2023 onde aplicável)
- [ ] Valores ausentes como vazio ou `NA`
- [ ] Sem símbolos de moeda ou unidades

## 📖 Uso do Dicionário de Dados

O dicionário criado para Abreulândia documenta a estrutura completa dos CSVs e serve como referência para todos os 139 municípios, pois:
- A estrutura de colunas é **idêntica** para todos os municípios
- Apenas os **valores** mudam de município para município
- Cada município terá sua própria linha na base consolidada

**Exemplo de uso:**
- Para entender o que significa `PIB_PER_CAPITA_2021`, consulte a linha correspondente no dicionário
- A descrição, fonte e unidade serão as mesmas para todos os municípios

## 📁 Consolidação

Após todos os CSVs serem gerados, serão consolidados em:
- `volumes-finalizados/volume-2/base-dados/BASE-DADOS-TOCANTINS-V02-COMPLETA.csv` (CSV único com 139 linhas)
- `volumes-finalizados/volume-2/base-dados/BASE-DADOS-TOCANTINS-V02-COMPLETA.xlsx` (Excel formatado)
- `volumes-finalizados/volume-2/base-dados/DICIONARIO-DADOS-V02.csv` (cópia do dicionário de referência)

## 🔧 Script de Consolidação

```python
import pandas as pd
import glob

# Consolidar todos os CSVs
csv_files = glob.glob('INDICADORES-*.csv')
dfs = [pd.read_csv(f, sep=';', encoding='utf-8') for f in csv_files]
base_consolidada = pd.concat(dfs, ignore_index=True)
base_consolidada.to_csv('BASE-DADOS-TOCANTINS-V02-COMPLETA.csv', sep=';', index=False, encoding='utf-8')
print(f"Base consolidada: {len(base_consolidada)} municípios")
```

---

**Atualizar este README conforme os CSVs forem sendo gerados!**
