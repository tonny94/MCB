# -*- coding: utf-8 -*-
import ChatBotProcessor
#*obser = unicode(self.edit_observ.toPlainText())*
#* obser1 = obser.encode('utf-8')*
import curses


import MetaChatBot

#processor = ChatBotProcessor.CBProcessor()



#GENERA EL MODELO-TRAINER
#processor.preparateModel('metachatbot','metachatbot.json','prueba')

#GENERA EL RESPONSE
#processor.preparateResponse('metachatbot','metachatbot.json','prueba')
#
#processor.classify('Hola')
#
#processor.response('Quiero añadir un chatbot')



#METACHATBOT


metacb = MetaChatBot.MetaChatBot()
metacb.iniciarResponseClass('metachatbot','metachatbot.json','prueba')
#metacb.response('Quiero añadir un chatbot')
#metacb.MCBResponse('Hola')
#metacb.MCBResponse('Quiero añadir un chatbot')

"""
"""
sentence = ''
while not (sentence=='s'):
    sentence = input()
    if not(sentence is 's'):
        metacb.response(sentence)






"""
si no entiende la frase:

 1.- que lo guarde y luego lo liste para guardarlo en intens -> accion: resolver
 2.- que diga que no lo reconocio y de opciones de guardarlo -> "no lo reconozco, diga que es {intent,acciont,pattern}"
 3.- "no lo he reconocido" (opciones):->"guardar, olvidar, esperar a que diga lo que es (con aciones : definir_insercion)"
 
cada chatbot tiene que tener una intetncion: SALIR 
#########
pasar a JSON una clase:
clase chatbot tiene metodo "toJSON"
en la clase INTENS(hay que recorrerlo)
se llamara al toJSON del chatbot que recorrerá todos los itents y cada intent tendrá su toJSON

-> ver todos los chatbots
Backend Qt5Agg is interactive backend. Turning interactive mode on.
Chatbots: ]
-> crear chatbot
Que chatbot quiere crear?
-> Lista_Compra
El ChatBot Lista_Compra se ha añadido correctamente.
-> ver todos los chatbots
Chatbots: [Lista_Compra]
-> Listar intenciones
Intents: ]
-> Que patterns  hay creados
"""






