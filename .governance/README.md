# Governança do Projeto

Esta pasta contém a documentação de governança do projeto Caderno Tocantins 2026, incluindo metodologias, prompts utilizados e avaliações de entregas.

## Estrutura

```
.governance/
├── prompts/          # Prompts utilizados nas análises
└── sessions/         # Avaliações e entregas de cada sessão
```

## Metodologia: IA Collab OS

O projeto utiliza a metodologia **IA Collab OS** (Inteligência Artificial Collaborative Operating System), que combina:

- **Colaboração Humano-IA**: Trabalho conjunto entre analistas e sistemas de IA
- **Iteração Incremental**: Desenvolvimento em versões (V1.0, V2.0, etc.)
- **Transparência Total**: Documentação de lacunas e limitações
- **Rastreabilidade Completa**: Registro de fontes e metodologias
- **Avaliação Sistemática**: Notas de qualidade (0-10) para cada entrega

## Princípios de Governança

### 1. Transparência
- Todas as lacunas de dados são explicitamente marcadas com `[LACUNA]`
- Limitações metodológicas são documentadas em cada ficha
- Fontes de dados são listadas com datas de acesso

### 2. Rastreabilidade
- Cada dado tem sua fonte identificada
- Prompts utilizados são versionados e armazenados
- Histórico de decisões é mantido

### 3. Qualidade
- Sistema de avaliação 0-10 para cada entrega
- Critérios objetivos de avaliação
- Revisão e refinamento contínuos

### 4. Versionamento
- Versão V1.0: Dados básicos disponíveis
- Versão V2.0: Dados complementares (IDEB, Saneamento, Agropecuária)
- Versões futuras: Refinamentos e atualizações

## Estrutura de Avaliação

Cada entrega é avaliada em:

1. **Completude** (0-3 pontos)
   - Cobertura de todos os tópicos solicitados
   - Profundidade da análise

2. **Qualidade dos Dados** (0-3 pontos)
   - Fontes oficiais utilizadas
   - Atualidade dos dados
   - Completude dos indicadores

3. **Análise e Insights** (0-2 pontos)
   - Profundidade analítica
   - Identificação de padrões e tendências
   - Insights estratégicos

4. **Transparência** (0-1 ponto)
   - Marcação clara de lacunas
   - Documentação de limitações

5. **Rastreabilidade** (0-1 ponto)
   - Referências completas
   - Links funcionais para fontes

**Total:** 10 pontos

## Prompts

A pasta `prompts/` contém os templates de prompts utilizados para análises regionais e municipais. Cada prompt é adaptado para:

- Características específicas da região
- Dados disponíveis
- Objetivos analíticos
- Lacunas identificadas

### Exemplo de Prompt

```markdown
PROMPT_ANALISE_[MICRORREGIAO].md
- Contexto da microrregião
- Dados disponíveis
- Perguntas orientadoras
- Formato esperado de resposta
- Critérios de qualidade
```

## Sessions (Entregas)

A pasta `sessions/` contém:

### Avaliações
- `AVALIACAO_ENTREGA_CLAUDE_[MICRORREGIAO].md`
- Nota atribuída (0-10)
- Pontos fortes identificados
- Áreas de melhoria
- Recomendações

### Entregas Finais
- `ENTREGA_FINAL_[MICRORREGIAO].md`
- Versão final aprovada
- Changelog de melhorias
- Status de conclusão

## Controle de Qualidade

### Checklist de Entrega

Antes de aprovar uma ficha regional, verificar:

- [ ] Todos os tópicos da estrutura foram cobertos
- [ ] Dados de fontes oficiais foram utilizados
- [ ] Lacunas estão marcadas com `[LACUNA]`
- [ ] Referências estão completas e com links
- [ ] Análises apresentam insights estratégicos
- [ ] Formatação está consistente
- [ ] Nota mínima de 8.0/10 foi atingida

## Histórico de Entregas

| Microrregião | Data | Versão | Nota | Status |
|--------------|------|--------|------|--------|
| Gurupi | Jan/2026 | V1.0 | 9.5/10 | ✅ Aprovada |
| Dianópolis | Jan/2026 | V1.0 | 9.2/10 | ✅ Aprovada |
| Jalapão | Jan/2026 | V1.0 | 9.5/10 | ✅ Aprovada |
| Rio Formoso | Jan/2026 | V1.0 | 9.8/10 | ✅ Aprovada |

## Contribuindo

Para propor melhorias na governança:
1. Documente a melhoria proposta
2. Justifique com base em experiências práticas
3. Sugira implementação incremental

---

**Última atualização:** 23 de janeiro de 2026
