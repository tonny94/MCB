#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

class CListIntents(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay ningun ChatBot actual para listar sus Intents.')
        else:
            self.chatbot.currentStructureChatBot.printDictIntents()
