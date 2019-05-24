# Docker + Python + Flask

Utilizamos el comando build para crear nuestra imagen del contedor

```PowerShell
# La opcion -t la utilizamos para darle un nombre a nuestra imagen
# El punto (.) le indica a docker que trabajaremos en la carpeta actual.
# Estructura del commando docker build -t <Nombre de nuestra imagen> . 
docker build -t test_py . 
```

Para iniciar nuestro contenedor utilizando la imagen que acabamos de crear ejectuamos el siguiente comando:

```PowerShell
# La opcion -d le indica a docker que estaremos corriendo nuestro contenedor como Daemon, en background.
# La opcion --name se utiliza para darle un nombre a nuestro contenedor
# La opcion -p es para crear un port forwarding con nuestro contenedor
# Estructura del comando docker run -d -p <Puerto mi maquina>:<Puerto del contenedor> --name <Nombre del contenedor> <Nombre de la imagen>
docker run -d -p 8080:80 --name testing test_py

# En caso de querer pasarle una variable de entorno a nuestro contenedor utilizamos la opcion -e 
# seguida con el nombre de la variable. Cambiar el valor Gabriel por el nombre de su preferencia
# Estructura de la opcion de variable de entorno: -e <Nombre de la variable>=<Valor de la variable> 
docker run -d -e NAME=Gabriel -p 8080:80 --name testing test_py
```

En caso de querer crear un segundo contenedor con nuestra imagen, necesitamos utilizar un puerto diferente y un nombre de contenedor diferente:
```PowerShell
docker run -d -p 8081:80 --name testing2 test_py
```

### Comandos de uso frecuente
```PowerShell
# Para listar nuestros contenedores
docker ps

# Para listar nuestros imagenes
docker image ls

# Para detener un contenedor
# Estrcutura del commando docker stop <Nombre del contenedor>
docker stop testing2

# Para detener un contenedor
# Estrcutura del commando docker start <Nombre del contenedor>
docker start testing2

# Para eliminar un contenedor
# Estrcutura del commando docker rm <Nombre del contenedor>
docker rm testing2
```