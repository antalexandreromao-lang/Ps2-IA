# PS2 Forge AI

**PS2 Forge AI** é um projeto em desenvolvimento derivado do **Open PS2 Loader (OPL)**. Ele reutiliza o motor aberto e mantém configurações herdadas; não apaga nem substitui o trabalho upstream. Consulte [`LICENSE`](LICENSE) e [`CREDITS`](CREDITS) para os termos, créditos e atribuições de origem. Veja também o [README histórico preservado](docs/README-repositorio-original.md).

> **Estado:** desenvolvimento. Esta versão ainda não foi validada em emulador ou console PlayStation 2 real. Um build bem-sucedido não comprova que o menu inicia, que um dispositivo funciona ou que um jogo é compatível.

## Interface e bibliotecas

A abertura usa fundo branco com o wordmark OPL preto e detalhes azuis. A biblioteca tem visual escuro/futurista, arte BG do jogo no fundo, lista à esquerda, capa COV menor à direita e identificadores separados para PS2 e PS1. O ícone 3D exibido para o save do OPL no navegador do cartão de memória usa o mesmo wordmark do boot.

A arte é opcional e fornecida pelo usuário na pasta `ART` da instalação do OPL. Use o ID/nome base do jogo com `_BG` para o fundo e `_COV` para a capa, por exemplo `ART/<ID>_BG.png` e `ART/<ID>_COV.png`. PNG e JPG são reconhecidos; os fundos também dependem da opção de arte de fundo herdada do OPL. Sem arte BG, o tema usa o fundo escuro de reserva.

As páginas e opções de configuração herdadas devem ser preservadas. Faça backup dos arquivos de configuração e dos dados pessoais antes de testar qualquer build; não apague, formate nem substitua configurações durante a instalação. O inventário das páginas e chaves fica em [`docs/SETTINGS.md`](docs/SETTINGS.md).

## Biblioteca PS2

A biblioteca PS2 pode listar imagens **ISO** e **ZSO** fornecidas pelo usuário. O repositório e os artefatos automáticos não incluem jogos, imagens de disco, dumps nem coleções de terceiros. Use somente cópias e dados que você tenha direito de utilizar.

## Biblioteca PS1

A biblioteca PS1 lista imagens **VCD**. A execução depende de **POPStarter/POPS** e de uma **BIOS** compatível que o próprio usuário já possua e instale separadamente. O projeto não distribui jogos PS1, VCDs, POPStarter, POPS, BIOS nem dumps de BIOS.

## Compilação pelo GitHub

O workflow [Build PS2 ELF](.github/workflows/build-ps2.yml) roda em pushes para `main`, pull requests e execução manual. Depois de um build aprovado, o GitHub Actions disponibiliza por sete dias o artifact `ps2-forge-ai-dev-build`, contendo exatamente `PS2ForgeAI-OPL.ELF`, `LICENSE`, `CREDITS` e `LICENSE-USMB2.txt`. O GitHub pode apresentar o artifact como arquivo compactado; ele não é uma release instalável nem inclui jogos ou firmware.

O build automático ainda precisa ser executado e aprovado pelo GitHub Actions. Instruções atuais para build local e configuração do SDK estão em [`docs/BUILD-CONFIGURATIONS.md`](docs/BUILD-CONFIGURATIONS.md). O ELF incorpora dependências abertas necessárias ao projeto sob suas respectivas licenças; não são distribuídos POPStarter, POPS, BIOS, jogos nem payload proprietário.

## Distribuição, licença e créditos

Não há releases instaláveis autorizadas neste repositório. [`tools/package_edition.py`](tools/package_edition.py) e `tools/assets.py release` estão desativados. O workflow não cria pacotes ZIP de instalação, kits ou imagens de mídia; o GitHub apenas armazena o artifact temporário descrito acima. Não são anexados jogos, POPStarter, POPS, BIOS ou payload proprietário. Não use ferramentas de publicação herdadas para distribuir bundles.

Mantenha [`LICENSE`](LICENSE), [`CREDITS`](CREDITS) e as atribuições upstream junto ao código. A compatibilidade em emulador e hardware real continua pendente de testes específicos; até isso acontecer, trate qualquer resultado apenas como preliminar.
