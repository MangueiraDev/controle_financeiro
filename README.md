## Ativar venv: 
    source venv/bin/activate % macOS/Linux
    source venv/Scripts/activate % Windows
===================================================================================
## Configuraão previa do ambiente:
    Caso você não tenha configurado o FLASK_APP, adicione isso no terminal:
        export FLASK_APP=run.py     % macOS/Linux
        set FLASK_APP=run.py        % Windows

    Execute o Arquivo run.py: python3 run.py

    Se o servidor iniciou com sucesso, você verá uma mensagem no terminal semelhante a:
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        * Debug mode: on
    Abra o navegador e acesse: http://127.0.0.1:5000/
===================================================================================

# Executar servidor Flask:
    flask run
===

1. Criação do Ambiente Virtual (venv)

Passo 1: Criar o Ambiente Virtual (O ambiente virtual será criado no diretório venv dentro do projeto)

Execute o comando abaixo no terminal para criar o ambiente virtual:
    python3 -m venv venv

2. Ativação do Ambiente Virtual

Passo 2: Ativar o Ambiente Virtual
	• macOS/Linux: source venv/bin/activate
    • Windows: venv\Scripts\activate

3. Desativação do Ambiente Virtual

Passo 3: Desativar o Ambiente Virtual

Para desativar o ambiente virtual, basta executar:
    deactivate

4. Instalação de Dependências

Passo 4: Instalar as Bibliotecas Necessárias

Com o ambiente virtual ativado, instale todas as bibliotecas listadas no arquivo requirements.txt:
    pip install -r requirements.txt

Se você precisar instalar as bibliotecas manualmente, use os comandos abaixo:
    pip install flask flask_sqlalchemy flask_migrate flask_login flask_wtf python-dotenv pymysql

Passo 5: Gerar ou Atualizar o Arquivo requirements.txt

Para documentar todas as dependências instaladas no ambiente virtual, execute:
    pip freeze > requirements.txt

5. Configuração do Banco de Dados

Passo 6: Criar as Migrações do Banco de Dados

Execute os comandos abaixo para configurar o banco de dados:
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

6. Executar o Projeto

Passo 7: Configurar o FLASK_APP

Defina o arquivo principal para o Flask. No terminal:
	• macOS/Linux: export FLASK_APP=run.py
    • Windows: set FLASK_APP=run.py

Passo 8: Executar o Servidor

Com todas as configurações concluídas, execute o servidor:
    flask run
    O servidor estará disponível em: http://127.0.0.1:5000




