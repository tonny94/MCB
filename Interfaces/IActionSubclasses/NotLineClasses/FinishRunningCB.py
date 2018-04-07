#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales
from ChatBot import ChatBot
from Intent import  Intent


class CFinishRunningCB(ActionLine):

    def __init__(self,runChatBot,currentChatbotChild):
        self.runChatBot = runChatBot
        self.currentChatbotChild = currentChatbotChild

    def exec(self,):
        if self.currentChatbotChild == '':
            print('No hay un chatbot ejecutandose.')
        else:
            self.runChatBot = False
