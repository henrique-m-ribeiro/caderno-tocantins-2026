# Instruções para Download dos PDFs SEPLAN-TO

## Fase 1: Download da Amostra (10-15 PDFs)

### Objetivo
Baixar uma amostra estratificada de 10-15 PDFs para análise de viabilidade antes da extração em massa.

### Amostra Estratificada Recomendada

#### Municípios Grandes (3-4 PDFs) - Pop > 50.000

| Município | População 2022 | Região Planejamento | Código IBGE | Prioridade |
|-----------|----------------|---------------------|-------------|------------|
| Palmas | ~313.000 | Central | 1721000 | ⭐⭐⭐ Capital |
| Araguaína | ~180.000 | Norte | 1702109 | ⭐⭐⭐ |
| Gurupi | ~87.000 | Sul | 1709500 | ⭐⭐ |
| Porto Nacional | ~53.000 | Central | 1718204 | ⭐⭐ |

#### Municípios Médios (4-5 PDFs) - Pop 10.000-50.000

Selecionar 4-5 municípios representando diferentes regiões:

| Município | População (aprox.) | Região Planejamento | Código IBGE |
|-----------|-------------------|---------------------|-------------|
| Paraíso do Tocantins | ~50.000 | Central | 1716109 |
| Colinas do Tocantins | ~32.000 | Bico do Papagaio | 1705508 |
| Guaraí | ~24.000 | Meio Norte | 1709302 |
| Miracema do Tocantins | ~21.000 | Meio Norte | 1713205 |
| Formoso do Araguaia | ~18.000 | Vale do Araguaia | 1708205 |

#### Municípios Pequenos (3-4 PDFs) - Pop < 10.000

Incluir o menor município e representantes de diferentes regiões:

| Município | População (aprox.) | Região Planejamento | Código IBGE |
|-----------|-------------------|---------------------|-------------|
| Oliveira de Fátima | ~1.100 | Central | 1715507 |
| Lagoa do Tocantins | ~3.500 | Jalapão | 1711951 |
| Santa Tereza do Tocantins | ~2.500 | Bico do Papagaio | 1719004 |
| Chapada da Natividade | ~3.000 | Sudeste | 1705102 |

### Passos para Download da Amostra

#### Opção A: Download Manual via Google Drive (Recomendado)

1. **Acesse o Google Drive compartilhado:**
   https://drive.google.com/drive/folders/1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F?usp=sharing

2. **Identifique os PDFs da amostra** (10-15 municípios listados acima)

3. **Baixe os arquivos:**
   - Selecione cada arquivo da amostra (Ctrl+Click ou Cmd+Click)
   - Clique com botão direito → "Download"
   - Ou clique em cada arquivo individualmente

4. **Salve no diretório correto:**
   ```bash
   # Mover PDFs baixados para:
   /home/user/caderno-tocantins-2026/dados/brutos/perfis-seplan-to-2024/amostra/
   ```

5. **Verifique a integridade:**
   ```bash
   cd dados/brutos/perfis-seplan-to-2024/amostra/
   ls -lh  # Verificar tamanho dos arquivos (~40MB cada)
   ```

#### Opção B: Download via gdown (Linha de Comando)

```bash
# Instalar gdown se necessário
pip install gdown

# Baixar arquivos específicos
# Nota: Requer IDs individuais dos arquivos no Drive
gdown [FILE_ID] -O dados/brutos/perfis-seplan-to-2024/amostra/
```

### Checklist da Fase 1

Após download da amostra:
- [ ] 10-15 PDFs baixados
- [ ] Arquivos salvos em `dados/brutos/perfis-seplan-to-2024/amostra/`
- [ ] Tamanho dos arquivos verificado (~40MB cada)
- [ ] PDFs abrem corretamente
- [ ] Nomes dos arquivos documentados

---

## Fase 4: Download Completo (139 PDFs)

### Timing
Executar APÓS análise de viabilidade (Fase 1) e desenvolvimento da infraestrutura (Fase 3).

### Passos para Download Completo

