#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales

class CShowChatBot(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot= chatbot

    def exec(self,):
        self.chatbot.printCurrentStructureChatbot()

