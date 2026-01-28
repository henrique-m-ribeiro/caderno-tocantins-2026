#!/usr/bin/env python3
"""
Script para processamento em massa de PDFs municipais usando extrator v9.

Características:
- Processamento paralelo (4 workers)
- Monitoramento de progresso em tempo real
- Captura e registro de erros
- Geração automática de relatório
- Pula municípios já processados

Uso:
    python3 processar_massa_v7.py

Autor: Claude Code
Data: 2026-01-28
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
import time

# Configurações
PDFS_DIR = Path("Perfil Municipios Tocantins")
OUTPUT_DIR = Path("dados/brutos/extraidos-perfis")
EXTRATOR_SCRIPT = Path("scripts/extracao_pdfs/extrator_v9_completo.py")
LOG_FILE = Path("logs/processamento_massa_v9.log")
MAX_WORKERS = 4

# Garantir que diretórios existem
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def log_message(msg, level="INFO"):
    """Registra mensagem no log e exibe no console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {msg}"

    # Exibir no console
    print(log_line)

    # Salvar no arquivo
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")


def processar_municipio(pdf_path):
    """
    Processa um único município.

    Args:
        pdf_path: Path para o PDF

    Returns:
        dict: Resultado do processamento
    """
    municipio = pdf_path.stem.replace("_perfil_2024pdf", "")
    output_json = OUTPUT_DIR / f"{municipio}_v9.json"

    # Pular se já processado
    if output_json.exists():
        return {
            "municipio": municipio,
            "status": "SKIP",
            "indicadores": contar_indicadores(output_json),
            "msg": "Já processado"
        }

    try:
        # Executar extrator
        resultado = subprocess.run(
            ["python3", str(EXTRATOR_SCRIPT), str(pdf_path), str(output_json)],
            capture_output=True,
            text=True,
            timeout=120  # 2 minutos timeout por município
        )

        if resultado.returncode == 0:
            # Sucesso
            indicadores = contar_indicadores(output_json)
            return {
                "municipio": municipio,
                "status": "OK",
                "indicadores": indicadores,
                "msg": f"Sucesso: {indicadores} indicadores"
            }
        else:
            # Erro na execução
            return {
                "municipio": municipio,
                "status": "ERROR",
                "indicadores": 0,
                "msg": f"Erro: {resultado.stderr[:200]}"
            }

    except subprocess.TimeoutExpired:
        return {
            "municipio": municipio,
            "status": "TIMEOUT",
            "indicadores": 0,
            "msg": "Timeout após 2 minutos"
        }
    except Exception as e:
        return {
            "municipio": municipio,
            "status": "EXCEPTION",
            "indicadores": 0,
            "msg": f"Exceção: {str(e)[:200]}"
        }


