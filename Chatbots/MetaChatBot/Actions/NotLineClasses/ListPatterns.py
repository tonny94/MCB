#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

class CListPatterns(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay ningun ChatBot actual para listar los Patterns de su Intent actual.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None:
            print('ERROR: No hay ningun Intent actual para listar sus Patterns')
        else:
            self.chatbot.currentStructureChatBot.currentIntent.printPatterns()
