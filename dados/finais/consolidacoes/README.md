# Planilhas de Consolidação Regional

## Descrição

Este diretório contém as **6 planilhas de consolidação** separadas por tipo de classificação regional, conforme decisão aprovada pelo usuário.

## Estrutura

```
dados/finais/consolidacoes/
├── README.md (este arquivo)
├── BASE_CONSOLIDACOES_MICRORREGIOES_IBGE_1989.csv (8 linhas)
├── BASE_CONSOLIDACOES_MESORREGIOES_IBGE_1989.csv (2 linhas)
├── BASE_CONSOLIDACOES_REGIOES_PLANEJAMENTO_SEPLAN_2024.csv (8 linhas)
├── BASE_CONSOLIDACOES_MACRORREGIOES_SEPLAN_2024.csv (3 linhas)
└── BASE_CONSOLIDACAO_ESTADUAL.csv (1 linha)
```

## Planilhas

### 1. BASE_CONSOLIDACOES_MICRORREGIOES_IBGE_1989.csv
**8 Microrregiões IBGE (Classificação 1989-2017)**
1. Araguaína
2. Bico do Papagaio
3. Dianópolis
4. Gurupi
5. Jalapão
6. Miracema
7. Porto Nacional
8. Rio Formoso

**Colunas:** Mesma estrutura que a planilha principal (~65 colunas)
**Método de agregação:** Por indicador (SUM, MÉDIA PONDERADA, ou N/A)

### 2. BASE_CONSOLIDACOES_MESORREGIOES_IBGE_1989.csv
**2 Mesorregiões IBGE (Classificação 1989-2017)**
1. Ocidental do Tocantins
2. Oriental do Tocantins

### 3. BASE_CONSOLIDACOES_REGIOES_PLANEJAMENTO_SEPLAN_2024.csv
**8 Regiões de Planejamento SEPLAN-TO 2024** (Portaria nº 91 - 22/10/2024)
1. Bico do Papagaio (25 municípios)
2. Norte (15 municípios)
3. Meio Norte (25 municípios)
4. Vale do Araguaia (15 municípios)
5. Central (14 municípios)
6. Jalapão (9 municípios)
7. Sul (17 municípios)
8. Sudeste (19 municípios)

### 4. BASE_CONSOLIDACOES_MACRORREGIOES_SEPLAN_2024.csv
**3 Macrorregiões SEPLAN-TO 2024**
1. Macrorregião Norte (65 municípios)
   - Bico do Papagaio + Norte + Meio Norte
2. Macrorregião Central (38 municípios)
   - Vale do Araguaia + Central + Jalapão
3. Macrorregião Sul (36 municípios)
   - Sul + Sudeste

### 5. BASE_CONSOLIDACAO_ESTADUAL.csv
**1 linha: Estado do Tocantins**
- Consolidação de todos os 139 municípios

## Métodos de Agregação

### Indicadores Agregáveis por Soma (SUM)
- População total
- PIB total
- Número de estabelecimentos de saúde
- Número de escolas
- Área territorial

### Indicadores Agregáveis por Média Ponderada (WEIGHTED_AVG)
Ponderados pela população:
- PIB per capita
- IDHM e seus componentes
- Taxa de urbanização
- IDEB
- Taxa de analfabetismo
- Mortalidade infantil

### Indicadores Não-Agregáveis (N/A)
- Código IBGE (substituir por código da região)
- Nome do território (substituir por nome da região)
- Observações (consolidar se necessário)

## Benefícios da Separação

✅ **Planilha principal limpa:** Apenas 139 municípios
✅ **Flexibilidade:** Usuário escolhe qual classificação usar
✅ **Comparações:** Fácil comparar diferentes divisões regionais
✅ **Atualizações independentes:** Consolidações podem ser recalculadas separadamente
✅ **Análises multi-escala:** Municipal → Micro → Meso → Regional → Macro → Estadual

## Script Relacionado

- `scripts/calcular_consolidacoes.py` - Gera todas as 6 planilhas

## Fase de Criação

**Fase 4:** Execução da Extração em Lote
**Fase 7:** Documentação e Encerramento

## Validações

Para cada planilha de consolidação:
- [ ] Número correto de linhas
- [ ] Todos os municípios classificados (soma = 139)
- [ ] Nenhum município duplicado entre regiões
- [ ] Totais estaduais = soma de todos os municípios (indicadores agregáveis)
- [ ] Médias ponderadas calculadas corretamente

## Status

- [ ] Script de consolidação desenvolvido
- [ ] Microrregiões IBGE 1989 gerada
- [ ] Mesorregiões IBGE 1989 gerada
- [ ] Regiões de Planejamento SEPLAN 2024 gerada
- [ ] Macrorregiões SEPLAN 2024 gerada
- [ ] Consolidação Estadual gerada
- [ ] Validações executadas
- [ ] Totais conferidos

---

**Última atualização:** 27 de janeiro de 2026
**Fase:** 0 (Preparação)
