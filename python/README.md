# Docker + Python + Flask

Utilizamos el comando build para crear nuestra imagen del contedor

```PowerShell
# La opcion -t la utilizamos para darle un nombre a nuestra imagen y el . le indica a docker la carpeta en la que se va a trabajar.
docker build -t test_py . 
```

Para iniciar nuestro contenedor utilizando la imagen que acabamos de crear ejectuamos el siguiente comando:

```PowerShell
# La opcion -d le indica a docker que estaremos corriendo nuestro contenedor como Daemon, en background.
# La opcion --name se utiliza para darle un nombre a nuestro contenedor y la opcion -p es para crear un port forwarding con nuestro contenedor
docker run -d -p 8080:80 --name testing test_py

# En caso de querer pasarle una variable de entorno a nuestro contenedor utilizamos la opcion -e seguida con el nombre de la variable.
docker run -d -e NAME=Gabriel -p 8080:80 --name testing test_py
```
