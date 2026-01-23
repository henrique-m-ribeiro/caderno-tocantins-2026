# 🤖 PROMPT PARA ANÁLISE DA MICRORREGIÃO DO RIO FORMOSO (V1.0 - PARCIAL)

**Projeto:** Caderno Tocantins 2026  
**Fase:** Parte II - Fichas Regionais  
**Microrregião:** Rio Formoso (Ficha 08 - ÚLTIMA MICRORREGIÃO)

---

## 1. CONTEXTO

Estamos elaborando análises detalhadas das 8 microrregiões do Tocantins. A coleta de dados municipais está **parcialmente incompleta** para indicadores setoriais (IDEB, Saneamento, Agropecuária). Para não bloquear o progresso, vamos avançar com a elaboração de uma **versão inicial (V1.0)** da análise para cada microrregião, utilizando os dados já disponíveis e os documentos de referência catalogados.

**Microrregião atual:** Rio Formoso (ÚLTIMA MICRORREGIÃO - 8 de 8)

**Contexto Geográfico:** O Rio Formoso está localizado no **sudoeste do Tocantins**, na divisa com o estado do Pará, às margens do Rio Araguaia. É uma região caracterizada pela **agricultura irrigada em larga escala** (Projeto Rio Formoso - maior projeto de irrigação da América Latina nos anos 1980), pecuária extensiva, e pela presença da **Ilha do Bananal** (maior ilha fluvial do mundo). A região possui forte vocação agropecuária e desafios relacionados à gestão hídrica, regularização fundiária e desenvolvimento sustentável.

---

## 2. OBJETIVO DA TAREFA

Elaborar um relatório de análise da Microrregião do **Rio Formoso**, seguindo a estrutura definida, utilizando os dados disponíveis e marcando explicitamente as lacunas de dados para revisão posterior. A análise deve ser rica em contexto, utilizando os documentos de referência para análises qualitativas, com foco especial em **agricultura irrigada, pecuária, gestão hídrica e desenvolvimento regional**.

---

## 3. RECURSOS DISPONÍVEIS

### 3.1. Dados Quantitativos

- **`dados-microrregiao-rio-formoso.csv`** (A SER CRIADO)
  - **Dados Completos (13-15 municípios):** Demografia (população, área, densidade, etc.) e Economia (PIB, PIB per capita, etc.)
  - **Dados Parciais (se houver):** IDEB 2023 e Saneamento (SNIS) para os maiores municípios da região.

### 3.2. Dados Qualitativos (Documentos de Referência)

- **`referencias/`** (102 documentos catalogados)
  - Relatórios do IPEA, IBGE, UFT, SEPLAN-TO, etc.
  - Análises sobre economia, sociedade, educação, saúde, agropecuária, mineração, etc.
  - Use estes documentos para enriquecer a análise, trazer contexto e citar fontes relevantes.

---

## 4. ESTRUTURA DO RELATÓRIO DE ANÁLISE

O relatório final deve seguir **exatamente** a estrutura abaixo:

