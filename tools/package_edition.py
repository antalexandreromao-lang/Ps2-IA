#!/usr/bin/env python3
"""Empacotador desativado: PS2 Forge AI distribui apenas ELFs de desenvolvimento."""
import argparse
import sys


DISABLED_MESSAGE = (
    "Empacotamento desativado para o PS2 Forge AI. Nenhum pacote, imagem ou release será criado.\n"
    "Não tente incluir jogos ou dumps, arquivos ISO/ZSO/VCD, POPStarter, POPS, BIOS, "
    "módulos ou pacotes de terceiros.\n"
    "O build de desenvolvimento é um ELF; consulte README.md e ROLLING_RELEASE.md."
)


def main(argv=None):
    """Recusar sempre, antes de ler entradas, baixar arquivos ou criar diretórios."""
    arguments = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=(
            "O empacotamento está desativado. São proibidos jogos, dumps, ISO/ZSO/VCD, "
            "POPStarter, POPS, BIOS e payloads/pacotes de terceiros."
        ),
    )
    if arguments in ([], ["-h"], ["--help"]):
        parser.parse_args(arguments)
        if not arguments:
            parser.exit(2, DISABLED_MESSAGE + "\n")
    else:
        parser.print_usage(sys.stderr)
        parser.exit(2, DISABLED_MESSAGE + "\n")


if __name__ == "__main__":
    main()
