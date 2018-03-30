#! /bin/bash
# -*- coding: utf-8 -*-


from ChatBotProcessor import CBProcessor
import os

# Clases generales
from Interfaces.IActionSubclasses.NotLineClasses.ToList import CToList
from Interfaces.IActionSubclasses.LineClasses.ChangeObject import CChangeObject
from Interfaces.IActionSubclasses.NotLineClasses.ShowObject import CShowObject

# Clases chatbot
from Interfaces.IActionSubclasses.LineClasses.CreateChatbot import CCreateChatbot
from Interfaces.IActionSubclasses.LineClasses.DeleteChatbot import CDeleteChatbot
from Interfaces.IActionSubclasses.NotLineClasses.BuildChatbot import CBuildChatbot

# Clases intents
from Interfaces.IActionSubclasses.LineClasses.CreateIntent import CCreateIntent
from Interfaces.IActionSubclasses.LineClasses.DeleteIntent import CDeleteIntent

# Clases patterns
from Interfaces.IActionSubclasses.LineClasses.CreatePattern import CCreatePattern
from Interfaces.IActionSubclasses.LineClasses.DeletePattern import CDeletePattern

# Clases responses
from Interfaces.IActionSubclasses.LineClasses.CreateResponse import CCreateResponse
from Interfaces.IActionSubclasses.LineClasses.DeleteResponse import CDeleteResponse



