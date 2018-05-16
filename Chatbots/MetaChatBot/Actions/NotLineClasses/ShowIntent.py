#Clases de acciones
from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales

class CShowIntent(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot= chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay Chatbot actual para mostrar su Intent actual.')
        else:
            self.chatbot.currentStructureChatBot.printCurrentIntent()
