# -*- coding: utf-8 -*-
import ChatBotProcessor
#*obser = unicode(self.edit_observ.toPlainText())*
#* obser1 = obser.encode('utf-8')*
import curses


import MetaChatBot

processor = ChatBotProcessor.CBProcessor()

#GENERA EL MODELO-TRAINER
#processor.preparateModel('metachatbot','metachatbot.json','prueba')

#GENERA EL RESPONSE
#processor.preparateResponse('metachatbot','metachatbot.json','prueba')
#
#processor.classify('Hola')
#
#processor.response('Quiero añadir un chatbot')



#METACHATBOT

"""
"""
metacb = MetaChatBot.MetaChatBot()
metacb.iniciarResponseClass('metachatbot','metachatbot.json','prueba')

sentence = ''
while not (sentence=='s'):
    sentence = input()
    if not(sentence is 's'):
        metacb.classify(sentence)
        metacb.response(sentence)





"""
si no entiende la frase:

 1.- que lo guarde y luego lo liste para guardarlo en intens -> accion: resolver
 2.- que diga que no lo reconocio y de opciones de guardarlo -> "no lo reconozco, diga que es {intent,acciont,pattern}"
 3.- "no lo he reconocido" (opciones):->"guardar, olvidar, esperar a que diga lo que es (con aciones : definir_insercion)"
 
cada chatbot tiene que tener una intetncion: SALIR  - Listo - Problema: la clase no tiene esa accion por defecto, habra que 
ponerla a mano por cada chatbot que se cree. Si se ejecuta un chatbot se tendrá que tener YA CREADA las acciones correspondientes...
como se hace?????

4.- poder cambiar de chatbot, intencion - Listo
5.- mostrar chatbot, intencion actual   - Listo
6.- metodos toJSON

#########
pasar a JSON una clase:  -  Listo
clase chatbot tiene metodo "toJSON"
en la clase INTENS(hay que recorrerlo)
se llamara al toJSON del chatbot que recorrerá todos los itents y cada intent tendrá su toJSON





nuevo chatbot

[('crearChatBot', 0.96070927)]
Que chatbot quiere crear?

Lista_Compra

[]
El ChatBot Lista_Compra se ha añadido correctamente.

chatbot actual

[('mostrarActualChatBot', 0.55726904), ('cambiarChatBot', 0.41205144)]
Chatbot activado: Lista_Compra

crear chatbot

[('crearChatBot', 0.97605604)]
Que chatbot quiere anhadir?

Compra_Online

[]
El ChatBot Compra_Online se ha añadido correctamente.

actual chatbot

[('mostrarActualChatBot', 0.55726904), ('cambiarChatBot', 0.41205144)]
Chatbot activado: Compra_Online

nueva intencion

[('crearIntent', 0.97215533)]
Que intencion quiere anhadir?

anhadirItem

[]
El Intent anhadirItem se ha añadido correctamente.

listar intenciones

[('listarIntent', 0.97653246)]
Intents: [ salirChatbot,anhadirItem ]

actul intencion

[('mostrarActualIntent', 0.97502089)]
Intencion activada: anhadirItem

listar patterns

[('mostrarPattern', 0.98581463)]
Pattern: [ ]

crear pattern

[('crearPattern', 0.9771319)]
Que pattern quiere anhadir?

que item desea anhadir

[('mostrarResponse', 0.64883029)]
El Pattern que item desea anhadir se ha añadido correctamente.

nuevo response

[('crearResponse', 0.97977602)]
Que response quiere crear?

digame el item que desea anhadir

[('mostrarActualChatBot', 0.35232401), ('listarChatBot', 0.28926972)]
El Response digame el item que desea anhdir se ha añadido correctamente.

borrar pattern

[('borrarPattern', 0.98784047)]
Digame que pattern quiere borrar

que item desea anhadir

[('mostrarResponse', 0.64883029)]
El Pattern que item desea anhadir se ha eliminado correctamente .

nuevo pattern

[('crearPattern', 0.98254138)]
Que pattern quiere crear?

nuevo item

[('toJSON', 0.40056661)]
El Pattern nuevo item se ha añadido correctamente.

crear json




"""






