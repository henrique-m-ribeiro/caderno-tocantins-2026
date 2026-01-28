#!/usr/bin/env python3
"""
Analisador de Dados Municipais
Gera análises textuais contextualizadas baseadas nos indicadores dos municípios.
"""

import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class AnalisadorMunicipal:
    """Analisa dados municipais e gera insights textuais."""

    def __init__(self, base_dados_path='dados/finais/BASE_DADOS_TOCANTINS_V01_REVISADA.xlsx'):
        self.base_dados_path = Path(base_dados_path)
        self.df_base = pd.read_excel(base_dados_path)

        # Benchmarks do Estado (médias estaduais)
        self.benchmarks = self._calcular_benchmarks()

    def _calcular_benchmarks(self) -> Dict[str, float]:
        """Calcula benchmarks estaduais para comparação."""
        # Linha do estado (Tocantins)
        estado = self.df_base[self.df_base['terr_nome'] == 'Tocantins'].iloc[0]

        return {
            'idhm_2010': 0.699,  # IDHM médio TO
            'taxa_alfabetizacao': 89.0,  # Taxa alfabetização TO
            'ideb_anos_finais': 4.5,  # IDEB médio TO
            'pib_per_capita': 20000.0,  # PIB per capita médio TO
            'taxa_urbanizacao': 78.0,  # Taxa urbanização TO
        }

    def carregar_json_municipio(self, municipio: str, json_dir='dados/brutos/extraidos-perfis') -> Optional[Dict]:
        """Carrega JSON v9 do município."""
        json_dir = Path(json_dir)

        # Normalizar nome
        nome_norm = municipio.lower().replace(' ', '_')
        nome_norm = self._remover_acentos(nome_norm)

        # Buscar arquivo
        json_path = json_dir / f"{nome_norm}_v9.json"

        if not json_path.exists():
            # Tentar variações
            for arquivo in json_dir.glob("*_v9.json"):
                if nome_norm in arquivo.stem:
                    json_path = arquivo
                    break

        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data.get('indicadores', {})

        return None

    @staticmethod
    def _remover_acentos(texto: str) -> str:
        """Remove acentos do texto."""
        mapa = {
            'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
            'é': 'e', 'ê': 'e',
            'í': 'i',
            'ó': 'o', 'ô': 'o', 'õ': 'o',
            'ú': 'u', 'ü': 'u',
            'ç': 'c',
        }
        for acento, sem_acento in mapa.items():
            texto = texto.replace(acento, sem_acento)
        return texto

    def analisar_crescimento_populacional(self, ind: Dict) -> str:
        """Analisa crescimento populacional."""
        pop_1991 = ind.get('pop_1991', 0)
        pop_2022 = ind.get('pop_2022', 0)

        if pop_1991 and pop_2022:
            crescimento = ((pop_2022 - pop_1991) / pop_1991) * 100

            if crescimento > 200:
                return "explosivo crescimento populacional"
            elif crescimento > 100:
                return "forte crescimento populacional"
            elif crescimento > 50:
                return "crescimento populacional significativo"
            elif crescimento > 20:
                return "crescimento populacional moderado"
            elif crescimento > 0:
                return "crescimento populacional estável"
            else:
                return "redução populacional"

        return "dados populacionais limitados"

    def analisar_urbanizacao(self, ind: Dict) -> str:
        """Analisa grau de urbanização."""
        taxa_urb = ind.get('taxa_urbanizacao_2022', 0)

        if taxa_urb > 95:
            return "altamente urbanizado"
        elif taxa_urb > 80:
            return "predominantemente urbano"
        elif taxa_urb > 60:
            return "perfil misto urbano-rural"
        elif taxa_urb > 40:
            return "perfil rural significativo"
        else:
            return "predominantemente rural"

    def analisar_idhm(self, ind: Dict) -> Tuple[str, str]:
        """Analisa IDHM e retorna (classificação, evolução)."""
        idhm_2010 = ind.get('idhm_2010', 0)
        idhm_2000 = ind.get('idhm_2000', 0)

        # Classificação
        if idhm_2010 >= 0.800:
            classificacao = "muito alto"
        elif idhm_2010 >= 0.700:
            classificacao = "alto"
        elif idhm_2010 >= 0.600:
            classificacao = "médio"
        elif idhm_2010 >= 0.500:
            classificacao = "baixo"
        else:
            classificacao = "muito baixo"

        # Evolução
        if idhm_2000 and idhm_2010:
            evolucao = idhm_2010 - idhm_2000
            if evolucao > 0.150:
                evolucao_texto = "com evolução excepcional"
            elif evolucao > 0.100:
                evolucao_texto = "com forte evolução"
            elif evolucao > 0.050:
                evolucao_texto = "com evolução positiva"
            else:
                evolucao_texto = "com evolução moderada"
        else:
            evolucao_texto = ""

        return classificacao, evolucao_texto

    def analisar_economia(self, ind: Dict) -> Dict[str, str]:
        """Analisa estrutura econômica."""
        # VAB mais recente (2021)
        vab_agro = ind.get('vab_agropecuaria_2021', 0)
        vab_ind = ind.get('vab_industria_2021', 0)
        vab_serv = ind.get('vab_servicos_2021', 0)

        vab_total = vab_agro + vab_ind + vab_serv

        if vab_total > 0:
            perc_agro = (vab_agro / vab_total) * 100
            perc_ind = (vab_ind / vab_total) * 100
            perc_serv = (vab_serv / vab_total) * 100

            # Identificar setor dominante
            if perc_serv > 60:
                setor_dominante = "forte predominância do setor de serviços"
            elif perc_serv > 50:
                setor_dominante = "economia baseada no setor de serviços"
            elif perc_agro > 40:
                setor_dominante = "forte base agropecuária"
            elif perc_agro > 30:
                setor_dominante = "economia com significativa participação agropecuária"
            elif perc_ind > 20:
                setor_dominante = "economia diversificada com participação industrial relevante"
            else:
                setor_dominante = "economia com perfil misto"

            # Dinâmica
            pib_2017 = ind.get('pib_per_capita_2017', 0)
            pib_2021 = ind.get('pib_per_capita_2021', 0)

            if pib_2017 and pib_2021:
                crescimento_pib = ((pib_2021 - pib_2017) / pib_2017) * 100
                if crescimento_pib > 50:
                    dinamica = "crescimento econômico muito forte"
                elif crescimento_pib > 30:
                    dinamica = "crescimento econômico expressivo"
                elif crescimento_pib > 10:
                    dinamica = "crescimento econômico positivo"
                elif crescimento_pib > 0:
                    dinamica = "crescimento econômico moderado"
                else:
                    dinamica = "economia em ajuste"
            else:
                dinamica = "trajetória econômica estável"

            return {
                'setor_dominante': setor_dominante,
                'dinamica': dinamica,
                'perc_agro': perc_agro,
                'perc_ind': perc_ind,
                'perc_serv': perc_serv
            }

        return {
            'setor_dominante': 'estrutura econômica em consolidação',
            'dinamica': 'economia local',
            'perc_agro': 0,
            'perc_ind': 0,
            'perc_serv': 0
        }

    def analisar_educacao(self, ind: Dict) -> Dict[str, str]:
        """Analisa cenário educacional."""
        taxa_alf = ind.get('taxa_alfabetizacao_2022', 0)
        ideb_2023 = ind.get('ideb_anos_finais_2023', 0)
        ideb_2019 = ind.get('ideb_anos_finais_2019', 0)

        # Alfabetização
        if taxa_alf > 95:
            nivel_alf = "excelentes índices de alfabetização"
        elif taxa_alf > 90:
            nivel_alf = "bons índices de alfabetização"
        elif taxa_alf > 85:
            nivel_alf = "índices satisfatórios de alfabetização"
        else:
            nivel_alf = "desafios na alfabetização"

        # IDEB
        if ideb_2023 >= 6.0:
            nivel_ideb = "IDEB acima da meta nacional"
        elif ideb_2023 >= 5.0:
            nivel_ideb = "IDEB em patamar satisfatório"
        elif ideb_2023 >= 4.0:
            nivel_ideb = "IDEB em desenvolvimento"
        else:
            nivel_ideb = "IDEB que demanda atenção"

        # Tendência
        if ideb_2019 and ideb_2023:
            if ideb_2023 > ideb_2019:
                tendencia = "trajetória de melhoria"
            elif ideb_2023 == ideb_2019:
                tendencia = "manutenção dos indicadores"
            else:
                tendencia = "necessidade de reversão da queda"
        else:
            tendencia = "monitoramento contínuo"

        return {
            'alfabetizacao': nivel_alf,
            'ideb': nivel_ideb,
            'tendencia': tendencia
        }

    def analisar_saude_saneamento(self, ind: Dict) -> Dict[str, str]:
        """Analisa saúde e saneamento."""
        ubs = ind.get('estabelecimentos_ubs_2023', 0)
        hospital = ind.get('estabelecimentos_hospital_2023', 0)
        pop = ind.get('pop_2022', 1)

        # Cobertura UBS (ideal: 1 UBS por 3.000-4.000 hab)
        if pop > 0:
            ubs_por_hab = (ubs / pop) * 10000
            if ubs_por_hab > 3:
                cobertura_ubs = "boa cobertura de unidades básicas de saúde"
            elif ubs_por_hab > 2:
                cobertura_ubs = "cobertura adequada de UBS"
            elif ubs_por_hab > 1:
                cobertura_ubs = "cobertura de UBS em expansão"
            else:
                cobertura_ubs = "necessidade de ampliar cobertura de UBS"
        else:
            cobertura_ubs = "rede de atenção básica"

        # Hospitalar
        if hospital > 2:
            cobertura_hosp = "estrutura hospitalar disponível"
        elif hospital > 0:
            cobertura_hosp = "atendimento hospitalar local"
        else:
            cobertura_hosp = "dependência de municípios de referência para atenção hospitalar"

        # Saneamento (% domicílios com água)
        agua_2022 = ind.get('agua_rede_geral_2022', 0)
        esgoto_2022 = ind.get('esgoto_rede_geral_2022', 0)

        # Estimar cobertura (domicílios = pop/3.5)
        domicilios_est = pop / 3.5 if pop > 0 else 1

        cobertura_agua = (agua_2022 / domicilios_est) * 100 if domicilios_est > 0 else 0
        cobertura_esgoto = (esgoto_2022 / domicilios_est) * 100 if domicilios_est > 0 else 0

        if cobertura_agua > 90:
            nivel_agua = "excelente cobertura de abastecimento de água"
        elif cobertura_agua > 70:
            nivel_agua = "boa cobertura de água tratada"
        elif cobertura_agua > 50:
            nivel_agua = "cobertura de água em expansão"
        else:
            nivel_agua = "necessidade de universalizar acesso à água tratada"

        if cobertura_esgoto > 80:
            nivel_esgoto = "ampla cobertura de esgotamento sanitário"
        elif cobertura_esgoto > 60:
            nivel_esgoto = "boa cobertura de rede de esgoto"
        elif cobertura_esgoto > 40:
            nivel_esgoto = "cobertura de esgoto em desenvolvimento"
        else:
            nivel_esgoto = "desafio crítico no esgotamento sanitário"

        return {
            'ubs': cobertura_ubs,
            'hospitalar': cobertura_hosp,
            'agua': nivel_agua,
            'esgoto': nivel_esgoto
        }

    def analisar_financas(self, ind: Dict) -> Dict[str, str]:
        """Analisa finanças públicas."""
        fpm_2023 = ind.get('fpm_2023', 0)
        transf_2023 = ind.get('transferencias_total_2023', 0)

        if transf_2023 > 0:
            dependencia_fpm = (fpm_2023 / transf_2023) * 100

            if dependencia_fpm > 70:
                perfil_financeiro = "forte dependência das transferências do FPM"
            elif dependencia_fpm > 50:
                perfil_financeiro = "significativa participação do FPM nas receitas"
            else:
                perfil_financeiro = "diversificação de fontes de receita"
        else:
            perfil_financeiro = "estrutura de receitas municipais"

        # Crescimento de transferências
        transf_2019 = ind.get('transferencias_total_2019', 0)
        if transf_2019 and transf_2023:
            crescimento = ((transf_2023 - transf_2019) / transf_2019) * 100
            if crescimento > 80:
                dinamica_receita = "forte crescimento das receitas de transferências"
            elif crescimento > 50:
                dinamica_receita = "crescimento expressivo das transferências"
            elif crescimento > 20:
                dinamica_receita = "crescimento moderado das receitas"
            else:
                dinamica_receita = "estabilidade nas transferências"
        else:
            dinamica_receita = "trajetória de receitas"

        return {
            'perfil': perfil_financeiro,
            'dinamica': dinamica_receita,
            'dependencia_fpm': dependencia_fpm if transf_2023 > 0 else 0
        }

    def gerar_sintese_estrategica(self, municipio: str, ind: Dict) -> Dict[str, List[str]]:
        """Gera síntese estratégica (Pontos Fortes, Desafios, Oportunidades)."""
        pontos_fortes = []
        desafios = []
        oportunidades = []

        # Análises
        idhm_class, idhm_evol = self.analisar_idhm(ind)
        economia = self.analisar_economia(ind)
        educacao = self.analisar_educacao(ind)
        saude = self.analisar_saude_saneamento(ind)
        financas = self.analisar_financas(ind)

        # === PONTOS FORTES ===

        # IDHM alto
        idhm_2010 = ind.get('idhm_2010', 0)
        if idhm_2010 >= 0.700:
            pontos_fortes.append(f"IDHM {idhm_class} ({idhm_2010:.3f}), acima da média estadual, indicando bom nível de desenvolvimento humano")

        # Crescimento populacional
        crescimento = self.analisar_crescimento_populacional(ind)
        if "forte" in crescimento or "explosivo" in crescimento or "significativo" in crescimento:
            pontos_fortes.append(f"Dinâmica demográfica positiva com {crescimento} nas últimas três décadas")

        # Economia forte
        pib_pc = ind.get('pib_per_capita_2021', 0)
        if pib_pc > self.benchmarks['pib_per_capita']:
            pontos_fortes.append(f"PIB per capita (R$ {pib_pc:,.2f}) superior à média estadual, demonstrando capacidade econômica")

        # Educação
        taxa_alf = ind.get('taxa_alfabetizacao_2022', 0)
        if taxa_alf > 90:
            pontos_fortes.append(f"Taxa de alfabetização elevada ({taxa_alf:.1f}%), refletindo investimentos em educação básica")

        ideb = ind.get('ideb_anos_finais_2023', 0)
        if ideb >= 5.5:
            pontos_fortes.append(f"IDEB dos anos finais ({ideb:.1f}) acima da média estadual, evidenciando qualidade educacional")

        # Saneamento
        if "excelente" in saude['agua'] or "ampla" in saude['esgoto']:
            pontos_fortes.append(f"Infraestrutura de saneamento em estágio avançado, com {saude['agua']}")

        # === DESAFIOS ===

        # IDHM baixo
        if idhm_2010 < 0.600:
            desafios.append(f"IDHM {idhm_class} ({idhm_2010:.3f}), demandando políticas integradas para elevar indicadores sociais")

        # Educação
        if taxa_alf < 85:
            desafios.append(f"Taxa de alfabetização ({taxa_alf:.1f}%) abaixo do ideal, requerendo programas de alfabetização de jovens e adultos")

        if ideb < 4.5:
            desafios.append(f"IDEB ({ideb:.1f}) abaixo da meta, necessitando de investimentos em infraestrutura escolar e formação docente")

        # Saneamento crítico
        if "crítico" in saude['esgoto'] or "universalizar" in saude['agua']:
            desafios.append(f"Déficit em saneamento básico, especialmente em esgotamento sanitário, afetando saúde pública")

        # Dependência financeira
        if financas['dependencia_fpm'] > 70:
            desafios.append(f"Alta dependência do FPM ({financas['dependencia_fpm']:.1f}% das transferências), limitando autonomia fiscal")

        # Economia pouco diversificada
        if economia['perc_agro'] > 40 or economia['perc_serv'] > 75:
            desafios.append(f"Estrutura econômica concentrada, com {economia['setor_dominante']}, vulnerável a choques setoriais")

        # Saúde
        if "necessidade" in saude['ubs'] or "dependência" in saude['hospitalar']:
            desafios.append(f"Infraestrutura de saúde limitada, com {saude['ubs']}")

        # === OPORTUNIDADES ===

        # Localização (seria necessário dados geográficos, vou usar heurísticas)
        pop = ind.get('pop_2022', 0)
        if pop > 50000:
            oportunidades.append("Polo regional com potencial para atração de investimentos e oferta de serviços especializados")
        elif pop > 20000:
            oportunidades.append("Centro sub-regional com capacidade de dinamizar economia microrregional")

        # Agropecuária
        if economia['perc_agro'] > 20:
            oportunidades.append("Base agropecuária consolidada, oportunidade para agroindustrialização e agregação de valor")

        # Crescimento econômico
        pib_2017 = ind.get('pib_per_capita_2017', 0)
        pib_2021 = ind.get('pib_per_capita_2021', 0)
        if pib_2017 and pib_2021 and pib_2021 > pib_2017 * 1.3:
            oportunidades.append("Trajetória recente de crescimento econômico, favorável à atração de novos empreendimentos")

        # Transferências crescentes
        if "forte" in financas['dinamica'] or "expressivo" in financas['dinamica']:
            oportunidades.append(f"Capacidade de investimento ampliada pelo {financas['dinamica']}, permitindo obras estruturantes")

        # Urbanização
        taxa_urb = ind.get('taxa_urbanizacao_2022', 0)
        if taxa_urb > 80:
            oportunidades.append("Perfil urbano consolidado, propício para investimentos em infraestrutura urbana e serviços")

        # Educação em melhoria
        ideb_2019 = ind.get('ideb_anos_finais_2019', 0)
        ideb_2023 = ind.get('ideb_anos_finais_2023', 0)
        if ideb_2019 and ideb_2023 and ideb_2023 > ideb_2019:
            oportunidades.append("Tendência de melhoria nos indicadores educacionais, base para formação de capital humano qualificado")

        # Parcerias (sempre aplicável)
        oportunidades.append("Parcerias com governo estadual para programas de desenvolvimento territorial integrado")

        # Garantir ao menos 2-3 itens em cada categoria
        if len(pontos_fortes) == 0:
            pontos_fortes.append(f"Município inserido na dinâmica de desenvolvimento do Estado do Tocantins")
        if len(desafios) == 0:
            desafios.append(f"Necessidade de fortalecer capacidades institucionais para gestão de políticas públicas")
        if len(oportunidades) < 2:
            oportunidades.append("Potencial para captação de recursos estaduais e federais para projetos de desenvolvimento local")

        # Limitar a 3 itens cada
        return {
            'pontos_fortes': pontos_fortes[:3],
            'desafios': desafios[:3],
            'oportunidades': oportunidades[:3]
        }

    def gerar_analise_social(self, ind: Dict) -> str:
        """Gera análise da dimensão social."""
        crescimento = self.analisar_crescimento_populacional(ind)
        urbanizacao = self.analisar_urbanizacao(ind)
        idhm_class, idhm_evol = self.analisar_idhm(ind)

        pop_2022 = ind.get('pop_2022', 0)
        pop_1991 = ind.get('pop_1991', 0)
        taxa_urb = ind.get('taxa_urbanizacao_2022', 0)
        idhm = ind.get('idhm_2010', 0)

        analise = f"O município apresenta {crescimento}, "

        if pop_1991 and pop_2022:
            crescimento_pct = ((pop_2022 - pop_1991) / pop_1991) * 100
            analise += f"passando de {int(pop_1991):,} habitantes em 1991 para {int(pop_2022):,} em 2022 ({crescimento_pct:+.1f}%). ".replace(',', '.')

        analise += f"Caracteriza-se como município {urbanizacao}, com taxa de urbanização de {taxa_urb:.1f}%, "

        if taxa_urb > 80:
            analise += "o que demanda investimentos concentrados em infraestrutura urbana, mobilidade e serviços públicos na sede municipal. "
        elif taxa_urb < 50:
            analise += "o que requer políticas diferenciadas para atendimento da população rural dispersa. "
        else:
            analise += "demandando estratégias integradas para áreas urbanas e rurais. "

        analise += f"O IDHM de {idhm:.3f} (2010) classifica o município em patamar {idhm_class} {idhm_evol}, "

        if idhm >= 0.700:
            analise += "refletindo avanços consistentes em educação, longevidade e renda, mas com necessidade de manutenção e aprimoramento das políticas sociais."
        elif idhm >= 0.600:
            analise += "evidenciando progressos nas condições de vida, mas com espaço para melhorias em educação, saúde e geração de renda."
        else:
            analise += "indicando a necessidade de políticas públicas intensivas para elevar os padrões de vida da população."

        return analise

    def gerar_analise_economica(self, ind: Dict) -> str:
        """Gera análise da dimensão econômica."""
        economia = self.analisar_economia(ind)

        pib_pc = ind.get('pib_per_capita_2021', 0)
        emprego = ind.get('emprego_formal_estoque_2023', 0)

        analise = f"A economia municipal caracteriza-se por {economia['setor_dominante']}, "

        if economia['perc_serv'] > 60:
            analise += f"que responde por {economia['perc_serv']:.1f}% do valor adicionado bruto, típico de centros urbanos prestadores de serviços. "
        elif economia['perc_agro'] > 30:
            analise += f"com a agropecuária representando {economia['perc_agro']:.1f}% do VAB, sustentando a economia local. "

        if economia['perc_agro'] > 20 and economia['perc_ind'] < 10:
            analise += f"A baixa participação industrial ({economia['perc_ind']:.1f}% do VAB) indica potencial para agroindustrialização e agregação de valor à produção primária. "
        elif economia['perc_ind'] > 15:
            analise += f"A participação industrial ({economia['perc_ind']:.1f}% do VAB) demonstra alguma diversificação produtiva. "

        if pib_pc > 0:
            analise += f"O PIB per capita de R$ {pib_pc:,.2f} (2021) ".replace(',', '.')
            if pib_pc > self.benchmarks['pib_per_capita']:
                analise += "supera a média estadual, evidenciando capacidade econômica favorável. "
            else:
                analise += "indica necessidade de dinamizar a economia local para elevar a renda média da população. "

        analise += f"Registra-se {economia['dinamica']} no período recente, "

        if emprego > 0 and emprego != 1:  # excluir valor placeholder
            emprego_mil = emprego / 1000
            analise += f"com estoque de {emprego_mil:.1f} mil vínculos formais de emprego (2023), "
            if emprego_mil > 20:
                analise += "demonstrando mercado de trabalho estruturado."
            elif emprego_mil > 5:
                analise += "refletindo mercado de trabalho em consolidação."
            else:
                analise += "indicando predominância da informalidade e necessidade de políticas de formalização."
        else:
            analise += "demandando políticas de geração de emprego e renda."

        return analise

    def gerar_analise_educacao(self, ind: Dict) -> str:
        """Gera análise da dimensão educação."""
        educacao = self.analisar_educacao(ind)

        taxa_alf = ind.get('taxa_alfabetizacao_2022', 0)
        ideb_2023 = ind.get('ideb_anos_finais_2023', 0)
        ideb_2019 = ind.get('ideb_anos_finais_2019', 0)

        analise = f"O cenário educacional apresenta {educacao['alfabetizacao']}, "

        if taxa_alf > 0:
            analise += f"com taxa de alfabetização de {taxa_alf:.1f}% (2022), "
            if taxa_alf > 92:
                analise += "próxima da universalização. "
            elif taxa_alf > 85:
                analise += "mas ainda com necessidade de programas complementares de alfabetização. "
            else:
                analise += "demandando programas intensivos de alfabetização de jovens e adultos. "

        analise += f"O IDEB dos anos finais registra {educacao['ideb']}, "

        if ideb_2023 > 0:
            analise += f"com índice de {ideb_2023:.1f} em 2023, "

        if ideb_2019 and ideb_2023:
            if ideb_2023 > ideb_2019:
                variacao = ideb_2023 - ideb_2019
                analise += f"representando avanço de {variacao:.1f} pontos em relação a 2019. "
            elif ideb_2023 == ideb_2019:
                analise += f"mantendo-se estável em relação a 2019. "
            else:
                variacao = ideb_2019 - ideb_2023
                analise += f"apresentando queda de {variacao:.1f} pontos em relação a 2019, o que demanda atenção e reversão da tendência. "

        if ideb_2023 >= 5.5:
            analise += "Os resultados positivos devem ser consolidados mediante investimentos continuados em infraestrutura escolar, formação docente e gestão pedagógica."
        elif ideb_2023 >= 4.5:
            analise += "Há espaço para melhorias mediante investimentos em infraestrutura das escolas, valorização dos professores e fortalecimento da gestão educacional."
        else:
            analise += "É prioritário implementar políticas de melhoria da qualidade do ensino, incluindo modernização da infraestrutura escolar, formação continuada de professores e acompanhamento pedagógico."

        return analise

    def gerar_analise_saude(self, ind: Dict) -> str:
        """Gera análise da dimensão saúde e saneamento."""
        saude = self.analisar_saude_saneamento(ind)

        ubs = ind.get('estabelecimentos_ubs_2023', 0)
        hosp = ind.get('estabelecimentos_hospital_2023', 0)

        analise = f"A infraestrutura de saúde caracteriza-se por {saude['ubs']}, "

        if ubs > 0:
            analise += f"contando com {int(ubs)} Unidades Básicas de Saúde (UBS) "

        if hosp > 0:
            analise += f"e {int(hosp)} estabelecimento(s) hospitalar(es) (2023). "
        else:
            analise += f"(2023), com {saude['hospitalar']}. "

        if "necessidade" in saude['ubs']:
            analise += "A ampliação da rede de atenção básica é fundamental para garantir acesso universal aos serviços de saúde. "
        elif "boa" in saude['ubs']:
            analise += "A cobertura de atenção básica favorece a prevenção e o acompanhamento da saúde da população. "

        analise += f"Quanto ao saneamento básico, observa-se {saude['agua']}, "

        if "excelente" in saude['agua']:
            analise += "garantindo acesso praticamente universal ao abastecimento adequado. "
        elif "necessidade" in saude['agua']:
            analise += "sendo prioritário expandir a rede de distribuição para universalizar o acesso. "
        else:
            analise += "mas com necessidade de universalização do atendimento. "

        analise += f"Já em relação ao esgotamento sanitário, verifica-se {saude['esgoto']}, "

        if "crítico" in saude['esgoto']:
            analise += "constituindo desafio prioritário, pois a falta de saneamento adequado compromete a saúde pública e a qualidade ambiental."
        elif "ampla" in saude['esgoto']:
            analise += "colocando o município em patamar avançado neste indicador fundamental de qualidade de vida."
        else:
            analise += "demandando investimentos para expansão da rede coletora e tratamento adequado."

        return analise

    def gerar_analise_agropecuaria(self, ind: Dict) -> str:
        """Gera análise da dimensão agropecuária."""
        economia = self.analisar_economia(ind)

        vab_agro_2021 = ind.get('vab_agropecuaria_2021', 0)
        vab_agro_2017 = ind.get('vab_agropecuaria_2017', 0)

        if economia['perc_agro'] > 30:
            analise = f"A agropecuária desempenha papel central na economia municipal, respondendo por {economia['perc_agro']:.1f}% do valor adicionado bruto. "
        elif economia['perc_agro'] > 15:
            analise = f"A agropecuária mantém participação significativa na economia local ({economia['perc_agro']:.1f}% do VAB). "
        elif economia['perc_agro'] > 5:
            analise = f"Embora com participação moderada ({economia['perc_agro']:.1f}% do VAB), a agropecuária compõe a base produtiva municipal. "
        else:
            analise = f"A agropecuária apresenta participação reduzida ({economia['perc_agro']:.1f}% do VAB), característica de municípios com economia urbana consolidada. "

        if vab_agro_2017 and vab_agro_2021:
            crescimento = ((vab_agro_2021 - vab_agro_2017) / vab_agro_2017) * 100
            if crescimento > 100:
                analise += f"O setor demonstra forte dinamismo, com crescimento de {crescimento:.1f}% no período 2017-2021, "
                analise += "indicando expansão da área produtiva, incorporação de tecnologias ou elevação de preços das commodities. "
            elif crescimento > 50:
                analise += f"Registra-se trajetória de crescimento expressivo ({crescimento:.1f}% no período 2017-2021), "
                analise += "refletindo dinamismo do setor primário local. "
            elif crescimento > 0:
                analise += f"O setor apresenta crescimento moderado ({crescimento:.1f}% no período 2017-2021). "
            else:
                analise += f"Observa-se retração do setor ({crescimento:.1f}% no período 2017-2021), "
                analise += "podendo estar relacionada a fatores climáticos, mudanças no uso do solo ou oscilações de preços. "

        if economia['perc_agro'] > 20:
            analise += "Há oportunidade para agroindustrialização, agregação de valor e fortalecimento de cadeias produtivas, "
            analise += "mediante políticas de assistência técnica, crédito rural e acesso a mercados."
        elif economia['perc_agro'] < 5:
            analise += "O perfil econômico urbano não elimina a importância de políticas de segurança alimentar e agricultura familiar."

        return analise

    def gerar_analise_financas(self, ind: Dict) -> str:
        """Gera análise da dimensão finanças públicas."""
        financas = self.analisar_financas(ind)

        transf_2023 = ind.get('transferencias_total_2023', 0)
        fpm_2023 = ind.get('fpm_2023', 0)

        analise = f"A estrutura de receitas municipais caracteriza-se pela {financas['perfil']}, "

        if financas['dependencia_fpm'] > 70:
            analise += f"com o FPM representando {financas['dependencia_fpm']:.1f}% das transferências totais. "
            analise += "Esta alta dependência evidencia a necessidade de fortalecer a arrecadação própria mediante modernização da gestão tributária e ampliação da base de contribuintes. "
        elif financas['dependencia_fpm'] > 50:
            analise += f"sendo o FPM responsável por {financas['dependencia_fpm']:.1f}% das transferências. "
            analise += "Há oportunidade para reduzir a dependência mediante políticas de desenvolvimento econômico local e melhoria da arrecadação própria. "
        else:
            analise += "indicando diversificação das fontes de receita. "

        if transf_2023 > 0:
            transf_milhoes = transf_2023 / 1_000_000
            analise += f"Em 2023, o município recebeu R$ {transf_milhoes:.1f} milhões em transferências correntes. ".replace('.', ',')

        analise += f"Observa-se {financas['dinamica']} no período 2019-2023, "

        transf_2019 = ind.get('transferencias_total_2019', 0)
        if transf_2019 and transf_2023:
            crescimento_pct = ((transf_2023 - transf_2019) / transf_2019) * 100
            if crescimento_pct > 50:
                analise += f"com expansão de {crescimento_pct:.1f}%, ampliando a capacidade de investimento municipal. "
            elif crescimento_pct > 20:
                analise += f"com crescimento de {crescimento_pct:.1f}%. "
            else:
                analise += f"com variação de {crescimento_pct:.1f}%. "

        analise += "A otimização da gestão financeira, mediante planejamento orçamentário rigoroso e controle de gastos, "
        analise += "é fundamental para viabilizar investimentos em infraestrutura e serviços públicos essenciais."

        return analise

    def gerar_diagnostico_integrado(self, municipio: str, ind: Dict) -> str:
        """Gera diagnóstico integrado e propositivo."""
        idhm_class, _ = self.analisar_idhm(ind)
        economia = self.analisar_economia(ind)
        educacao = self.analisar_educacao(ind)

        pop = ind.get('pop_2022', 0)
        idhm = ind.get('idhm_2010', 0)

        # Classificar porte
        if pop > 100000:
            porte = "grande porte populacional"
            funcao = "polo regional"
        elif pop > 50000:
            porte = "porte médio"
            funcao = "centro sub-regional"
        elif pop > 20000:
            porte = "porte intermediário"
            funcao = "município com área de influência microrregional"
        else:
            porte = "pequeno porte"
            funcao = "município de base local"

        diagnostico = f"{municipio} configura-se como {funcao}, com {porte} ({int(pop):,} habitantes), ".replace(',', '.')
        diagnostico += f"apresentando IDHM {idhm_class} e {economia['setor_dominante']}. "

        # Diretrizes para plano de governo
        diagnostico += "\n\n**Diretrizes Prioritárias para o Plano de Governo Estadual:**\n\n"

        diretrizes = []

        # Diretriz 1: Educação (sempre prioritário)
        if educacao['tendencia'] == "necessidade de reversão da queda":
            diretrizes.append("**Educação**: Implementar programa emergencial de melhoria da qualidade do ensino, com foco em infraestrutura escolar, formação docente e acompanhamento pedagógico para reverter queda do IDEB")
        elif idhm < 0.650:
            diretrizes.append("**Educação**: Fortalecer políticas educacionais integradas, articulando alfabetização, ensino fundamental de qualidade e educação profissionalizante para elevar capital humano")
        else:
            diretrizes.append("**Educação**: Consolidar avanços educacionais mediante valorização docente, modernização tecnológica das escolas e ampliação da educação integral")

        # Diretriz 2: Infraestrutura (baseada em saneamento)
        saude = self.analisar_saude_saneamento(ind)
        if "crítico" in saude['esgoto']:
            diretrizes.append("**Saneamento**: Priorizar investimentos em esgotamento sanitário mediante parcerias com governo federal e financiamentos específicos, visando universalização do acesso")
        elif "necessidade" in saude['agua']:
            diretrizes.append("**Saneamento**: Expandir rede de abastecimento de água tratada e esgotamento sanitário, com metas de universalização alinhadas ao novo marco legal do saneamento")
        else:
            diretrizes.append("**Infraestrutura**: Investir em mobilidade urbana, drenagem e pavimentação para consolidar infraestrutura urbana de qualidade")

        # Diretriz 3: Desenvolvimento Econômico
        if economia['perc_agro'] > 30:
            diretrizes.append("**Desenvolvimento Econômico**: Apoiar agroindustrialização e cadeias produtivas do agronegócio mediante assistência técnica, crédito e acesso a mercados")
        elif pop > 50000:
            diretrizes.append("**Desenvolvimento Econômico**: Fortalecer ambiente de negócios para atração de investimentos, com foco em serviços qualificados e economia criativa")
        else:
            diretrizes.append("**Desenvolvimento Econômico**: Estimular empreendedorismo local e economia solidária, com programas de microcrédito e capacitação empresarial")

        # Diretriz 4: Saúde
        if "necessidade" in saude['ubs']:
            diretrizes.append("**Saúde**: Ampliar cobertura da atenção básica com expansão de UBS e Estratégia Saúde da Família, fortalecendo prevenção e promoção da saúde")
        elif "dependência" in saude['hospitalar']:
            diretrizes.append("**Saúde**: Estruturar rede regionalizada de atenção à saúde, garantindo acesso a serviços especializados e hospitalares de média complexidade")
        else:
            diretrizes.append("**Saúde**: Qualificar serviços de saúde existentes com foco em gestão, regulação e integração da rede de atenção")

        # Diretriz 5: Gestão Pública
        financas = self.analisar_financas(ind)
        if financas['dependencia_fpm'] > 70:
            diretrizes.append("**Gestão Pública**: Modernizar administração tributária e fortalecer arrecadação própria para reduzir dependência de transferências e ampliar autonomia fiscal")
        else:
            diretrizes.append("**Gestão Pública**: Aprimorar planejamento estratégico, governança e capacitação de servidores para otimizar aplicação de recursos públicos")

        for i, diretriz in enumerate(diretrizes, 1):
            diagnostico += f"{i}. {diretriz}\n\n"

        diagnostico += "A implementação articulada destas diretrizes, com protagonismo do governo estadual em coordenação federativa, "
        diagnostico += "pode alavancar o desenvolvimento municipal sustentável e a melhoria da qualidade de vida da população."

        return diagnostico.strip()

    def gerar_analises_completas(self, municipio: str) -> Dict[str, any]:
        """Gera todas as análises para um município."""
        # Carregar dados
        ind = self.carregar_json_municipio(municipio)

        if not ind:
            return None

        # Gerar análises
        sintese = self.gerar_sintese_estrategica(municipio, ind)

        analises = {
            'sintese_estrategica': sintese,
            'analise_social': self.gerar_analise_social(ind),
            'analise_economica': self.gerar_analise_economica(ind),
            'analise_educacao': self.gerar_analise_educacao(ind),
            'analise_saude': self.gerar_analise_saude(ind),
            'analise_agropecuaria': self.gerar_analise_agropecuaria(ind),
            'analise_financas': self.gerar_analise_financas(ind),
            'diagnostico_integrado': self.gerar_diagnostico_integrado(municipio, ind)
        }

        return analises


if __name__ == '__main__':
    # Teste
    analisador = AnalisadorMunicipal()

    # Testar com Palmas
    print("Gerando análises para Palmas...")
    analises = analisador.gerar_analises_completas('Palmas')

    if analises:
        print("\n=== SÍNTESE ESTRATÉGICA ===")
        print("\nPontos Fortes:")
        for pf in analises['sintese_estrategica']['pontos_fortes']:
            print(f"- {pf}")

        print("\nDesafios:")
        for d in analises['sintese_estrategica']['desafios']:
            print(f"- {d}")

        print("\nOportunidades:")
        for o in analises['sintese_estrategica']['oportunidades']:
            print(f"- {o}")

        print("\n=== ANÁLISE SOCIAL ===")
        print(analises['analise_social'])

        print("\n=== DIAGNÓSTICO INTEGRADO ===")
        print(analises['diagnostico_integrado'])
    else:
        print("Erro ao carregar dados de Palmas")