```markdown
# PARTE II - FICHA 08: MICRORREGIÃO DO RIO FORMOSO (V1.0 - PARCIAL)

## 1. APRESENTAÇÃO E PERFIL TERRITORIAL
- Localização geográfica da microrregião no Tocantins (sudoeste, divisa com Pará)
- Lista dos municípios que a compõem (13-15 municípios, conforme IBGE)
- Área total (km²)
- População total e densidade demográfica
- Contexto do Rio Araguaia e da Ilha do Bananal
- Histórico do Projeto Rio Formoso (agricultura irrigada)

## 2. PERFIL DEMOGRÁFICO
- Análise da distribuição da população (urbana/rural)
- Análise da pirâmide etária e estrutura por sexo
- Evolução populacional nos últimos anos
- Padrões migratórios (atração/expulsão populacional)

## 3. ECONOMIA E AGROPECUÁRIA
- Análise do PIB total e PIB per capita da microrregião
- Análise da composição setorial da economia (agropecuária, indústria, serviços)
- Destaque para a **agricultura irrigada** (Projeto Rio Formoso)
- Análise da **pecuária bovina** (rebanho, produção)
- Análise qualitativa do potencial agrícola e pecuário
- Desafios da gestão hídrica e sustentabilidade
- **[LACUNA: Dados de produção agropecuária de 13-15 municípios - coleta prevista para 2026-01-23]**

## 4. EDUCAÇÃO
- Análise do contexto estadual e regional, com base nos documentos de referência
- Análise dos dados de IDEB 2023 dos municípios disponíveis
- **[LACUNA: IDEB 2023 de 13-15 municípios - coleta prevista para 2026-01-23]**
- Análise qualitativa dos desafios e oportunidades da educação na região, com base nos documentos de referência
- Desafios específicos da educação rural

## 5. SAÚDE E SANEAMENTO
- Análise do contexto estadual e regional, com base nos documentos de referência
- Análise dos dados de saneamento dos municípios disponíveis
- **[LACUNA: Dados de saneamento de 13-15 municípios - coleta prevista para 2026-01-23]**
- Análise qualitativa dos desafios e oportunidades da saúde e saneamento na região
- Desafios específicos da saúde rural e acesso a serviços

## 6. INFRAESTRUTURA E LOGÍSTICA
- Análise da infraestrutura rodoviária (BR-242, TO-050, etc.)
- Análise da infraestrutura hídrica (Projeto Rio Formoso, canais de irrigação)
- Desafios de acesso e conectividade
- Potencial logístico (proximidade com Pará, Rio Araguaia)

## 7. DESENVOLVIMENTO SUSTENTÁVEL E DESAFIOS AMBIENTAIS
- Análise do conflito entre expansão agropecuária e preservação ambiental
- Gestão hídrica e uso sustentável da água (Projeto Rio Formoso)
- Desafios da regularização fundiária
- Pressão sobre a Ilha do Bananal e áreas de preservação
- Potencial da agricultura sustentável e pecuária de baixo carbono

## 8. SÍNTESE: DESAFIOS E OPORTUNIDADES
- Análise integrada, conectando os pontos das diferentes dimensões
- Identificação dos principais desafios da microrregião (gestão hídrica, infraestrutura, desenvolvimento social)
- Identificação das principais oportunidades de desenvolvimento (agricultura irrigada, pecuária, logística)
- Potencial de integração regional (Pará, Mato Grosso)

## 9. LIMITAÇÕES DESTA ANÁLISE (V1.0)
- Lista explícita das lacunas de dados (IDEB, Saneamento, Agropecuária)
- Data prevista para revisão completa (2026-01-23)
- Declaração de que esta é uma versão parcial e que as conclusões podem ser revisadas após a coleta completa dos dados

## 10. REFERÊNCIAS
- Lista de todos os documentos de referência citados na análise
```

---

## 5. REQUISITOS E RESTRIÇÕES CRÍTICAS

1.  **MARCAÇÃO DE LACUNAS:** É **obrigatório** marcar todas as lacunas de dados de forma explícita, usando o marcador `[LACUNA: descrição do dado faltante - previsão de coleta]`.
2.  **TRANSPARÊNCIA:** A seção "Limitações desta Análise" é **obrigatória** e deve ser clara sobre o caráter parcial do documento.
3.  **USO DE REFERÊNCIAS:** A análise deve ser enriquecida com informações dos documentos de referência catalogados. Cite as fontes quando apropriado.
4.  **NÃO ESTIMAR DADOS:** É terminantemente proibido estimar, mockar ou preencher as lacunas de dados. A análise deve ser feita apenas com os dados disponíveis.
5.  **FOCO NA ANÁLISE QUALITATIVA:** Onde os dados quantitativos são limitados, a análise deve se aprofundar no contexto qualitativo fornecido pelos documentos de referência.
6.  **FOCO EM AGROPECUÁRIA E GESTÃO HÍDRICA:** A análise deve dar ênfase especial à agricultura irrigada (Projeto Rio Formoso), pecuária e aos desafios da gestão hídrica e sustentabilidade ambiental.

---

## 6. PASSO A PASSO SUGERIDO

