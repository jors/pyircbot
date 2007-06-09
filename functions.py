#!/usr/bin/python
# coding: iso-8859-15

import socket,os,string,sys,linecache,random,time
import config

### METAFUNCIONES ###
#####################
def isInt(str):
   """Is the given string an integer?"""
   try:int(str)
   except ValueError:return 0
   else:return 1

### FUNCIONES ###
#################

def crea_stats(s):
   fp = open(config.LOG_FILE, 'r')
   lines = fp.readlines() # lines es una list de urls
   fp.close()

   nicks = []
   apariciones = []

   for i in lines:
      split = i.split(':')
      split2 = split[2].split('!')

      if(split2[0] in nicks):
         pos = nicks.index(split2[0])
         apariciones[pos] = apariciones[pos] + 1
         #print split2[0]+" ya esta en la lista! Tiene "+str(apariciones[pos])+" entradas."
      else:
         #print "Agregando "+split2[0]+" al array general."
         nicks.append(split2[0])
         apariciones.append(1)

   j = 0
   #s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,"Loros del canal:"))
   for i in nicks:
      s.send("PRIVMSG %s :%s - %s lineas.\r\n" % (config.CHANNEL,i,apariciones[j]))
      time.sleep(1)
      j = j + 1

def ayuda(s, line):
   list = line.split('ayuda')

   if(list[1].strip() == ''):
      s.send("PRIVMSG %s :Uso: %s: servicio\r\n" % (config.CHANNEL,config.NICK))
      s.send("PRIVMSG %s :Lista de servicios: %s\r\n" % (config.CHANNEL,config.SERVICIOS))
   elif(list[1].strip() == 'acerca de'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_ACERCADE))
   elif(list[1].strip() == 'quit'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_QUIT))
   elif(list[1].strip() == 'quote'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_QUOTE))
   elif(list[1].strip() == 'saluda'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_SALUDA))
   elif(list[1].strip() == 'url'):
      s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,config.SERVICIO_URL))
   else:
      s.send("PRIVMSG %s :Opción no reconocida.\r\n" % (config.CHANNEL))

def registra_linea(line):
   if(line.find("PRIVMSG "+config.CHANNEL) != -1):
      line = line.replace(" PRIVMSG ", "")
      line = line.replace(config.CHANNEL, "")
      fp = open(config.LOG_FILE, 'a')
      fp.write(time.strftime("%Y-%m-%d:%H-%M-%S")+line+'\n')
      fp.close()

def espia_url(line):
   if(line.find("PRIVMSG "+config.CHANNEL) != -1):
      list = line.split(' ')
      for i in list:
         if((i.find('http://') != -1) or (i.find('ftp://')) != -1):
	         fp = open(config.URLS_FILE, 'a')
	         fp.write(i+'\n')
	         fp.close()
	         break

def lee_urls(s, line):
   # Lee y muestra las urls almacenadas.
   list = line.split('url')
   fp = open(config.URLS_FILE, 'r')
   lines = fp.readlines() # lines es una list de urls
   fp.close()

   if(isInt(list[1])):
      req_urls = int(list[1]) # requested urls
      avail_urls = int(len(lines)) # available urls
      if(req_urls <= avail_urls):
         url_start = avail_urls - req_urls
         lines = lines[url_start:avail_urls] # seleccionamos un rango de elementos, elem inicial:final
         for i in lines:
	        s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,i))
	        time.sleep(2) # Bug#3.
      else:
         s.send("PRIVMSG %s :Petición fuera de rango! Sólo hay %s urls!\r\n" % (config.CHANNEL,len(lines)))
   else:
      # Busqueda de texto.
      for i in lines:
         if(i.find(list[1].strip()) != -1):
            s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,i))
            time.sleep(2) # Bug#3.

def anyade_quote(s, line):
   list = line.split('quote add')
   if(list[1] != ''):
      fp = open(config.QUOTES_FILE, 'a')
      fp.write(list[1]+'\n')
      fp.close()
      s.send("PRIVMSG %s :Quote añadido! \r\n" % (config.CHANNEL))
   else:
      s.send("PRIVMSG %s :Debes especificar una cadena como quote! \r\n" % (config.CHANNEL))

def lee_quote(s):
   # Leer una random quote.
   fp = open(config.QUOTES_FILE, 'r')
   lines = fp.readlines() # lines es una list de quotes
   fp.close()
   elems = len(lines)
   rand_num = random.randint(0,elems-1)
   s.send("PRIVMSG %s :%s\r\n" % (config.CHANNEL,lines[rand_num]))

def salir(s, line):
   if(line.find(config.QUITPWD) != -1):
      s.send("PRIVMSG %s :Chao!\r\n" % config.CHANNEL)
      #s.close();
      sys.exit(1)
   else:
      s.send("PRIVMSG %s :Reservado a los privilegiados.\r\n" % config.CHANNEL)

def mostrar_salida(s):
   recvd = s.recv(4096)
   if config.DEBUG == 1:
      print "Recibido: "+recvd

def mandar_pong(s):
   recvd = s.recv(4096)
   recvd = recvd.replace("PING", "PONG")
   s.send(recvd+'\r\n')
