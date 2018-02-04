from ChatBot import ChatBot
from ChatBotProcessor import CBProcessor
from Intent import Intent
import curses

class MetaChatBot(CBProcessor):
    """Father class"""
    def __init__(self):

        self.dicChatBots = {}
        self.currentChatBot = None



    def iniciarResponseClass(self,chatbotName,jsonFile,pathModel):
        CBProcessor.__init__(self)
        self.preparateResponse(chatbotName, jsonFile, pathModel)
        self.actions = {'crearChatBot': self.crearChatBot, 'borrarChatBot': self.borrarChatBot, 'listarChatBot':self.listarChatBot,
                        'crearIntent':self.crearIntent,'borrarIntent':self.borrarIntent, 'listarIntent':self.listarIntent,
                        'crearPattern':self.crearPattern,'borrarPattern':self.borrarPattern,'mostrarPattern':self.mostrarPattern,
                        'crearResponse':self.crearResponse,'borrarResponse':self.borrarResponse,'mostrarResponse':self.mostrarResponse}



    """
    def MCBResponse(self,sentence):
        self.response(sentence)
        action = self.getAction()
        self.actions[action](sentence)
        self.resetAction()
    """

    """
    
    def addChatBot(self, nameChatBot):
        myChatBot = ChatBot()
        myChatBot.setName(nameChatBot)
        self.dicChatBots[nameChatBot] = myChatBot
        self.currentChatBot = myChatBot
        #return myChatBot
    """

    """
    def removeChatBot(self, nameChatBot):
        #myChatBot = None
        if nameChatBot in self.dicChatBots:
            #myChatBot = self.dicChatBots[nameChatBot]
            del self.dicChatBots[nameChatBot]

        if nameChatBot is self.currentChatBot:
            self.currentChatBot = None
    """

    def selectChatBot(self, nameChatBot):
        if nameChatBot in self.dicChatBots:
            self.currentChatBot = nameChatBot
            return self.dicChatBots[nameChatBot]

        return None

    def listar(self,lista,nombreLista):
        cadena = nombreLista+': [ '
        if lista == {}:
            cadena += ']'
        else:
            for elem in lista:
                cadena += elem + ','
            cadena = cadena[:-1]
            cadena += ' ]'
        print(cadena)


    ##CHATBOT METODOS
    def crearChatBot(self,sentence):
        #self.addChatBot(sentence)
        if not sentence in self.dicChatBots:
            myChatBot = ChatBot()
            myChatBot.setName(sentence)
            self.dicChatBots[sentence] = myChatBot
            self.currentChatBot = myChatBot
            return print('El ChatBot '+sentence+' se ha añadido correctamente.')
        else:
            return print('El ChatBot ' + sentence + ' ya existe.')

    def borrarChatBot(self,sentence):
        #self.removeChatBot(sentence)
        if sentence in self.dicChatBots:
            # myChatBot = self.dicChatBots[nameChatBot]
            del self.dicChatBots[sentence]

            if sentence is self.currentChatBot.name:
                self.currentChatBot = None
            return print('El ChatBot '+sentence+' se ha eliminado correctamente .')
        else:
            return print('El ChatBot ' + sentence + ' no existe .')

    def listarChatBot(self):
        self.listar(self.dicChatBots,'Chatbots')

    ##INTENTS METODOS
    def crearIntent(self,sentence):
        #self.addChatBot(sentence)
        if not sentence in self.currentChatBot.dicIntents:
            myIntent = Intent()
            myIntent.setTag(sentence)
            self.currentChatBot.dicIntents[sentence] = myIntent
            self.currentChatBot.currentIntent = myIntent
            return print('El Intent '+sentence+' se ha añadido correctamente.')
        else:
            return print('El Intent ' + sentence + ' ya existe.')

    def borrarIntent(self,sentence):
        #self.removeChatBot(sentence)
        if sentence in self.currentChatBot.dicIntents:
            # myChatBot = self.dicChatBots[nameChatBot]
            self.currentChatBot.removeIntent(sentence)

            if sentence is self.currentChatBot.currentIntent:
                self.currentChatBot.currentIntent = None
            return print('El Intent '+sentence+' se ha eliminado correctamente .')
        else:
            return print('El Intent ' + sentence + ' no existe .')

    def listarIntent(self):
        if not (self.currentChatBot == None):
            self.listar(self.currentChatBot.dicIntents,'Intents')
        else:
            self.mode = 'chatbot'
            print('No hay chatbot actual')


    ##PATTERNS METODOS
    def crearPattern(self,sentence):
        actualIntent = self.currentChatBot.currentIntent
        #self.addChatBot(sentence)
        if not sentence in actualIntent.patterns:
            actualIntent.addPattern(sentence)
            return print('El Pattern '+sentence+' se ha añadido correctamente.')
        else:
            return print('El Pattern ' + sentence + ' ya existe.')

    def borrarPattern(self,sentence):
        #self.removeChatBot(sentence)
        actualIntent = self.currentChatBot.currentIntent

        if sentence in actualIntent.patterns:
            actualIntent.removePattern(sentence)
            return print('El Pattern ' + sentence + ' se ha eliminado correctamente .')
        else:
            return print('El Pattern ' + sentence + ' no existe .')

    def mostrarPattern(self):
        if not (self.currentChatBot.currentIntent == None):
            self.listar(self.currentChatBot.currentIntent.patterns,'Pattern')
        else:
            self.mode = 'chatbot'
            print('No hay intencion actual')


    ##RESPONSES METODOS
    def crearResponse(self,sentence):
        actualIntent = self.currentChatBot.currentIntent
        # self.addChatBot(sentence)
        if not sentence in actualIntent.responses:
            actualIntent.addResponse(sentence)
            return print('El Response ' + sentence + ' se ha añadido correctamente.')
        else:
            return print('El Response ' + sentence + ' ya existe.')

    def borrarResponse(self,sentence):
        #self.removeChatBot(sentence)
        actualIntent = self.currentChatBot.currentIntent

        if sentence in actualIntent.responses:
            actualIntent.removeResponse(sentence)
            return print('El Pattern ' + sentence + ' se ha eliminado correctamente .')
        else:
            return print('El Pattern ' + sentence + ' no existe .')

    def mostrarResponse(self):
        if not (self.currentChatBot.currentIntent == None):
            self.listar(self.currentChatBot.currentIntent.responses, 'Responses')
        else:
            self.mode = 'chatbot'
            print('No hay intencion actual')