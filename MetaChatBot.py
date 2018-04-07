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

            'createChatBot': CCreateChatbot(self.currentChatBot,self.dicChatBots), 'deleteChatBot': CDeleteChatbot(self.currentChatBot,self.dicChatBots), 'listChatBot': CToList(self.dicChatBots,'Los chatbots creados son: ','ChatBot'),'changeChatBot': CChangeObject(self.currentChatBot,), 'showcurrentChatBot': self.showcurrentCB,
            #'createChatBot': self.createCB, 'deleteChatBot': self.deleteCB,'listChatBot': self.listCB,'changeChatBot': self.changeCB , 'showcurrentChatBot': self.showcurrentCB,
            # 'crearChatBot': self.crearChatBot, 'borrarChatBot': self.borrarChatBot, 'listarChatBot':self.listarChatBot, 'cambiarChatBot':self.cambiarChatBot,'mostrarActualChatBot':self.mostrarActualChatBot,

            'createIntent':self.createIntent,'deleteIntent':self.deleteIntent, 'listIntent':self.listIntent, 'changeIntent':self.changeIntent,'showcurrentIntent':self.showcurrentIntent,
            # 'crearIntent':self.crearIntent,'borrarIntent':self.borrarIntent, 'listarIntent':self.listarIntent, 'cambiarIntent':self.cambiarIntent,'mostrarActualIntent':self.mostrarActualIntent,

            'createPattern':self.createPattern,'deletePattern':self.deletePattern,'listPattern':self.listPattern,
            # 'crearPattern':self.crearPattern,'borrarPattern':self.borrarPattern,'mostrarPattern':self.listPattern,

            'createResponse':self.createResponse,'deleteResponse':self.deleteResponse,'listResponse':self.listResponse
            # 'crearResponse':self.crearResponse,'borrarResponse':self.borrarResponse,'mostrarResponse':self.mostrarResponse

            # salirChatbot':self.salirChatbot
                        # #'reconocerSentencia':self.reconocerSentencia,'resolverSentencia':self.resolverSentencia, #construirchatbot -> genera ficheros de los chatbots
                        # 'resolverError':self.resolverError,
                             }
                        )

    """
        Métodos para CONSTRUIR chatbots
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
        self.currentChatbotChild = self.currentChatBot.name

    def deleteCB(self):
        CDeleteChatbot(self.currentChatBot, self.dicChatBots).exec()

    def listCB(self):
        CToList(self.dicChatBots,'Los chatbots creados son: ','ChatBot').exec()

    def changeCB(self):
        CChangeObject(self.currentChatBot,self.dicChatBots).exec()

    def showcurrentCB(self):
        CShowObject(self.currentChatBot,'ChatBot').exec()


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
            CShowObject(self.currentChatBot.currentIntent,'Intent').exec()


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


