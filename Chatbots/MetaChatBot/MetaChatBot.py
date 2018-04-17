#! /bin/bash
# -*- coding: utf-8 -*-



import os
import inspect
# Clases generales


from Interfaces.IActionSubclasses.NotLineClasses.ShowChatBot import CShowChatBot

# Clases chatbot
from Interfaces.IActionSubclasses.NotLineClasses.ListChatBots import CListChatBots
from Interfaces.IActionSubclasses.LineClasses.ChangeChatbot import CChangeChatbot
from Interfaces.IActionSubclasses.LineClasses.CreateChatbot import CCreateChatbot
from Interfaces.IActionSubclasses.LineClasses.DeleteChatbot import CDeleteChatbot
from Interfaces.IActionSubclasses.NotLineClasses.BuildChatbot import CBuildChatbot

# Clases intents
from Interfaces.IActionSubclasses.NotLineClasses.ListIntents import CListIntents
from Interfaces.IActionSubclasses.LineClasses.ChangeIntent import CChangeIntent
from Interfaces.IActionSubclasses.LineClasses.CreateIntent import CCreateIntent
from Interfaces.IActionSubclasses.LineClasses.DeleteIntent import CDeleteIntent
from Interfaces.IActionSubclasses.NotLineClasses.ShowIntent import CShowIntent

# Clases patterns
from Interfaces.IActionSubclasses.LineClasses.CreatePattern import CCreatePattern
from Interfaces.IActionSubclasses.LineClasses.DeletePattern import CDeletePattern
from Interfaces.IActionSubclasses.NotLineClasses.ListPatterns import CListPatterns

# Clases responses
from Interfaces.IActionSubclasses.LineClasses.CreateResponse import CCreateResponse
from Interfaces.IActionSubclasses.LineClasses.DeleteResponse import CDeleteResponse
from Interfaces.IActionSubclasses.NotLineClasses.ListResponses import CListResponses

# Clases actions
from Interfaces.IActionSubclasses.LineClasses.CreateAction import CCreateAction
from Interfaces.IActionSubclasses.NotLineClasses.DeleteAction import CDeleteAction
from Interfaces.IActionSubclasses.NotLineClasses.ShowAction import CShowAction

from Interfaces.IChatBot import CChatBot
from StructureChatBot.StructureChatBot import CStructureChatBot

class CMetaChatBot(CChatBot):
    """Father class"""
    def __init__(self):
        self.dictChatBots = {}
        self.currentStructureChatBot = None
        #self.pathNewChatbots = os.getcwd() #os.path.join(os.path.sep, os.getcwd(), 'Chatbots')  # ruta donde estan los chatbots
        self.name = 'MetaChatBot'


        self.actions ={

            'buildChatBot': CBuildChatbot(self),

            'createChatBot': CCreateChatbot(self),
            'deleteChatBot': CDeleteChatbot(self),
            'listChatBot': CListChatBots(self),
            'changeChatBot': CChangeChatbot(self),
            'showcurrentChatBot': CShowChatBot(self),

            'createIntent': CCreateIntent(self),
            'deleteIntent':CDeleteIntent(self),
            'listIntent': CListIntents(self),
            'changeIntent': CChangeIntent(self),
            'showcurrentIntent': CShowIntent(self),

            'createPattern': CCreatePattern(self),
            'deletePattern': CDeletePattern(self),
            'listPattern': CListPatterns(self),

            'createResponse': CCreateResponse(self),
            'deleteResponse': CDeleteResponse(self),
            'listResponse': CListResponses(self),

            'createAction': CCreateAction(self),
            'deleteAction': CDeleteAction(self),
            'showAction':CShowAction(self)
        }
        self.initializePaths(self.name)

    def initializePaths(self,chatbotName):
        self.chatbotName = chatbotName
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,chatbotName+'.json')

    def saveUnrecognizedSentence(self,key,value):
        newDict = {key:value}
        self.errorDict.update(newDict)


    #Metodos propios de la clase METACHATBOT
    def addStructureChatbotDict(self,sentence):
        if not sentence in self.dictChatBots:
            myChatBot = CStructureChatBot()
            myChatBot.setName(sentence)

            # crea la intencion de salir para cada chatbot que se cree
            CCreateIntent(myChatBot).createExitIntent(myChatBot)

            self.dictChatBots[sentence] = myChatBot
            self.currentStructureChatBot = myChatBot
            print('El ChatBot "' + sentence + '" se ha añadido correctamente.')
        else:
            print('El ChatBot "' + sentence + '" ya existe.')

    def deleteStructureChatbotDict(self,sentence):
        if sentence in self.dictChatBots:
            # myChatBot = self.dicChatBots[nameChatBot]
            del self.dictChatBots[sentence]

            if not(self.currentStructureChatBot is None) and sentence is self.currentStructureChatBot.name:
                self.currentStructureChatBot = None
                print('El ChatBot "',sentence,'" ha dejado de ser el ChatBot actual.')
            print('El ChatBot "' + sentence + '" se ha eliminado correctamente .')
        else:
            print('El ChatBot "' + sentence + '" no existe .')

    def changeStrunctureCurrentChatbot(self,sentence):
        if not sentence in self.dictChatBots:
            print('No existe ese Chatbot.')
        else:
            if not self.currentStructureChatBot is None:
                nameCB = self.currentStructureChatBot
                self.currentStructureChatBot = self.dictChatBots[sentence]
                print('Se ha cambiado "', nameCB, '" por "', sentence, '".')
            else:
                self.currentStructureChatBot = self.dictChatBots[sentence]
                print('Ahora "', sentence, '" es el actual Chatbot.')

    def printCurrentStructureChatbot(self):
        if self.currentStructureChatBot is None:
            print('No hay ningun ChatBot actual.')
        else:
            print('"', self.currentStructureChatBot.name, '"')

    def printStructureChatbotDict(self):
        result = ", ".join(str(value.tag) for key, value in self.dictChatBots.items())
        print('Los chatbot creados son:', result)

    def setUnrecognizedSentence(self, sentence):
        self.unrecognizedSentence = sentence

    def setUnrecognizedIntent(self, intent):
        self.unrecognizeIntent = intent

    def setCurrentSentence(self, sentence):
        self.currentSentence = sentence

    def setCurrentIntent(self, intent):
        self.currentIntent = intent

    def setListIntents(self,list):
        self.intents = list

    def setCurrentIntent(self,intent):
        self.currentIntent = intent

    def setNameChabot(self,name):
        self.name = name

    def getErrorList(self):
        return self.errorDict