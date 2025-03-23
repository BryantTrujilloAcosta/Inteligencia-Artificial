# INTELIGENCIA ARTIFICIAL 9-10

## TAREA 8
### Detección de Spam con razonamiento monótono
## Objetivo: 
- Desarrollar un sistema para detectar correos electrónicos no deseados
(spam) utilizando razonamiento monótono

## Funcionamiento
Esta Tabla muestra un resumen breve de lo que se consideraria correo spam y lo que no.
| Remitente  | Asunto                    | Mensaje                          | Enlaces           | Archivos adjuntos |   Spam |
|------------|---------------------------|----------------------------------|-------------------|-------------------|--------|      
|Desconocido| !Oferta  increíble!        | Gana dinero rápido.              | URL:malware.com   |URL:<br>malware.com|**Sí.** |   
| amigo      | Reunión<br> mañana        | Te veo a las 10:00               |                   |                   |**No.** |
| Empresa    | Nuevo <br> Producto.      | Presentamos nuestro producto     | URL:istmo.tecnm.mx|                   |**No**  |
| Banco      | Aviso importante          | Presentamos nuestro producto     | URL:FraudeSpain.es|                   |**Sí**  | 
