#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales
from ChatBot import ChatBot
from Intent import  Intent


class CStartRunningCB(ActionLine):

    def __init__(self,currentChatbotChild,pathChatbots):
        self.pathChatbots = pathChatbots
        self.currentChatbotChild = currentChatbotChild

    def exec(self,):
        if self.currentChatbotChild == '':
            print('No hay un chatbot creado.')
        else:
            self.runChatBot = False
