#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CSaveSentence(ActionLine):

    def __init__(self,chatbotProcessor):
        self.chatbotProcessor = chatbotProcessor


    def exec(self,):
        if self.chatbotProcessor.currentRunningChatbot.unrecognizedSentence is None:
            print('ERROR: No hay sentencia que guardar.')
        else:
            key = self.chatbotProcessor.currentIntent
            value = self.chatbotProcessor.currentRunningChatbot.unrecognizedSentence
            self.chatbotProcessor.currentRunningChatbot.saveUnrecognizedSentence(key,value)

    def addNoReconocido(self, nombChatbot):
        #self.dictionary[nombChatbot][0].append(self.sentence)
        print('Se ha anhadido la sentencia a la lista de error.')