class MetaChatBot(CBProcessor):
    """Father class"""
    def __init__(self):
        self.listUnrecognizedSentences = []
        self.sentenceToResolve = ''
        self.dicChatBots = {}
        self.currentChatBot = None
        self.name = ''

    def startTrainerClass(self, chatbotName, jsonFile, pathModel):
        CBProcessor.__init__(self)
        self.preparateModel(chatbotName, jsonFile, pathModel)
        self.name = chatbotName

    def startResponseClass(self, chatbotName, jsonFile, pathModel):
        CBProcessor.__init__(self)
        self.preparateResponse(chatbotName, jsonFile, pathModel)
        self.name = chatbotName
        self.actions.update({

            'buildChatBot':self.buildCB,

            'crearChatBot': self.createCB, 'borrarChatBot': self.deleteCB,'listarChatBot': self.listCB,'cambiarChatBot': self.changeCB , 'mostrarActualChatBot': self.showcurrentCB,
            # 'crearChatBot': self.crearChatBot, 'borrarChatBot': self.borrarChatBot, 'listarChatBot':self.listarChatBot, 'cambiarChatBot':self.cambiarChatBot,'mostrarActualChatBot':self.mostrarActualChatBot,

            'crearIntent':self.createIntent,'borrarIntent':self.deleteIntent, 'listarIntent':self.listIntent, 'cambiarIntent':self.changeIntent,'mostrarActualIntent':self.showcurrentIntent,
            # 'crearIntent':self.crearIntent,'borrarIntent':self.borrarIntent, 'listarIntent':self.listarIntent, 'cambiarIntent':self.cambiarIntent,'mostrarActualIntent':self.mostrarActualIntent,

            'crearPattern':self.createPattern,'borrarPattern':self.deletePattern,'mostrarPattern':self.listPattern,
            # 'crearPattern':self.crearPattern,'borrarPattern':self.borrarPattern,'mostrarPattern':self.listPattern,

            'crearResponse':self.createResponse,'borrarResponse':self.deleteResponse,'mostrarResponse':self.listResponse
            # 'crearResponse':self.crearResponse,'borrarResponse':self.borrarResponse,'mostrarResponse':self.mostrarResponse

            # 'toJSON':self.toJSON,'salirChatbot':self.salirChatbot,'crearJSON':self.crearJSON,
                        # #'reconocerSentencia':self.reconocerSentencia,'resolverSentencia':self.resolverSentencia, #construirchatbot -> genera ficheros de los chatbots
                        # 'resolverError':self.resolverError,
                             }
                        )

    """
        Métodos para controlar la creación de CHATBOTS
    """

    def buildCB(self):
        path = os.path.join(os.path.sep,os.getcwd(),'CreatedChatbots')
        CBuildChatbot(self.currentChatBot, path).exec()
        # self.currentChatBot = newCB



    """
        Métodos para controlar la creación de CHATBOTS
    """
    def createCB(self):
        newCB = CCreateChatbot(self.currentChatBot, self.dicChatBots).exec()
        self.currentChatBot = newCB

    def deleteCB(self):
        CDeleteChatbot(self.currentChatBot, self.dicChatBots).exec()

    def listCB(self):
        CToList(self.dicChatBots,'Los chatbots creados son: ','ChatBot').exec()

    def changeCB(self):
        CChangeObject(self.currentChatBot,self.dicChatBots).exec()

    def showcurrentCB(self):
        CShowObject(self.currentChatBot).exec()


    """
        Métodos para controlar la creación de INTENTS
    """
    def createIntent(self):
        CCreateIntent(self.currentChatBot).exec()

    def deleteIntent(self):
        CDeleteIntent(self.currentChatBot).exec()

    def listIntent(self):
        if self.currentChatBot is None:
            print('No hay ningun chatbot para listar sus Intents.')
        else:
            CToList(self.currentChatBot.dicIntents, 'Los Intents creados son: ','Intent').exec()

    def changeIntent(self):
        if self.currentChatBot is None:
            print('No existe ningun chatbot para cambiar su Intent actual.')
        else:
            CChangeObject(self.currentChatBot.currentIntent, self.currentChatBot.dicIntents).exec()

    def showcurrentIntent(self):
        if self.currentChatBot is None:
            print('No existe ningun chatbot para mostrar su Intent actual.')
        else:
            CShowObject(self.currentChatBot.currentIntent).exec()


    """
        Métodos para controlar la creación de PATTERNS
    """
    def createPattern(self):
        CCreatePattern(self.currentChatBot).exec()

    def deletePattern(self):
        CDeletePattern(self.currentChatBot).exec()

    def listPattern(self):
        if self.currentChatBot is None:
            print('No hay ningun Chatbot para listar los Patterns de un Intent.')
        elif self.currentChatBot.currentIntent is None:
            print('No hay ningin Intent para listar sus Patterns.')
        else:
            CToList(self.currentChatBot.currentIntent.patterns, 'Los Patterns creados son: ').exec()


    """
        Métodos para controlar la creación de RESPONSES
    """
    def createResponse(self):
        CCreateResponse(self.currentChatBot).exec()

    def deleteResponse(self):
        CDeleteResponse(self.currentChatBot).exec()

    def listResponse(self):
        if self.currentChatBot is None:
            print('No hay ningun Chatbot para listar los Responses de un Intent.')
        elif self.currentChatBot.currentIntent is None:
            print('No hay ningun Intent para listar sus Responses.')
        else:
            CToList(self.currentChatBot.currentIntent.responses, 'Los Responses creados son: ').exec()



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
        self.listUnrecognizedSentences.append(sentence)
        self.sentenceToResolve = sentence
        print('No se reconocio la sentencia. Quiere eliminarla o anhadirla a: Intenciones, Patterns, Responses')

    def resolverSentencia(self):
        print('resolver')



    def toJSON(self,chatbotName):
        self.crearJSON(chatbotName)
        #print (self.dicToJSON(self.dicChatBots) )

    def crearJSON(self,chatbotName):

        if chatbotName in self.dicChatBots:
            dirChatbot = os.getcwd()
            dirChatbot = os.path.join(os.sep,dirChatbot,chatbotName)
            if not os.path.exists(dirChatbot):
                os.makedirs(dirChatbot)

            dirJsonFile = os.path.join(os.sep,dirChatbot,chatbotName+'.json')
            jsonFile = open(dirJsonFile, 'w')
            jsonFile.write(self.chatbotToJson(self.dicChatBots[chatbotName]))
            # jsonFile.write(self.dicToJSON(self.dicChatBots) )
            jsonFile.close()

            self.runTrainer()

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



"""