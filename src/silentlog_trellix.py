import requests
import os
import sys


# gera o token de acesso
def get_acess_token():
    url = "https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token"
    auth = (client_id, secret)
    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }
    data = {
        "scope": "xdr.alr.r xdr.alr.rw xdr.cc.r xdr.cc.rw xdr.dbr.r xdr.dbr.rw xdr.dp.r xdr.dp.rw xdr.fed.r xdr.fed.rw xdr.hidden.rw xdr.ind.r xdr.ind.rw xdr.intel.rw xdr.org.adm xdr.rul.r xdr.rul.rw xdr.so.r xdr.so.rw xdr.srh.adv xdr.srh.r xdr.srh.rw",
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data, auth=auth)
    return response.json().get("access_token",response.json())


# enviar o csv para o trellix
def upload_csv_to_helix(company):
    file_path = f"src/{company}_silentlog.csv"

    url = f"https://xdr.trellix.com/helix/id/{helix_id}/api/v3/senders"
    
    headers = {
        "x-trellix-api-token": f"Bearer {get_acess_token()}"
    }
    
    with open(file_path, 'rb') as file:
        files = {
            'file': ('file.csv', file, 'text/csv')
        }
        response = requests.post(url, headers=headers, files=files)
    
    return response.json()


# limpa as configuraçoes do silent log
def clear_config():
    url = f"https://xdr.trellix.com/helix/id/{helix_id}/api/v3/senders"
    
    headers = {
        "x-trellix-api-token": f"Bearer {get_acess_token()}",
        "Content-Type": "application/json"
    }
    
    response = requests.delete(url, headers=headers)
    
    return response.json().get("message", response.json())


# habilita o silent log
def enable_silent_log():
    url = f"https://xdr.trellix.com/helix/id/{helix_id}/api/v3/senders/enable"
    
    headers = {
        "x-trellix-api-token": f"Bearer {get_acess_token()}",
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, headers=headers)
    
    return response.json().get("message", response.json())


# limpa as configuraçoes do silent log
def disabe_silent_log():
    url = f"https://xdr.trellix.com/helix/id/{helix_id}/api/v3/senders/enable"
    
    headers = {
        "x-trellix-api-token": f"Bearer {get_acess_token()}",
        "Content-Type": "application/json"
    }
    
    response = requests.delete(url, headers=headers)
    
    return response.json().get("message", response.json())


# verifica o status do silent log
def get_senders():
    url = f"https://xdr.trellix.com/helix/id/{helix_id}/api/v3/senders/"
    headers = {
        "accept": "application/json",
        "x-trellix-api-token": f"Bearer {get_acess_token()}"
    }
    response = requests.get(url, headers=headers)
    return response.json().get("message",response.json())


## Funçoe extras 


# cria o csv caso não exista na aplicação
def create_csv_if_not_exists(company):
    file_path = f"src/{company}_silentlog.csv"
    if not os.path.exists(file_path):
        with open(file_path, 'w') as csv_file:
            headers = ['device_name', 'device_ipv4', 'threshold_eps', 'email_recipients', 'duration']
            csv_file.write(','.join(headers) + '\n')


# banner animado
def animated_banner():
    # Banner text
    banner = """
    ███████╗██╗██╗     ███████╗███╗   ██╗████████╗    ██╗      ██████╗  ██████╗ 
    ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝    ██║     ██╔═══██╗██╔════╝ 
    ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║       ██║     ██║   ██║██║  ███╗
    ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║       ██║     ██║   ██║██║   ██║
    ███████║██║███████╗███████╗██║ ╚████║   ██║       ███████╗╚██████╔╝╚██████╔╝
    ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝ 
    """
    print(f"\033[31m{banner}\033[0m")


# pega os dados de entrada
def get_inputs():
    # recebe os inputs
    while True:
        company = input("Digite o nome da empresa: ")
        if len(company) < 5:
            print("Erro: O nome da empresa deve ter pelo menos 5 caracteres")
            continue
        break

    while True:
        helix_id = input("Digite o ID do Helix: ")
        if len(helix_id) < 5:
            print("Erro: O ID do Helix deve ter pelo menos 5 caracteres")
            continue
        break

    while True:
        client_id = input("Digite o ID do Cliente: ")
        if len(client_id) < 5:
            print("Erro: O ID do Cliente deve ter pelo menos 5 caracteres")
            continue
        break

    while True:
        secret = input("Digite a secret: ")
        if len(secret) < 5:
            print("Erro: A secret deve ter pelo menos 5 caracteres")
            continue
        break
    
    return company, helix_id, client_id, secret


# menu principal
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        animated_banner()
        print("\n=== Menu de Gerenciamento do Silent Log ===")
        print("1. Enviar CSV para o Helix")
        print("2. Limpar Configuração do Silent Log")
        print("3. Ativar Silent Log")
        print("4. Desativar Silent Log") 
        print("5. Verificar Status do Silent Log")
        print("0. Sair")
        
        choice = input("\nDigite sua escolha (1-6): ")
        
        if choice == '1':
            result = upload_csv_to_helix(company)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Resultado do upload:", result)
        elif choice == '2':
            result = clear_config()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Configuração limpa:", result)
        elif choice == '3':
            result = enable_silent_log()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Silent log ativado:", result)
        elif choice == '4':
            result = disabe_silent_log()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Silent log desativado:", result)
        elif choice == '5':
            result = get_senders()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Status atual:", result)
        elif choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")


# Execução


try:
    animated_banner()

    company, helix_id, client_id, secret = get_inputs()

    create_csv_if_not_exists(company)

    show_menu()
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nSaindo do script")
    sys.exit(0)
