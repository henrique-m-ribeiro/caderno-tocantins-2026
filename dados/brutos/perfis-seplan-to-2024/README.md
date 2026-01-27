# Perfis Socioeconômicos Municipais SEPLAN-TO 2024

## Descrição

Este diretório contém os 139 Perfis Socioeconômicos Municipais da SEPLAN-TO (8ª Edição - Dezembro 2024).

## Fonte

- **Portal:** https://www.to.gov.br/seplan/perfil-socioeconomico-municipal/
- **Google Drive (compartilhado):** https://drive.google.com/drive/folders/1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F?usp=sharing
- **Edição:** 8ª edição
- **Data:** Dezembro 2024
- **Quantidade:** 139 PDFs (um por município)
- **Tamanho médio:** ~40 MB por PDF

## Estrutura dos PDFs

Cada perfil municipal contém 10 capítulos:
1. Aspectos Físicos
2. Demografia
3. Economia
4. Educação
5. Saúde
6. Saneamento Básico
7. Assistência Social
8. Meio Ambiente
9. Finanças Públicas
10. Serviços Urbanos e Equipamentos

## Como Baixar

### Opção A: Download Manual via Navegador

1. Acesse o link do Google Drive: https://drive.google.com/drive/folders/1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F?usp=sharing
2. Selecione todos os arquivos (Ctrl+A ou Cmd+A)
3. Clique com botão direito → "Download"
4. O navegador criará um arquivo ZIP com todos os PDFs
5. Extraia o ZIP neste diretório (`dados/brutos/perfis-seplan-to-2024/`)

### Opção B: Download via gdown (linha de comando)

```bash
# Instalar gdown
pip install gdown

# Baixar pasta inteira do Google Drive
gdown --folder https://drive.google.com/drive/folders/1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F -O dados/brutos/perfis-seplan-to-2024/
```

### Opção C: Script Python (será criado na Fase 3)

Um script `scripts/download_perfis_seplan_to.py` será desenvolvido para automatizar o download.

## Organização Esperada

Após o download, este diretório deve conter:
```
dados/brutos/perfis-seplan-to-2024/
├── README.md (este arquivo)
├── amostra/ (10-15 PDFs para análise de viabilidade - Fase 1)
├── [Município 1].pdf
├── [Município 2].pdf
├── ...
└── [Município 139].pdf
```

## Nomenclatura dos Arquivos

Os PDFs devem seguir o padrão:
- `Perfil_Socioeconomico_[Nome_Municipio]_2024.pdf`
- Exemplo: `Perfil_Socioeconomico_Palmas_2024.pdf`

Se a nomenclatura for diferente, documentar aqui o padrão encontrado.

## Status

- [ ] PDFs baixados (0/139)
- [ ] Amostra selecionada (0/10-15)
- [ ] Nomenclatura validada
- [ ] Integridade verificada (tamanho, legibilidade)

## Próximos Passos (Fase 1)

1. Baixar 10-15 PDFs de amostra estratificada
2. Analisar estrutura e variabilidade
3. Criar `RELATORIO_VARIABILIDADE_PDFS_SEPLAN.md`
4. Baixar os 139 PDFs completos
5. Validar integridade

---

**Última atualização:** 27 de janeiro de 2026
**Fase:** 0 (Preparação)
