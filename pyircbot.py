#!/usr/bin/python
# coding: iso-8859-15

"""
pyircbot2 - Bot pythoniano de IRC, Feb'07, by qat.
Parte del codigo 'pillado' de un texto de o'Reilly:
   http://www.oreilly.com/pub/h/1968
Public License.

----------
Changelog:
----------

06 Jun'07 - Modificación funcionalidad de mostrar urls. Sin argumentos no se muestran todas,
            y es posible pasarle un string en lugar de un nº para hacer busquedas de url.

05 Jun'07 - Adición funcionalidad de logging para aplicar stats (stats TBD yet).

04 Jun'07 - División del proyecto en 3 ficheros: main, funciones y configuraciones.
          - Adición de otro modo de llamada al bot; puede ser bot: accion y bot accion.
          - Sustitución de hardcoded strings por otros dinámicos.

21 Mar'07 - Bug#3. sleep() para controlar flood urls. No, no recuerdo los 2 anteriores.

27 Feb'07 - Adición funcionalidad grabar quotes.
          - Adición funcionalidad mostrar X últimas urls.

Mediados de Feb'07 - Script principal.

"""

import socket,os,string,sys,linecache,random,time
import functions,config

### MAIN ###
############

# Create socket & connect to IRC server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(config.DEBUG):
	print 'Connecting to server...'
s.connect((config.SERVER_NAME, int(config.SERVER_PORT)))

# Mandamos datos iniciales...
if(config.DEBUG):
   print 'Sending NICK...'
s.send('NICK %s\r\n' % config.NICK)
functions.mostrar_salida(s)
functions.mandar_pong(s)

if(config.DEBUG):
   print 'Sending USER...'
s.send('USER %s\r\n' % config.USER)
functions.mostrar_salida(s)

if(config.DEBUG):
   print 'Sending JOIN...'
s.send('JOIN %s\r\n' % config.CHANNEL)
functions.mostrar_salida(s)

readbuffer = ""

while 1:

   """
   Reads a maximum of 1024 bytes from the server and appends it
   to the readbuffer. You need a readbuffer because you might 
   not always be able to read complete IRC commands from the server.
   """
   readbuffer=readbuffer+s.recv(1024)
   # En temp tenemos el mogollon sin el \n.
   temp=string.split(readbuffer, "\n")
   """
   The read buffer is then split into a list of strings, using \n
   as a separator. The last line in this list is possibly a 
   half-received line, so it is stored back into the read buffer.
   """
   readbuffer=temp.pop()

   for line in temp:
      """
      Before we're able to process the lines from the read buffer
      in a normal manner, there's one thing left to do. You need
      to remove the trailing \r character from the end of the lines.
      """
      line=string.rstrip(line)
      line_list=string.split(line)
      
      if(line_list[0]=='PING'):
         if(config.DEBUG):
            print 'PING received, sending PONG...'
            s.send("PONG %s\r\n" % line_list[1])
    
      # ayuda #
      if(config.M_AYUDA):
         if((line.find(config.NICK+': ayuda') != -1) or (line.find(config.NICK+' ayuda') != -1)):
            s.send("PRIVMSG %s :Uso: %s: servicio\r\n" % (config.CHANNEL,config.NICK))
            s.send("PRIVMSG %s :Lista de servicios: %s\r\n" % (config.CHANNEL,config.SERVICIOS))

      # saluda #
      if(config.M_SALUDA):
         if((line.find(config.NICK+': saluda') != -1) or (line.find(config.NICK+' saluda') != -1)):
            elems = len(line_list)
            if(line_list[elems-1] == 'saluda'):
	           s.send("PRIVMSG %s :Hola!\r\n" % config.CHANNEL)
            else:
               s.send("PRIVMSG %s :Hola %s\r\n" % (config.CHANNEL,line_list[elems-1]))

      # quote: leer/añadir #
      if(config.M_QUOTE):
         if((line.find(config.NICK+': quote') != -1) or (line.find(config.NICK+' quote') != -1)):
            if((line.find(config.NICK+': quote add') != -1) or (line.find(config.NICK+': quote add') != -1)):
	           functions.anyade_quote(s, line)
            else:
               functions.lee_quote(s)

      # url #
      if(config.M_URL):
         if((line.find(config.NICK+': url') != -1) or (line.find(config.NICK+' url') != -1)):
            functions.lee_urls(s, line)

      # acerca de #
      if(config.M_ACERCADE):
         if((line.find(config.NICK+': acerca de') != -1) or (line.find(config.NICK+' acerca de') != -1)):
            MSG = 'pyircbot2 - Bot pythoniano de IRC, Feb\'07, by qat.'
            s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,MSG))

      # quit #
      if(config.M_QUIT):
         if((line.find(config.NICK+ ': quit') != -1) or (line.find(config.NICK+ ' quit') != -1)):
            functions.salir(s, line)

      # url catcher #
      if(config.M_URLCATCHER):
         if((line.find('http:') != -1) or (line.find('ftp:') != -1)):
            functions.espia_url(line)

      # stats #
      if(config.M_STATS):
         functions.registra_linea(line)
