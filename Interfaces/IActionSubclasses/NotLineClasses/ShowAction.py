#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales

class CShowAction(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot= chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay ningun Chatbot actual para mostrar un Action en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            print('ERROR: No hay ningun Intent actual para asociarle un Action.')
        else:
            self.chatbot.currentStructureChatBot.currentIntent.printAction()

