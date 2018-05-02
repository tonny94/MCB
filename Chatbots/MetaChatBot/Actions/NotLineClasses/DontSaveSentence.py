#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDontSaveSentence(ActionLine):

    def __init__(self,chatbotProcessor):
        self.chatbotProcessor = chatbotProcessor

    def exec(self,):
        if self.chatbotProcessor.currentRunningChatbot.unrecognizedSentence is None:
            print('No hay una sentencia.')
        else:
            print('No se ha guardado la sentencia "',self.sentence,'".')