#### Opção A: Download Manual via Navegador (Simples)

1. **Acesse o Google Drive:**
   https://drive.google.com/drive/folders/1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F?usp=sharing

2. **Selecione todos os arquivos:**
   - Ctrl+A (Windows/Linux) ou Cmd+A (Mac)

3. **Download em massa:**
   - Clique com botão direito → "Download"
   - O navegador criará um arquivo ZIP com todos os PDFs
   - Tamanho total esperado: ~5.5 GB

4. **Extraia o ZIP:**
   ```bash
   # Navegar até o diretório correto
   cd /home/user/caderno-tocantins-2026/dados/brutos/perfis-seplan-to-2024/

   # Extrair ZIP baixado
   unzip ~/Downloads/perfis-seplan-to-2024.zip

   # Ou se o navegador já extraiu, mover arquivos
   mv ~/Downloads/perfis-seplan-to-2024/*.pdf .
   ```

5. **Verificar integridade:**
   ```bash
   # Contar arquivos
   ls *.pdf | wc -l  # Deve retornar 139

   # Verificar tamanho total
   du -sh .  # Deve ser ~5.5 GB

   # Listar arquivos com tamanho
   ls -lh *.pdf | head -20
   ```

#### Opção B: Script Python (Será desenvolvido na Fase 3)

Um script `scripts/download_perfis_seplan_to.py` será criado para automatizar:
- Autenticação no Google Drive
- Download de todos os 139 PDFs
- Verificação de integridade
- Retry em caso de falhas
- Barra de progresso

```python
# Uso futuro (Fase 3):
python scripts/download_perfis_seplan_to.py \
    --source google-drive \
    --folder-id 1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F \
    --output dados/brutos/perfis-seplan-to-2024/
```

### Validação Pós-Download

Após baixar os 139 PDFs, executar:

```bash
# Script de validação (será criado)
python scripts/validar_integridade_pdfs.py
```

Verificações:
- [ ] 139 arquivos PDF presentes
- [ ] Nenhum arquivo corrompido
- [ ] Tamanho médio ~40MB
- [ ] PDFs abrem corretamente
- [ ] Todos os municípios cobertos
- [ ] Nomenclatura documentada

---

## Alternativa: URLs Diretas (Se Disponíveis)

Se os PDFs estiverem disponíveis em URLs diretas da SEPLAN-TO:

```bash
# Exemplo de download direto (ajustar conforme estrutura real)
wget https://central.to.gov.br/download/[ID] -O dados/brutos/perfis-seplan-to-2024/[Municipio].pdf
```

**Nota:** Nos testes anteriores, URLs diretas retornaram erro 403 (autenticação necessária). Por isso, o Google Drive é a fonte recomendada.

---

## Troubleshooting

### Problema: Download muito lento
**Solução:**
- Dividir download em lotes menores (30-40 PDFs por vez)
- Usar download noturno
- Verificar conexão de internet

### Problema: Arquivo ZIP corrompido
**Solução:**
- Re-baixar os arquivos
- Desabilitar extensões do navegador
- Tentar navegador diferente (Chrome, Firefox)

### Problema: Espaço em disco insuficiente
**Solução:**
- Verificar espaço disponível: `df -h`
- Liberar espaço: remover arquivos temporários
- Espaço necessário: ~6 GB total

### Problema: PDFs não abrem
**Solução:**
- Verificar integridade com: `file *.pdf`
- Instalar visualizador de PDF se necessário
- Re-baixar arquivos corrompidos

---

## Recursos

- **Google Drive:** https://drive.google.com/drive/folders/1BOS0LW8GEiwAPdAA3UlW_m6KpzRaG7-F?usp=sharing
- **Portal SEPLAN-TO:** https://www.to.gov.br/seplan/perfil-socioeconomico-municipal/
- **Suporte:** Henrique M. Ribeiro

---

**Última atualização:** 27 de janeiro de 2026
**Fase:** 0 (Preparação)
**Status:** Documentação completa - Pronto para execução
