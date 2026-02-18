# DesafioDioKeylloger

Simulação de Malware em Python: Ransomware e Keylogger Educacionais 🚀😈
Olá, aventureiros da cibersegurança! 👋 Se você está aqui, provavelmente é porque curte um bom desafio técnico com uma pitada de adrenalina (mas tudo fake, hein? Nada de virar vilão de filme de hacker! 😂). Esse repositório é o meu projeto final para o desafio do Bootcamp da Riachuelo em parceria com a DIO! 🚀 É 100% educacional, inspirado nas aulas sobre malwares, e serve pra gente entender como essas pragas digitais funcionam – e, mais importante, como se proteger delas no mundo real.
Aviso Importante ⚠️:
Tudo aqui é simulado e deve ser rodado só em ambiente controlado (tipo uma VM ou pasta isolada). NUNCA use isso em máquinas reais, redes de produção ou pra qualquer fim malicioso. É pra aprender e se divertir estudando! Se você é iniciante, rode com cuidado e delete tudo depois. Eu avisei, tá? 😜
O Que Esse Projeto Faz? 🤔
Esse repo implementa dois malwares simulados em Python, baseados nos exemplos do curso: um Ransomware e um Keylogger. A ideia é mostrar na prática como eles "atacam" (mas de mentirinha), capturam dados ou criptografam arquivos, e depois refletir sobre defesas. Tudo é reversível e seguro – nada de danos reais!
1. Ransomware Simulado 🗝️🔒

O que ele faz?
Cria uma pasta de testes com arquivos bobos (como .txt, .jpg, .pdf), gera uma chave de criptografia, "sequestra" esses arquivos criptografando eles, e exibe uma mensagem de resgate hilária (tipo "Pague 0.5 Bitcoin ou adeus arquivos! 😈"). Depois, você pode descriptografar tudo com a chave certa. É como um jogo de esconde-esconde com seus dados!
Como funciona por baixo dos panos?
Usamos a biblioteca cryptography com o algoritmo Fernet (simétrico e forte). O script encrypt.py varre a pasta, criptografa arquivos selecionados e muda a extensão pra algo como .sequestrado. O decrypt.py reverte tudo se você der a chave. Pra tornar mais real, gera um arquivo README_RESGATE.txt com instruções fake de pagamento.
Por que isso é educativo?
Mostra como ransomwares exploram falhas humanas (como cliques em anexos suspeitos) e a importância de backups. No mundo real, vítimas pagam milhões porque não têm cópias seguras!
Como rodar?
Instale as dependências: pip install cryptography
Vá pra pasta /ransomware/
Crie arquivos de teste em /test_files/ (ex: um txt com "Olá mundo!")
Rode python encrypt.py – veja a mágica (ruim) acontecer!
Rode python decrypt.py com a chave (salva em chave_secreta.key pra estudo).
Dica divertida: Tente criptografar uma foto sua e veja ela virar um monte de bits bagunçados! 📸➡️🔢


2. Keylogger Simulado ⌨️🕵️‍♂️

O que ele faz?
Captura as teclas que você digita e salva em um arquivo .txt (como senhas ou mensagens). Tem uma versão básica e uma "furtiva" que envia o log por e-mail automaticamente a cada X minutos. É como um espião invisível no seu teclado – mas só pra demonstrar o perigo!
Como funciona por baixo dos panos?
Usamos a biblioteca pynput pra escutar o teclado. O script keylogger_simples.py loga tudo em log_teclas.txt. A versão avançada (keylogger_com_email.py) usa smtplib pra mandar e-mails (use contas fake ou de teste!). Pra ser mais ninja, roda em background e captura até cliques de mouse ou info do PC.
Por que isso é educativo?
Revela como keyloggers se escondem em apps maliciosos ou sites phishing, explorando brechas como falta de antivírus. No curso, vimos que conscientização é chave: nunca digite senhas em PCs públicos!
Como rodar?
Instale as dependências: pip install pynput (e python-dotenv pro e-mail)
Vá pra pasta /keylogger/
Rode python keylogger_simples.py – digite algo e pare com Ctrl+C. Veja o log!
Pra versão com e-mail: Configure um .env com credenciais fake (NUNCA reais!) e rode python keylogger_com_email.py.
Dica divertida: Teste digitando uma receita de bolo e veja se o "espião" capturou tudo certinho. 🍰🔍


Reflexão sobre Defesa: Virando o Jogo Contra os Malwares! 🛡️💪
Agora que vimos o lado "malvado", vamos pro herói! Aqui vai uma reflexão baseada no que aprendi no bootcamp: malwares como esses exploram vulnerabilidades técnicas (como software desatualizado) e humanas (curiosidade ou descuido). Mas dá pra se proteger sim! 😎

Backups Regulares: Use a regra 3-2-1 (3 cópias, 2 mídias diferentes, 1 offline). Teste sempre – é o antídoto perfeito pro ransomware!
Antivírus e EDR: Ferramentas como Avast ou Windows Defender com heurística detectam comportamentos suspeitos (ex: criptografia em massa).
Firewall e Sandboxing: Bloqueie tráfego estranho e rode apps duvidosos em "caixas de areia" isoladas (tipo VirtualBox).
Conscientização do Usuário: Não clique em links malucos, use MFA (autenticação de dois fatores) em tudo, e gerencie senhas com apps como LastPass. No bootcamp, aprendemos que 99% dos ataques vêm de erro humano – então, eduque-se!
Atualizações e Menor Privilégio: Mantenha SO e apps em dia. Não rode nada como admin desnecessariamente.
Monitoramento: Ferramentas como Wireshark pra ver tráfego de rede – keyloggers adoram mandar dados pro exterior.

No final, o bootcamp da Riachuelo DIO me mostrou que cibersegurança é como um jogo de xadrez: entenda o inimigo pra vencer. Esse projeto foi minha jogada mestra! ♟️
Tecnologias Usadas 🛠️

Python 3.x
Bibliotecas: cryptography, pynput, smtplib, threading
Ambiente: Testado no Windows/Linux (use VM pra segurança extra)

Pastas e Arquivos 📂

/ransomware/: Scripts de encrypt/decrypt + pasta de testes.
/keylogger/: Scripts do keylogger + logs de exemplo.
/images/: Prints e GIFs da execução (antes/depois, logs, etc.).
defesa.md: Reflexão completa sobre prevenção (leia pra se inspirar!).

Como Contribuir ou Melhorar? 🌟
Se você tá no bootcamp também, fork esse repo e adicione suas ideias! Tipo: um keylogger que captura tela ou um ransomware com timer. Mas lembre: só educacional! Me manda um pull request ou comenta no GitHub. Vamos trocar figurinhas sobre cibersegurança? 😄
Créditos: Inspirado nas aulas do Bootcamp Riachuelo DIO. Obrigado aos instrutores por tornarem isso divertido e prático! 🙌
