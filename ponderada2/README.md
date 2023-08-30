## Criação de um App de notas dockerizado

Abaixo se encontra o código fonte da aplicação fullstack de um aplicativo de notas utilizando python, o framework Flask para renderização e rotas das paginas e SQLAlchemy para criação e manejo do banco de dados. Para o docker compose foi criado duas imagens, uma da aplicação descrita acima, e outra responsável pelo banco de dados (usando a Imagem oficial do POstgres)
Para o sistema de proteção de rotas, foi utilizado um middleware externo, que usa JWT e Flask, exemplificado no site [Loginradius - securing-flask-api-with-jwt](https://www.loginradius.com/blog/engineering/guest-post/securing-flask-api-with-jwt/) ( Dica do João Carazzato :) )

### Porque da Arquitetura escolhida

Comecei o desenvolvimento pensando na arquitetura de 3 containers, front end em Nextjs, backend e autentificação usando FastAPI e Banco de dados com Postgres. Após finalizar cada parte tive problemas ao integrar, principalmente as rotas protegidas do backend ao tentar acessar pela aplicação em Nextjs. Só consegui recuperar o token de acesso através do swagger do FastAPI, o que basicamente inutilizava minha aplicação. Devido essas dificuldades prefeti refazer a arquitetura e manter apenas em 2 containers. 



### Estrutura de pastas
```
|
|- app
    |
    |- static
        |
        |- style.css
        |
    |
    |- templates
        |
        |- auth
            |- login.html
            |- signup.html
        |- index
            |- index.html
            |- notes.html
            |- postNote.html
        |- layout.html
        |
    |
    |- auth.py
    |- database.py
    |- docker-compose.yml
    |- DockerFile
    |- main.py
    |- requirements.txt
|

```

## Como executar a aplicação?
Com o docker ja instalado, garantimos que ele esta rodando abrindo o Dcoker Hub.

Para iniciar o app, devemos nos estar dentro da pasta 'app' onde está localizado nosso 'docker-compose'

```
cd ponderada2/app
```
Para executar o docker-compose up:

```
docker-compose up
```
Com isso, já temos acesso a aplicação que estará rodando no endereço [http://localhost:5000](http://localhost:5000). Para acesso ao banco de dados use algum gerenciador de banco de dados e acesse com os seguintes parametros:

```
POSTGRES HOST: localhost
POSTGRES DB: postgres
POSTGRES USER: postgres
POSTGRES PASSWORD: password
```
