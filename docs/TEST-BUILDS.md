# Testes de builds de desenvolvimento

## Estado dos artifacts

O workflow [Build PS2 ELF](../.github/workflows/build-ps2.yml) está configurado para `push` em `main`, pull request e execução manual. Ele disponibiliza o artifact temporário `ps2-forge-ai-dev-build` somente após um build bem-sucedido, com retenção de sete dias. O artifact contém exatamente `PS2ForgeAI-OPL.ELF`, `LICENSE`, `CREDITS` e `LICENSE-USMB2.txt`; o GitHub pode apresentá-lo como um arquivo compactado para download. Não é pacote instalável nem release.

O workflow ainda precisa ser executado e aprovado para produzir o primeiro artifact desta revisão. Ele não inclui jogos, dumps, ISO/ZSO/VCD, POPStarter, POPS, BIOS ou firmware proprietário. O ELF pode incorporar dependências abertas do projeto sob suas respectivas licenças; os avisos acompanham o artifact. O empacotador [`tools/package_edition.py`](../tools/package_edition.py) e o comando `tools/assets.py release` estão desativados.

As instruções atuais para build local e SDK estão em [`BUILD-CONFIGURATIONS.md`](BUILD-CONFIGURATIONS.md); não use o antigo `tools/build_edition.py` para preparar uma release. A configuração herdada deve ser preservada e respaldada antes de qualquer teste. Os jogos PS2 ISO/ZSO e as imagens PS1 VCD são fornecidos pelo usuário; a biblioteca PS1 depende de POPStarter/POPS/BIOS que o próprio usuário já possua e instale separadamente.

## Como registrar um teste

Compatibilidade em emulador e em hardware real ainda não foi testada para esta versão. Um resultado de compilação, teste de host, abertura do menu ou leitura da lista não é prova de compatibilidade de jogo ou de periférico. Até que haja validação independente na plataforma correspondente, descreva os resultados como preliminares e não como suporte confirmado.

Ao reportar um problema, informe o commit, a versão do ELF, a configuração local, o modelo do console ou versão do emulador, dispositivo e sistema de arquivos, opções alteradas, etapas de reprodução e mensagem/resultado observado. Use somente jogos, imagens, firmware e arquivos que você próprio fornece e tem direito de utilizar; não envie dumps, BIOS ou conteúdo de jogos junto ao relatório.
