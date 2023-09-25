# Fz3r0 OWASP - Configuración Inicial de Burpsuite

Para configurar Burpsuite ya sea en Linux o Windows e interceptar tráfico HTTP/HTTPS desde cualquier explorador solo se deben seguir 3 sencillos pasos:

1. **`CANTO I`: Configurar Proxy e instalar SSL certificate en Firefox**
2. **`CANTO II`: Instalación y configuración de Foxy Proxy**
3. **`CANTO III`: Interceptar Tráfico**

A continuación se muestra el paso a paso del proceso:

## CANTO I: Configurar Proxy e instalar SSL certificate en Firefox

Para que `Burp Suite` funcione correctamente debemos **configurar el Proxy Local en nuestro navegador favorito e instalar un Certificado** (hablaremos de esto también en esta publicación), recomendamos que sea `Mozilla Firefox`. 

### `Parte 1`: Configurar Proxy en Firefox:

Antes que nada hay que desplazarnos hacia el menú para configurar el Proxy:

1. En nuestro navegador favorito tenemos que configurar el Proxy por defecto de Burp Suite, por ejemplo si utilizáramos Firefox seria en la parte de `Preferences (General) > Network Settings`, aunque es más sencillo solo hacer una búsqueda con la palabra `proxy` y dar click en `settings`:

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/5fe624b4-439b-4749-aa33-b9903529f96b" alt="burpsuite_install" height=320px/> </a> </p> 

2. Configurar el `Proxy` con los siguientes datos:

````py
Proxy HTTP:  127.0.0.1
Port:        8080
````

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/dc9ea442-a67a-4752-a88c-d9dee06316bf" alt="burpsuite_install" height=580px/> </a> </p> 

### `Parte 2`: Instalar Certificados SSL:


Para esta parte hay que instalar el certificado que Burp Suite provee. Esto servirá para interceptar el tráfico `HTTPS` sin problemas:

1. Con Burp Suite en ejecución, abriremos un Tab en Firefox y luego navegaremos el sitio **`http://burp`** esto nos permitirá conectarnos a Burp Suite para descargar el certificado autofirmado, haciendo clic en `CA Certificate`.

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/493d50b9-0069-46f3-bf5d-acbf864c5c28"burpsuite_install" height=400px/> </a> </p> 

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/758e54c5-67ce-4eb7-aea1-84dd173ec211" height=250px/> </a> </p> 


2. Aceptamos el archivo que se descargará: `cacert.der`

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/4526f84c-ce5f-44b8-9245-2d41529aa1b9"/> </a> </p> 

3. Habiendo descargado el archivo, necesitamos instalarlo. Desde Firefox esto se encuentra en `Preferences (Privacy & Security) > Certificates` o simplemente buscando `certificates`:

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/6cd8bd0c-58a3-4873-96a0-ffd3a12e07c6" height=450px/> </a> </p> 

4. En el menu que se desplegara hacemos clic en `Import`.

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/af55505c-c6a0-437e-91c8-d2940f203028" height=400px/> </a> </p> 

5. Agregamos el `cacert.der` que descargamos previamente y nos preguntará para qué queremos usarlo. Marcamos la primera opción: `Trust this CA to identify websites`.

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/0032d0e5-464a-4961-8441-a312fcaa387e)

¡Listo! Con esta configuración ya podemos comenzar a interceptar el tráfico entre Burp Suite y Firefox sin problemas.



## CANTO II: Instalación y configuración de Foxy Proxy

1. Instalar la extensión de `Foxy Proxy` en Fiefox simplemente buscándola en google o el siguiente link:
- https://addons.mozilla.org/es/firefox/addon/foxyproxy-standard/

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/e941b24e-4f7f-4ea6-a7ba-e21c07917e56)

2. Se recomienda ponerlo como pin en el Firefox para tenerlo a la mano, después ir a la parte de `options`:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/5c69ceae-129d-48b8-9ac3-4f9d10b343fe)

3. Dar click en `add` para añadir un nuevo Proxy:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/673600c5-fecc-4af0-97ed-377960cf8fa4)

4. Configurar con los parámetros del Proxy que creamos anteriormente y guardar:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/defa926c-d201-4c73-a40a-c3e4b24f67fb)

5. Validar que se haya creado el Proxy:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/b6325914-e16f-4b94-8ec1-888b17b4ab76)

6. ¡Listo! Ahora ya se puede utilizar este nuevo Proxy:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/685a876b-32bf-4e82-8f27-06c6f827058c)


## CANTO 3: Interceptar Tráfico

Para validar que funcione correctamente solo es necesario ir a la pestaña de `Proxy` dentro de `Burpsuite` y encender la función de `intercept`.

- Entrar a la pestaña `Proxy` y encender el `intercept`:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/c78c8404-d134-4218-a2fe-fe05f839246a)

- Al navegar a cualquier URL se interceptará el tráfico como el siguiente `POST` de Google:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/6c8ff49d-7626-498b-9e91-bcd59600769e)

¡Listo! a interceptar tráfico como si fuera el útlimo día... Se está tornando oscuro, muy oscuro... 

## Recursos

- [ArtsSEC - Configuración de Burpsuite con Foxy Proxy](https://medium.com/@ArtsSEC/burp-suite-configuraci%C3%B3n-del-proxy-88b7b90355f2)
- [Instalar y Configurar FoxyProxy para Burp Suite, CA Certificate (SSL)](https://www.youtube.com/watch?v=lqfUclxl0K0)
