# administrador-predios

Esta prueba esta realizada con Python Django y PostgreSql.

# Capas
El proyecto se divide en dos capas principales
  - Capa backend: consta de una base de datos postgreSql conectada con el framework Django.
  - Capa frontend: consta de una pagina web realizada en html y css, esta es administrada por Django tanto las URLs como sus correspondientes renderizados.
 
### Instalacion

Para ejecutar esta aplicacion require: 
  - Python3
  - PostgreSql
  - Django 
 
Para tener la base de datos conectada con Django debe revisar el archivo __settings.py__ que se encuentra en la carpeta /administrador/administrador.
En la linea 79 encontrara la siguiente estructura que pertence a la configuracion de base de datos de Django.
  
-DATABASES = { 	
   - 'default': {	
       - 'ENGINE': 'django.db.backends.postgresql_psycopg2',	
       - 'NAME': 'DataBase',	
       - 'USER': 'postgres',	
       - 'PASSWORD': '__INSERTE AQUI CONTRASEÑA DE SU USUARIO POSTGRES__',	
       - 'HOST': 'localhost',	
       - 'PORT': '5433',	
   - }	
 - }	
 
A continuacion corra postgresql y cree una base de datos llamada __DataBase__ (aqui Django creara las tablas y almacenara los registros).
Asegurece de que la base de datos creada este en el puerto __5433__ .
 
Ahora debe realizar las migraciones desde su editor de codigo o terminal para que Django cree las modelos en Postgresql:
 - $ Python manage.py makemigrations
 - $ Python manage.py migrate


### Para ejecutar
Posteriormente corra el programa: 
 - $ Python manage.py runserver

La web se desplegara en le puerto 8000


### Como usar
La pagina web cuenta con un sistema CRUD (Create, Read, Update, Delete):
  - Para agregar haga click en el boton __agregar__ que lo llevara a los formularios.
  - Para ver los registros realizado haga click en el boton __ver todos__ .   
  - Para editar, ver mas o borrar haga click en la opcion que desee.
  - Para buscar utilice la barra de busqueda.
  - La web cuenta con paginacion, para ver la siguiente tabla o la anterior haga uso de los botones inferiores (solo son visibles cuando existan mas de 5 filas).

### M.E.R.
Uso de muchos a muchos para la relacion entre tablas.




