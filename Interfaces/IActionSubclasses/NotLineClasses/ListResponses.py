#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine
#Clases generales
from Interfaces.IActionSubclasses.NotLineClasses.ToList import CToList

class CListResponses(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot is None:
            print('ERROR: No hay ningun ChatBot actual para listar los Responses de su Intent actual.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None:
            print('ERROR: No hay ningun Intent actual para listar sus Responses')
        else:
            self.chatbot.currentStructureChatBot.currentIntent.printResponses()
