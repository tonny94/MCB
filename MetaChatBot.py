from ChatBot import ChatBot
from ChatBotProcessor import CBProcessor
from Intent import Intent
import os

from chatbotResolverErrores.Resolutor import Resolutor
import curses

class MetaChatBot(CBProcessor):
    """Father class"""
    def __init__(self):
        self.listaSentenciasNoReconocidas = []
        self.sentenciaParaResolver = ''
        self.dicChatBots = {}
        self.currentChatBot = None
        self.name = ''


    def iniciarTRainerClass(self,chatbotName,jsonFile,pathModel):
        CBProcessor.__init__(self)
        self.preparateModel(chatbotName, jsonFile, pathModel)
        self.name = chatbotName


    def iniciarResponseClass(self,chatbotName,jsonFile,pathModel):
        CBProcessor.__init__(self)
        self.preparateResponse(chatbotName, jsonFile, pathModel)
        self.name = chatbotName
        self.actions.update({'toJSON':self.toJSON,'salirChatbot':self.salirChatbot,'crearJSON':self.crearJSON,
                        #'reconocerSentencia':self.reconocerSentencia,'resolverSentencia':self.resolverSentencia, #construirchatbot -> genera ficheros de los chatbots
                        'resolverError':self.resolverError,
                        'crearChatBot': self.crearChatBot, 'borrarChatBot': self.borrarChatBot, 'listarChatBot':self.listarChatBot, 'cambiarChatBot':self.cambiarChatBot,'mostrarActualChatBot':self.mostrarActualChatBot,
                        'crearIntent':self.crearIntent,'borrarIntent':self.borrarIntent, 'listarIntent':self.listarIntent, 'cambiarIntent':self.cambiarIntent,'mostrarActualIntent':self.mostrarActualIntent,
                        'crearPattern':self.crearPattern,'borrarPattern':self.borrarPattern,'mostrarPattern':self.mostrarPattern,
                        'crearResponse':self.crearResponse,'borrarResponse':self.borrarResponse,'mostrarResponse':self.mostrarResponse}
                        )



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

    def resolverError(self,nombChatbot):
        objResolutor = Resolutor()
        #objResolutor.preparateModel()
        objResolutor.preparateResponse()
        objResolutor.setParametters(nombChatbot,self.dicPattersnNoReconocidos)

        sentence = ''
        while not (sentence == 's'):
            sentence = input()
            if not (sentence is 's'):
                objResolutor.classify(sentence)
                objResolutor.response(sentence)

    def salirChatbot(self):
        #cancelar ejecucion del chatbot
        print('chatbot cancelado')

    def reconocerSentencia(self,sentence):
        self.listaSentenciasNoReconocidas.append(sentence)
        self.sentenciaParaResolver = sentence
        print('No se reconocio la sentencia. Quiere eliminarla o anhadirla a: Intenciones, Patterns, Responses')

    def resolverSentencia(self):
        print('resolver')



    def toJSON(self,chatbotName):
        self.crearJSON(chatbotName)
        #print (self.dicToJSON(self.dicChatBots) )

    def crearJSON(self,chatbotName):

        if chatbotName in self.dicChatBots:
            cwd = os.getcwd()
            if not os.path.exists(cwd + '\\'+chatbotName):
                os.makedirs(cwd + '\\'+chatbotName)

            jsonFile = open(cwd + '\\'+chatbotName+'\\'+chatbotName+'.json', 'w')
            jsonFile.write(self.chatbotToJson(self.dicChatBots[chatbotName]))
            # jsonFile.write(self.dicToJSON(self.dicChatBots) )
            jsonFile.close()
            print ('json creado')
        else:
            print('No existe el chatbot para convertir a json.')

    def chatbotToJson(self,chatbot):
        strJSON = '[\n\t'
        strJSON += chatbot.toJSON() + '\n]'
        return strJSON

    def dicToJSON(self,dicc):
        if len(dicc) > 0:
            i = 0
            strJSON = '[\n\t'
            for chatbot in dicc:
                if i == len(dicc) - 1:
                    strJSON += dicc[chatbot].toJSON() + '\n]'
                else:
                    strJSON += dicc[chatbot].toJSON() + ',\n\t'
                i += 1
            return strJSON
        else:
            return '[]'


    def selectChatBot(self, nameChatBot):
        if nameChatBot in self.dicChatBots:
            self.currentChatBot = nameChatBot
            return self.dicChatBots[nameChatBot]

        return None

    def listar(self,lista,nombreLista):
        cadena = nombreLista+': [ '
        if lista == {} or lista == []:
            cadena += ']'
        else:
            for elem in lista:
                cadena += elem + ','
            cadena = cadena[:-1]
            cadena += ' ]'
        print(cadena)

    #metodo que crea a estructura de una intencion para un chatbot
    def crearIntentSalir(self,chatbot):

        #crea la intencion
        intent = Intent()
        intent.setTag('salirChatbot')
        intent.setAction('salirChatbot')
        intent.addPattern('Salir del chatbot')
        intent.addPattern('Finalizar chatbot')
        intent.addPattern('Salir del chatbot')
        intent.addPattern('Dejar de ejecutar chatbot')
        intent.responses = []

        chatbot.dicIntents['salirChatbot'] = intent



    ##CHATBOT METODOS
    def crearChatBot(self,sentence):
        #self.addChatBot(sentence)
        if not sentence in self.dicChatBots:
            myChatBot = ChatBot()
            myChatBot.setName(sentence)

            #crea la intencion de salir para cada chatbot que se cree
            self.crearIntentSalir(myChatBot)

            self.dicChatBots[sentence] = myChatBot
            self.currentChatBot = myChatBot
            self.currentChatbotName = sentence
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

    def cambiarChatBot(self,sentence):
        if not sentence in self.dicChatBots:
            print('El chatbot no exsite')
        else:
            self.currentChatBot = self.dicChatBots[sentence]
            print('Chatbot actual: '+self.currentChatBot.name)

    def mostrarActualChatBot(self):
        if self.currentChatBot == None:
            print ('No hay chatbot creado')
        else:
            print('Chatbot activado: '+self.currentChatBot.name)

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

    def cambiarIntent(self, sentence):
        if not sentence in self.currentChatBot.dicIntents:
            print('La intencion no exsite')
        else:
            self.currentChatBot.currentIntent = self.currentChatBot.dicIntents[sentence]
            print('Intencion actual: '+self.currentChatBot.currentIntent.tag)

    def mostrarActualIntent(self):
        if self.currentChatBot.currentIntent == None:
            print ('No hay intencion creado')
        else:
            print('Intencion activada: '+self.currentChatBot.currentIntent.tag)

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