

import ChatBotProcessor
#from Trainer import *
#import Trainer

print('dentro del main')

"""
entrenador = ChatBotProcessor.CBProcessor()
entrenador.preparateModel('metachatbot','metachatbot.json','prueba1_mcb_')
# entrenador.readJSON('metachatbot.json','metachatbot')
# entrenador.createElementsToModel()
# entrenador.trainingModel('prueba1_mcb_')
# entrenador.doPickle()

"""
processor = ChatBotProcessor.CBProcessor()

#processor.setInten('metachatbot','metachatbot.json')
processor.preparateResponse('metachatbot','metachatbot.json','prueba1_mcb_')

processor.classify('Hola')

processor.response('Quiero añadir un chatbot')
