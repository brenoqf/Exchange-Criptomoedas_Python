import json as js
from datetime import datetime as dt
import os
import random as r

usuarios = {}
extra = {}

###############################################################################################################################################################################################################

#função para voltar para o menu
def voltar(cpf):
    print("1-Voltar")
    a = int(input())
    if(a==1):
        menu(cpf)

###############################################################################################################################################################################################################

#coloca os pontos e o traço no cpf
def f_cpf(cpf):
    cn = ''.join(filter(str.isdigit, cpf))

    cf = f'{cn[:3]}.{cn[3:6]}.{cn[6:9]}-{cn[9:]}'

    return cf

###############################################################################################################################################################################################################

#registra o dia e hora quando a função for chamada
def dia_hora():
    global data
    global data2
    data = dt.now()
    data2 = data.strftime("%d-%m-%Y %H:%M")

###############################################################################################################################################################################################################

#verifica se o arquivo json existe e da para acessar-lo. Se existir, o json exporta os dados para a biblioteca. Se não, ele abre o json vazio e exporta a biblioteca
def salvando_dados():
    if os.path.exists('contas.json'):
        with open('contas.json', 'r') as arquivo:  
            conteudo = arquivo.read()
            if conteudo.strip():
                global usuarios
                usuarios = js.loads(conteudo)
    else:
        usuarios = {}

###############################################################################################################################################################################################################

#salva qualquer alteração no json e na biblioteca ao ser chamada
def salva():
    with open('contas.json', 'w') as arquivo:
        js.dump(usuarios, arquivo, indent=2)
        
###############################################################################################################################################################################################################

#verifica o tamanho do json. Se estiver vazio, adiciona as cotações das criptomoesdas no arquivo json. Se não estiver vazio, a biblioteca é atualizada com as cotações
def verifica_json():
    if os.path.exists("contas.json"):
        with open("contas.json", 'r') as arquivo:
            conteudo = arquivo.read()
            if len(conteudo) == 0:
                usuarios.update({"Cotacoes":{
                        "BTC": 313050.25,
                        "ETH": 15030.11,
                        "XRP": 2.60
                    },})
                with open("contas.json", 'w') as arquivo:
                    js.dump(usuarios, arquivo, indent=2)  
            else:
                usuarios.update(arquivo)

###############################################################################################################################################################################################################

#função para mostrar as opções de confirmar
def conf():
    print("1 - Sim | 2 - Não")
    a = int(input())
    return a

###############################################################################################################################################################################################################

#CADASTRO DO USUÁRIO
def cadastra():
    print("---------- CADASTRO DO INVESTIDOR ----------")
    nome = str(input("Digite o nome do usuário: "))
    cpf = str(input("Digite o CPF do usuário(sem pontos ou traço): "))
    
    #verificação de cpf(se tem 11 dígitos)
    if(len(cpf)!=11):
        print("CPF inválido. Digite um CPF válido.")
        print()
        cadastra()
    
    #verificação de cpf(se já está sendo usado)
    elif cpf in usuarios:
        print("CPF já utilizado. Insira outro CPF.")
        print()
        cadastra()

    else:
        senha = str(input("Digite uma senha de 6 dígitos para a sua conta: "))

        #verificação de senha(se tem 6 dígitos)
        if len(senha)!=6:
            print("Senha inválida. Digite uma senha de 6 dígitos.")
            print()
            cadastra()

        else:
            confsenha = str(input("Confirme a senha: "))

            #verificação de senha(as duas senhas digitadas são iguais)
            if confsenha!=senha:
                print("As senhas digitadas são diferentes. Por favor, digite-as novamnete.")
                print()
                cadastra()
    
            else:
                print("As informações estão corretas?")
                print()
                print("Nome:", nome)
                print("CPF:", cpf)
                print("Senha:", senha)

                x = conf()
                if(x==1):
                    usuarios[cpf] = {
                        "Nome": nome,
                        "CPF": cpf,
                        "Senha": senha,
                        "Reais": 0.0,
                        "Bitcoin": 0.0,
                        "Ethereum": 0.0,
                        "Ripple": 0.0,
                        "Extratos": []
                    }
                    with open("dados.txt", "a") as arquivo:
                        arquivo.write(f"Nome: {nome} | CPF: {cpf} | Senha: {senha}\n")
                    salva()
                    print(f"Cadastro efetuado com sucesso. Bem-Vindo {usuarios[cpf]['Nome']}.")
                    menu(cpf)
                else:
                    print("Tudo bem. Realize o cadastro novamente.")
                    cadastra()

