# Docker Containers

## Docker
Docker es una plataforma para desarrolladores y administradores de sistemas para desarrollar, implementar y ejecutar aplicaciones con contenedores.

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

## Mi primer container
```bash
# Para lanzar mi primer el contenedor
docker run -d --name my-first-container hello-world

# Para listar mis contenedores
docker ps

# Para listar mis imagenes de contenedores
docker image ls
```
