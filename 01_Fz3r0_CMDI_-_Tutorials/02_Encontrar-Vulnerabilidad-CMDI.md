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

## `White Box Testing`

### 1. `Source Code review` 


## Recursos

- [Port Swigger - Command Injection](https://portswigger.net/web-security/os-command-injection)
- [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- - [OWASP - Command Injection](https://owasp.org/www-community/attacks/Command_Injection)


