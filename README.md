Test academia de mágia python
Aplicación python para administrar solicitudes de estudiantes a la academia de mágia construído principalmente con fastapi y sqlite. se utilizó un entorno virtualizado por medio de ubuntu 22.04 LTS y con el editor visual code

requermientos:
- ubuntu 22.04.2 LTS
- python 3 instalado en ubuntu
- virtualenv y virtualenvwrapper instlado en ubuntu
- pip3 instalado en ubuntu
- visual code

instalación:
1.- desde ubuntu LTS crear un directorio para almacenar el proyecto, posicionarnos en ella y abrir visual code
        mkdir academia_magia
        cd academia_magia
        code .

2.- en visual code dirigirse a "source control", selecciona clone y ingresar la siguiente url:
        https://github.com/isma-rn/academia_magia.git

3.- al seleccionar "clone https://github.com/isma-rn/academia_magia.git" pedira un directorio, ahi seleccionamos el creado en el paso 2 y damos "ok"

4.- abrimos terminal y creamos un entorno virtual:
        mkvirtualenv academia_magia
5.- instalamos dependencias:
        pip install -r requirements.txt
6.- ejecutamos aplicacion
        uvicorn gestionacademia.main:app --reload
7.- en un navegador web ingresamos a la siguiente url 
        http://127.0.0.1:8000/docs
