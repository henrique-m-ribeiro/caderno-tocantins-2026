#!/usr/bin/env python3
"""
Assembles Caderno Tocantins 2026 volumes by concatenating:
1. Front matter (capa, ficha técnica, índice, apresentação, sumário executivo)
2. Microregion ficha (from fase-1-1)
3. V2 municipal fichas (alphabetical order)
"""
import os
import re
import glob

BASE = "/home/user/caderno-tocantins-2026"
V2_DIR = os.path.join(BASE, "parte-iii-fichas-municipais/fichas-v2")
MICRO_DIR = os.path.join(BASE, "analises/fase-1-1-agregacao-municipal")

VOLUMES = {
    3: {
        "name": "ARAGUAINA",
        "micro": "Araguaína",
        "ficha": "FICHA-02-ARAGUAINA-REVISADA.md",
        "municipalities": [
            "ARAGOMINAS", "ARAGUAINA", "ARAGUANA", "ARAPOEMA", "BABACULANDIA",
            "BANDEIRANTES-DO-TOCANTINS", "CARMOLANDIA", "COLINAS-DO-TOCANTINS",
            "FILADELFIA", "MURICILANDIA", "NOVA-OLINDA", "PALMEIRANTE",
            "PAU-DARCO", "PIRAQUE", "SANTA-FE-DO-ARAGUAIA",
            "WANDERLANDIA", "XAMBIOA"
        ]
    },
    4: {
        "name": "BICO-DO-PAPAGAIO",
        "micro": "Bico do Papagaio",
        "ficha": "FICHA-03-BICO-DO-PAPAGAIO-REVISADA.md",
        "municipalities": [
            "AGUIARNOPOLIS", "ANANAS", "ANGICO", "ARAGUATINS", "AUGUSTINOPOLIS",
            "AXIXA-DO-TOCANTINS", "BURITI-DO-TOCANTINS", "CACHOEIRINHA",
            "CARRASCO-BONITO", "DARCINOPOLIS", "ESPERANTINA", "ITAGUATINS",
            "LUZINOPOLIS", "MAURILANDIA-DO-TOCANTINS", "NAZARE",
            "PALMEIRAS-DO-TOCANTINS", "PRAIA-NORTE", "RIACHINHO", "SAMPAIO",
            "SANTA-TEREZINHA-DO-TOCANTINS", "SAO-BENTO-DO-TOCANTINS",
            "SAO-MIGUEL-DO-TOCANTINS", "SAO-SEBASTIAO-DO-TOCANTINS",
            "SITIO-NOVO-DO-TOCANTINS", "TOCANTINOPOLIS"
        ]
    },
    5: {
        "name": "MIRACEMA",
        "micro": "Miracema do Tocantins",
        "ficha": "FICHA-07-MIRACEMA-REVISADA.md",
        "municipalities": [
            "ABREULANDIA", "ARAGUACEMA", "BARROLANDIA", "BERNARDO-SAYAO",
            "BRASILANDIA-DO-TOCANTINS", "CASEARA", "COLMEIA", "COUTO-MAGALHAES",
            "DIVINOPOLIS-DO-TOCANTINS", "DOIS-IRMAOS-DO-TOCANTINS", "GOIANORTE",
            "GUARAI", "ITAPORA-DO-TOCANTINS", "JUARINA",
            "MARIANOPOLIS-DO-TOCANTINS", "MIRACEMA-DO-TOCANTINS", "MIRANORTE",
            "MONTE-SANTO-DO-TOCANTINS", "PEQUIZEIRO", "PRESIDENTE-KENNEDY",
            "RIO-DOS-BOIS", "TABOCAO", "TUPIRAMA", "TUPIRATINS"
        ]
    },
    6: {
        "name": "GURUPI",
        "micro": "Gurupi",
        "ficha": "FICHA-05-GURUPI-REVISADA.md",
        "municipalities": [
            "ALIANCA-DO-TOCANTINS", "ALVORADA", "BREJINHO-DE-NAZARE",
            "CARIRI-DO-TOCANTINS", "CRIXAS-DO-TOCANTINS", "FIGUEIROPOLIS",
            "GURUPI", "JAU-DO-TOCANTINS", "PALMEIROPOLIS", "PEIXE",
            "SANTA-RITA-DO-TOCANTINS", "SAO-SALVADOR-DO-TOCANTINS",
            "SUCUPIRA", "TALISMA"
        ]
    },
    7: {
        "name": "DIANOPOLIS",
        "micro": "Dianópolis",
        "ficha": "FICHA-04-DIANOPOLIS-REVISADA.md",
        "municipalities": [
            "ALMAS", "ARRAIAS", "AURORA-DO-TOCANTINS", "CHAPADA-DA-NATIVIDADE",
            "COMBINADO", "CONCEICAO-DO-TOCANTINS", "DIANOPOLIS", "LAVANDEIRA",
            "NATIVIDADE", "NOVO-ALEGRE", "NOVO-JARDIM", "PARANA",
            "PINDORAMA-DO-TOCANTINS", "PONTE-ALTA-DO-BOM-JESUS",
            "PORTO-ALEGRE-DO-TOCANTINS", "RIO-DA-CONCEICAO",
            "SANTA-ROSA-DO-TOCANTINS", "SAO-VALERIO-DA-NATIVIDADE",
            "TAGUATINGA", "TAIPAS-DO-TOCANTINS"
        ]
    }
}

