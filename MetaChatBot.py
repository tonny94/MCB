from ChatBot import ChatBot
from ChatBotProcessor import CBProcessor
import curses

class MetaChatBot(CBProcessor):
    """Father class"""
    def __init__(self):

        self.dicChatBots = {}
        self.currentChatBot = None



    def iniciarResponseClass(self,chatbotName,jsonFile,pathModel):
        CBProcessor.__init__(self)
        self.preparateResponse(chatbotName, jsonFile, pathModel)
        self.actions = {'crearChatBot': self.crearChatBot, 'borrarChatBot': self.borrarChatBot}



    """
    def MCBResponse(self,sentence):
        self.response(sentence)
        action = self.getAction()
        self.actions[action](sentence)
        self.resetAction()
    """

    def addChatBot(self, nameChatBot):
        myChatBot = ChatBot()
        myChatBot.setName(nameChatBot)
        self.dicChatBots[nameChatBot] = myChatBot
        self.currentChatBot = nameChatBot
        return myChatBot

    def removeChatBot(self, nameChatBot):
        myChatBot = None

        if nameChatBot in self.dicChatBots:
            myChatBot = self.dicChatBots[nameChatBot]
            del self.dicChatBots[nameChatBot]

        if nameChatBot is self.currentChatBot:
            self.currentChatBot = None

    def selectChatBot(self, nameChatBot):
        if nameChatBot in self.dicChatBots:
            self.currentChatBot = nameChatBot
            return self.dicChatBots[nameChatBot]

        return None

    def crearChatBot(self,sentence):
        self.addChatBot(sentence)
        return print('El ChatBot '+sentence+' se ha añadido correctamente.')

    def borrarChatBot(self,sentence):
        self.removeChatBot(sentence)
        return print('El ChatBot '+sentence+' se ha eliminado correctamente .')
