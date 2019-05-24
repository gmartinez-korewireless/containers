# Docker Containers

## Docker
Docker es una plataforma para desarrolladores y administradores de sistemas para desarrollar, implementar y ejecutar aplicaciones con contenedores bajo un esquema de "Integración Contínua" y "Envío Contínuo" (CI/CD).

## Contenedores
La contenedorización es cada vez más popular porque los contenedores son:

*Flexible:* Incluso las aplicaciones más complejas se pueden transportar en contenedores.
*Lightweight:* los contenedores aprovechan y comparten el núcleo del host.
*Interchangeable:* puede implementar actualizaciones y actualizaciones sobre la marcha.
*Portable:* puede compilar localmente, implementarlo en la nube y ejecutar en cualquier lugar.
*Scalable:* puede aumentar y distribuir automáticamente réplicas de contenedor.
*Stackable:* puede apilar servicios verticalmente y sobre la marcha.

## Contenedores y máquinas virtuales.

Un contenedor se ejecuta de forma nativa en Linux y comparte el kernel de la máquina host con otros contenedores. Ejecuta un proceso discreto, no ocupa más memoria que cualquier otro ejecutable, lo que lo hace liviano.

Por el contrario, una máquina virtual (VM) ejecuta un sistema operativo "invitado" completo con acceso virtual a los recursos del host a través de un hipervisor. En general, las máquinas virtuales proporcionan un entorno con más recursos de los que necesitan la mayoría de las aplicaciones.

<img width="300" alt="Containers" src="https://docs.docker.com/images/Container%402x.png"/>
<img width="300" alt="Virtual Machine" src="https://docs.docker.com/images/VM%402x.png"/>

## Mi primer contenedor
```bash
# Para descargar una image sin ejecutarla
docker pull <image_name>

# Para lanzar mi primer el contenedor
docker run --name my-first-container hello-world

# Para lanzar mi primer el contenedor desacoplado de la terminal.
docker run -d --name my-first-container hello-world

# Para lanzar mi primer el contenedor desacoplado de la terminal .
docker run -d --name my-first-container -p <desired_port>:<Source_port> hello-world

# Para listar mis contenedores
docker ps

# Para listar mis contenedores aun asi no esten ejecutandose
docker ps -a 

# Para listar mis imagenes de contenedores
docker image ls
```
