from ChatBotProcessor import *
from Trainer import  *

print('dentro del main')

"""
entrenador = Model()

entrenador.readJSON('chatbotprocessor.json','chatbotprocessor')
entrenador.createElementsToModel()
entrenador.trainingModel('prueba1_mcb_')
entrenador.doPickle()
"""



processor = ChatBotProcessor('prueba1_mcb_')

#processor.setInten('chatbotprocessor','chatbotprocessor.json')
processor.preparateResponse('chatbotprocessor','chatbotprocessor.json')

processor.classify('Hola')

processor.response('Quiero añadir un chatbot')