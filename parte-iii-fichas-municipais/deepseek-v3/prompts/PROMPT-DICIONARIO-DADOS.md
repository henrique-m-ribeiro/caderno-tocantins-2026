# PROMPT PARA GERAÇÃO DE DICIONÁRIO DE DADOS (CSV)

## CONTEXTO

Você receberá o **Perfil Socioeconômico Municipal** de um município do Tocantins em formato PDF. Com base neste documento, você deverá criar um **DICIONÁRIO DE DADOS completo** que descreva cada um dos 900+ indicadores presentes na planilha de dados municipais.

## OBJETIVO

Criar um arquivo CSV (separado por ponto e vírgula) que documente **TODAS as colunas** da planilha de indicadores municipais, fornecendo metadados completos para cada indicador.

---

## ESTRUTURA DO CSV - DICIONÁRIO DE DADOS

### REGRAS GERAIS

1. **Separador:** Ponto e vírgula (`;`)
2. **Codificação:** UTF-8
3. **Primeira linha:** Cabeçalho com nomes das colunas
4. **Linhas seguintes:** Uma linha para cada coluna/indicador da planilha (900+ linhas)
5. **Textos longos:** Entre aspas duplas se contiverem ponto e vírgula
6. **Valores ausentes:** Deixar vazio ou usar `NA`

### COLUNAS DO DICIONÁRIO

```csv
ROTULO_COLUNA;NOME_CURTO;DESCRICAO_COMPLETA;TIPO_DADO;UNIDADE;ANO_REFERENCIA;FONTE_PRIMARIA;FONTE_SECUNDARIA;SECAO_PDF;PAGINA_PDF;TABELA_PDF;OBSERVACOES;FORMULA_CALCULO;PERIODICIDADE_ATUALIZACAO;LIMITACOES;CONTEXTO_USO
```

---

## DESCRIÇÃO DETALHADA DE CADA COLUNA DO DICIONÁRIO

### 1. ROTULO_COLUNA
**O que é:** Nome exato da coluna na planilha de indicadores
**Formato:** Exatamente como aparece no cabeçalho do CSV de indicadores
**Exemplo:** `POPULACAO_2022`, `PIB_2021`, `IDEB_ANOS_INICIAIS_2023`

### 2. NOME_CURTO
**O que é:** Nome resumido e legível para humanos
**Formato:** Texto curto (máximo 50 caracteres)
**Exemplo:** `População 2022`, `PIB 2021`, `IDEB Anos Iniciais 2023`

### 3. DESCRICAO_COMPLETA
**O que é:** Descrição detalhada do que o indicador representa
**Formato:** Texto explicativo completo (100-300 caracteres)
**Exemplo:**
- `População residente total estimada para o ano de 2022, incluindo área urbana e rural`
- `Produto Interno Bruto a preços correntes em reais para o ano de 2021`
- `Índice de Desenvolvimento da Educação Básica para os anos iniciais do ensino fundamental em 2023`

### 4. TIPO_DADO
**O que é:** Tipo de dado da coluna
**Valores permitidos:**
- `INTEGER` - Número inteiro (ex: população, número de escolas)
- `DECIMAL` - Número decimal (ex: PIB, taxas, índices)
- `PERCENTAGE` - Percentual (ex: taxa de urbanização)
- `TEXT` - Texto (ex: nome do município, bioma)
- `CODE` - Código (ex: código IBGE)
- `BOOLEAN` - Sim/Não (ex: presença de hospital)
- `DATE` - Data (se houver)

### 5. UNIDADE
**O que é:** Unidade de medida do indicador
**Formato:** Texto curto
**Exemplos:**
- `habitantes`
- `reais (R$)`
- `km²`
- `%` (percentual)
- `pontos` (para índices)
- `toneladas`
- `metros`
- `unidades`
- `NA` (para texto ou código)

