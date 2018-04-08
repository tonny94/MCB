#! /bin/bash
# -*- coding: utf-8 -*-

import Response
import Trainer
#Clase para ejecutar ChatbotResolutor

from Interfaces.IActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence
from Interfaces.IActionSubclasses.NotLineClasses.SaveSentence import CSaveSentence
from Interfaces.IActionSubclasses.NotLineClasses.DontSaveSentence import CDontSaveSentence
from Interfaces.IActionSubclasses.NotLineClasses.FinishRunningCB import CFinishRunningCB
from Interfaces.IActionSubclasses.NotLineClasses.StartRunningCB import CStartRunningCB
from Interfaces.IActionSubclasses.LineClasses.RunSolveErrors import CRunSolveErrors

class CBProcessor(object):

    def __init__(self):
        #para guardar sentencia no reconocida
        self.errorSentence = ''
        self.dictSentences = {}

        #para ejecutar un chatbot - finalizar ejecucion
        self.currentChatbotChild = '' #el nombre del chatbot que se esta ejecutando
        self.runChatBot = False #variable que cancela la ejecucion de un chatbot
        self.currentChatbotName = ''

        # para ejecutar chatbot resolutor
        self.jsonFileCurrentChatbot = ''
        self.currentChatbotFather = ''

        self.currentAction = ''
        self.actions = {}

        self.chatbotModel = None
        self.chatbotResponse = None #Response.Response()

    def updateActionsCBProcessor(self,newDict):
        self.actions.update({
            'saveSentence': CSaveSentence(self.currentChatbotFather, self.errorSentence, self.dictSentences),
            'dontSaveSentence': CDontSaveSentence(self.errorSentence),
            'runSolveErrors': CRunSolveErrors(self.currentChatbotFather,self.jsonFileCurrentChatbot,self.dictSentences),
            'finishRunningChatbot': self.finishRunningChatbot, 'startRunningChatbot': self.startRunningChatbot
            }
        )
        self.actions.update(newDict)


    def setErrorSentence(self,sentence):
        self.errorSentence = sentence

    def preparateModel(self,chatbotName,jsonFile,pathModel):
        if not ('.json' in jsonFile) or (chatbotName == ''):
            print('Se necesita especificar la ruta del fichero JSON.')
        else:
            print('inicio de modelo')
            self.chatbotModel = Trainer.Model()
            self.chatbotModel.readJSON(jsonFile,chatbotName)
            self.chatbotModel.createElementsToModel()
            self.chatbotModel.trainingModel(pathModel)
            self.chatbotModel.doPickle()
            self.chatbotModel.closeResource()
            print('fin de modelo')

    def preparateResponse(self,chatbotName,jsonFile,pathModel):
        # if self.chatbotModel == None:
        #     print('Se necesita crear el Modelo primero.')
        if not ('.json' in jsonFile) or (chatbotName == ''):
            print('Se necesita especificar la ruta del fichero JSON.')
        else:
            print('inicio response')
            self.currentChatbotFather = chatbotName
            self.jsonFileCurrentChatbot = jsonFile
            self.chatbotResponse = Response.Response()
            self.chatbotResponse.loadArrays(pathModel)
            self.chatbotResponse.readJSON(jsonFile,chatbotName)
            self.chatbotResponse.buildNetwork()
            self.chatbotResponse.loadModel()
            print('fin response')

    ## Encuentra las posibles respuestas ##
    def classify(self,sentence):
        return self.chatbotResponse.classify(sentence)

    def response(self,sentence):
        self.chatbotResponse.response(sentence)


    """
        Metodo para ejecutar el Chatbot Resolutor
    """
    # def runResolutorCB(self):
    #     CRunSolveErrors(self.currentChatbotFather,self.dictSentences,self.jsonFileCurrentChatbot)

    """
        Metodos para guardar las sentencias no reconocidas
    """
    def saveSentence(self):
        CSaveSentence(self.currentChatbotFather, self.errorSentence, self.dictSentences).exec()

    def dontSaveSentence(self):
        CDontSaveSentence(self.errorSentence).exec()

    def notSentenceRecognized(self):
        CNotRecognizedSentence(self.errorSentence).exec()


    """
        Metodos para terminar/empezar la ejecucion de un chatbot
    """
    def finishRunningChatbot(self):
        CFinishRunningCB(self.runChatBot,self.currentChatbotChild)

    def startRunningChatbot(self):
        CStartRunningCB(self.currentChatbotChild,self.pathChildrenChatbots)


