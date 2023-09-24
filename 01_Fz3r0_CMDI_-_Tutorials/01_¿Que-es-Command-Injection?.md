# Command Injection

## ¿Qué es Command Injection?

- La inyección de comandos es un ataque en el que el objetivo es ejecutar comandos arbitrarios en el sistema operativo host a través de una aplicación vulnerable.
- Los ataques de inyección de comandos son posibles cuando una aplicación pasa datos proporcionados por el usuario de manera insegura (formularios, cookies, encabezados HTTP, etc.) a una shell del sistema.
- En este tipo de ataque, los comandos del sistema proporcionados por el atacante suelen ejecutarse con los privilegios de la aplicación vulnerable.
- Los ataques de inyección de comandos son posibles en gran medida debido a una validación insuficiente del `input`.
- Este ataque difiere de la Inyección de Código (Code Injection) en el sentido de que la inyección de código permite al atacante agregar su propio código que luego es ejecutado por la aplicación. En la Inyección de Comandos, el atacante extiende la funcionalidad predeterminada de la aplicación, ejecutando comandos del sistema, sin la necesidad de inyectar código.

## Las 2 condiciones que se necesitan para CMDI

Para que una WebApp sea vulnerable a CMDI es necesario que cumpla con 2 condiciones: 

1. La aplicación debe tener una `function` que ejecute comandos del sistema `system commands`
2. Los parámetros de esta función puedan ser controlables por el usuario _(Por ejemplo, que se pueda ingresar un string entre 2 variables)_

Las 2 condiciones se pueden mostrar en el siguiente ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_Command_Injection/assets/94720207/124ffb4b-d821-4383-861d-f156cf39ebeb)

- La `linea 6` se encarga de ejecutar comandos arbitrarios via `client-side input` _(es decir, que los ingresa el cliente manualmente)_
- Debido a que los 2 request son inputs que vienen de 2 variables ingresadas por el cliente _(lineas 4 y 5)_, es tan sencillo como dividir el comando `cat /etc/passwd` en los 2 inputs arbitrarios, en caso de no estar debidamente protegido contra CMDI, se podrá ejecutar el comando en el servidor. 

<br>

<br>

<br>

# Ejemplos de CMDI

A continuación se muestran diferentes escenarios vulnerables a Command Injection:

## Ejemplo 1

El siguiente código es un wrap del comando UNIX `cat`, que imprime el contenido de un archivo en la salida estándar. También es susceptible a inyección:

````c
#include <stdio.h>
#include <unistd.h>

int main(int argc, char **argv) {
 char cat[] = "cat ";
 char *command;
 size_t commandLength;

 commandLength = strlen(cat) + strlen(argv[1]) + 1;
 command = (char *) malloc(commandLength);
 strncpy(command, cat, commandLength);
 strncat(command, argv[1], (commandLength - strlen(cat)) );

 system(command);
 return (0);
}
````

Utilizado normalmente, la salida es simplemente el contenido del archivo solicitado:

````sh
$ ./catWrapper Soy_Fz3r0.txt
Yo soy Fz3r0 y este es un string guardado en un .txt ejecutado con catWrapper...
````

Sin embargo, si agregamos un punto y coma `;` y otro comando al final de esta línea, el comando se ejecuta en el binario `catWrapper` sin problemas, como cualquier one liner de bash script, por ejemplo `$ ./catWrapper "Story.txt; ls"`:

````sh
$ ./catWrapper "Soy_Fz3r0; ls"
Yo soy Fz3r0 y este es un string guardado en un .txt ejecutado con catWrapper...
Story.txt               doubFree.c              nullpointer.c
unstosig.c              www*                    a.out*
format.c                strlen.c                useFree*
catWrapper*             misnull.c               strlength.c             useFree.c
commandinjection.c      nodefault.c             trunc.c                 writeWhatWhere.c
````

Si `catWrapper` se hubiera configurado con un nivel de privilegio más alto que el usuario estándar (por ejemplo `root`), se podrían ejecutar comandos arbitrarios con ese mayor privilegio.



## Ejemplo 2

El siguiente programa simple acepta un nombre de archivo como argumento de línea de comandos y muestra el contenido del archivo al usuario. 
- El programa se instala con `setuid root` porque está destinado a ser utilizado como una herramienta de aprendizaje que permite a los administradores del sistema en formación inspeccionar archivos del sistema con privilegios sin darles la capacidad de modificarlos o dañar el sistema.

````c
int main(char* argc, char** argv) {
 char cmd[CMD_MAX] = "/usr/bin/cat ";
 strcat(cmd, argv[1]);
 system(cmd);
}

````

Dado que el programa se ejecuta con privilegios de `root`, la llamada a `system()` también se ejecuta con privilegios de `root`. 
Si un usuario especifica un nombre de archivo estándar, la llamada funciona como se espera. Sin embargo, si un atacante pasa una cadena en la forma `;rm -rf /`, entonces la llamada a `system()` no puede ejecutar `cat` debido a la falta de argumentos y luego procede a eliminar recursivamente el contenido de la partición raíz, lo que puede causar daños graves en el sistema.



## Ejemplo 3





## Recursos

[OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
