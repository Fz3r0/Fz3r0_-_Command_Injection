# ¿Cómo encontrar vulnerabilidad CMDI?

Existen 3 perspectivas diferentes, y depende de cómo se enfrentará el escenario para decidir cuál camino tomar _(en ocasiones se deberá tomar metodologías personales que más se adapten a un escenario en particular, por ejemplo buscar otras vulnerabilidades OWASP al mismo tiempo)_:

1. `Blackbox Test`: Se tiene poca o nada de información respecto a la App, es básicamente emular un ataque real desde "fuera" realizado por un intruso. 
2. `Whitebox Test`: Tenemos el código fuente para poder hacer pruebas de seguridad y se tiene información y documentación.
3. `Graybox Test`: Se tiene información y acceso limitados al sistema _(Una especie de combinación de las 2 anteriores)._

## `Black Box Testing`

Si bien cada escenario es diferente y la experiencia juega un gran papel en esta perspectiva, existen ciertos tips que puedan ayudar para encontrar esta vulnerabilidad:

### 1. `Application Maping` 

Identificar todas las instancias donde la WebApp indique que está interactuando con un sistema operativo por detrás:

- Visitar la URL de la aplicación y enumerar todos los directorios y/o subdominios posibles.
- Buscar cualquier página que sea accesible via pública para visitar dentro de la URL.
- Buscar vectores donde se puedan realizar `inputs` de datos.
- Entender un poco del `backend` de la aplicación, entendiendo cómo podría estar funcionando.
- Tratar de razonar la lógica de la aplicación
- **Al mismo tiempo que hago esto, tengo activado mi `proxy` _(Burpsuite + FoxyProxy)_ para interceptar todos los `request` que hago hacia la aplicación.**

### 2. `Application Fuzzing` 

Una vez que tengamos algún campo que consideremos podría ser vulnerable, es hora de hacer `fuzzing` con `payloads` diseñados para CMDI, es decir, `shell metacharacters`:

- **Nota**: Depende del Sistema Operativo y el tipo de shell es el comando que se inyecta, no es lo mismo el `CMD Windows` que `Bash Linux`

````sh
# Command Injection payloads:

## Chain commands: encadena comandos unos con otros

&
&&
|
||

## Separator commands: separa comandos unos de otros

;
\n
`
$()

````

### 3. `Response Analyze` _(For In-Band CMDI only)_ 

En caso que la respuesta que arroje el comando de un resultado que indique una vulnerabilidad, se podrá seguir forjando el comando necesario para explotar el sistema.

- En unos escenarios es suficiente inyectar un payload seguido de un comando para visualizar un resultado esperado, por ejemplo `;` + `ls`
- En otros escenarios es un poco más complicado ya que algunos caracteres o comandos pueden estar bloqueados, para esto hay que hacer `fuzzing` con una serie de `payloads`.
- En ocasiones se verán respuestas directas, en otras se podría ver un `error`, esto también podría ser explotado. 

### 4. `Blind CMDI Testing` 

En estos casos hay que ser más creativos... 

- Una manera "colmilluda" de detectar Cblind CMDI es utilizar los comandos `ping` o `sleep` para utilizar el tiempo como medida de detección _(Muy similar al time-based SQLi)_
- Para tener el `output` se deben hacer cosas un poco más complejas, como exportarlas en un archivo y descargarlas via web para exfiltrar los datos. 

## `White Box Testing`

### 1. `Source Code review` 


## Recursos

- [Port Swigger - Command Injection](https://portswigger.net/web-security/os-command-injection)
- [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- [OWASP - Command Injection Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [OWASP - Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)


