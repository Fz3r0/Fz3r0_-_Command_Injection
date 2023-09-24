

## CANTO I: Configurar Proxy e instalar SSL certificate en Firefox

Para que `Burp Suite` funcione correctamente debemos **configurar el Proxy Local en nuestro navegador favorito e instalar un Certificado** (hablaremos de esto también en esta publicación), recomendamos que sea `Mozilla Firefox`. 

### Parte 1: Configurar Proxy en Firefox:

Antes que nada hay que desplazarnos hacia el menú para configurar el Proxy:

1. En nuestro navegador favorito tenemos que configurar el Proxy por defecto de Burp Suite, por ejemplo si utilizáramos Firefox seria en la parte de `Preferences (General) > Network Settings`, aunque es más sencillo solo hacer una búsqueda con la palabra `proxy` y dar click en `settings`:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/5fe624b4-439b-4749-aa33-b9903529f96b)

2. Configurar el `Proxy` con los siguientes datos:

````py
Proxy HTTP:  127.0.0.1
Port:        8080
````
![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/dc9ea442-a67a-4752-a88c-d9dee06316bf)

---

### Parte 2: Instalar Certificados SSL:


Para esta parte hay que instalar el certificado que Burp Suite provee. Esto servirá para interceptar el tráfico `HTTPS` sin problemas:

1. Con Burp Suite en ejecución, abriremos un Tab en Firefox y luego navegaremos el sitio **`http://burp`** esto nos permitirá conectarnos a Burp Suite para descargar el certificado autofirmado, haciendo clic en `CA Certificate`.

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/493d50b9-0069-46f3-bf5d-acbf864c5c28)

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/758e54c5-67ce-4eb7-aea1-84dd173ec211)

2. Aceptamos el archivo que se descargará: `cacert.der`

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/4526f84c-ce5f-44b8-9245-2d41529aa1b9)

3. Habiendo descargado el archivo, necesitamos instalarlo. Desde Firefox esto se encuentra en `Preferences (Privacy & Security) > Certificates` o simplemente buscando `certificates`:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/6cd8bd0c-58a3-4873-96a0-ffd3a12e07c6)

4. En el menu que se desplegara hacemos clic en `Import`.

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/af55505c-c6a0-437e-91c8-d2940f203028)

5. Agregamos el `cacert.der` que descargamos previamente y nos preguntará para qué queremos usarlo. Marcamos la primera opción: `Trust this CA to identify websites`.

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/0032d0e5-464a-4961-8441-a312fcaa387e)

¡Listo! Con esta configuración ya podemos comenzar a interceptar el tráfico entre Burp Suite y Firefox sin problemas.

## Recursos

- [ArtsSEC - Configuración de Burpsuite con Foxy Proxy](https://medium.com/@ArtsSEC/burp-suite-configuraci%C3%B3n-del-proxy-88b7b90355f2)
- [Instalar y Configurar FoxyProxy para Burp Suite, CA Certificate (SSL)](https://www.youtube.com/watch?v=lqfUclxl0K0)