# CSVs de Indicadores Municipais - Deepseek V3

Esta pasta armazenará os **139 arquivos CSV** com todos os indicadores de cada município extraídos pelo Deepseek V3.

## 📄 Conteúdo Esperado

Cada CSV seguirá o padrão:
- **Nome:** `INDICADORES-[NOME-DO-MUNICIPIO]-COMPLETO.csv`
- **Estrutura:** 900+ colunas conforme `../prompts/PROMPT-CSV-INDICADORES-MUNICIPAIS.md`
- **Formato:** Separador `;` (ponto e vírgula), decimal `.` (ponto)

## 📊 Status

- **Meta:** 139 CSVs
- **Concluídos:** 0
- **Progresso:** 0%

## ✅ Padrões de Qualidade

Cada CSV deve conter:
- [ ] Cabeçalho completo (900+ colunas)
- [ ] Linha de dados correspondente ao município
- [ ] Formatação correta (`;` separador, `.` decimal)
- [ ] Séries históricas completas (2019-2023 onde aplicável)
- [ ] Valores ausentes como vazio ou `NA`
- [ ] Sem símbolos de moeda ou unidades

## 📁 Consolidação

Após todos os CSVs serem gerados, serão consolidados em:
- `volumes-finalizados/volume-2/base-dados/BASE-DADOS-TOCANTINS-V02-COMPLETA.csv` (CSV único)
- `volumes-finalizados/volume-2/base-dados/BASE-DADOS-TOCANTINS-V02-COMPLETA.xlsx` (Excel formatado)

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
