# Docker + Python + Flask + SQL Server

Para iniciar nuestros servicios ejecutamos el comando up utilizando la opcion -d para que se ejecuten en background.
```PowerShell
docker-compose up -d
```

En caso de solo querer crear la imagen de nuestro contenedor utilizamos:
```PowerShell
docker-compose build
```

Para detener los contenedores ejecutamos
```PowerShell
docker-compose stop
```

En caso de querer escalar un servicio a mas contenedores ejecutamos el siguiente comando:
```PowerShell
docker-compose scale db=2
```

## References
[Docker Compose](https://docs.docker.com/compose/reference/overview/)
[SQL Server Image](https://hub.docker.com/_/microsoft-mssql-server)
[SQL Server reference](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-2017)