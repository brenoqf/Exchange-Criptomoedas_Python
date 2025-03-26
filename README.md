# **Projeto 1 - Desenvolvimento de Algoritmos**

## Objetivo
- O Exchange de Criptomoedas é um programa desenvolvido em C, para a matéria de Desenvolvimento de Algoritimos, que permite usuários gerenciar suas finanças em reais (R$) e três tipos de criptomoedas, tais sendo, Bitcoin (BTC), Ethereum (ETH) e Ripple (XRP). O sistema oferece as seguintes funcionalidades:

    - Cadastro: Efetuar login​ usando CPF e senha:

    - Menu: O menu principal deve aparecer apenas se estas informações estiverem corretas

    - Consultar saldo: Verificar quantidade de reais, bitcoin, ethereum e ripple da carteira de investimentos​

    - Consultar extrato: Verificar de operações da carteira de investimentos​

    - Depositar: Conseguir depositar real na carteira de investimento​

    - Sacar: Conseguir sacar real da carteira de investimento​

    - Comprar criptomoedas: usuário deve informar valor da compra e senha para validação. caso os dados estiverem corretos e a compra for possível, exibir as informações da compra (incluindo a taxa cobrada) e pedir a confirmação do usuário

    - Vender criptomoedas: caso os dados estiverem corretos, exibir as informações da venda (incluindo a taxa cobrada) e pedir a confirmação do usuário

    - Atualizar cotação das criptomoedas: usar valores aleatórios pra gerar mudanças de no máximo 5% e mínimo -5% do valor atual
   
&nbsp;

# **Dicionários**

## Usuários
 - O dicionário 'usuarios' armazena todas as informações necessárias para gerenciar a conta de um usuário, incluindo: 
    - Nome: Armazena o primeiro nome do usuário.
    - CPF: Identificador único do usuário.
    - Senha: Senha de acesso à conta.
    - Saldo: Saldo em reais.
    - Bit, Eth, Rip: Saldo em Bitcoin, Ethereum e Ripple, respectivamente

&nbsp;
## Extra

- O dicionário 'extra' armazena os extratos de cada ação realizada pelo usuário. Ele inclui:
    - Data: Armazana o ano, mês, dia, hora, minuto e segundo no momento da transação.
    - '+/-': Registra se a transação adicionou um valor ou retirou através dos símbolos "+" e "-", respectivamente.
    - Valor: Quanto foi rearanjado nessa operação.
    - Tipo: O que foi manuseado na transação(Real, Bitcoin, Ethereum ou Ripple)
    - 'CT': Se houve uma operação envolvendo criptomoeda, ela irá mostrar a cotação da mesma no momento da operação.
    - 'TX': Taxa, em decimal, cobrada sobre o tipo de transação com cada criptomoeda.
    - "REAL BTC ETH XRP": Saldo da conta após a transação.

&nbsp;
# **Funções**

- O programa é composto por diversas funções interconectadas que gerenciam as operações financeiras dos usuários. A seguir, apresentamos as principais funcionalidades e como elas interagem para fornecer uma experiência completa e segura.

&nbsp;
## Salvar
- A função "salva" é responsável por gravar os dados do usuário no arquivo JSON. Ela abre o arquivo, escreve os dados da biblioteca 'usuario' e fecha o arquivo. Se ocorrer algum erro durante a abertura do arquivo, uma mensagem de erro é exibida.

&nbsp;
## Cadastro de Usuário
- A função de cadastro permite que novos usuários criem uma conta no sistema. Durante o cadastro, o usuário deve fornecer:

    - Nome: O primeiro nome do usuário.
    - CPF: O Cadastro de Pessoas Físicas, utilizado como identificador único.
    - Senha: Uma senha segura para acessar a conta.

&nbsp;
- Após a inserção dessas informações, o sistema valida a senha para garantir que ela atende aos critérios de segurança (por exemplo, mínimo de 6 caracteres). Se a validação for bem-sucedida, os dados do usuário são salvos dentro da biblioteca "usuario", nomeado pelo CPF do usuário, garantindo que cada usuário tenha seu próprio arquivo de dados JSON.

