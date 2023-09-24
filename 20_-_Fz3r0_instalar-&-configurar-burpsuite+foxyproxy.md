Para que `Burp Suite` funcione correctamente debemos **configurar el Proxy Local en nuestro navegador favorito e instalar un Certificado** (hablaremos de esto también en esta publicación), recomendamos que sea `Mozilla Firefox`. 

## Instrucciones

Antes que nada hay que desplazarnos hacia el menú para configurar el Proxy:

1. En nuestro navegador favorito tenemos que configurar el Proxy por defecto de Burp Suite, por ejemplo si utilizáramos Firefox seria en la parte de `Preferences (General) > Network Settings`, aunque es más sencillo solo hacer una búsqueda con la palabra `proxy` y dar click en `settings`:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/5fe624b4-439b-4749-aa33-b9903529f96b)

2. Configurar el `Proxy` con los siguientes datos:

````py
Proxy HTTP:  127.0.0.1
Port:        8080
````
![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/dc9ea442-a67a-4752-a88c-d9dee06316bf)

3. Instalar el certificado que Burp Suite provee. Esto servirá para interceptar el tráfico `HTTPS` sin problemas:

2.a Con Burp Suite en ejecución, abriremos un Tab en Firefox y luego navegaremos el sitio http://burp esto nos permitirá conectarnos a Burp Suite para descargar el certificado autofirmado, haciendo clic en CA Certificate.


Aceptamos el archivo que se descargará: cacert.der


2.b Habiendo descargado el archivo, necesitamos instalarlo. Desde Firefox esto se encuentra en Preferences (Privacy & Security) > Certificates.


En el menu que se desplegara hacemos clic en Import.


Agregamos el cacert.der que descargamos previamente y nos preguntará para qué queremos usarlo. Marcamos la primera opción: Trust this CA to identify websites.


Con esta configuración ya podemos comenzar a interceptar el tráfico entre Burp Suite y Firefox sin problemas.

Recuerden que si en Burp Suite, el Proxy > Intercept esta en ON, no podrán ver pasar el tráfico y esperará a que ustedes tomen una acción: Forward, Drop, enviar a otra herramienta.


Cómo cambiar la configuración por defecto en Burp Suite?
Desde Proxy > Options > Proxy Listeners es posible definir otros puertos, generar nuevos certificados, tomar acciones como capturar las respuestas del Server, Match & Replace, etc. En una nueva edición pondremos en práctica esto ;)


Gracias por leernos, compartiremos más entradas para que puedan ir aprendiendo sobre Burp Suite en español.

## Recursos

- [ArtsSEC - Configuración de Burpsuite con Foxy Proxy](https://medium.com/@ArtsSEC/burp-suite-configuraci%C3%B3n-del-proxy-88b7b90355f2)
- [Instalar y Configurar FoxyProxy para Burp Suite, CA Certificate (SSL)](https://www.youtube.com/watch?v=lqfUclxl0K0)
