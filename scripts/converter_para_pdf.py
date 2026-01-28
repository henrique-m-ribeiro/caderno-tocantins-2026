#!/usr/bin/env python3
"""
Script para converter o documento consolidado Markdown para PDF com numeração de páginas.

Autor: Claude Code
Data: 2026-01-28
"""

import subprocess
from pathlib import Path
import sys


def converter_para_pdf(input_md, output_pdf, engine='pandoc'):
    """Converte Markdown para PDF com numeração de páginas."""

    print("=" * 80)
    print("CONVERSÃO MARKDOWN → PDF")
    print("=" * 80)
    print()

    input_path = Path(input_md)
    output_path = Path(output_pdf)

    if not input_path.exists():
        print(f"❌ Erro: Arquivo de entrada não encontrado: {input_path}")
        sys.exit(1)

    print(f"📄 Arquivo de entrada: {input_path}")
    print(f"📄 Arquivo de saída: {output_path}")
    print(f"🔧 Engine: {engine}")
    print()

    if engine == 'pandoc':
        converter_com_pandoc(input_path, output_path)
    else:
        print(f"❌ Engine '{engine}' não suportada. Use 'pandoc'.")
        sys.exit(1)


def converter_com_pandoc(input_path, output_path):
    """Converte usando Pandoc."""

    print("🔍 Verificando instalação do Pandoc...")

    # Verificar se pandoc está instalado
    try:
        result = subprocess.run(['pandoc', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            raise FileNotFoundError
        print(f"✅ Pandoc encontrado: {result.stdout.split()[1]}")
    except FileNotFoundError:
        print("❌ Pandoc não está instalado!")
        print()
        print("Para instalar o Pandoc:")
        print("  Ubuntu/Debian: sudo apt-get install pandoc texlive-latex-base texlive-latex-extra")
        print("  Fedora/RHEL: sudo dnf install pandoc texlive")
        print("  macOS: brew install pandoc basictex")
        print()
        print("Após instalar, execute este script novamente.")
        sys.exit(1)

    # Verificar se template existe
    template_path = Path(__file__).parent / 'template-pdf.tex'
    if not template_path.exists():
        print(f"❌ Template LaTeX não encontrado: {template_path}")
        print("Crie o arquivo template-pdf.tex no diretório scripts/")
        sys.exit(1)
    print(f"✅ Template LaTeX encontrado: {template_path}")

    print()
    print("🔄 Convertendo Markdown → PDF...")
    print("   (Isso pode levar alguns minutos para documentos grandes)")
    print()

    # Comando pandoc com template customizado para numeração de páginas
    comando = [
        'pandoc',
        str(input_path),
        '-o', str(output_path),
        '--pdf-engine=pdflatex',
        '--template', str(template_path),
        '-V', 'geometry:margin=2.5cm',
        '-V', 'fontsize=11pt',
        '-V', 'papersize=a4',
        '-V', 'documentclass=article',
        '--highlight-style=tango',
    ]

    try:
        result = subprocess.run(comando, capture_output=True, text=True, timeout=600)

        if result.returncode == 0:
            tamanho_mb = output_path.stat().st_size / (1024 * 1024)
            print()
            print("=" * 80)
            print("✅ CONVERSÃO CONCLUÍDA COM SUCESSO!")
            print("=" * 80)
            print(f"\n📄 PDF gerado: {output_path}")
            print(f"📏 Tamanho: {tamanho_mb:.2f} MB")
            print()
            print("=" * 80)
        else:
            print("❌ Erro na conversão!")
            print()
            print("STDERR:")
            print(result.stderr)
            sys.exit(1)

    except subprocess.TimeoutExpired:
        print("❌ Timeout: A conversão demorou mais de 10 minutos.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Converter documento Markdown para PDF')
    parser.add_argument('--input', '-i',
                      default='parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.md',
                      help='Arquivo Markdown de entrada')
    parser.add_argument('--output', '-o',
                      default='parte-iii-fichas-municipais/PARTE-III-FICHAS-MUNICIPAIS.pdf',
                      help='Arquivo PDF de saída')
    parser.add_argument('--engine', '-e', default='pandoc',
                      choices=['pandoc'],
                      help='Engine de conversão (padrão: pandoc)')

    args = parser.parse_args()

    converter_para_pdf(args.input, args.output, engine=args.engine)