###############################################################################################################################################################################################################

#LOGIN DO USUÁRIO
def login():
    print("---------- LOGIN DO INVESTIDOR ----------")

    cpf = str(input("Digite o CPF (sem pontos ou traço): "))
    
    #verificação de cpf(se tem 11 dígitos)
    if(len(cpf)!=11):
        print("Usuário inválido ou senha inválida. Insira os dados correspondentes da conta.")
        print()
        login()
    
    else:
        senha2 = str(input("Digite a senha: "))
        
        #verificação de senha(se tem 6 dígitos)
        if(len(senha2)!=6):
            print("Usuário inválido ou senha inválida. Insira os dados correspondentes da conta.")
            print()
            login()
        
        else:
            with open('contas.json', 'r') as arquivo:
                linha = js.load(arquivo)

                #verificação de senha(se tem é a mesma do cpf digitado)
                if cpf in linha and senha2 == linha[cpf]['Senha']:
                        print(f"Login efetuado com sucesso. Bem-Vindo {linha[cpf]['Nome']}.")
                        menu(cpf)

                else:
                    print("Usuário ou senha inválida. Insira os dados correspondentes da conta.")
                    print()
                    login()

###############################################################################################################################################################################################################

#MENU DO USUÁRIO
#opções do menu são gerenciadas pelos números. Se o número da opção desejada for digitada, a função da mesma será chamada  
def menu(cpf):
    while True:
        print()
        print("---------- MENU DO INVESTIDOR ----------")
        print("1. Consultar saldo")
        print("2. Consultar extrato")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Comprar criptomoedas")
        print("6. Vender criptomoedas")
        print("7. Atualizar cotação")
        print("8. Sair")

        a = int(input())
        if(a==1):
            senha = str(input("Insira sua senha para consultar essa função: "))
            with open('contas.json', 'r') as arquivo:
                linha = js.load(arquivo)
                if senha == linha[cpf]['Senha']:
                    consultar_saldo(cpf)
                else:
                    print("Senha inválida. Voltando para o menu principal.")
                    menu(cpf)
        
        elif(a==2):
            senha = str(input("Insira sua senha para consultar essa função: "))
            with open('contas.json', 'r') as arquivo:
                linha = js.load(arquivo)
                if senha == linha[cpf]['Senha']:
                    consultar_extrato(cpf)
                else:
                    print("Senha inválida. Voltando para o menu principal.")
                    menu(cpf)
        
        elif(a==3):
            print("Deseja realizar algum deposito?")
            x = conf()

            if(x==1):
                depositar(cpf)
            
            else:
                menu(cpf)
        
        elif(a==4):
            print("Deseja realizar algum saque?")
            x = conf()

            if(x==1):
                sacar(cpf)
            
            else:
                menu(cpf)

        elif(a==5):
            senha = str(input("Insira sua senha para consultar essa função: "))
            with open('contas.json', 'r') as arquivo:
                linha = js.load(arquivo)
                if senha == linha[cpf]['Senha']:
                    c_cripto(cpf)
                else:
                    print("Senha inválida. Voltando para o menu principal.")
                    menu(cpf)
        
        elif(a==6):
            senha = str(input("Insira sua senha para consultar essa função: "))
            with open('contas.json', 'r') as arquivo:
                linha = js.load(arquivo)
                if senha == linha[cpf]['Senha']:
                    v_cripto(cpf)
                else:
                    print("Senha inválida. Voltando para o menu principal.")
                    menu(cpf)

        elif(a==7):
            cota(cpf)

        elif(a==8):
            print("Deseja sair de sua conta?")
            x = conf()
            if(x==1):
                print("Tudo Bem. Aguarde um momento.")
                print("Saindo da conta...")
                print("Conta deslogada com sucesso.")
                print()
                inicio()
            else:
                menu(cpf)  

###############################################################################################################################################################################################################

