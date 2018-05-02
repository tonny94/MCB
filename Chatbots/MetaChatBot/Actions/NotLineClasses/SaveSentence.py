#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CSaveSentence(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot


    def exec(self,):
        if self.chatbot.unrecognizedSentence is None:
            print('ERROR: No hay sentencia que guardar.')
        else:
            key = ''
            value = ''
            if self.chatbot.unrecognizedSentence is None:
                value= self.chatbot.currentIntent.tag
                key = self.chatbot.unrecognizedSentence
            else:
                value = self.chatbot.unrecognizeIntent
                key = self.chatbot.unrecognizedSentence


            self.chatbot.saveUnrecognizedSentence(key,value)
            print('Se ha guardado la sentencia "',key,'"')

    def addNoReconocido(self, nombChatbot):
        #self.dictionary[nombChatbot][0].append(self.sentence)
        print('Se ha anhadido la sentencia a la lista de error.')