&nbsp;
## Login de Usuário
- A função de login permite que usuários existentes acessem suas contas. Para realizar o login, o usuário deve fornecer:

    - CPF: Para identificar sua conta.
    - Senha: Para autenticação.

&nbsp;
- O sistema verifica se o CPF está cadastrado lendo o arquivo correspondente. Em seguida, compara a senha fornecida com a senha armazenada no arquivo. Se ambas as informações coincidirem, o usuário é autenticado com sucesso e pode acessar o menu principal do sistema. Caso contrário, uma mensagem de erro é exibida, e o usuário é solicitado a tentar novamente.

&nbsp;
## Menu Principal 
- Após o login ou cadastro bem-sucedido, o usuário é direcionado ao menu principal, que oferece as seguintes opções:

    - Consultar Saldo: Exibe o saldo atual em reais e nas diferentes criptomoedas.
    - Consultar Extrato: Mostra o histórico de transações realizadas, incluindo depósitos e saques, com data e hora.
    - Depositar: Permite ao usuário adicionar fundos em reais à sua conta.
    - Sacar: Permite ao usuário retirar fundos em reais da sua conta.
    - Comprar Criptomoedas: Oferece a opção de comprar Bitcoin, Ethereum ou Ripple.
    - Vender Criptomoedas: Oferece a opção de vender Bitcoin, Ethereum ou Ripple.
    - Atualizar Cotação: Atualiza as cotações das criptomoedas com variações aleatórias.
    - Sair: Finaliza a sessão e retorna à tela de início.
    
&nbsp;
## Depósito de Fundos
- A função de depositar permite que o usuário adicione fundos em reais à sua conta. O usuário é solicitado a inserir o valor a ser depositado. O sistema valida se o valor é positivo e, em seguida, atualiza o saldo do usuário. Após isso, o extrato da transação é gerado, com a data e hora que ocorreu.
  
&nbsp;
## Saque de Fundos
- A função de sacar permite que o usuário retire fundos em reais da sua conta. O usuário é solicitado a inserir o valor a ser sacado. O sistema verifica se o valor é positivo e se o saldo disponível é suficiente para a operação. Caso as condições sejam atendidas, o saldo é atualizado e a transação é como um extrato, com a descrição do saque e a data e hora em que foi realizado.

&nbsp;
## Compra de Criptomoedas
- A função de comprar criptomoedas permite que o usuário adquira Bitcoin, Ethereum ou Ripple. O usuário seleciona a criptomoeda desejada e a quantidade a ser comprada. O sistema calcula o custo total da compra com uma taxa adicional e verifica se o saldo em reais é suficiente para a transação. Se aprovado, o saldo em reais é decrementado e o saldo da criptomoeda correspondente é incrementado. A transação é registrada no histórico com detalhes da compra e a data e hora.

&nbsp;
## Venda de Criptomoedas
- A função de vender criptomoedas permite que o usuário venda Bitcoin, Ethereum ou Ripple. O usuário seleciona a criptomoeda desejada e a quantidade a ser vendida. O sistema calcula o valor a ser creditado em reais após a venda e verifica se o saldo da criptomoeda é suficiente para a operação. Se aprovado, o saldo da criptomoeda é decrementado e o saldo em reais é incrementado. A transação é registrada no histórico com detalhes da venda e a data e hora.

&nbsp;
## Atualização de Cotação
- A função de atualizar cotação permite que o usuário atualize as cotações das criptomoedas disponíveis (Bitcoin, Ethereum e Ripple). O sistema gera variações aleatórias nas cotações, simulando a volatilidade do mercado. As novas cotações são exibidas ao usuário, que pode optar por confirmar a atualização ou cancelar a operação.

&nbsp;
## Consultar Saldo
- A função de consultar saldo exibe ao usuário o saldo atual em reais e nas diferentes criptomoedas. Isso permite que o usuário tenha uma visão clara de suas finanças e ativos digitais.

&nbsp;
## Consultar Extrato
- A função de consultar extrato exibe o histórico de transações do usuário, listando depósitos, saques, compras e vendas realizadas. Cada transação é acompanhada pela data e hora em que foi realizada, proporcionando transparência e controle sobre as movimentações financeiras.
  
