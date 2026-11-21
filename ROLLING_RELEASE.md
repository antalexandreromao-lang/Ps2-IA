# Distribuição e builds — PS2 Forge AI

## Estado atual

O PS2 Forge AI é um projeto em desenvolvimento derivado do Open PS2 Loader (OPL). O código e as opções de build mantêm elementos herdados do projeto upstream; a configuração existente deve ser preservada. Veja [`LICENSE`](LICENSE) e [`CREDITS`](CREDITS), que mantêm a licença, os créditos e as atribuições upstream.

**Não há releases instaláveis autorizadas por este repositório.** O workflow do GitHub Actions é destinado exclusivamente a builds de desenvolvimento. Após uma execução aprovada, ele disponibiliza por sete dias o artifact `ps2-forge-ai-dev-build`, com apenas o ELF do projeto (`PS2ForgeAI-OPL.ELF`) e os avisos `LICENSE`, `CREDITS` e `LICENSE-USMB2.txt`. O GitHub pode apresentar o artifact compactado para download; isso não o torna um instalador ou uma release.

**A compatibilidade desta versão em emuladores e em consoles/hardware real ainda não foi testada.** Compilação bem-sucedida, testes de host e geração do ELF não provam que o programa inicia, que um dispositivo funciona ou que um jogo é compatível.

## Conteúdo que não é distribuído

Os jogos e dados de execução são fornecidos pelo usuário. Não incluir em builds, artifacts ou releases:

- jogos de PS2 ou PS1, imagens **ISO**, **ZSO**, **VCD**, dumps ou backups de jogos;
- **POPStarter**, arquivos **POPS** ou módulos proprietários de POPS;
- BIOS de PS1/PS2 ou dumps de BIOS;
- firmware ou componentes proprietários de terceiros.

O ELF pode incorporar dependências de código aberto necessárias ao projeto, conforme suas licenças; os avisos correspondentes devem ser preservados. As imagens ISO/ZSO que o programa pode listar ou carregar são fornecidas pelo usuário, que deve possuir os direitos necessários. A biblioteca PS1 usa VCD e depende de POPStarter/POPS e BIOS que o próprio usuário já possua e instale separadamente. Este projeto não hospeda nem fornece esses arquivos.

## Build de desenvolvimento

O build automático e as instruções para build local estão documentados em [`docs/BUILD-CONFIGURATIONS.md`](docs/BUILD-CONFIGURATIONS.md). O workflow não cria releases, kits instaláveis ou pacotes com jogos/firmware.

Os scripts [`tools/package_edition.py`](tools/package_edition.py) e `tools/assets.py release` estão deliberadamente desativados. Não use comandos ou instruções antigos de `build_edition.py` para preparar releases ou bundles: eles não correspondem ao fluxo atual deste repositório.

## Licença e atribuições

Mantenha a licença aplicável, os créditos upstream e as atribuições de cada componente. Consulte [`LICENSE`](LICENSE) e [`CREDITS`](CREDITS). A documentação histórica preservada não altera o estado atual de distribuição descrito acima.
