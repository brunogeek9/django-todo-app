# django-todo-app
Simple todo list project for pratice basic MVT django concepts
## Instaling Guide
### 1. Ambiente virtual
```console
python3 -m venv myvenv
```

### 2. Trabalhando com o virtualenv
```console
source myvenv/bin/activate
```
### 3. Instalando o Django
```console
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Iniciando o servidor web
```console
cd todo/
python3 manage.py runserver
```

### 5. Criar database e User Admin
```console
./init_project.sh
```