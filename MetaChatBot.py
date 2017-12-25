from ChatBot import ChatBot

class MetaChatBot:
    """Father class"""
    def __init__(self):
        self.dicChatBots = {}
        self.currentChatBot = None



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

        return myChatBot


    def selectChatBot(self, nameChatBot):
        if nameChatBot in self.dicChatBots:
            self.currentChatBot = nameChatBot
            return self.dicChatBots[nameChatBot]

        return None
