# PETICIONES Y RESPUESTAS HTTP MAS COMUNES

## PETICIONES HTTP :calling:
HTTP contiene un grupo de peticiones que ayudan a especificar la accion que requiere realizar a determinado elemento.

### Clasificacion :label:
Las peticiones se pueden clasificar en *Safe* e *Idenpotent*

* #### Peticiones HTTP Safe
  Un metodo HTTP es considerado safe o seguro si no altera el servidor, es decir si es de solo lectura.

* #### Peticiones HTTP Idempotent
  Se considera un metodo HTTP idenpotent si una solicitud identica puede realizarse ona o varias veces consecutivas opteniendo el mismo resultado dejando en el mismo estado al servidor

### Lista de Peticiones HTTP :scroll:

* #### Peticiones HTTP: **GET**
  El método GET significa recuperar cualquier información (en forma de una entidad) identificada por el Request-URI

* #### Peticiones HTTP: **OPTIONS**
  El método OPTIONS representa una solicitud de información acerca de las opciones de comunicación disponibles en el canal de solicitud/respuesta identificada por el Request-URI

* #### Peticiones HTTP: **HEAD**
  El método HEAD es muy similar al GET (funcionalmente hablando), a excepción de que el servidor responde con líneas y headers, pero no con el body de la respuesta.

* #### Peticiones HTTP: **PUT**
  El método PUT es usado para solicitar que el servidor almacene el cuerpo de la entidad en una ubicación específica dada por el URL.

* #### Peticiones HTTP: **POST**
  El método POST es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc.

* #### Peticiones HTTP: **DELETE**
  Este método es utilizado para solicitar al servidor que elimine un archivo en una ubicación específica dada por la URL. 

* #### Peticiones HTTP: **CONNECT**
  Este método por su parte es usado por el cliente para establecer una conexión de red con un servidor web mediante HTTP misma que se establece en forma de un túnel.

* #### Peticiones HTTP: **TRACE**
  Éste método se utiliza para realizar pruebas de eco (de retornos) de mensajes en el camino que existe hacia un recurso determinado.

## RESPUESTAS HTTP :speech_balloon:
Los códigos de estado HTTP describen de forma abreviada la respuesta HTTP. El primer dígito del código de estado especifica uno de los 5 tipos de respuesta, el mínimo para que un cliente pueda trabajar con HTTP es que reconozca estas 5 clases.

### Tipos de Respuestas HTTP :bookmark_tabs:
Este tipo de código de estado indica una respuesta provisional.

* #### 1XX Respuestas informativas
  Este tipo de código de estado indica una respuesta provisional.  
  -**100 Continue.** El servidor ha recibido los headers del request y el cliente debería proceder a enviar el cuerpo de la respuesta.  
  -**101 Switching Protocols.** El requester ha solicitado al servidor conmutar protocolos.
  
* #### 2XX Peticiones correctas
  Este código de estado indica que la acción solicitada por el cliente ha sido recibida, entendida, aceptada y procesada correctamente.  
  -**200 OK.** El request es correcto. Esta es la respuesta estándar para respuestas correctas.  
  -**201 Created.** El request se ha completado y se ha creado un nuevo recurso.  
  -**202 Aceptada.** El request se ha aceptado para procesarlo, pero el proceso aún no ha terminado.  

* #### 3XX Redirecciones
  El cliente ha de tomar una acción adicional para completar el request. Muchos de estos estados se utilizan para redirecciones.  
  -**300 Multiple Choices.** Es una lista de enlaces. El usuario puede seleccionar un enlace e ir a esa dirección. Hay un máximo de cinco direcciones.  
  -**302 Found.** La página solicitada se ha movido temporalmente a una nueva URI.  
  -**304 Not Modified.** Indica que la página solicitada no se ha modificado desde la última petición.  
  
* #### 4XX Errores del cliente
  Excepto cuando se responde a un HEAD request, el servidor debe incluir una entidad que contiene una explicación del error, y si es temporal o permanente.  
  -**400 Bad Request.** El servidor no puede o no va a procesar el request por un error de sintaxis del cliente.  
  -**403 Forbidden.** El request fue válido pero el servidor se niega a responder.  
  -**404 Not Found.** El recurso del request no se ha podido encontrar pero podría estar disponible en el futuro.  
  -**408 Request Timeout.** El cliente no ha enviado un request con el tiempo necesario con el que el servidor estaba preparado para esperar.  

* #### 5XX Errores del servidor
  El servidor ha fallado al completar una solicitud aparentemente válida. Cuando los códigos de estado empiezan por 5 indica casos en los que el servidor sabe que tiene un error o realmente es incapaz de procesar el request.  
  -**500 Internal Server Error.** Error genérico, cuando se ha dado una condición no esperada y no se puede concretar el mensaje.  
  -**502 Bad Gateway.** El server actuaba como puerta de entrada o proxy y recibió una respuesta inválida del servidor upstream.  
  -**503 Service Unavailable.** El servidor está actualmente no disponible, ya sea por mantenimiento o por sobrecarga.  
  
## Referencias
[Códigos de estado HTTP](https://diego.com.es/codigos-de-estado-http)  
[Peticiones HTTP](https://yosoy.dev/peticiones-http-get-post-put-delete-etc/)
