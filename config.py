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
USER = "jirili localhost libres.irc-hispano.org :jirili"

# CANAL al que se asocia el bot.
CHANNEL = "#tty"

# SERVICIOS ofrecidos por el bot.
SERVICIOS = "acerca de, ayuda [comando], quit, quote [add], saluda, url [numero]|[palabra]"

# PASSWORD para desconectar el bot.
QUITPWD = "tarantino"

# FICHEROS de url, quotes y demas. Ambos son ficheros de texto plano.
URLS_FILE = "/home/jors/.pyircbot2/urls.txt"
QUOTES_FILE = "/home/jors/.pyircbot2/quotes.txt"

# MODULOS a activar/desactivar.
M_AYUDA = 1
M_SALUDA = 1
M_QUOTE = 1
M_URL = 1
M_ACERCADE = 1
M_QUIT = 1
M_URLCATCHER = 1
M_STATS = 1
