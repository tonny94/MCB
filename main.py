#! /bin/bash
# -*- coding: utf-8 -*-

import os
from ChatBotProcessor import CBProcessor
from Chatbots.MetaChatBot.MetaChatBot import CMetaChatBot
from Chatbots.SolveError.SolveError import CSolveError

#META CHATBOT
mcb = CMetaChatBot()
cbp = CBProcessor(mcb)
cbp.startModel()
cbp.startPredictor()
cbp.run()



#SOLVE ERROR
# se = CSolveError()
# cbp = CBProcessor(se)
# cbp.startModel()
# cbp.startPredictor()
# cbp.run()

"""
FALLOS:
1.- Tras ejecutar un chatbot desde el MEtaChatbot, se sale de la ejecucion siempre que no sea una palabra del un pattern
2.- No genera el código de las acciones de un nuevo chatbot en la ejecucion, pero tras cerrar el programa y abrirlo al dia siguiente los
ficheros si se habían creado

"""


"""

interaction
    -2 atributos : input, output
    - metodo: __init__
   
python metodos, variables de clase "@staticmethod".

ejecutar nuevo chatbot desde metachatbot.

realizar un SolveError separado. - TERMINAR DE PROBAR

crear un ejemplo de "Lista_Compra" funcional.

el nombre del chatbot, acciones -> quitar tildes, ñ, y espacios. - POSIBLES PROBLEMAS

"""




"""
1.- Que se muestre la solucion (sentencia e intent) del SolveError - PROBAR
2.- no admitir vacios en las acciones que esperan una sentencia
3.- el problema de sustitución de "ñ y tildes" en los nombres de ficheros/carpetas y la clave del JSON
"""