def assemble_volume(vol_num, vol_data):
    front_matter_path = os.path.join(BASE, f"front-matter-vol{vol_num}.md")
    micro_path = os.path.join(MICRO_DIR, vol_data["ficha"])
    output_path = os.path.join(BASE, f"CADERNO-TOCANTINS-2026-Vol{vol_num}-{vol_data['name']}-V1.0.md")

    if not os.path.exists(front_matter_path):
        print(f"  SKIP Vol {vol_num}: front matter not ready ({front_matter_path})")
        return False

    parts = []

    # 1. Front matter
    with open(front_matter_path, 'r') as f:
        parts.append(f.read().rstrip())

    # 2. Separator + Microregion ficha
    parts.append("\n\n---\n\n")
    parts.append(f"# FICHA DA MICRORREGIÃO DE {vol_data['micro'].upper()}\n\n")
    with open(micro_path, 'r') as f:
        parts.append(f.read().rstrip())

    # 3. Municipal fichas separator
    parts.append("\n\n---\n\n")
    parts.append(f"# FICHAS MUNICIPAIS — MICRORREGIÃO DE {vol_data['micro'].upper()}\n\n")
    parts.append(f"As fichas municipais estão organizadas em **ordem alfabética** para facilitar a consulta.\n\n")

    # 4. V2 fichas in alphabetical order
    missing = []
    for mun in vol_data["municipalities"]:
        # Try multiple filename patterns
        candidates = [
            os.path.join(V2_DIR, f"FICHA-MUNICIPAL-{mun}-V2.md"),
            os.path.join(V2_DIR, f"FICHA-MUNICIPAL-{mun.replace('DARCO','D-ARCO')}-V2.md"),
        ]
        found = False
        for path in candidates:
            if os.path.exists(path):
                parts.append("\n\n---\n\n")
                with open(path, 'r') as f:
                    parts.append(f.read().rstrip())
                found = True
                break
        if not found:
            # Try glob
            pattern = os.path.join(V2_DIR, f"FICHA-MUNICIPAL-{mun}*-V2.md")
            matches = glob.glob(pattern)
            if matches:
                parts.append("\n\n---\n\n")
                with open(matches[0], 'r') as f:
                    parts.append(f.read().rstrip())
            else:
                missing.append(mun)

    if missing:
        print(f"  WARNING Vol {vol_num}: missing fichas for: {missing}")

    # Write output
    content = "".join(parts) + "\n"
    with open(output_path, 'w') as f:
        f.write(content)

    lines = content.count('\n')
    size_kb = len(content.encode('utf-8')) / 1024
    print(f"  OK Vol {vol_num} ({vol_data['name']}): {lines} lines, {size_kb:.0f} KB, {len(vol_data['municipalities'])} municipalities")
    return True

if __name__ == "__main__":
    print("Assembling Caderno Tocantins 2026 volumes...")
    for vol_num in sorted(VOLUMES.keys()):
        assemble_volume(vol_num, VOLUMES[vol_num])
    print("Done.")
