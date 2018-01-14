from ChatBot import ChatBot
import ChatBotProcessor


class MetaChatBot():
    """Father class"""
    def __init__(self):
        self.dicChatBots = {}
        self.currentChatBot = None
        self.actions = {'crearChatBot' : self.crearChatBot, 'borrarChatBot' : self.borrarChatBot}

    def MCBResponse(self,sentence):
        ChatBotProcessor.CBProcessor.response(sentence)
        action = ChatBotProcessor.CBProcessor.getAction()
        self.actions[action](sentence)
        ChatBotProcessor.CBProcessor.resetAction()

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
    	#addChatBot(sentence)
        return print('El ChatBot '+sentence+' se ha añadido correctamente.')


    def borrarChatBot(self,sentence):
    	#removeChatBot(sentence)
        return print('El ChatBot '+sentence+' se ha eliminado correctamente .')
