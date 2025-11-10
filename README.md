para acceder en la url se pone la ip y /numero  
ej: http://127.0.0.1:5000/18  

### ¿Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa?  

Si el microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa, tendría que incluir una llamada HTTP al finalizar cada operación, entonces después de calcular el factorial y generar la respuesta, se envían los datos obtenidos (el número, el factorial y la etiqueta) a otro servicio mediante una petición usando la librería requests. De esta manera, se encargaría solo del cálculo y delegaría el almacenamiento al otro servicio.
