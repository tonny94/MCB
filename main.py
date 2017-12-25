from ChatBotProcessor import *

print('dentro del main')

processor = ChatBotProcessor()

processor.setInten('lista_compra','lista_compra.json')
#processor.preparateModel('lista_compra','lista_compra.json')
processor.preparateResponse('lista_compra')

processor.classify('Hola')
processor.classify('Quiero introducir un item')

#fallara porque no le paso el json, solo la ruta y el nombre, peo no la estructura JSON
processor.response('Quiero anhadir un item')