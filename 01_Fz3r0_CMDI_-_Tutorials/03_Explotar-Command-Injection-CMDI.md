# Fz3r0 OWASP 💀🐝 - Command Injection 💉

## 💀 ¿Cómo explotar vulnerabilidad CMDI?

Una vez que se encontró la vulnerabilidad `in-band` o `blind` se procede a explotar de las siguientes maneras: 

### 💥 `In-Band CMDI: exploitation`

1. Utilizar `shell metacharacters`

````sh
## General deny list to be included for command injection:
| ; & $ > < ' \ ! >> #

## Escape or filter special characters for --->>> Windows
( ) < > & * ‘ | = ? ; [ ] ^ ~ ! . " % @ / \ : + , `

## Escape or filter special characters for --->>> Linux
{ } ( ) > < & * ‘ | = ? ; [ ] $ – # ~ ! . " %  / \ : + , `

````



## 📖 Recursos

- [Port Swigger - Command Injection](https://portswigger.net/web-security/os-command-injection)
- [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- [OWASP - Command Injection Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [OWASP - Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [Udemy - Rana Khalil | Command Injection ](https://www.udemy.com/course/mastering-command-injection-the-ultimate-hands-on-course/learn/lecture/39297722#overview)
