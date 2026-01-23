# Caderno Tocantins 2026

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Parte II](https://img.shields.io/badge/Parte%20II-100%25%20Conclu%C3%ADda-green)
![Cobertura](https://img.shields.io/badge/Cobertura-130%2F139%20munic%C3%ADpios-blue)

Sistema de Inteligência Territorial para subsidiar a campanha eleitoral ao governo do Estado do Tocantins em 2026.

---

## 📋 Sobre o Projeto

O **Caderno Tocantins 2026** é um documento estratégico que apresenta análises profundas e baseadas em dados sobre as **8 microrregiões** e **139 municípios** do Estado do Tocantins. O projeto utiliza metodologias de análise territorial, dados oficiais de múltiplas fontes governamentais e inteligência artificial para produzir insights estratégicos que apoiam a tomada de decisão em políticas públicas.

### Objetivos

- Fornecer análise territorial detalhada de todas as regiões do Tocantins
- Identificar desafios e oportunidades em cada microrregião
- Subsidiar propostas de políticas públicas baseadas em evidências
- Mapear indicadores socioeconômicos, educacionais, de saúde e infraestrutura
- Criar base de conhecimento para planejamento estratégico estadual

---

## 🗂️ Estrutura do Caderno

O projeto está organizado em **3 partes principais**:

### Parte I - Visão Geral do Estado do Tocantins
**Status:** ⏸️ Não iniciada (aguarda conclusão da coleta de dados)

Síntese estratégica integrando análises das 8 microrregiões:
- Perfil demográfico estadual
- Economia estadual (PIB, setores, comparação regional)
- Educação, saúde e saneamento
- Agropecuária e mineração
- Infraestrutura e logística
- Desafios e oportunidades do Tocantins
- Recomendações estratégicas para o governo estadual

### Parte II - Fichas Regionais (8 Microrregiões)
**Status:** ✅ 100% Concluída (versão preliminar V1.0)

Análise detalhada de cada microrregião:

| # | Microrregião | Municípios | Nota | Arquivo |
|---|--------------|------------|------|---------|
| 01 | Porto Nacional | 11 | 9.9/10 | ⚠️ Pendente integração |
| 02 | Araguaína | 17 | 10/10 | ⚠️ Pendente integração |
| 03 | Bico do Papagaio | 25 | 8.5/10 | ⚠️ Pendente integração |
| 04 | Miracema | 23 | 9.0/10 | ⚠️ Pendente integração |
| 05 | Gurupi | 15 | 9.5/10 | ✅ [FICHA-05](./parte-ii-fichas-regionais/PARTE-II-FICHA-05-MICRORREGIAO-GURUPI-V01.md) |
| 06 | Dianópolis | 18 | 9.2/10 | ✅ [FICHA-06](./parte-ii-fichas-regionais/PARTE-II-FICHA-06-MICRORREGIAO-DIANOPOLIS-V01.md) |
| 07 | Jalapão | 15 | 9.5/10 | ✅ [FICHA-07](./parte-ii-fichas-regionais/PARTE-II-FICHA-07-MICRORREGIAO-JALAPAO-V01.md) |
| 08 | Rio Formoso | 13 | 9.8/10 | ✅ [FICHA-08](./parte-ii-fichas-regionais/PARTE-II-FICHA-08-MICRORREGIAO-RIO-FORMOSO-V01.md) |

**Total:** 130 municípios analisados (93,5% dos 139 municípios do estado)
**Média de Notas:** 9.4/10

### Parte III - Fichas Municipais (139 Municípios)
**Status:** ⏸️ Não iniciada (aguarda conclusão da Parte I)

Análise individual detalhada de cada município do Tocantins.

---

## 📊 Estrutura do Repositório

```
caderno-tocantins-2026/
│
├── README.md                           # Este arquivo
├── .gitignore                          # Arquivos ignorados pelo Git
│
├── .governance/                        # Governança do projeto
│   ├── prompts/                        # Prompts utilizados nas análises
│   └── sessions/                       # Avaliações e entregas
│
├── docs/                               # Documentação do projeto
│   └── RELATORIO_COMPLETO.md          # Relatório completo do projeto
│
├── dados/                              # Dados coletados
│   └── finais/                         # Datasets das microrregiões
│       ├── dados-microrregiao-*.csv   # CSVs com dados regionais
│       └── RELATORIO-COLETA-*.md      # Relatórios de coleta
│
└── parte-ii-fichas-regionais/          # Fichas das microrregiões
    └── PARTE-II-FICHA-*.md            # Análises regionais detalhadas
```

---

## 📈 Status do Projeto

### ✅ Concluído

- ✅ Estrutura do repositório organizada
- ✅ 8 datasets CSV das microrregiões
- ✅ 4 fichas regionais completas (Gurupi, Dianópolis, Jalapão, Rio Formoso)
- ✅ 130 municípios com dados de população coletados
- ✅ Metodologia de análise estabelecida
- ✅ Sistema de governança implementado

### 🚧 Em Andamento

- 🚧 Integração das 4 primeiras fichas regionais ao repositório
- 🚧 Coleta de dados complementares (IDEB 2023, Saneamento, Agropecuária)
- 🚧 Refinamento de dados para versão V2.0 das fichas

### ⏳ Planejado

- ⏳ Elaboração da Parte I (Visão Geral do Estado)
- ⏳ Elaboração da Parte III (Fichas Municipais)
- ⏳ Integração com Google Drive
- ⏳ Dashboard de visualização de dados

---

## 🔍 Principais Insights

### Destaques Regionais

1. **Araguaína** - Capital econômica do norte, crescimento acelerado
2. **Lagoa da Confusão** - 4º maior produtor de arroz do Brasil
3. **Mateiros (Jalapão)** - PIB per capita excepcional (R$ 170.006,81) vs. declínio populacional
4. **Bico do Papagaio** - Mortalidade infantil crítica, maior declínio populacional do estado
5. **Rio Formoso** - Paradoxo riqueza agropecuária vs. desenvolvimento social

---

## 📊 Indicadores Coletados

### Cobertura Atual (139 municípios)

| Indicador | Cobertura | Status |
|-----------|-----------|--------|
| População 2010 e 2022 | 100% | ✅ |
| Área Territorial | 35% | ⚠️ |
| PIB per capita | 35% | ⚠️ |
| IDHM | 35% | ⚠️ |
| Taxa de Escolarização | 35% | ⚠️ |
| Mortalidade Infantil | 32% | ⚠️ |
| IDEB 2023 | 0% | ❌ |
| Saneamento | 0% | ❌ |
| Agropecuária | 0% | ❌ |

---

## 🔗 Fontes de Dados

O projeto utiliza dados de fontes oficiais:

- **IBGE** - Instituto Brasileiro de Geografia e Estatística
  - [IBGE Cidades](https://cidades.ibge.gov.br/)
  - [SIDRA](https://sidra.ibge.gov.br/) - Sistema IBGE de Recuperação Automática
- **INEP** - Instituto Nacional de Estudos e Pesquisas Educacionais
  - [IDEB](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/ideb)
- **DATASUS** - Departamento de Informática do SUS
  - [Sistema de Informações sobre Mortalidade](https://datasus.saude.gov.br/)
- **SNIS** - Sistema Nacional de Informações sobre Saneamento
  - [Portal SNIS](http://www.snis.gov.br/)
- **PNUD** - Programa das Nações Unidas para o Desenvolvimento
  - Atlas do Desenvolvimento Humano no Brasil

---

## 🛠️ Metodologia

O projeto utiliza a **IA Collab OS** - metodologia de colaboração entre humanos e IA para:

1. **Coleta de Dados**: Extração de dados de múltiplas fontes oficiais
2. **Análise Territorial**: Processamento e análise de indicadores regionais
3. **Identificação de Padrões**: Detecção de tendências e anomalias
4. **Geração de Insights**: Produção de análises estratégicas
5. **Documentação**: Registro completo de fontes, metodologias e limitações

### Princípios

- **Transparência**: Todas as lacunas são explicitamente marcadas
- **Rastreabilidade**: Todas as fontes são documentadas
- **Qualidade**: Sistema de avaliação com notas (0-10)
- **Iteração**: Versões incrementais (V1.0 → V2.0 → ...)

---

## 📅 Cronograma

### Janeiro 2026
- ✅ Conclusão da Parte II (8 microrregiões) - V1.0
- 🚧 Coleta de dados complementares (IDEB, Saneamento, Agropecuária)

### Fevereiro 2026
- ⏳ Atualização das fichas regionais (V2.0)
- ⏳ Elaboração da Parte I (Visão Geral do Estado)

### Março 2026
- ⏳ Elaboração da Parte III (Fichas Municipais)

---

## 🤝 Contribuindo

Este é um repositório privado para uso estratégico. Para contribuir:

1. Crie uma branch a partir de `main`
2. Faça suas alterações
3. Abra um Pull Request com descrição detalhada
4. Aguarde revisão

---

## 📝 Licença

Este projeto contém informações estratégicas de campanha e é de uso restrito.

© 2026 - Caderno Tocantins 2026. Todos os direitos reservados.

---

## 📧 Contato

Para dúvidas sobre o projeto, entre em contato com a equipe de coordenação.

---

**Última atualização:** 23 de janeiro de 2026
**Versão:** 1.0.0
**Status:** Em Desenvolvimento
