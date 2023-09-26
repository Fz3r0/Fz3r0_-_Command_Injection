# Lab: OS command injection, simple case

Este laboratorio contiene una vulnerabilidad de **inyección de comandos** en el verificador de existencias de productos.

La aplicación ejecuta un comando de shell que contiene identificadores de productos y tiendas suministrados por el usuario, y devuelve la salida sin procesar del comando en su respuesta.

Para resolver el laboratorio, ejecuta el comando `whoami` para determinar el nombre del usuario actual.

## Solución

- Para este laboratorio es necesario `Burpsuite`.
- Para la solución se explotará `in-band` CMDI, esto debido a que se verá el resultado en pantalla.

### Paso 1: Buscar el POST


- Para esto es más sencillo apagar el Proxy y navegar por la página utilizando la pestaña de HTTP history
- Para esto se necesita utilizar el navegador de Burpsuite:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/1d938207-5232-4c17-bdc3-21c0fe59d69b)

- Al seleccionar cualquier `button` se registra un REQUEST o POST. 



## Recursos

- Lab: https://portswigger.net/web-security/os-command-injection/lab-simple
