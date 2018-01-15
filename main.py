# -*- coding: utf-8 -*-
import ChatBotProcessor
#*obser = unicode(self.edit_observ.toPlainText())*
#* obser1 = obser.encode('utf-8')*

print('dentro del main')
processor = ChatBotProcessor.CBProcessor()



#GENERA EL MODELO-TRAINER
# processor.preparateModel('metachatbot','metachatbot.json','prueba')

#GENERA EL RESPONSE
processor.preparateResponse('metachatbot','metachatbot.json','prueba')
#
processor.classify('Hola')
#
processor.response('Quiero añadir un chatbot')
