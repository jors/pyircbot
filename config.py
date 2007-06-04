#!/usr/bin/python
# coding: iso-8859-15

### VARIABLES ###
#################

# DGBUG info; booleano para activarlo/desactivarlo.
DEBUG = 0

# NICKNAME del bot.
NICK = "jirili"

# SERVER de IRC al que conectarlo y el puerto.
SERVER_NAME = "libres.irc-hispano.org"
SERVER_PORT = "6667"

# ident del bot.
USER = "jirili localhost libres.irc-hispano.org :jirili"

# CANAL al que se asocia el bot.
CHANNEL = "#tty_devel"

# SERVICIOS ofrecidos por el bot.
SERVICIOS = "acerca de, ayuda, quit, quote [add], saluda, url [number]"

# PASSWORD para desconectar el bot.
QUITPWD = "tarariro"

# FICHEROS de url, quotes y demas. Ambos son ficheros de texto plano.
URL_FILE = "/home/jors/.pyircbot2/urls.txt"
QUOTES_FILE = "/home/jors/.pyircbot2/quotes.txt"
