# -*- coding: utf-8 -*-
import ChatBotProcessor
#*obser = unicode(self.edit_observ.toPlainText())*
#* obser1 = obser.encode('utf-8')*
import curses


import MetaChatBot


print('dentro del main')
#processor = ChatBotProcessor.CBProcessor()



#GENERA EL MODELO-TRAINER
#processor.preparateModel('metachatbot','metachatbot.json','prueba')

#GENERA EL RESPONSE
#processor.preparateResponse('metachatbot','metachatbot.json','prueba')
#
#processor.classify('Hola')
#
#processor.response('Quiero añadir un chatbot')



#METACHATBOT


metacb = MetaChatBot.MetaChatBot()
metacb.iniciarResponseClass('metachatbot','metachatbot.json','prueba')
#metacb.response('Quiero añadir un chatbot')
#metacb.MCBResponse('Hola')
#metacb.MCBResponse('Quiero añadir un chatbot')



sentence = ''
while not (sentence=='s'):
    sentence = input()
    if not(sentence is 's'):
        metacb.response(sentence)











