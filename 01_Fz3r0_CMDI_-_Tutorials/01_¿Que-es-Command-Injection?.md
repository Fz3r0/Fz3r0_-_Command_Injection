# Command Injection

## ¿Qué es?

- La inyección de comandos es un ataque en el que el objetivo es ejecutar comandos arbitrarios en el sistema operativo host a través de una aplicación vulnerable.
- Los ataques de inyección de comandos son posibles cuando una aplicación pasa datos proporcionados por el usuario de manera insegura (formularios, cookies, encabezados HTTP, etc.) a una shell del sistema.
- En este tipo de ataque, los comandos del sistema proporcionados por el atacante suelen ejecutarse con los privilegios de la aplicación vulnerable.
- Los ataques de inyección de comandos son posibles en gran medida debido a una validación insuficiente del `input`.
- Este ataque difiere de la Inyección de Código (Code Injection) en el sentido de que la inyección de código permite al atacante agregar su propio código que luego es ejecutado por la aplicación. En la Inyección de Comandos, el atacante extiende la funcionalidad predeterminada de la aplicación, ejecutando comandos del sistema, sin la necesidad de inyectar código.

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
$ ./catWrapper Story.txt
Yo soy Fz3r0 y este es un string guardado en un .txt...
````

Sin embargo, si agregamos un punto y coma `;` y otro comando al final de esta línea, el comando se ejecuta en el binario `catWrapper` sin problemas, como cualquier one liner de bash script, por ejemplo `$ ./catWrapper "Story.txt; ls"`:

````sh
$ ./catWrapper "Story.txt; ls"
Cuando los dejamos por última vez a nuestros héroes...
Story.txt               doubFree.c              nullpointer.c
unstosig.c              www*                    a.out*
format.c                strlen.c                useFree*
catWrapper*             misnull.c               strlength.c             useFree.c
commandinjection.c      nodefault.c             trunc.c                 writeWhatWhere.c
````

Si `catWrapper` se hubiera configurado con un nivel de privilegio más alto que el usuario estándar (por ejemplo `root`), se podrían ejecutar comandos arbitrarios con ese mayor privilegio.