def contar_indicadores(json_path):
    """Conta número de indicadores no JSON."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return len(data.get("indicadores", {}))
    except:
        return 0


def gerar_relatorio(resultados):
    """Gera relatório consolidado do processamento."""

    # Separar por status
    sucesso = [r for r in resultados if r["status"] == "OK"]
    skip = [r for r in resultados if r["status"] == "SKIP"]
    erro = [r for r in resultados if r["status"] in ["ERROR", "TIMEOUT", "EXCEPTION"]]

    # Estatísticas de indicadores (apenas sucesso + skip)
    indicadores_counts = [r["indicadores"] for r in sucesso + skip if r["indicadores"] > 0]

    if indicadores_counts:
        media = sum(indicadores_counts) / len(indicadores_counts)
        mediana = sorted(indicadores_counts)[len(indicadores_counts) // 2]
        minimo = min(indicadores_counts)
        maximo = max(indicadores_counts)
    else:
        media = mediana = minimo = maximo = 0

    # Outliers (< 60 indicadores)
    outliers = [r for r in sucesso + skip if 0 < r["indicadores"] < 60]

    # Gerar relatório
    relatorio = []
    relatorio.append("=" * 80)
    relatorio.append("RELATÓRIO DE PROCESSAMENTO EM MASSA - EXTRATOR V9")
    relatorio.append("=" * 80)
    relatorio.append(f"\nData: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    relatorio.append(f"\n{'='*80}")
    relatorio.append("\n📊 RESUMO GERAL")
    relatorio.append(f"{'='*80}")
    relatorio.append(f"Total de municípios processados: {len(resultados)}")
    relatorio.append(f"  ✅ Sucesso (novos):              {len(sucesso)}")
    relatorio.append(f"  ⏭️  Skip (já processados):        {len(skip)}")
    relatorio.append(f"  ❌ Erros:                        {len(erro)}")

    relatorio.append(f"\n{'='*80}")
    relatorio.append("\n📈 ESTATÍSTICAS DE INDICADORES")
    relatorio.append(f"{'='*80}")
    relatorio.append(f"Média:   {media:.1f} indicadores/município")
    relatorio.append(f"Mediana: {mediana} indicadores/município")
    relatorio.append(f"Mínimo:  {minimo} indicadores")
    relatorio.append(f"Máximo:  {maximo} indicadores")

    if outliers:
        relatorio.append(f"\n{'='*80}")
        relatorio.append(f"\n⚠️  OUTLIERS (< 60 indicadores): {len(outliers)} municípios")
        relatorio.append(f"{'='*80}")
        for r in sorted(outliers, key=lambda x: x["indicadores"]):
            relatorio.append(f"  {r['municipio']:30s} - {r['indicadores']:2d} indicadores")

    if erro:
        relatorio.append(f"\n{'='*80}")
        relatorio.append(f"\n❌ ERROS: {len(erro)} municípios")
        relatorio.append(f"{'='*80}")
        for r in erro:
            relatorio.append(f"  {r['municipio']:30s} - {r['status']}: {r['msg']}")

    relatorio.append(f"\n{'='*80}")
    relatorio.append("\n📋 TODOS OS MUNICÍPIOS (ordenados por indicadores)")
    relatorio.append(f"{'='*80}")
    for r in sorted(sucesso + skip, key=lambda x: (-x["indicadores"], x["municipio"])):
        status_icon = "✅" if r["status"] == "OK" else "⏭️"
        relatorio.append(f"  {status_icon} {r['municipio']:30s} - {r['indicadores']:2d} indicadores")

    relatorio.append(f"\n{'='*80}\n")

    return "\n".join(relatorio)


def main():
    """Função principal."""
    log_message("="*80)
    log_message("INICIANDO PROCESSAMENTO EM MASSA - EXTRATOR V9")
    log_message("="*80)

    # Listar todos os PDFs
    pdfs = sorted(PDFS_DIR.glob("*_perfil_2024pdf.pdf"))
    log_message(f"PDFs encontrados: {len(pdfs)}")

    # Contar já processados
    ja_processados = len(list(OUTPUT_DIR.glob("*_v9.json")))
    log_message(f"Municípios já processados: {ja_processados}")
    log_message(f"Municípios a processar: {len(pdfs) - ja_processados}")

    # Processar em paralelo
    log_message(f"\nIniciando processamento paralelo ({MAX_WORKERS} workers)...")
    log_message("-"*80)

    inicio = time.time()
    resultados = []

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submeter todas as tarefas
        futures = {executor.submit(processar_municipio, pdf): pdf for pdf in pdfs}

        # Processar conforme completam
        for i, future in enumerate(as_completed(futures), 1):
            resultado = future.result()
            resultados.append(resultado)

            # Log de progresso
            status_icon = {
                "OK": "✅",
                "SKIP": "⏭️",
                "ERROR": "❌",
                "TIMEOUT": "⏱️",
                "EXCEPTION": "💥"
            }.get(resultado["status"], "❓")

            log_message(
                f"[{i:3d}/{len(pdfs)}] {status_icon} {resultado['municipio']:30s} - {resultado['msg']}",
                level="PROGRESS"
            )

    tempo_total = time.time() - inicio

    log_message("-"*80)
    log_message(f"Processamento concluído em {tempo_total:.1f} segundos ({tempo_total/60:.1f} minutos)")

    # Gerar e salvar relatório
    relatorio = gerar_relatorio(resultados)

    relatorio_path = Path("relatorios/processamento_massa_v9.txt")
    relatorio_path.parent.mkdir(parents=True, exist_ok=True)
    with open(relatorio_path, "w", encoding="utf-8") as f:
        f.write(relatorio)

    # Exibir relatório
    print("\n" + relatorio)

    log_message(f"\nRelatório salvo em: {relatorio_path}")
    log_message(f"Log completo salvo em: {LOG_FILE}")

    # Retornar código de erro se houver problemas
    erros = [r for r in resultados if r["status"] in ["ERROR", "TIMEOUT", "EXCEPTION"]]
    if erros:
        log_message(f"\n⚠️  Atenção: {len(erros)} municípios com erro!", level="WARNING")
        return 1

    log_message("\n✅ Processamento concluído com sucesso!")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        log_message("\n\n⚠️  Processamento interrompido pelo usuário", level="WARNING")
        sys.exit(130)
    except Exception as e:
        log_message(f"\n\n💥 Erro fatal: {str(e)}", level="ERROR")
        import traceback
        log_message(traceback.format_exc(), level="ERROR")
        sys.exit(1)
