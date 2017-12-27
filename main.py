from ChatBotProcessor import *
from Trainer import  *

print('dentro del main')

""""""
entrenador = Model()

entrenador.readJSON('metachatbot.json','metachatbot')
entrenador.createElementsToModel()
entrenador.trainingModel('prueba1_mcb_')
entrenador.doPickle()



"""
processor = ChatBotProcessor('prueba1_mcb_')

#processor.setInten('metachatbot','metachatbot.json')
processor.preparateResponse('metachatbot','metachatbot.json')

processor.classify('Hola')

processor.response('Quiero añadir un chatbot')
"""