#CONSULTAR SALDO
def consultar_saldo(cpf):
    cpf2 = f_cpf(cpf)
    print()
    print("---------- SALDO ----------")
    print(f"Nome: {usuarios[cpf]['Nome']}")
    print(f"CPF: {cpf2}")
    print()
    print(f"Reais: {usuarios[cpf]['Reais']}")
    print(f"Bitcoin: {usuarios[cpf]['Bitcoin']}")
    print(f"Ethereum: {usuarios[cpf]['Ethereum']}")
    print(f"Ripple: {usuarios[cpf]['Ripple']}")
    print()
    voltar(cpf)

###############################################################################################################################################################################################################

#CONSULTAR EXTRATOS
def consultar_extrato(cpf):
    cpf2 = f_cpf(cpf)
    print()
    print("---------- EXTRATO ----------")
    print(f"Nome: {usuarios[cpf]['Nome']}")
    print(f"CPF: {cpf2}")
    print()
    
    #verifica se tem extrato ou não
    if usuarios[cpf]['Extratos'] == "":
        print("Nenhum extrato registrado.")
    
    else:
        for extrato in usuarios[cpf]['Extratos']:
            print(f"{extrato['Data']:<17}", end="")
            print(f"{extrato['+/-']:<2}", end="")
            print(f"{extrato['Valor']:<10}", end="")
            print(f"{extrato['Tipo']:<5}", end="")
            print(f"CT: {extrato['CT']:<11}", end="")
            print(f"TX: {extrato['TX']:<10}", end="")
            print(f"REAL: {extrato['REAL']:<15}", end="")
            print(f"BTC: {extrato['BTC']:<15}", end="")
            print(f"ETH: {extrato['ETH']:<15}", end="")
            print(f"XRP: {extrato['XRP']:<15}", end="\n")

    print()
    voltar(cpf)

###############################################################################################################################################################################################################

