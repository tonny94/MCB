#! /bin/bash
# -*- coding: utf-8 -*-

import os
from ChatBotProcessor import CBProcessor
from Chatbots.MetaChatBot.MetaChatBot import CMetaChatBot

# import keras
# import sys
# import tensorflow as tf
# print("pyton: {}, keras: {}".format(sys.version,keras.__version__))

#METACHATBOT
mcb = CMetaChatBot()
cbp = CBProcessor(mcb)
cbp.startModel()
cbp.startPredictor()
cbp.run()

"""
FALLOS:
1.- Tras ejecutar un chatbot desde el MEtaChatbot, se sale de la ejecucion siempre que no sea una palabra del un pattern
2.- No genera el código de las acciones de un nuevo chatbot en la ejecucion, pero tras cerrar el programa y abrirlo al dia siguiente los
ficheros si se habían creado
3.- Los chatbots creados no pueden ejecutar el SolveError por el tema de bucle en las llamadas de los imports


IDEAS
1.- Para la ejecucion del SolveError, se podría ejecutar desde el metachatbot pasandole la estructura de un chatbot (se tendría que crear otra intencion
 para que pudiese recibir el chatbot que se quiere resolver), se necesita saber la lista de intenciones (que se puede cojer de la estructura del chatbot),
 la lista de errores (que se obtendría del fichero de errores tras ejecutar el chatbot); pero no se sabe la ruta del chatbot -> se tendría que poner la ruta
 teniendo en cuenta que el SolveError esta en la misma carpeta que los otros chatbots y se concatenaría con la palabra clave del fichero de errores.
 Para ejecutar el cahtbot de SolveError se ejecutaría primero el metachatbot
 
 2.- Se podría generar el chatbot SolveError fuera del metachatbot para su ejecución independiente, se obtendría el nombre del chatbot que se quiera resolver 
 con una una intencion, la ruta se obtendría igual que la idea 1, para la lista de intenciones se leeria el json del chatbot, similar al que hace el metachatbot 
 para cargar la structura de todos los chatbots
"""



"""
Falta guardar los errores en el fichero, los errores resueltos en otro fichero (o solo imprimir la resolucion sin guardarlo)
"""