### 6. ANO_REFERENCIA
**O que é:** Ano ou período de referência dos dados
**Formato:**
- Ano específico: `2022`, `2021`, `2020`
- Série histórica: `2019-2023`
- Censo: `Censo 2022`, `Censo 2010`
- Indefinido: `Variável` ou `NA`

### 7. FONTE_PRIMARIA
**O que é:** Fonte original dos dados
**Formato:** Nome da instituição ou órgão produtor
**Exemplos:**
- `IBGE - Instituto Brasileiro de Geografia e Estatística`
- `INEP/MEC - Instituto Nacional de Estudos e Pesquisas Educacionais`
- `DATASUS - Ministério da Saúde`
- `SEPLAN-TO - Secretaria de Planejamento do Tocantins`
- `SNIS - Sistema Nacional de Informações sobre Saneamento`
- `CONAB - Companhia Nacional de Abastecimento`
- `ANATEL - Agência Nacional de Telecomunicações`
- `DENATRAN - Departamento Nacional de Trânsito`

### 8. FONTE_SECUNDARIA
**O que é:** Fonte intermediária ou base de dados utilizada
**Formato:** Nome da pesquisa, censo ou sistema específico
**Exemplos:**
- `Censo Demográfico 2022`
- `PNAD Contínua`
- `Contas Regionais do Brasil`
- `Censo Escolar`
- `IDEB - Índice de Desenvolvimento da Educação Básica`
- `SINAN - Sistema de Informação de Agravos de Notificação`
- `Pesquisa Agrícola Municipal (PAM)`
- `Pesquisa Pecuária Municipal (PPM)`

### 9. SECAO_PDF
**O que é:** Nome da seção do Perfil Socioeconômico onde o dado aparece
**Formato:** Nome da seção conforme sumário do PDF
**Exemplos:**
- `3. Aspectos Demográficos`
- `5. Aspectos Econômicos`
- `6. Educação`
- `7. Saúde`
- `8. Saneamento Básico`

### 10. PAGINA_PDF
**O que é:** Número da página no PDF onde o indicador aparece
**Formato:** Número da página ou intervalo
**Exemplos:** `18`, `45-46`, `NA`

### 11. TABELA_PDF
**O que é:** Identificação da tabela no PDF
**Formato:** Título da tabela ou número
**Exemplos:**
- `Tabela 3.1 - População Residente por Situação de Domicílio`
- `Gráfico 5.2 - PIB por Setor`
- `Quadro 6.3 - Matrículas por Tipo de Ensino`

### 12. OBSERVACOES
**O que é:** Observações importantes sobre o indicador
**Formato:** Texto livre com informações relevantes
**Exemplos:**
- `Estimativa populacional, não censo`
- `Valores a preços correntes`
- `Meta estabelecida pelo INEP`
- `Dados preliminares sujeitos a revisão`
- `Série interrompida em 2020 devido à pandemia`

### 13. FORMULA_CALCULO
**O que é:** Fórmula de cálculo do indicador (se aplicável)
**Formato:** Expressão matemática ou descrição do cálculo
**Exemplos:**
- `(População Urbana / População Total) × 100`
- `PIB / População`
- `Nota SAEB × Taxa de Aprovação`
- `(Número de óbitos infantis / Nascidos vivos) × 1000`
- `NA` (para dados primários não calculados)

### 14. PERIODICIDADE_ATUALIZACAO
**O que é:** Com que frequência o indicador é atualizado
**Formato:** Texto descrevendo a periodicidade
**Exemplos:**
- `Anual`
- `Bienal`
- `Decenal (censo)`
- `Trimestral`
- `Irregular`
- `Contínua`

### 15. LIMITACOES
**O que é:** Limitações conhecidas do indicador
**Formato:** Texto livre descrevendo limitações
**Exemplos:**
- `Pode haver subnotificação em municípios pequenos`
- `Não inclui setor informal da economia`
- `Metodologia mudou em 2017, dificulta comparação histórica`
- `Depende de autodeclaração, sujeito a viés`

