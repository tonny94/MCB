from ChatBotProcessor import *
from Trainer import  *

print('dentro del main')


entrenador = Model()

entrenador.readJSON('chatbotprocessor.json','chatbotprocessor')
entrenador.createElementsToModel()
entrenador.trainingModel('prueba1_mcb')
entrenador.doPickle()




processor = ChatBotProcessor()

#processor.setInten('chatbotprocessor','chatbotprocessor.json')
processor.preparateResponse('chatbotprocessor','chatbotprocessor.json','prueba1_mcb')

processor.classify('Hola')
processor.classify('Quiero introducir un item')

#fallara porque no le paso el json, solo la ruta y el nombre, peo no la estructura JSON
processor.response('Quiero anhadir un item')