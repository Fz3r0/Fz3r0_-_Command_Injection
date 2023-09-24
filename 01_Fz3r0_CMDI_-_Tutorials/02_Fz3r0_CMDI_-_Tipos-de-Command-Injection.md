# Tipos de Command Injection 

Existen 2 tipos de CMDI:

1. In-Band Command Injection
2. Blind Command Injection

Las 2 funcionan basicamente igual, la única diferencia es que en una se pueden ver los resultados del comando a simple vista, en la otra no. 

## In-band Command Injection 

Es el tipo de CMDI donde el atacante puede inyectar comandos en la máquina víctima a travéz de una WebApp vulnerable y **recibe una respuesta del comando visiblemente a travéz de la aplicación.**

## Blind Command Injection 

Es el tipo de CMDI donde el atacante puede inyectar comandos en la máquina víctima a travéz de una WebApp vulnerable y **NO recibe una respuesta del comando mediante el HTTP response recibido.**
