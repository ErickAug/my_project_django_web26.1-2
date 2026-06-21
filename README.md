#  Sistema de Portfólio + Microserviço de Notificações

Este repositório contém dois projetos independentes que se comunicam entre si:
1. **Portfólio Pessoal (Porta 8000):** O sistema principal construído com Django Templates, que atua como o cliente (consumidor) das notificações.
2. **Microserviço de Notificação (Porta 8001):** Uma API REST independente criada com Django REST Framework, responsável por armazenar, gerenciar e servir notificações via requisições HTTP (CORS + Headers customizados).

---

## Pré-requisitos

Certifique-se de ter instalado em sua máquina:
* [Python 3.x](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

---

## Como executar o projeto localmente

Siga o passo a passo abaixo estritamente na ordem para garantir que a integração funcione perfeitamente. Você precisará de **dois terminais** abertos simultaneamente.

### Passo 1: Clonar o repositório

Crie uma pasta geral para agrupar os projetos (opcional, mas recomendado) e abra o seu terminal nela. Em seguida, clone os dois repositórios:

```
# 1. Clonar o repositório do Microserviço
git clone [https://github.com/ErickAug/microservice-notifications.git](https://github.com/ErickAug/microservice-notifications.git) notificacao_ms

# 2. Clonar o repositório do Portfólio
git clone [https://github.com/ErickAug/my_project_django_web26.1-2.git](https://github.com/ErickAug/my_project_django_web26.1-2.git) django_tutorial
```

### Passo 2: Configurar o Microserviço (Terminal 1)
O microserviço precisa estar rodando primeiro para que o portfólio consiga se conectar a ele.
Navegue até a pasta do microserviço:

``` 
cd notificacao_ms
```
Crie e ative o ambiente virtual (venv):

``` 
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
Instale as dependências:

```
pip install django djangorestframework django-cors-headers
```
Aplique as migrações no banco de dados e crie um superusuário:

```
python manage.py migrate
python manage.py createsuperuser

# Siga as instruções na tela para criar o usuário e senha (ex: admin / admin)
```

Inicie o servidor do microserviço na porta 8001:

```
python manage.py runserver 8001
```

### Passo 3: Cadastrar a "Empresa" e obter a API Key
Com o microserviço rodando, precisamos gerar a chave de acesso que o portfólio usará.
- 1. Abra o navegador e acesse o painel admin: http://127.0.0.1:8001/admin/
- 2. Faça login com o superusuário criado no passo anterior.
- 3. Vá em Empresas e clique em Adicionar.
- 4. Digite um nome (ex: Portfólio Local) e salve.
- 5. Ao salvar, um Hash de 16 caracteres será gerado automaticamente. Copie esse Hash.
- 6. Vá em Targets e clique em Adicionar.
- 7. Selecione a Empresa que você acabou de criar e coloque user_id = 1 (Isso vincula o seu usuário principal do portfólio ao sistema de notificações).

### Passo 4: Configurar o Portfólio (Terminal 2)
Agora, vamos configurar o portfólio para consumir a API. Abra uma nova janela/aba de terminal.

 - Navegue até a pasta do portfólio:

```
cd django_tutorial
```
- Crie e ative um novo ambiente virtual para o portfólio:

```
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
Instale as dependências do portfólio:

```
pip install django
```

- Configuração Crucial: Abra o arquivo django_tutorial/settings.py no seu editor de código e cole o Hash que você copiou no Passo 3 na seguinte variável (geralmente no final do arquivo):

```
NOTIFICACAO_MS_URL = '[http://127.0.0.1:8001](http://127.0.0.1:8001)'
NOTIFICACAO_MS_API_KEY = 'COLE_SEU_HASH_AQUI' 
```
- Aplique as migrações do portfólio (caso ainda não tenha feito) e crie um usuário para o portfólio:

```
python manage.py migrate
python manage.py createsuperuser

# (Crie o usuário que terá o ID 1, para bater com o Target criado no Passo 3)
```
Inicie o servidor do portfólio (na porta padrão 8000):

```
python manage.py runserver
```
# Como testar a integração
Com os dois servidores rodando (Terminal 1 na 8001 e Terminal 2 na 8000):

- 1. Acesse o Portfólio: http://127.0.0.1:8000/portfolio/
- 2. Faça o Login: Se você não estiver logado, acesse http://127.0.0.1:8000/admin/, faça o login com o usuário criado no Passo 4 e volte para a página do portfólio.
- 3. Verifique o Sino: No menu de navegação, você deverá ver um ícone de sino na cor verde com um "0" (indicando conexão com o microserviço, mas sem mensagens).

### Disparando uma notificação em tempo real
- Abra um terceiro terminal ou use o Prompt de Comando para simular um sistema externo enviando uma notificação para você via API.

- Substitua ``COLE_SEU_HASH_AQUI`` pela sua API Key e execute:

```
curl -X POST [http://127.0.0.1:8001/api/notificacoes/criar/](http://127.0.0.1:8001/api/notificacoes/criar/) ^
     -H "X-Api-Key: COLE_SEU_HASH_AQUI" ^
     -H "Content-Type: application/json" ^
     -d "{\"user_id\": 1, \"mensagem\": \"Sua integracao funcionou perfeitamente!\"}"
 ```
(Nota: O comando acima usa ^ para quebra de linha no CMD do Windows. No PowerShell use crase   e no Linux/Mac use barra invertida`). Alternativamente, rode tudo em uma única linha.

#### O Resultado:  Aguarde até 5 segundos na página do seu portfólio. O JavaScript fará o polling, identificará a nova notificação, e o badge do sino ficará vermelho marcando "1". Clique no sino para ler a mensagem e clique nela para marcá-la como lida!
