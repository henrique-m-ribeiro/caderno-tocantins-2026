# Parte III - Fichas Municipais

## Sobre este Documento

Este diretório contém as **fichas municipais** dos 139 municípios do Estado do Tocantins, elaboradas para subsidiar a campanha da Senadora Dorinha Seabra ao governo do estado.

## Estrutura

```
parte-iii-fichas-municipais/
├── README.md                                    # Este arquivo
├── prototipos/                                  # Protótipos iniciais (5 municípios)
│   ├── FICHA-MUNICIPAL-PALMAS.md
│   ├── FICHA-MUNICIPAL-ARAGUAÍNA.md
│   ├── FICHA-MUNICIPAL-COLINAS.md
│   ├── FICHA-MUNICIPAL-GUARAÍ.md
│   └── FICHA-MUNICIPAL-LAGOA-DO-TOCANTINS.md
├── fichas/                                      # Fichas de todos os 139 municípios
│   ├── FICHA-MUNICIPAL-ABREULANDIA.md
│   ├── FICHA-MUNICIPAL-AGUIARNOPOLIS.md
│   └── ... (137 outras fichas)
├── PARTE-III-FICHAS-MUNICIPAIS.md              # Documento consolidado (Markdown)
└── PARTE-III-FICHAS-MUNICIPAIS.pdf             # Documento consolidado (PDF)
```

## Estrutura de Cada Ficha

Cada ficha municipal possui **2 páginas** (aproximadamente 160 linhas) com:

### PÁGINA 1 - Visão Geral

1. **Dados Básicos**: População, PIB, IDHM, Área, Microrregião
2. **Síntese Estratégica**:
   - Pontos Fortes
   - Desafios Prioritários
   - Oportunidades
3. **Dimensão 1 - Dados Sociais e Demográficos**: 8 indicadores
4. **Dimensão 2 - Economia**: 6 indicadores
5. **Dimensão 3 - Educação**: 5 indicadores
6. **Dimensão 4 - Saúde e Saneamento**: 5 indicadores

### PÁGINA 2 - Aprofundamento

7. **Dimensão 5 - Agropecuária**: 2 indicadores + análise
8. **Dimensão 6 - Finanças Públicas**: 6 indicadores (2019 vs 2023)
9. **Análise Integrada**: Diagnóstico sistêmico
10. **Diretrizes para o Plano de Governo**: Ações e políticas públicas

## Documento Consolidado

O documento consolidado **PARTE-III-FICHAS-MUNICIPAIS.md** (e sua versão PDF) contém:

1. **Capa**: Título, subtítulo, data
2. **Apresentação**: Objetivo, estrutura, fontes, como utilizar
3. **Índice Alfabético**: 139 municípios com números de página
4. **139 Fichas Municipais**: Ordenadas alfabeticamente
5. **Fontes e Elaboração**: Metodologia, referências, data

**Páginas totais**: Aproximadamente **283 páginas**
- Capa e apresentação: 3 páginas
- Índice: 2 páginas
- Fichas (139 × 2): 278 páginas

## Scripts de Geração

Os seguintes scripts foram utilizados para gerar as fichas:

### 1. `scripts/gerar_ficha_municipal.py`
Gera ficha individual de um município a partir dos dados dos PDFs SEPLAN-TO.

**Uso**:
```bash
python3 scripts/gerar_ficha_municipal.py "Palmas"
```

### 2. `scripts/gerar_fichas_em_massa.py`
Gera fichas de todos os 139 municípios automaticamente.

**Uso**:
```bash
python3 scripts/gerar_fichas_em_massa.py --output parte-iii-fichas-municipais/fichas
```

### 3. `scripts/consolidar_fichas_municipais.py`
Consolida todas as fichas em um documento único com capa, índice e formatação.

**Uso**:
```bash
python3 scripts/consolidar_fichas_municipais.py \
    --input parte-iii-fichas-municipais/fichas \
    --output parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.md
```

### 4. `scripts/converter_para_pdf.py`
Converte o documento Markdown consolidado para PDF com numeração de páginas.

**Uso**:
```bash
python3 scripts/converter_para_pdf.py \
    --input parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.md \
    --output parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.pdf
```

**Requisito**: Requer `pandoc` e `texlive` instalados.

## Fontes de Dados

Os indicadores foram extraídos de:

- **SEPLAN-TO**: Perfil Socioeconômico dos Municípios do Tocantins 2024 (8ª Edição)
- **IBGE**: Censos, PIB Municipal, Estimativas Populacionais
- **INEP**: IDEB (Índice de Desenvolvimento da Educação Básica)
- **DATASUS**: Cadastro Nacional de Estabelecimentos de Saúde
- **Tesouro Nacional**: SICONFI (Finanças Públicas)

## Indicadores Apresentados

### Dados Sociais e Demográficos (8)
- População 2022 e 2010
- IDHM 2010 (Geral, Renda, Longevidade, Educação)
- Densidade demográfica
- Taxa de urbanização

### Economia (6)
- PIB Total e per capita (2021)
- VAB Agropecuária, Indústria, Serviços
- Emprego Formal (2023)

### Educação (5)
- Taxa de alfabetização (2022, 2010)
- IDEB Anos Finais (2023, 2021, 2019)

### Saúde e Saneamento (5)
- Estabelecimentos UBS e Hospitalares
- Domicílios com água, esgoto e coleta de lixo

### Agropecuária (2)
- VAB Agropecuária (2021, 2017)

### Finanças Públicas (6)
- Transferências Totais
- FPM, ICMS, IPVA, FUNDEB, ITR
- Séries históricas 2019-2023

**Total**: 32 indicadores principais + séries históricas

## Metodologia

1. **Extração**: Dados extraídos automaticamente dos PDFs SEPLAN-TO usando pdfplumber
2. **Estruturação**: Indicadores organizados em 139 arquivos JSON
3. **Validação**: Verificação de consistência e completude
4. **Geração**: Criação automática das fichas em Markdown
5. **Consolidação**: Junção em documento único com capa e índice
6. **Conversão**: Markdown → PDF com numeração de páginas

## Atualização

**Data de geração**: 28 de janeiro de 2026
**Dados mais recentes**: Janeiro de 2026
**Cobertura**: 139/140 municípios (exceto "Tocantins" - consolidação estadual)

## Observações

- **Indicadores N/D**: Não são exibidos nas tabelas (linhas ocultas)
- **Análises**: Placeholders `[A DEFINIR]` para preenchimento posterior
- **Comparações**: Futuras versões incluirão comparações com médias regionais/estaduais
- **Atualização**: Documento pode ser facilmente regenerado com dados atualizados

## Suporte

Para dúvidas ou ajustes, consulte a documentação dos scripts em `scripts/`.