#DEPOSITO
def depositar(cpf):
    cpf2 = f_cpf(cpf)
    print()
    print("---------- DEPOSITAR ----------")
    print(f"Nome: {usuarios[cpf]['Nome']}")
    print(f"CPF: {cpf2}")
    print(f"Saldo na conta: R${usuarios[cpf]['Reais']}")
    print()

    #valor do deposito
    dep = float(input("Digite o valor que deseja depositar: R$"))
    print(f"Confirme o valor do depósito: R${dep} na conta de {usuarios[cpf]['Nome']}")
    
    x = conf()

    #confirma o valor do deposito. Se confirmar, atualiza o json e cria o extrato. Se não, chama a função novamente
    if x == 1:
        dia_hora()
        usuarios[cpf]['Reais'] += dep
        usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "+", "Valor": dep, "Tipo": "REAL", "CT": 0.0, "TX": 0.00, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
        salva()
        with open("extratos.txt", "a") as arquivo:
            arquivo.write(f"CPF: {cpf} / {data2} + {dep} REAL CT: 0,0    TX: 0.00 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
       
        print("Depósito realizado com sucesso.")
        print()
        print("Deseja realizar outro depósito?")
        y = conf()

        if y == 1:
            depositar(cpf)
        else:
            menu(cpf)
    else:
        print("Tudo bem. Faça o depósito novamente.")
        depositar(cpf)

###############################################################################################################################################################################################################

#SAQUE
def sacar(cpf):
    cpf2 = f_cpf(cpf)
    print()
    print("---------- SACAR ----------")
    print()
    print(f"Nome: {usuarios[cpf]['Nome']}")
    print(f"CPF: {cpf2}")
    print(f"Saldo na conta: R${usuarios[cpf]['Reais']}")
    print()

    #valor do saque
    saq = float(input("Digite o valor que deseja sacar: R$"))
    
    #verifica se o valor colocado é maior que o saldo da conta logada
    if(usuarios[cpf]['Reais']<saq):
        print("Saque impossivel de ser realizado. Sua conta não pode ficar no negativo. Insira um valor que corresponda à realidade.")
        sacar(cpf)
    else:
        print(f"Confirme o valor do saque: R${saq} na conta de {usuarios[cpf]['Nome']}")
    
    x = conf()

    #confirma o valor do saque. Se confirmar, atualiza o json e cria o extrato. Se não, chama a função novamente
    if x == 1:
        dia_hora()
        usuarios[cpf]['Reais'] -= saq
        usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "-", "Valor": saq, "Tipo": "REAL", "CT": 0.0, "TX": 0.00, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
        salva()
        with open("extratos.txt", "a") as arquivo:
            arquivo.write(f"CPF: {cpf} / {data2} - {saq} REAL CT: 0,0    TX: 0.00 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
        
        print("Saque realizado com sucesso.")
        print()
        print("Deseja realizar outro saque?")
        y = conf()
        if y == 1:
            depositar(cpf)
        else:
            menu(cpf)
    else:
        print("Tudo bem. Faça o saque novamente.")
        depositar(cpf)

###############################################################################################################################################################################################################

#COMPRAR CRIPTOMOEDA
def c_cripto(cpf):
    cpf2 = f_cpf(cpf)
    print()
    print("---------- COMPRAR CRIPTOMOEDAS ----------")
    print(f"Nome: {usuarios[cpf]['Nome']}")
    print(f"CPF: {cpf2}")
    print()
    print(f"Saldo: R${usuarios[cpf]['Reais']}")
    print(f"Bitcoin: {usuarios[cpf]['Bitcoin']}")
    print(f"Ethereum: {usuarios[cpf]['Ethereum']}")
    print(f"Ripple: {usuarios[cpf]['Ripple']}")
    print()

    #seleciona a criptomoeda por número. Ao selecionar a cripto desejada, chama a função de compra da cripto
    print("Selecione a criptomoeda qeu deseja comprar:\n1.Bitcoin\n2.Ethereum\n3.Ripple")
    a = int(input())
    if(a==1):
        print("Deseja comprar Bitcoin?")
        x = conf()
        if(x==1):
            c_bit(cpf)
        else:
            c_cripto(cpf)
        
    if(a==2):
        print("Deseja comprar Ethereum?")
        x = conf()
        if(x==1):
            c_eth(cpf)
        else:
            c_cripto(cpf)
        
    if(a==3):
        print("Deseja comprar Ripple?")
        x = conf()
        if(x==1):
            c_xrp(cpf)
    else:
        c_cripto(cpf)
    
    print()
    voltar(cpf)

###############################################################################################################################################################################################################

#COMPRA DE BITCOIN
def c_bit(cpf):
    print()
    print("---------- COMPRAR BITCOIN ----------")
    print(f"Saldo atual: R${usuarios[cpf]['Reais']}")
    print(f"Valor do Bitcoin(BTC): R${usuarios['Cotacoes']['BTC']}")

    #seleciona a quantidade de Bitcoins que quer comprar
    y = float(input(f"Selecione quanto(s) Bitcoin(s) você quer comprar: "))
    valor = y*usuarios['Cotacoes']['BTC']

    #verifica se o valor da compra é maior que o saldo da conta. Se for, a função é chamada novamnete. Se naõ for, a compra continua
    if(valor > usuarios[cpf]['Reais']):
        print("Sua conta não possui saldo suficiente para realizar essa compra. Selecione um valor correspondente.")
        c_bit(cpf)
    else:
        print(f"Confirme o valor da compra: {y}BTC na conta de {usuarios[cpf]['Nome']}")
        x = conf()

        #confirma o valor da compra. Se confirmar, atualiza o json e cria o extrato. Se não, chama a função novamente
        if(x==1):
            dia_hora()
            usuarios[cpf]['Bitcoin'] += y
            usuarios[cpf]['Reais'] -= (valor + valor*0.02)
            usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "+", "Valor": y, "Tipo": "BTC", "CT": usuarios['Cotacoes']['BTC'], "TX": 0.02, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
            salva()
            with open("extratos.txt", "a") as arquivo:
                arquivo.write(f"CPF: {cpf} / {data2} + {y} BTC CT: {usuarios['Cotacoes']['BTC']}    TX: 0.02 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
            
            print("Compra realizado com sucesso.")
            print()
            print("Deseja realizar outra compra?")
            z = conf()
            if z == 1:
                c_cripto(cpf)
            else:
                menu(cpf)
        else:
            print("Tudo bem. Faça a compra novamente.")
            c_bit(cpf)

###############################################################################################################################################################################################################

#COMPRA DE ETHEREUM
def c_eth(cpf):
    print()
    print("---------- COMPRAR ETHEREUM ----------")
    print(f"Saldo atual: R${usuarios[cpf]['Reais']}")
    print(f"Valor do Ethereum(ETH): R${usuarios['Cotacoes']['ETH']}")

    #seleciona a quantidade de Ethereuns que quer comprar
    y = float(input("Selecione quanto(s) Ethereum(s) você quer compra: "))
    valor = y*usuarios['Cotacoes']['ETH']

    #verifica se o valor da compra é maior que o saldo da conta. Se for, a função é chamada novamnete. Se naõ for, a compra continua
    if(valor > usuarios[cpf]['Reais']):
        print("Sua conta não possui saldo suficiente para realizar essa compra. Selecione um valor correspondente.")
        c_eth(cpf)
    else:
        print(f"Confirme o valor da compra: {y}ETH da conta de {usuarios[cpf]['Nome']}")
        x = conf()

        #confirma o valor da compra. Se confirmar, atualiza o json e cria o extrato. Se não, chama a função novamente
        if(x==1):
            dia_hora()
            usuarios[cpf]['Ethereum'] += y
            usuarios[cpf]['Reais'] -= (valor + valor*0.01)
            usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "+", "Valor": y, "Tipo": "ETH", "CT": usuarios['Cotacoes']['ETH'], "TX": 0.01, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
            salva()
            with open("extratos.txt", "a") as arquivo:
                arquivo.write(f"CPF: {cpf} / {data2} + {y} ETH CT: {usuarios['Cotacoes']['ETH']}    TX: 0.01 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
            
            print("Compra realizado com sucesso.")
            print()
            print("Deseja realizar outra compra?")
            z = conf()
            if z == 1:
                c_cripto(cpf)
            else:
                menu(cpf)
        else:
            print("Tudo bem. Faça a compra novamente.")
            c_eth(cpf)

###############################################################################################################################################################################################################

#COMPRA DE RIPPLE
def c_xrp(cpf):
    print()
    print("---------- COMPRAR RIPPLE ----------")
    print(f"Saldo atual: R${usuarios[cpf]['Reais']}")
    print(f"Valor do Ripple(XRP): R${usuarios['Cotacoes']['XRP']}")

    #seleciona a quantidade de Ripples que quer comprar
    y = float(input("Selecione quanto você quer compra: XRP"))
    valor = y*usuarios['Cotacoes']['XRP']

    #verifica se o valor da compra é maior que o saldo da conta. Se for, a função é chamada novamnete. Se naõ for, a compra continua
    if(valor > usuarios[cpf]['Reais']):
        print("Sua conta não possui saldo suficiente para realizar essa compra. Selecione um valor correspondente.")
        c_xrp(cpf)
    else:
        print(f"Confirme o valor da compra: {y}XRP da conta de {usuarios[cpf]['Nome']}")
        x = conf()
        
        #confirma o valor da compra. Se confirmar, atualiza o json e cria o extrato. Se não, chama a função novamente
        if(x==1):
            dia_hora()
            usuarios[cpf]['Ripple'] += y
            usuarios[cpf]['Reais'] -= (valor + valor*0.01)
            usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "+", "Valor": y, "Tipo": "XRP", "CT": usuarios['Cotacoes']['XRP'], "TX": 0.01, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
            salva()
            with open("extratos.txt", "a") as arquivo:
                arquivo.write(f"CPF: {cpf} / {data2} + {y} XRP CT: {usuarios['Cotacoes']['XRP']}    TX: 0.01 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
            
            print("Compra realizado com sucesso.")
            print()
            print("Deseja realizar outra venda?")
            z = conf()
            if z == 1:
                c_cripto(cpf)
            else:
                menu(cpf)
        else:
            print("Tudo bem. Faça a compra novamente.")
            c_xrp(cpf)

###############################################################################################################################################################################################################

#VENDA DE CRIPTOMOEDAS
def v_cripto(cpf):
    cpf2 = f_cpf(cpf)
    print()
    print("---------- VENDER CRIPTOMOEDAS ----------")
    print(f"Nome: {usuarios[cpf]['Nome']}")
    print(f"CPF: {cpf2}")
    print()
    print(f"Saldo: R${usuarios[cpf]['Reais']}")
    print(f"Bitcoin: {usuarios[cpf]['Bitcoin']}")
    print(f"Ethereum: {usuarios[cpf]['Ethereum']}")
    print(f"Ripple: {usuarios[cpf]['Ripple']}")
    print()

    #seleciona a criptomoeda por número. Ao selecionar a cripto desejada, chama a função de venda da cripto
    print("Selecione a criptomoeda qeu deseja comprar:\n1.Bitcoin\n2.Ethereum\n3.Ripple")
    a = int(input())
    if(a==1):
        print("Deseja vender Bitcoin?")
        x = conf()
        if(x==1):
            v_bit(cpf)
        else:
            v_cripto(cpf)
        
    if(a==2):
        print("Deseja vender Ethereum?")
        x = conf()
        if(x==1):
            v_eth(cpf)
        else:
            v_cripto(cpf)
        
    if(a==3):
        print("Deseja vender Ripple?")
        x = conf()
        if(x==1):
            v_xrp(cpf)
        else:
            v_cripto(cpf)
    
    print()
    voltar(cpf)

###############################################################################################################################################################################################################

def v_bit(cpf):
    print()
    print("---------- VENDER BITCOIN ----------")
    print(f"Saldo atual: R${usuarios[cpf]['Reais']}")
    print(f"Valor do Bitcoin(BTC): R${usuarios['Cotacoes']['BTC']}")
    y = float(input(f"Selecione quanto(s) Bitcoin(s) você quer vender: "))
    if(y > usuarios[cpf]['Bitcoin']):
        print("Sua conta não possui Bitcoin suficiente para realizar essa venda. Selecione um valor correspondente.")
        v_bit(cpf)
    else:
        print(f"Confirme o valor da venda: {y}BTC da conta de {usuarios[cpf]['Nome']}")
        x = conf()
        if(x==1):
            valor = y*usuarios['Cotacoes']['BTC']
            dia_hora()
            usuarios[cpf]['Bitcoin'] -= y
            usuarios[cpf]['Reais'] += (valor - valor*0.03)
            usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "-", "Valor": y, "Tipo": "BTC", "CT": usuarios['Cotacoes']['BTC'], "TX": 0.03, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
            salva()
            with open("extratos.txt", "a") as arquivo:
                arquivo.write(f"CPF: {cpf} / {data2} - {y} BTC CT: {usuarios['Cotacoes']['BTC']}    TX: 0.03 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
            
            print("Venda realizado com sucesso.")
            print()
            print("Deseja realizar outra venda?")
            z = conf()
            if z == 1:
                v_cripto(cpf)
            else:
                menu(cpf)
        else:
            print("Tudo bem. Faça a venda novamente.")
            v_bit(cpf)

###############################################################################################################################################################################################################

def v_eth(cpf):
    print()
    print("---------- VENDER ETHEREUM ----------")
    print(f"Saldo atual: R${usuarios[cpf]['Reais']}")
    print(f"Valor do Ethereum(ETH): R${usuarios['Cotacoes']['ETH']}")
    y = float(input("Selecione quanto você quer vender: "))
    if(y > usuarios[cpf]['Ethereum']):
        print("Sua conta não possui tanto isso de Ethereum. Selecione um valor correspondente")
        v_eth(cpf)
    else:
        print(f"Confirme o valor da venda: {y}ETH da conta de {usuarios[cpf]['Nome']}")
        x = conf()
        if(x==1):
            valor = y*usuarios['Cotacoes']['ETH']
            dia_hora()
            usuarios[cpf]['Ethereum'] -= y
            usuarios[cpf]['Reais'] += (valor - valor*0.02)
            usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "-", "Valor": y, "Tipo": "ETH", "CT": usuarios['Cotacoes']['ETH'], "TX": 0.02, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
            salva()
            with open("extratos.txt", "a") as arquivo:
                arquivo.write(f"CPF: {cpf} / {data2} - {y} ETH CT: {usuarios['Cotacoes']['ETH']}    TX: 0.02 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
            
            print("Venda realizado com sucesso.")
            print()
            print("Deseja realizar outra venda?")
            z = conf()
            if z == 1:
                v_cripto(cpf)
            else:
                menu(cpf)
        else:
            print("Tudo bem. Faça a venda novamente.")
            v_eth(cpf)

###############################################################################################################################################################################################################

def v_xrp(cpf):
    print()
    print("---------- VENDER RIPPLE ----------")
    print(f"Saldo atual: R${usuarios[cpf]['Reais']}")
    print(f"Valor do Ethereum(ETH): R${usuarios['Cotacoes']['XRP']}")
    y = float(input("Selecione quanto você quer vender: "))
    if(y>usuarios[cpf]['Ripple']):
        print("Sua conta não possui tanto isso de Ripple. Selecione um valor correspondente")
        v_xrp(cpf)
    else:
        print(f"Confirme o valor da venda: {y}XRP da conta de {usuarios[cpf]['Nome']}")
        x = conf()
        if(x==1):
            valor = y*usuarios['Cotacoes']['XRP']
            dia_hora()
            usuarios[cpf]['Ripple'] -= y
            usuarios[cpf]['Reais'] += (valor - valor*0.01)
            usuarios[cpf]['Extratos'].append({"Data": data2, "+/-": "-", "Valor": y, "Tipo": "XRP", "CT": usuarios['Cotacoes']['XRP'], "TX": 0.01, "REAL": usuarios[cpf]['Reais'], "BTC": usuarios[cpf]['Bitcoin'], "ETH": usuarios[cpf]['Ethereum'], "XRP": usuarios[cpf]['Ripple']})
            salva()
            with open("extratos.txt", "a") as arquivo:
                arquivo.write(f"CPF: {cpf} / {data2} - {y} XRP CT: {usuarios['Cotacoes']['XRP']}    TX: 0.01 REAL: {usuarios[cpf]['Reais']} BTC: {usuarios[cpf]['Bitcoin']} ETH: {usuarios[cpf]['Ethereum']} XRP: {usuarios[cpf]['Ripple']}\n")
            
            print("Venda realizado com sucesso.")
            print()
            print("Deseja realizar outra venda?")
            z = conf()
            if z == 1:
                v_cripto(cpf)
            else:
                menu(cpf)
        else:
            print("Tudo bem. Faça a venda novamente.")
            v_xrp(cpf)

###############################################################################################################################################################################################################

#ATUALIZAÇÃO DE COTAÇÕES
def cota(cpf):
    print()
    print("---------- ATUALIZAR COTAÇÃO ----------")
    print(f"Cotação Bitcoin(BTC): R${usuarios['Cotacoes']['BTC']}")
    print(f"Cotação Ethereum(ETH): R${usuarios['Cotacoes']['ETH']}")
    print(f"Cotação Ripple(XRP): R${usuarios['Cotacoes']['XRP']}")
    print()
    print("Aqui você pode acompanhar a cotações do nosso portifólio de criptomoedas. Deseja atualizar essas cotações?")
    x = conf()

    #confirma a atualização. Se houver a cotação, três taxas que variam de -0,05 até 0.05 são geradas , multiplicam as cotações e salva essa alteração. Se não, o usuário é levado para o menu
    if(x==1):
        taxa1 = (r.randint(-5,5))/100
        taxa2 = (r.randint(-5,5))/100
        taxa3 = (r.randint(-5,5))/100

        usuarios['Cotacoes']['BTC']*taxa1
        usuarios['Cotacoes']['ETH']*taxa2
        usuarios['Cotacoes']['XRP']*taxa3
        salva()
        print()
        print("Cotações atualizadas.")
        cota(cpf)
    
    else:
        menu(cpf)

###############################################################################################################################################################################################################

#INICIO DO PROGRAMA
def inicio():
    z = int(input("---------- Bem-Vindo à Exchange de Criptomoedas da FEI! ----------\nDeseja cadastrar uma conta (1) ou logar uma já existente (2)?: "))

    #opção de cadastro
    if(z==1):
        print()
        cadastra()

    #opção de login
    elif(z==2):
        print()
        login()

    else:
        print("Insira um valor correspondente com as opções válidas.")
        inicio()

###############################################################################################################################################################################################################

verifica_json()
salvando_dados()
inicio()