### 16. CONTEXTO_USO
**O que é:** Para que o indicador é tipicamente usado
**Formato:** Texto livre descrevendo aplicações
**Exemplos:**
- `Planejamento de políticas populacionais e cálculo de recursos per capita`
- `Avaliação da capacidade econômica do município`
- `Monitoramento da qualidade da educação básica`
- `Acompanhamento de metas de saúde pública`

---

## EXEMPLO DE LINHAS DO DICIONÁRIO

```csv
ROTULO_COLUNA;NOME_CURTO;DESCRICAO_COMPLETA;TIPO_DADO;UNIDADE;ANO_REFERENCIA;FONTE_PRIMARIA;FONTE_SECUNDARIA;SECAO_PDF;PAGINA_PDF;TABELA_PDF;OBSERVACOES;FORMULA_CALCULO;PERIODICIDADE_ATUALIZACAO;LIMITACOES;CONTEXTO_USO
NOME_MUNICIPIO;Nome do Município;Nome oficial do município conforme registro no IBGE;TEXT;NA;Atual;IBGE - Instituto Brasileiro de Geografia e Estatística;Divisão Territorial Brasileira;1. Informações Gerais;10;NA;Nome pode ter mudado ao longo do tempo;NA;Irregular;Apenas mudanças oficiais por lei;Identificação do município em análises e relatórios
CODIGO_IBGE;Código IBGE;Código único de 7 dígitos atribuído pelo IBGE ao município;CODE;NA;Atual;IBGE - Instituto Brasileiro de Geografia e Estatística;Divisão Territorial Brasileira;1. Informações Gerais;10;NA;Código permanente mesmo se município mudar de nome;NA;Permanente;Nenhuma;Chave primária para integração de bases de dados
AREA_KM2;Área Territorial;Área territorial oficial do município em quilômetros quadrados;DECIMAL;km²;2022;IBGE - Instituto Brasileiro de Geografia e Estatística;Área Territorial Brasileira;2. Aspectos Físicos;13;Tabela 2.1;Pode haver pequenas revisões com tecnologias de medição mais precisas;NA;Irregular;Áreas de litígio podem causar imprecisões;Cálculo de densidade demográfica e planejamento territorial
POPULACAO_2022;População 2022;População residente total estimada para o ano de 2022, incluindo área urbana e rural;INTEGER;habitantes;2022;IBGE - Instituto Brasileiro de Geografia e Estatística;Estimativas de População;3. Aspectos Demográficos;18;Tabela 3.1;Estimativa intercensitária, não é contagem exata;NA;Anual;Baseada em projeções do Censo 2010, pode ter desvios;Planejamento de políticas públicas e cálculo de recursos per capita
PIB_2021;PIB 2021;Produto Interno Bruto a preços correntes em reais para o ano de 2021;DECIMAL;reais (R$);2021;IBGE - Instituto Brasileiro de Geografia e Estatística;Contas Regionais do Brasil;5. Aspectos Econômicos;30;Tabela 5.1;Valores a preços correntes (não deflacionados);Soma do VAB de todos os setores + impostos;Anual;Não captura economia informal;Avaliação da capacidade econômica e comparação entre municípios
PIB_PER_CAPITA_2021;PIB per capita 2021;Produto Interno Bruto dividido pela população, em reais, para o ano de 2021;DECIMAL;reais (R$);2021;IBGE - Instituto Brasileiro de Geografia e Estatística;Contas Regionais do Brasil;5. Aspectos Econômicos;30;Tabela 5.1;Calculado com PIB e população do mesmo ano;PIB / População;Anual;Não reflete distribuição de renda;Comparação de riqueza per capita entre municípios
TAXA_URBANIZACAO_2022;Taxa de Urbanização 2022;Percentual da população que reside em área urbana em relação ao total;PERCENTAGE;%;2022;IBGE - Instituto Brasileiro de Geografia e Estatística;Estimativas de População;3. Aspectos Demográficos;18;Tabela 3.2;Definição de área urbana é do município, pode variar;(População Urbana / População Total) × 100;Anual;Definição de 'urbano' varia entre municípios;Planejamento de infraestrutura urbana e serviços
IDEB_ANOS_INICIAIS_2023;IDEB Anos Iniciais 2023;Índice de Desenvolvimento da Educação Básica para os anos iniciais (1º ao 5º ano) do ensino fundamental em 2023;DECIMAL;pontos;2023;INEP/MEC - Instituto Nacional de Estudos e Pesquisas Educacionais;IDEB - Índice de Desenvolvimento da Educação Básica;6. Educação;48;Tabela 6.8;Escala de 0 a 10, meta estabelecida pelo INEP;Nota SAEB × Taxa de Aprovação;Bienal;Escolas com poucos alunos podem ter volatilidade;Monitoramento da qualidade da educação básica
LEITOS_TOTAL_2024;Leitos Hospitalares Totais 2024;Número total de leitos hospitalares disponíveis no município em 2024;INTEGER;unidades;2024;DATASUS - Ministério da Saúde;CNES - Cadastro Nacional de Estabelecimentos de Saúde;7. Saúde;53;Tabela 7.4;Inclui leitos SUS e não-SUS;NA;Mensal;Pode haver desatualização no cadastro;Planejamento de capacidade hospitalar
AGUA_REDE_GERAL_2021;Domicílios com Água Encanada 2021;Percentual de domicílios com abastecimento de água por rede geral de distribuição;PERCENTAGE;%;2021;IBGE - Instituto Brasileiro de Geografia e Estatística;Censo Demográfico 2022 - dados preliminares;8. Saneamento Básico;59;Tabela 8.1;Não indica qualidade da água;(Domicílios com rede geral / Total de domicílios) × 100;Decenal;Conexão não garante fornecimento contínuo;Avaliação de cobertura de saneamento básico
```

