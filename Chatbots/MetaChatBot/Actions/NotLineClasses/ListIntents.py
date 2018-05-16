#Clases de acciones
from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine

class CListIntents(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay ningun ChatBot actual para listar sus Intents.')
        else:
            self.chatbot.currentStructureChatBot.printDictIntents()
