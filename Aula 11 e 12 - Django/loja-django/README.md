# SISTEMA LOJA - DJANGO #

### 1. Crie o Repositorio para organizar o projeto

### 2. Crie e ative o ambiente virtual 
python -m venv .env
.\.env\Script\activate

### Instale as Dependencias
pip install django
pip install Pillow   

### Crie o projeto (core) e os apps
django-admin startproject <nome-projeto> .
django-admin startapp <nome-app>

### Desenvolva
- crie os modelos dentro do app
- adicione o app criado em settings 
- implemente o modelo no arquivo admin.py do app 


### Executar
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py createsuperuser
python .\manage.py runserver

### Crie o requeriments.txt 
 pip freeze > requeriments.txt

 ### Continar o Desenvolvimento