---

## INSTRUÇÕES ESPECÍFICAS PARA DEEPSEEK

### 1. COBERTURA COMPLETA

- **Documente TODAS as 900+ colunas** da planilha de indicadores
- Siga a ordem exata das colunas do CSV de indicadores
- Não pule nenhuma coluna, mesmo que seja difícil encontrar informações

### 2. QUALIDADE DAS DESCRIÇÕES

- **DESCRICAO_COMPLETA:** Seja específico e claro. Evite jargões desnecessários.
- **OBSERVACOES:** Inclua informações que um analista de dados precisaria saber
- **LIMITACOES:** Seja honesto sobre o que o indicador não captura
- **CONTEXTO_USO:** Pense em um gestor público usando o dado

### 3. PREENCHIMENTO DOS CAMPOS

**Campos obrigatórios (sempre preencher):**
- ROTULO_COLUNA
- NOME_CURTO
- DESCRICAO_COMPLETA
- TIPO_DADO
- ANO_REFERENCIA
- FONTE_PRIMARIA

**Campos condicionais (preencher quando aplicável):**
- UNIDADE (sempre que for numérico)
- FONTE_SECUNDARIA (se houver)
- SECAO_PDF (se localizado)
- FORMULA_CALCULO (para indicadores derivados)
- PERIODICIDADE_ATUALIZACAO (quando souber)

**Campos opcionais (preencher se tiver informação):**
- PAGINA_PDF
- TABELA_PDF
- OBSERVACOES
- LIMITACOES
- CONTEXTO_USO

### 4. PADRÕES DE NOMENCLATURA

**TIPO_DADO - Escolha correta:**
- População, número de escolas, leitos → `INTEGER`
- PIB, áreas, taxas → `DECIMAL`
- Porcentagens → `PERCENTAGE`
- Nome de município, bioma → `TEXT`
- Código IBGE → `CODE`

**ANO_REFERENCIA - Seja específico:**
- Se é série histórica: `2019-2023`
- Se é dado pontual: `2022`
- Se varia: `Variável`

