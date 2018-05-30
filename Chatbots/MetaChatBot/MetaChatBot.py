#! /bin/bash
# -*- coding: utf-8 -*-



import os,json
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
from Chatbots.MetaChatBot.Actions.LineClasses.StartRunningChatbot import CStartRunningChatbot

class CMetaChatBot(CChatBot):
    """Father class"""
    def __init__(self):
        super(CMetaChatBot, self).__init__()
        self.dictChatBots = {}
        self.currentStructureChatBot = None
        self.listNoChatbots = ['MetaChatBot','SolveError']
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

            # 'runSolveErrors': CRunSolveErrors(self),
            'startRunningChatbot': CStartRunningChatbot(self)
        }
        self.initializePaths()
        self.loadChatbots()


    def loadChatbots(self):
        pathChatbots = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) )
        listAllChatbots = os.listdir(pathChatbots)
        if len(listAllChatbots) == len(self.listNoChatbots):
            self.output.exec('No hay chatbots para cargar.')
        else:
            currentChatbotLoaded = False
            for nameChatbot in listAllChatbots:
                if not nameChatbot in self.listNoChatbots:
                    pathJson = os.path.join(os.path.sep, pathChatbots, nameChatbot,nameChatbot+'.json')
                    if os.path.isfile(pathJson):
                        chatbot = CStructureChatBot()
                        chatbot.setName(nameChatbot)
                        chatbot.codeToStructureChatbot(chatbot, pathJson)
                        self.dictChatBots[nameChatbot] = chatbot
                        if not currentChatbotLoaded :
                            self.currentStructureChatBot =chatbot
                            currentChatbotLoaded = True
            self.output.exec('Ahora el chatbot actual es "'+self.currentStructureChatBot.name+'".')




    #Metodos comunes a todos los chatbots
    def initializePaths(self):
        strSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)
        self.name = strSplit[len(strSplit)-1]
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+'.json')
        self.errorFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorFile.json')
        self.errorSolvedFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorSolvedFile.json')

        if not os.path.isfile(self.errorFilePath):
            with open(self.errorFilePath, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        if not os.path.isfile(self.errorSolvedFilePath):
            with open(self.errorSolvedFilePath, 'w', encoding='utf-8') as f:
                json.dump({}, f)
        # self.initializate()

    # def execPrediction(self,sentence):
    #     valorClasificacion = self.TrainerAndPredictor.classify(sentence)
    #     if (not valorClasificacion == []) and valorClasificacion[0][1] >= 0.9:
    #         self.TrainerAndPredictor.predict(sentence)
    #         self.currentAction = self.TrainerAndPredictor.action
    #
    #         if not self.currentAction == '':
    #             # self.updateActionsCBProcessor(self.actionsMetaCB)
    #             self.setCurrentSentence(sentence)
    #             self.setCurrentIntent(self.TrainerAndPredictor.intent['tag'])
    #             self.actions[self.currentAction].exec()
    #             self.TrainerAndPredictor.action = ''
    #
    #         # reinicia el atributo
    #         self.setUnrecognizedSentence(None)
    #         self.setUnrecognizedIntent(None)
    #     else:
    #         # guarda la sentencia que no se reconocio
    #         self.setUnrecognizedSentence(sentence)
    #         value = '"No se encontró intent"'
    #         if not valorClasificacion == []:
    #            value = valorClasificacion[0][0] #self.currentRunningChatbot.TrainerAndPredictor.getIntent(valorClasificacion[0][0])
    #         self.setUnrecognizedIntent(value)
    #         CNotRecognizedSentence(self.unrecognizedSentence).exec()


    #Metodos propios de la clase METACHATBOT
    def addStructureChatbotDict(self,sentence):
        if not sentence in self.dictChatBots:
            myChatBot = CStructureChatBot()
            myChatBot.setName(sentence)

            # crea la intencion de salir para cada chatbot que se cree
            CCreateIntent(myChatBot).createExitIntent(myChatBot)
            CCreateIntent(myChatBot).createSaveSentenceIntent(myChatBot)
            CCreateIntent(myChatBot).createDontSaveSentenceIntent(myChatBot)

            self.dictChatBots[sentence] = myChatBot
            self.currentStructureChatBot = myChatBot
            self.output.exec('El ChatBot "' + sentence + '" se ha añadido correctamente.')
        else:
            self.output.exec('El ChatBot "' + sentence + '" ya existe.')

    def deleteStructureChatbotDict(self,sentence):
        if sentence in self.dictChatBots:
            # myChatBot = self.dicChatBots[nameChatBot]
            del self.dictChatBots[sentence]

            if not(self.currentStructureChatBot is None) and sentence == self.currentStructureChatBot.name:
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
                self.output.exec('Se ha cambiado "'+ nameCB.name+ '" por "'+ sentence+ '".')
            else:
                self.currentStructureChatBot = self.dictChatBots[sentence]
                self.output.exec('Ahora "'+ sentence+ '" es el actual Chatbot.')

    def printCurrentStructureChatbot(self):
        if self.currentStructureChatBot is None:
            self.output.exec('No hay ningun ChatBot actual.')
        else:
            self.output.exec('El cahtbot actual es "'+ self.currentStructureChatBot.name+ '"')

    def printStructureChatbotDict(self):
        result = ", ".join(str(value.name) for key, value in self.dictChatBots.items())
        self.output.exec('Los chatbot creados son: '+ result)

    def printIntents(self):
        self.output.exec(self.intents)

    def setListIntents(self,list):
        self.intents = list

    def setNameChabot(self,name):
        self.name = name

    def getErrorList(self):
        return self.errorDict