1.  **Analisar este prompt** em detalhe.
2.  **Carregar e analisar** o arquivo `dados-microrregiao-rio-formoso.csv`.
3.  **Explorar** os documentos de referência na pasta `referencias/` para obter contexto, especialmente sobre agricultura irrigada, pecuária, gestão hídrica e desenvolvimento regional.
4.  **Elaborar o relatório** de análise, seguindo a estrutura definida, seção por seção.
5.  **Para as seções 1, 2 e 3 (Dados Completos):** Focar na análise dos dados quantitativos.
6.  **Para as seções 4, 5, 6 e 7 (Dados Parciais):** Combinar a análise dos dados parciais com a análise qualitativa dos documentos de referência, e marcar as lacunas.
7.  **Elaborar a síntese** (seção 8) e as limitações (seção 9).
8.  **Entregar o relatório completo** em formato Markdown.

---

## 7. ENTREGA

O resultado final deve ser um **único arquivo Markdown** contendo a análise completa da Microrregião do **Rio Formoso** (Versão 1.0 - Parcial), pronto para ser salvo como `PARTE-II-FICHA-08-MICRORREGIAO-RIO-FORMOSO-V1.md`.

---

## 8. INFORMAÇÕES ADICIONAIS

### 8.1 Características Distintivas do Rio Formoso

- **Localização:** Sudoeste do Tocantins, divisa com o Pará
- **População:** Estimada entre 80.000 e 120.000 habitantes (confirmar com dados do CSV)
- **Densidade Demográfica:** Baixa a média (região de expansão agropecuária)
- **Economia:** Agricultura irrigada (arroz, soja, milho), pecuária bovina extensiva
- **Projeto Rio Formoso:** Maior projeto de irrigação da América Latina nos anos 1980 (13.000 hectares irrigados)
- **Hidrografia:** Bacia do Rio Araguaia, Rio Formoso, Rio Javaés
- **Preservação:** Ilha do Bananal (Parque Nacional do Araguaia), Terras Indígenas
- **Desafios:** Gestão hídrica, regularização fundiária, conflitos socioambientais, infraestrutura precária, acesso a serviços públicos
- **Número de Municípios:** 13-15 municípios (confirmar com IBGE)

### 8.2 Municípios Principais (estimativa)

- **Formoso do Araguaia** - Polo regional, sede do Projeto Rio Formoso
- **Lagoa da Confusão** - Importante polo agropecuário
- **Cristalândia** - Polo regional de serviços
- **Dueré** - Agricultura e pecuária

**Nota:** Confirme a hierarquia urbana e a lista completa de municípios com os dados populacionais do CSV.

### 8.3 Contexto Histórico do Projeto Rio Formoso

O **Projeto Rio Formoso** foi implantado a partir de 1979 como um dos maiores projetos de agricultura irrigada da América Latina, com o objetivo de desenvolver a região através da produção de arroz irrigado em larga escala. O projeto enfrentou diversos desafios ao longo das décadas (gestão, sustentabilidade, conflitos fundiários), mas continua sendo um marco importante da economia regional.

### 8.4 Alertas para a Análise

- **Atenção especial** para a análise da gestão hídrica (uso intensivo de água para irrigação)
- **Atenção especial** para os conflitos entre expansão agropecuária e preservação ambiental (Ilha do Bananal)
- **Atenção especial** para os desafios da regularização fundiária (histórico de ocupação desordenada)
- **Atenção especial** para a integração regional (proximidade com Pará e potencial logístico)

---

## 9. OBSERVAÇÃO FINAL

**Esta é a ÚLTIMA microrregião da Parte II do Caderno Tocantins 2026!** 🎯

Após a conclusão desta análise, teremos completado as **8 fichas regionais** do estado, representando um marco importante do projeto. A análise do Rio Formoso deve manter o mesmo padrão de excelência das 7 microrregiões anteriores:

1. ✅ Porto Nacional - V1.0 - Nota 9.9/10
2. ✅ Araguaína - V1.0 - Nota 10/10
3. ✅ Bico do Papagaio - V1.0 - Nota 8.5/10
4. ✅ Miracema - V0.5 - Nota 9.0/10
5. ✅ Gurupi - V0.1 - Nota 9.5/10
6. ✅ Dianópolis - V0.1 - Nota 9.2/10
7. ✅ Jalapão - V0.1 - Nota 9.5/10
8. 🔄 **Rio Formoso - EM ELABORAÇÃO**

**Vamos concluir com excelência!** 💪