### 5. CONSISTÊNCIA

- Use sempre os mesmos nomes para as mesmas fontes
- Mantenha padrão de capitalização
- Seja consistente em abreviações

### 6. ORGANIZAÇÃO

As linhas devem seguir exatamente a mesma ordem das colunas do CSV de indicadores:

1. **Informações Gerais** (NOME_MUNICIPIO, CODIGO_IBGE, AREA_KM2, etc.)
2. **Aspectos Físicos** (ALTITUDE_M, LATITUDE, LONGITUDE, etc.)
3. **Demografia** (POPULACAO_*, DENSIDADE_*, etc.)
4. **Indicadores Sociais** (IDHM_*, FAMILIAS_*, etc.)
5. **Economia** (PIB_*, VAB_*, EMPRESAS_*, etc.)
6. **Educação** (MATRICULAS_*, IDEB_*, etc.)
7. **Saúde** (ESTABELECIMENTOS_*, LEITOS_*, etc.)
8. **Saneamento** (AGUA_*, ESGOTO_*, etc.)
9. **Infraestrutura** (ENERGIA_*, VEICULOS_*, etc.)
10. **Meio Ambiente** (QUEIMADAS_*, etc.)

---

## VALIDAÇÃO FINAL

Antes de entregar, verifique:

- [ ] Todas as 900+ colunas documentadas (uma linha por coluna)?
- [ ] Cabeçalho com as 16 colunas do dicionário presente?
- [ ] Campos obrigatórios preenchidos em todas as linhas?
- [ ] Formatação CSV correta (`;` separador, aspas quando necessário)?
- [ ] Descrições claras e úteis?
- [ ] Fontes identificadas corretamente?
- [ ] Tipos de dados apropriados?
- [ ] Unidades especificadas para indicadores numéricos?
- [ ] Anos de referência corretos?

---

## NOME DO ARQUIVO DE SAÍDA

`DICIONARIO-DADOS-[NOME-DO-MUNICIPIO].csv`

Exemplo: `DICIONARIO-DADOS-ALIANCA-DO-TOCANTINS.csv`

---

## OBSERVAÇÃO IMPORTANTE

Este dicionário de dados é **CRÍTICO** para:
- Entender o significado de cada indicador
- Atualizar a base de dados no futuro
- Integrar com outras bases de dados
- Garantir uso correto dos indicadores
- Documentar limitações e contexto

**Qualidade é mais importante que velocidade.** Se tiver dúvida sobre um campo, deixe em branco ou use `NA`, mas não invente informações.

---

## FORMATO DE SAÍDA

### Primeiras 3 linhas devem ser assim:

```csv
ROTULO_COLUNA;NOME_CURTO;DESCRICAO_COMPLETA;TIPO_DADO;UNIDADE;ANO_REFERENCIA;FONTE_PRIMARIA;FONTE_SECUNDARIA;SECAO_PDF;PAGINA_PDF;TABELA_PDF;OBSERVACOES;FORMULA_CALCULO;PERIODICIDADE_ATUALIZACAO;LIMITACOES;CONTEXTO_USO
NOME_MUNICIPIO;Nome do Município;Nome oficial do município conforme registro no IBGE;TEXT;NA;Atual;IBGE - Instituto Brasileiro de Geografia e Estatística;Divisão Territorial Brasileira;1. Informações Gerais;10;NA;Nome pode ter mudado ao longo do tempo;NA;Irregular;Apenas mudanças oficiais por lei;Identificação do município em análises e relatórios
CODIGO_IBGE;Código IBGE;Código único de 7 dígitos atribuído pelo IBGE ao município;CODE;NA;Atual;IBGE - Instituto Brasileiro de Geografia e Estatística;Divisão Territorial Brasileira;1. Informações Gerais;10;NA;Código permanente mesmo se município mudar de nome;NA;Permanente;Nenhuma;Chave primária para integração de bases de dados
```

---

**BOA DOCUMENTAÇÃO!** 📚
