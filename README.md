<h1 align="center">🐍 Phonebook Django 🐍<h1>

<br>
<br>
<br>

<ol>
    <li><a href="#topico1">Instalar/Configurar</a></li>
    <li><a href="#topico2">settings.py</a></li>
    <li><a href="#topico3">Arquitetura MTV</a></li>
</ol>

<br>
<br>
<br>
<h2 align="center" id="topico1">🔷 Instalar/Configurar 🔷</h2>

<br>
🔹 Podemos começar a configurar o django criando um ambiente virtual com o seguinte comando:

    python3 -m venv .venv

<br>
<br>
🔹 Com a venv criada, devemos iniciá-la com o comando:

    . .venv/bin/activate

<br>
<br>
🔹 E, daí, instalar o Django:

    pip install django

<br>
<br>
🔹 Com o Django instalado, podemos dar início ao nosso projeto com o comando:

    django-admin startproject mysite .

É necessário incluir o ponto no fim do comando para que a estrutura de arquivos seja gerada no seu diretório atual.

<br>
<br>
🔹 Os comandos anteriores criam esta estrutura de diretórios:

<br>
<div align="center">
    <img src="./readme-img/img01.png">
</div>

<br>
<br>
🔹 Para rodar o servidor de desenvolvimento, executamos o seguinte comando:

    python manage.py runserver

Executando o comando acima, você verá uma saída parecida com esta:

<br>
<div align="center">
    <img src="./readme-img/img02.png">
</div>

<br>
Com isso você pode visitar a página inicial do servidor de desenvolvimento pelo link: http://127.0.0.1:8000/

<br>
<br>
🔹 Para criar seu aplicativo, verifique se você está no mesmo diretório que o arquivo "manage.py" e digite o comando:

    python manage.py startapp phonebook

Note que "phonebook" é o nome da minha aplicação. Você deve substituí-lo pelo nome que desejar.

<br>
O Comando acima cria uma nova estrutura de diretórios:

<br>
<div align="center">
    <img src="./readme-img/img03.png">
</div>

É essa estrutura que abrigará o seu aplicativo.

<br>
<br>
<br>
<h2 align="center" id="topico2">🔷 settings.py 🔷</h2>

<br>
<br>
🔹 Agora registre seu aplicativo no mysite/settings.py:

<br>
<div align="center">
    <img src="./readme-img/img04.png">
</div>

<br>
<br>
🔹 Aproveitando que estamos no arquivo settings.py, vamos aproveitar para configurar outras informações:

<br>
<br>
🔻 Timezone e linguagem são definidas no fim do arquivo.

<br>
<div align="center">
    <img src="./readme-img/img05.png">
</div>

Encontrei um repositório muito interessante que fala um pouco sobre o timezone, sem falar que no próprio arquivo há um link (possível ver no print acima) que leva a documentação oficial:

<br>
@marinho
<br>
🔗 https://github.com/marinho/aprendendo-django/blob/master/apendice-09-fusos-horarios.md

<br>
<br>
🔻 Para subir o projeto para o GitHub, criei um arquivo chamado testing.py e guardei lá algumas informações mais sensíveis — como a chave secreta e informações sobre o meu banco de dados. Então importei as variáveis que usaria do testing no início do settings.

<br>
<div align="center">
    <img src="./readme-img/img06.png">
</div>

<br>
E ficaram assim:

<br>
<div align="center">
    <img src="./readme-img/img07.png">
    <img src="./readme-img/img08.png">
</div>

<br>
<br>
🔻 Para o meu banco de dados usei o MariaDB. Se você quiser usar o MariaDB ou MySQL, pode usar algo parecido com:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'seu_projeto',
            'USER': 'seu_usuário_do_banco_de_dados',
            'PASSWORD': 'sua_senha',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

Mas é necessário instalar o driver mysqlclient que é uma interface para o servidor de banco de dados MySQL/MariaDB que fornece uma API do servidor de banco de dados Python.

    pip install mysqlclient

<br>
<br>
<br>
<h2 align="center" id="topico3">🔷 Arquitetura MTV 🔷</h2>

<br>
<h3 align="center">Model | Template | Views</h3>

<br>
O Model é o arquivo que contém a estrutura lógica do projeto e funciona como um intermediário para manipular dados entre o banco de dados e a View. Dentro do arquivo Model é determinado quais tipos de dados, como será armazenado dentro do seu banco e <b>como será exibido quando for requisitado pela View</b> (ou seja, o papel da view é formatar os dados que são vindos do banco através da Model para visualização). O model é a única e definitiva fonte de informações sobre seus dados. Ele contém os campos e comportamentos essenciais dos dados que você está armazenando. Django segue o princípio DRY (Don’t repeat yourself). O objetivo é definir o seu modelo de dados em um só lugar e automaticamente derivar coisas dele. O Template cuida da parte de visualização para o usuário final. Ele é como o front-end de sua aplicação. Nesta arquitetura, esta camada fica armazenado os arquivos html, css, javascript...

<br>
<br>
<br>
<h2 align="center" id="topico3">🔷 Models 🔷</h2>
