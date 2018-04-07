#! /bin/bash
# -*- coding: utf-8 -*-

import os
import MetaChatBot



#GENERA EL MODELO-TRAINER
#processor = ChatBotProcessor.CBProcessor()
#processor.preparateModel('metachatbot','metachatbot.json',os.getcwd()+'\\metachatbot\\tmp')

#GENERAR MODELO - RESOLUTOR
# resolutor = Resolutor()
# resolutor.startTrainerClass()#'resolutor','/chatbotResolverErrores/chatbotresolvererrores.json')





#METACHATBOT



"""
"""
print (os.getcwd()+'\\metachatbot')
metacb = MetaChatBot.MetaChatBot()
# metacb.startTrainerClass('metachatbot', 'metachatbot.json', os.path.join(os.sep, os.getcwd(), 'MetaChatBot'))
metacb.startResponseClass('metachatbot','metachatbot.json',os.path.join(os.sep, os.getcwd(), 'MetaChatBot'))

sentence = ''
while not (sentence=='s'):
    sentence = input('=>')
    if not(sentence is 's'):
        metacb.classify(sentence)
        metacb.response(sentence)



"""
PROBLEMAS:
1.- si supera el umbral y es erroneo: no puedo reconocer la siguiente sentencia (ERROR) como si fuese un intent ya que 
se ejecuta el input en una clase aparte.
2.- ejecutar chatbots hijos: trainer y response a la vez
3.- al ejecutar un chatbot hay que tener programado todas su lista de acciones (no se puede instanciar un objeto directamente)
3.1.- el fichero .py de cada chatbot que se quiera ejecutar tiene que 

DUDAS:
1.- Intenciones por defecto: saveSentences (afirmativo, negative) ???? , 
2.- la lista de reconocidos es para cada chatbot o está en una variable del CBProcessor?????


FALTA:
2.- intencion ejecutar chatbot
4.- terminar chatbot resolutor
"""







"""

 
**Posible fallo: se empieza a ejecutar el Response antes de que termine de ejecutarse el Trainer(modelo)

#########

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







nuevo chatbot
Backend Qt5Agg is interactive backend. Turning interactive mode on.
[('crearChatBot', 0.97326082)]
Que chatbot quiere anhadir?

Lista_Compra
[('error', 0.34604287)]
El ChatBot Lista_Compra se ha añadido correctamente.

chatbot actual
[('mostrarActualChatBot', 0.99797946)]
Chatbot activado: Lista_Compra

crear chatbot
[('crearChatBot', 0.98794109)]
Que chatbot quiere anhadir?

Compra_Online
[('error', 0.34604287)]
El ChatBot Compra_Online se ha añadido correctamente.

actual chatbot
[('mostrarActualChatBot', 0.99797946)]
Chatbot activado: Compra_Online

cambiarChatBot
[('error', 0.34604287)]
No se ha reconocido la frase.
Que queire hacer: 
G -> guardar la frase 
N -> no hacer nada 

G
[('error', 0.34604287)]
Se ha anhadido la sentencia a la lista de error

Otro chatbot
[('cambiarChatBot', 0.99061567)]
Seleccione el nombre del chatbot

Lista_Compra
[('error', 0.34604287)]
Chatbot actual: Lista_Compra

nueva intencion
[('crearIntent', 0.99181807)]
Digame el nombre de la intencion

anhadirItem
[('error', 0.34604287)]
El Intent anhadirItem se ha añadido correctamente.

nuevo pattern
[('crearPattern', 0.99282128)]
Que pattern quiere crear?

nuevo item de la compra
[('error', 0.83908486)]
El Pattern nuevo item de la compra se ha añadido correctamente.

nuevo response
[('crearResponse', 0.9969427)]
Que response quiere crear?

digame el item que desea anhadir
[('crearIntent', 0.44244176), ('crearPattern', 0.27432156)]
El Response digame el item que desea anhadir se ha añadido correctamente.

generar json
[('toJSON', 0.999345)]

"""






