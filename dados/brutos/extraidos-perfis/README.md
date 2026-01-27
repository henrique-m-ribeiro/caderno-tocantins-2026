# Dados Extraídos dos Perfis SEPLAN-TO

## Descrição

Este diretório contém os dados intermediários extraídos dos 139 PDFs dos Perfis Socioeconômicos Municipais.

## Estrutura

Cada município terá um arquivo CSV individual com os dados extraídos:

```
dados/brutos/extraidos-perfis/
├── README.md (este arquivo)
├── 1700101_Abreulandia.csv
├── 1700251_Aguiarnopolis.csv
├── ...
└── 1722081_Xambioa.csv
```

## Nomenclatura

**Padrão:** `[CODIGO_IBGE]_[Nome_Municipio].csv`

Exemplos:
- `1721000_Palmas.csv`
- `1702109_Araguaina.csv`
- `1709500_Gurupi.csv`

## Formato dos Arquivos CSV

Cada CSV terá a seguinte estrutura:

```csv
indicador,valor,ano_referencia,unidade,fonte_pagina,observacoes
demo_pop_2010,228332,2010,habitantes,p.15,
demo_pop_2022,313349,2022,habitantes,p.15,estimativa
econ_pib_total_mil_reais,45678900,2021,mil_reais,p.23,
...
```

## Campos

- **indicador:** Nome do indicador (conforme estrutura V02)
- **valor:** Valor numérico extraído
- **ano_referencia:** Ano de referência do dado
- **unidade:** Unidade de medida
- **fonte_pagina:** Página do PDF onde foi encontrado
- **observacoes:** Notas sobre extração, qualidade, etc.

## Scripts Relacionados

- `scripts/extrair_tabelas_perfis_seplan.py` - Extração automatizada
- `scripts/consolidar_extraidos_perfis.py` - Consolidação em planilha única

## Fase de Criação

**Fase 3:** Desenvolvimento de Infraestrutura de Extração (12-18h)
**Fase 4:** Execução da Extração em Lote (4-6h)

## Validação

Após extração, validar:
- [ ] 139 arquivos CSV criados
- [ ] Nenhum arquivo vazio
- [ ] Todos os indicadores-chave presentes (mínimo 70%)
- [ ] Formatação consistente
- [ ] Anos de referência preenchidos

## Status

- [ ] Script de extração desenvolvido
- [ ] Testes com amostra (10 municípios)
- [ ] Extração em lote executada (0/139)
- [ ] Validação de integridade concluída

---

**Última atualização:** 27 de janeiro de 2026
**Fase:** 0 (Preparação)
