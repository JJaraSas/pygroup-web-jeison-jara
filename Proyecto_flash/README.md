# AUTRIZACIÓN y AUTENTICACIÓN

## OAuth2 :calling:
OAuth 2.0 es un estándar abierto para la autorización de APIs, que nos permite compartir información entre sitios sin tener que compartir la identidad. 

Es un mecanismo utilizado a día de hoy por grandes compañías como Google, Facebook, Microsoft, Twitter, GitHub o LinkedIn, entre otras muchas.

Utiliza diferentes flujos de autenticación, como el flujo de código de autorización, el flujo de propietario de la contraseña, el flujo implícito, entre otros, así como la extensión de flujos, que también nos permiten definir nuevos flujos.

### Funcionamiento
Supongamos que un usuario tiene una cuenta en Facebook o Twitter, y quiere acceder a otra plataforma, pero sin tener que registrarse. En este caso esa aplicación puede pedir al usuario que se autentique en Facebook o Twitter, y si considera que la información a la que le da acceso es correcta, le te podría permitir realizar un conjunto cerrado de acciones dentro de su plataforma.

De esa manera, esa plataforma de terceros no tendría por qué tener ese nombre de usuario ni la contraseña almacenados, sobre todo siendo un nombre de usuario y contraseña de otro servicio distinto, como podría ser alguna de estas redes sociales.

### Roles
Dentro de OAuth 2.0 encontramos diferentes roles que van a participar en el proceso:

 * #### Dueño del recurso (Owner):
 Se trata del usuario. Se le llama el propietario de los recursos porque, si bien la API no es tuya los datos que maneja si lo son.
 * #### Cliente (Client): 
 La aplicación que quiere acceder al recurso que está protegido, en nombre de alguien. Este cliente puede ser una aplicación web, móvil, de escritorio, para Smart TV, un dispositivo IoT, etcétera.
 * #### Servidor de recursos protegidos (Resource Server):
 El recurso al que queremos acceder, una API.
 * #### Servidor de autorización (Authorization Server):
 Es el responsable de gestionar las peticiones de autorización.
 
 
## OpenID :scroll:
Con OAuth y los diferentes flujos que tenemos para obtener un token, podemos ver que este no es perfecto y que tiene carencias frente a algunas necesidades. Por ejemplo:

* Solo es un framework de autorización
* No es capaz de identificar a los usuarios

OpenID Connect está pensado para la autenticación y OAuth para la autorización. Este añade las siguientes funcionalidades que complementan a OAuth:

* Un ID token que nos permite saber quién es el usuario.
* Un nuevo endpoint, UserInfo, que nos permite recuperar más información del usuario.
* Un conjunto de scopes estándar.
* Un conjunto de claims que nos permite obtener datos del sujeto.

### ID token
Este nos va a proporcionar información sobre el usuario del cual estamos recibiendo la autorización. Esta información viene en formato JWT o JSON Web Token, el cual es un estándar, que pretende transmitir de manera segura información entre dos partes en formato JSON. Esta información puede ser verificada, ya que normalmente está digitalmente firmada.

### UserInfo
Una vez que tienes un ID token puedes usar este mismo para recuperar más información acerca del usuario:
```
HTTP/1.1 200 OK
Content-Type: application/json

 {
   "sub": "248289761001",
   "name": "Jane Doe",
   "given_name": "Jane",
   "family_name": "Doe",
   "preferred_username": "j.doe",
   "email": "janedoe@example.com",
   "picture": "http://example.com/janedoe/me.jpg"
}
```

### Hybrid Flow
Con OpenID Connect aparece además un nuevo flujo llamado Hybrid Flow. Se trata de una combinación entre el Authorization Code Flow y el Implicit Flow. Dependiendo del response_type que solicites, podrás recuperar algunos tokens desde el authorization endpoint y otros desde el token endpoint. Este tipo se utiliza cuando quieres que el usuario tenga acceso inmediato al token de identidad (id_token), pero también quieres hacer llamadas al back end para intercambiar un código de autorización por un token de acceso. El tipo de respuesta debe tener de forma obligatoria el tipo code y cualquiera de las siguientes combinaciones:

* response_type=code token
* response_type=code id_token
* response_type=code id_token token


## SAML Authentication :bookmark_tabs:
La autenticación SAML es un método de verificación de identidad que aprovecha un proveedor de identidades para autenticar a los usuarios de forma centralizada en una amplia gama de sitios web no afiliados. Al transmitir el proceso de autenticación a un único proveedor de identidad de confianza, las organizaciones obtienen numerosos beneficios de seguridad, administración y ahorro de costos y, sobre todo, liberan a los usuarios de la necesidad de mantener docenas de nombres de usuario y contraseñas diferentes.

### Componentes SAML
SAML tiene diversas utilidades. Una de sus funciones es la de hacer declaraciones sobre las propiedades y autorizaciones de un usuario para otros usuarios o empresas asociadas, pero en especial sobre aplicaciones, es decir, a los "proveedores de servicios".

#### Aserciones
Una aserción SAML es el documento XML creado por el proveedor de identidad que envía al proveedor de servicios, y puede contener una o más declaraciones. De hecho, existen tres tipos diferentes de aserciones SAML, que se especifican en SAML 2.0: autenticación, atributo y decisión de autorización.

#### Protocolos
La especificación SAML 2.0 define un conjunto de protocolos de consulta / respuesta. A través de ellos, la aplicación puede solicitar o consultar una aserción, o bien solicitar a un usuario que se autentifique.

#### Bindings
Las asignaciones de mensajes SAML en los protocolos estándar de mensajería o comunicación se denominan "enlaces de protocolo SAML" o simplemente "enlaces". Por ejemplo, el enlace SOAP define cómo se pueden intercambiar mensajes SAML dentro de entornos SOAP, mientras que el enlace de redireccionamiento HTTP define cómo se pueden transportar los mensajes del protocolo SAML mediante el reenvío HTTP.

#### Perfiles
Una de las principales cualidades de SAML es su gran flexibilidad, que facilita su uso para una amplia variedad de propósitos. No obstante, hay que tener en cuenta que esa flexibilidad puede ser la causa de que algunas aplicaciones no lo admitan. Aunque en estos casos existe una solución que consiste en limitarla. La forma de hacerlo es usar los llamados perfiles. En general, un perfil de SAML define restricciones y / o extensiones en apoyo del uso de SAML para una aplicación en particular; su finalidad es mejorar la interoperabilidad al eliminar parte de la flexibilidad inevitable en un estándar de uso general.

## Referencias
[Qué es OAuth 2](https://openwebinars.net/blog/que-es-oauth2/)   
[OAuth 2.0, OpenID Connect y JSON Web Tokens (JWT) ¿Qué es qué?](https://www.returngis.net/2019/04/oauth-2-0-openid-connect-y-json-web-tokens-jwt-que-es-que/)   
[¿Qué es SAML?](https://www.nts-solutions.com/blog/saml-que-es.html)
