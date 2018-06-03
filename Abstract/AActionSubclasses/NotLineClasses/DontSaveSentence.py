#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDontSaveSentence(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.unrecognizedSentence is None:
            self.chatbot.output.exec('No hay una sentencia.')
        else:
            self.chatbot.output.exec('No se ha guardado la sentencia "'+self.chatbot.unrecognizedSentence+'".')