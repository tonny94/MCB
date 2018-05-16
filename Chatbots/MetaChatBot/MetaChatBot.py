#! /bin/bash
# -*- coding: utf-8 -*-



import os
import inspect
# Clases generales


from Chatbots.MetaChatBot.Actions.NotLineClasses.ShowChatBot import CShowChatBot

# Clases chatbot
from Chatbots.MetaChatBot.Actions.NotLineClasses.ListChatBots import CListChatBots
from Chatbots.MetaChatBot.Actions.LineClasses.ChangeChatbot import CChangeChatbot
from Chatbots.MetaChatBot.Actions.LineClasses.CreateChatbot import CCreateChatbot
from Chatbots.MetaChatBot.Actions.LineClasses.DeleteChatbot import CDeleteChatbot
from Chatbots.MetaChatBot.Actions.NotLineClasses.BuildChatbot import CBuildChatbot

# Clases intents
from Chatbots.MetaChatBot.Actions.NotLineClasses.ListIntents import CListIntents
from Chatbots.MetaChatBot.Actions.LineClasses.ChangeIntent import CChangeIntent
from Chatbots.MetaChatBot.Actions.LineClasses.CreateIntent import CCreateIntent
from Chatbots.MetaChatBot.Actions.LineClasses.DeleteIntent import CDeleteIntent
from Chatbots.MetaChatBot.Actions.NotLineClasses.ShowIntent import CShowIntent

# Clases patterns
from Chatbots.MetaChatBot.Actions.LineClasses.CreatePattern import CCreatePattern
from Chatbots.MetaChatBot.Actions.LineClasses.DeletePattern import CDeletePattern
from Chatbots.MetaChatBot.Actions.NotLineClasses.ListPatterns import CListPatterns

# Clases responses
from Chatbots.MetaChatBot.Actions.LineClasses.CreateResponse import CCreateResponse
from Chatbots.MetaChatBot.Actions.LineClasses.DeleteResponse import CDeleteResponse
from Chatbots.MetaChatBot.Actions.NotLineClasses.ListResponses import CListResponses

# Clases actions
from Chatbots.MetaChatBot.Actions.LineClasses.CreateAction import CCreateAction
from Chatbots.MetaChatBot.Actions.NotLineClasses.DeleteAction import CDeleteAction
from Chatbots.MetaChatBot.Actions.NotLineClasses.ShowAction import CShowAction

from Abstract.AChatBot import CChatBot
from StructureChatBot.StructureChatBot import CStructureChatBot
from Chatbots.MetaChatBot.Actions.NotLineClasses.RunSolveErrors import CRunSolveErrors
from Abstract.AActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence

from Chatbots.MetaChatBot.Actions.NotLineClasses.SaveSentence import CSaveSentence
from Chatbots.MetaChatBot.Actions.NotLineClasses.DontSaveSentence import CDontSaveSentence

class CMetaChatBot(CChatBot):
    """Father class"""
    def __init__(self):
        super(CMetaChatBot, self).__init__()
        self.dictChatBots = {}
        self.currentStructureChatBot = None
        self.actionsCB ={

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
            'showAction':CShowAction(self),

            'saveSentence': CSaveSentence(self),
            'dontSaveSentence': CDontSaveSentence(self),

            'runSolveErrors': CRunSolveErrors(self)
        }
        self.initializePaths()



    #Metodos comunes a todos los chatbots
    def initializePaths(self):
        strSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)
        self.name = strSplit[len(strSplit)-1]
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+'.json')
        # self.initializate()

    def saveUnrecognizedSentence(self,key,value):
        newDict = {key:value}
        self.errorDict.update(newDict)

    def execPrediction(self,sentence):
        valorClasificacion = self.TrainerAndPredictor.classify(sentence)
        if (not valorClasificacion == []) and valorClasificacion[0][1] >= 0.9:
            self.TrainerAndPredictor.predict(sentence)
            self.currentAction = self.TrainerAndPredictor.action

            if not self.currentAction == '':
                # self.updateActionsCBProcessor(self.actionsMetaCB)
                self.setCurrentSentence(sentence)
                self.setCurrentIntent(self.TrainerAndPredictor.intent['tag'])
                self.actions[self.currentAction].exec()
                self.TrainerAndPredictor.action = ''

            # reinicia el atributo
            self.setUnrecognizedSentence(None)
            self.setUnrecognizedIntent(None)
        else:
            # guarda la sentencia que no se reconocio
            self.setUnrecognizedSentence(sentence)
            value = '"No se encontró intent"'
            if not valorClasificacion == []:
               value = valorClasificacion[0][0] #self.currentRunningChatbot.TrainerAndPredictor.getIntent(valorClasificacion[0][0])
            self.setUnrecognizedIntent(value)
            CNotRecognizedSentence(self.unrecognizedSentence).exec()


    #Metodos propios de la clase METACHATBOT
    def addStructureChatbotDict(self,sentence):
        if not sentence in self.dictChatBots:
            myChatBot = CStructureChatBot()
            myChatBot.setName(sentence)

            # crea la intencion de salir para cada chatbot que se cree
            CCreateIntent(myChatBot).createExitIntent(myChatBot)

            self.dictChatBots[sentence] = myChatBot
            self.currentStructureChatBot = myChatBot
            self.output.exec('El ChatBot "' + sentence + '" se ha añadido correctamente.')
        else:
            self.output.exec('El ChatBot "' + sentence + '" ya existe.')

    def deleteStructureChatbotDict(self,sentence):
        if sentence in self.dictChatBots:
            # myChatBot = self.dicChatBots[nameChatBot]
            del self.dictChatBots[sentence]

            if not(self.currentStructureChatBot is None) and sentence is self.currentStructureChatBot.name:
                self.currentStructureChatBot = None
                self.output.exec('El ChatBot "'+sentence+'" ha dejado de ser el ChatBot actual.')
            self.output.exec('El ChatBot "' + sentence + '" se ha eliminado correctamente .')
        else:
            self.output.exec('El ChatBot "' + sentence + '" no existe .')

    def changeStrunctureCurrentChatbot(self,sentence):
        if not sentence in self.dictChatBots:
            self.output.exec('No existe ese Chatbot.')
        else:
            if not self.currentStructureChatBot is None:
                nameCB = self.currentStructureChatBot
                self.currentStructureChatBot = self.dictChatBots[sentence]
                self.output.exec('Se ha cambiado "'+ nameCB+ '" por "'+ sentence+ '".')
            else:
                self.currentStructureChatBot = self.dictChatBots[sentence]
                self.output.exec('Ahora "'+ sentence+ '" es el actual Chatbot.')

    def printCurrentStructureChatbot(self):
        if self.currentStructureChatBot is None:
            self.output.exec('No hay ningun ChatBot actual.')
        else:
            self.output.exec('"'+ self.currentStructureChatBot.name+ '"')

    def printStructureChatbotDict(self):
        result = ", ".join(str(value.name) for key, value in self.dictChatBots.items())
        self.output.exec('Los chatbot creados son: '+ result)

    def printIntents(self):
        self.output.exec(self.intents)

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

    def setNameChabot(self,name):
        self.name = name

    def getErrorList(self):
        return self.errorDict