# Configurações de build — PS2 Forge AI

Este projeto em desenvolvimento deriva do Open PS2 Loader (OPL). O código mantém opções e comportamentos herdados; a lista de páginas e configurações preservadas está em [`SETTINGS.md`](SETTINGS.md). Consulte também [`LICENSE`](../LICENSE) e [`CREDITS`](../CREDITS), que devem permanecer junto ao código.

## Build automático

O workflow [Build PS2 ELF](../.github/workflows/build-ps2.yml) está configurado para rodar em push para `main`, pull request ou execução manual por `workflow_dispatch`. Ele instala versões fixadas do SDK `ps2build` e dos ports oficiais, prepara assets/traduções e compila o alvo GCC.

Depois de uma execução bem-sucedida, o Actions disponibiliza por sete dias o artifact `ps2-forge-ai-dev-build`. Ele contém exatamente quatro arquivos: `PS2ForgeAI-OPL.ELF`, `LICENSE`, `CREDITS` e `LICENSE-USMB2.txt` (aviso MIT da dependência usmb2). O GitHub pode entregar o artifact compactado; isso não é uma release instalável. O workflow não publica releases ou bundles.

O artifact ainda não foi produzido nesta versão: é necessário que o workflow seja executado e aprovado no GitHub Actions. Mesmo um ELF compilado com sucesso não comprova funcionamento em emulador ou console real.

## Build manual

Em uma máquina Linux compatível, com acesso à internet para obter as dependências abertas indicadas pelo projeto:

```sh
python3 -m pip install -r requirements.txt
export PS2DEV_INSTALL_DIR="$HOME/.local/share/ps2build"
export PS2BUILD_HOME="$PS2DEV_INSTALL_DIR"
export PS2BUILD_SDK_NO_FALLBACK=1
sh tools/ps2build_sdk.sh "$PS2BUILD_HOME"
export PATH="$PS2BUILD_HOME:$PATH"
sh tools/install_ps2build.sh
python3 tools/assets.py all
python3 tools/build.py --toolchain gcc --out-dir build
```

O alvo ELF intermediário é `build/bin/riptopl-packed.elf`. O build manual não cria um pacote de instalação. Os scripts `tools/package_edition.py` e `tools/assets.py release` estão desativados; não use ferramentas de publicação herdadas para criar releases ou bundles.

## Parâmetros, dados e licenças

- As versões do SDK e dos ports usados pelo workflow ficam registradas em [`.github/ps2build-sdk.env`](../.github/ps2build-sdk.env). O SDK foi configurado para falhar em vez de usar o mirror legado.
- As configurações existentes do OPL devem ser preservadas. Faça backup dos arquivos pessoais antes de qualquer teste; o build não deve apagar nem substituir configurações do usuário.
- Jogos PS2 em ISO/ZSO e VCDs PS1 são fornecidos pelo usuário. A biblioteca PS1 depende de POPStarter/POPS e BIOS que o próprio usuário já possua e instale separadamente. Esses jogos e componentes proprietários não são fornecidos nem incluídos no artifact.
- O ELF incorpora dependências abertas necessárias ao funcionamento do projeto. `LICENSE`, `CREDITS` e o aviso de licença usmb2 acompanham o artifact; mantenha também as atribuições de cada componente upstream.
