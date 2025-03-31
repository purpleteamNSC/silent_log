# Gerenciador de Silent Log

Uma ferramenta Python para gerenciar configurações do Silent Log no Trellix Helix.

## Funcionalidades

- Upload de configurações CSV para o Helix
- Limpeza das configurações do Silent Log
- Ativar/Desativar Silent Log
- Verificar status do Silent Log

## Pré-requisitos

- Python 3.x
- Pacotes Python necessários:
  - requests
  - os
  - time
  - sys

## Instalação Windows

1. Clone o repositório:

   ```bash  
   git clone
   git clone https://github.com/purpleteamNSC/silent_log.git
   cd silent_log
   ```

2. Crie o ambiente virtual para windows:
   ```bash
   python -m venv venv
    ```

3. Ative o ambiente virtual para o windows:
   ```bash
   venv\Scripts\activate
   ```

2. Instale os pacotes Python:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python src\app.py
   ```

## Instalação Linux

1. Clone o repositório:

   ```bash  
   git clone
   git clone https://github.com/purpleteamNSC/silent_log.git
   cd silent_log
   ```

2. Crie o ambiente virtual para windows:
   ```bash
   python3 -m venv venv
    ```

3. Ative o ambiente virtual para o windows:
   ```bash
   source venv/bin/activate
   ```

2. Instale os pacotes Python:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python3 src\app.py

## Authors

- Diogo Caldas - Trabalho inicial e manutenção
- Purple Team NSC - Supervisão e contribuições do projeto

Para dúvidas ou suporte, entre em contato:
- Email: diogovdcpa@gmail.com
- GitHub: @diogovdcpa
