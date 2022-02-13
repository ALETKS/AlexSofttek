# AlexSofttek


REPOSITORIO CON LOS TRES PROYECTOS DE BACKEND.
Para su funcion seguir paso a paso.

## PRIMEROS PASOS
- IDLE Visual Studio Code
-  Base de datos en Mysql :  El uso para estos proyectos se creo con PhpMyAdmin en Localhost
    - Generar unicamente las bases de datos vacias con los siguientes nombres:
     - 1- CREATE DATABASE customer_order_status;
     - 2- CREATE DATABASE detecting_change;
     - 3- CREATE DATABASE season_problem;


  
  
 ## 1 Entorno Virtual
 - Agregar una de las tres carpeta a Visual Studio Code
 - Abrir terminal (este debe mostrar la ubicacion de la carpeta) y Ejecutar:
```bash
  virtualenv -p python3 env
```
- NOTA: Ahora la carpeta env debe estar junto la carpeta del proyecto
- para entrar al entorno, acceder ejecutando
```bash
  .\env\Scripts\activate
```
-NOTA: la consola esta activado si al principio de su terminal muestra como : (env) 

## 2 ACCEDER al PROYECTO
Ejecutar el comando "cd .\Elproyecto"  dependiendo de la carpeta que lo contenga, ejemplo:
| carpeta           | comando                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Documents\Customer Order Status>     | cd .\CustomerOrderStatus\  |

 ## 3 Instalar Django 3.2.4
 - Con el entorno virtual activado Ejecutar:
```bash
 pip install django==3.2.4
```
 ## 4 Instalar Conectores de Base de Datos
 - Con el entorno virtual activado Ejecutar:
```bash
pip install mysqlclient pymysql
```
 ## 5 Instalar Pandas
 - Con el entorno virtual activado Ejecutar:
```bash
pip install --upgrade  pandas
```

 ## 6 Migraion de datos y Servicio de Servidor
 - Con el entorno virtual activado Ejecutar:
```bash
python manage.py migrate
```
- Si desea verificar que se creo la migracion, en la base de datos con nombre a el proyecto abierto se creo una tabla con iniciales "api_"
- Para terminar y arrancar el Servicio ejecutar
```bash
python manage.py runserver
```
  


VER COMENTARIOS PARA EJECUTAR LOS INSERT DE CADA TABLA DE LA BASE DE DATOS. ESTO PARA PROBAR LA API




@Este repositorio fuen hecho en agradecimiento al equipo de Softtek, 
