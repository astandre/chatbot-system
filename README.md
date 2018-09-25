#chatbot-system
La aplicacion cuenta con tres apps: 
* nluengine
* cursoshandler
* chatbothandler
## nluengine
La aplicacion nluengine es la encargada de resolver los intents y entities de los usuarios.

Para entrenar al sistema en el archivo engine.py existe el metodo train_engine() que entrenara al sistema con los datos
 de la base de datos.

Actualmente el sistema se entrena cada vez que se lanza la aplicacion; si se añaden nuevos intents o entities, deberemos
 reiniciar el sistema para volver a entrenar.

Gracias a django tenemos un admin en el cual podemos editar la informacion manualmente.

Si queremos cargar informacion de manera rapida, lo podemos hacer en la opcion de engine/upload. Debemos tener cuidado
al cargar informacion, ya que el sistema actual no soporta espacios despues de las comas y no soporta otros archivos que
 no sean csv. Podemos ver ejemplos dentro de la carpeta de data. Primero debemos cargar las entities y luego los intents.

**Nota:** Actualmente la base de datos soporta multiples entities en un intent, pero en la carga de datos a la base de datos,
 y en la carga de datos al engine solo soporta un entity.

Para visualizar la informacion que se esta cargando en el engine, lo podemos ver en la pagina knowledge/.

Si queremos usar el engine para que resuelva los intents y entities, debemos hacerlo a traves del endpoint
engine/resolve/, al cual debemos enviar un json de entrada con la key "query"

## Requerimentos
Los requerimientos se encuentran en el archivo requirements.txt,
adcionalmente debemos descargar el complemento de snips para español con el comando

python -m snips_nlu download en


