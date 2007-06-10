#!/usr/bin/python
# coding: iso-8859-15

### VARIABLES ###
#################

# DGBUG info; booleano para activarlo/desactivarlo.
DEBUG = 1

# NICKNAME del bot.
NICK = "jirili"

# SERVER de IRC al que conectarlo y el puerto.
SERVER_NAME = "libres.irc-hispano.org"
SERVER_PORT = "6667"

# ident del bot.
USER = NICK+" localhost libres.irc-hispano.org :"+NICK

# CANAL al que se asocia el bot.
CHANNEL = "#tty"

# SERVICIOS ofrecidos por el bot.
SERVICIOS = "acerca de, ayuda [comando], quit, quote [add], saluda, stats, url [numero]|[palabra]"
SERVICIO_ACERCADE = "Muestra una breve descripcion del bot."
SERVICIO_QUIT = "Desconecta el bot; requiere ciertos privilegios."
SERVICIO_QUOTE = "Muestra un quote aleatorio. Con el parametro add seguido de una frase, añade un quote."
SERVICIO_SALUDA = "Muestra un saludo. Saluda a un destino concreto con un parametro final."
SERVICIO_SALUDA = "Muestra una pequeña estadistica del canal."
SERVICIO_URL = "Muestra urls. Necesita un parametro. Si este es un número N, muestra las N ultimas urls. Si es una cadena, hace una busqueda de las urls que la contengan para mostrarlas."

# PASSWORD para desconectar el bot.
QUITPWD = "tarantino"

# FICHEROS de url, quotes y demas. Ambos son ficheros de texto plano.
BASE = "/home/jors/.pyircbot2/"
URLS_FILE = BASE+"/urls.txt"
QUOTES_FILE = BASE+"/quotes.txt"
LOG_FILE = BASE+CHANNEL+".log"

# MODULOS a activar/desactivar.
M_AYUDA = 1
M_SALUDA = 1
M_QUOTE = 1
M_URL = 1
M_ACERCADE = 1
M_QUIT = 1
M_URLCATCHER = 1
M_LOGGING = 1
M_STATS = 1
