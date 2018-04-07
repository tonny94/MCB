#! /bin/bash
# -*- coding: utf-8 -*-
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
import Response
import Trainer
import os
#Clase para ejecutar ChatbotResolutor
from Interfaces.IActionSubclasses.NotLineClasses.RunChatbotResolutor import CRunChatbotResolutor

from Interfaces.IActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence
from Interfaces.IActionSubclasses.NotLineClasses.SaveSentence import CSaveSentence
from Interfaces.IActionSubclasses.NotLineClasses.DontSaveSentence import CDontSaveSentence
from Interfaces.IActionSubclasses.NotLineClasses.FinishRunningCB import CFinishRunningCB
from Interfaces.IActionSubclasses.NotLineClasses.StartRunningCB import CStartRunningCB

class CBProcessor(object):

    def __init__(self):
        #para guardar sentencia no reconocida
        self.errorSentence = ''
        self.dictSentences = {}

        #para ejecutar un chatbot - finalizar ejecucion
        self.pathChildrenChatbots = os.path.join(os.path.sep,os.getcwd(),'CreatedChatbots') #ruta donde estan los chatbots
        self.currentChatbotChild = '' #el nombre del chatbot que se esta ejecutando
        self.runChatBot = False #variable que cancela la ejecucion de un chatbot

        # para ejecutar chatbot resolutor
        self.jsonFileCurrentChatbot = ''
        self.currentChatbotFather = ''

        self.currentAction = ''
        self.actions = {'saveSentence':self.saveSentence,'dontSaveSentence':self.dontSaveSentence,
                        'runResolutorCB': self.runResolutorCB,
                        'finishRunningChatbot':self.finishRunningChatbot, 'startRunningChatbot':self.startRunningChatbot
                        }

        self.chatbotModel = None
        self.chatbotResponse = None #Response.Response()


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
        print(self.chatbotResponse.classify(sentence))

    def response(self,sentence):

        valorClasificacion = self.chatbotResponse.classify(sentence)
        if  (not valorClasificacion == []) and valorClasificacion[0][1] >= 0.9:
            self.chatbotResponse.response(sentence)
            self.currentAction = self.chatbotResponse.action

            #guarda la sentencia que no se reconocio
            #if self.currentAction == 'saveSentence': self.errorSentence = sentence

            #comprueba que tenga una accion para ejecutar
            if not self.currentAction == '':
                self.actions[self.chatbotResponse.action]().exec()

            #reinicia el atributo
            self.chatbotResponse.action = ''
        else:
            # guarda la sentencia que no se reconocio
            self.errorSentence = sentence
            self.notSentenceRecognized()


    """
        Metodo para ejecutar el Chatbot Resolutor
    """
    def runResolutorCB(self):
        CRunChatbotResolutor(self.currentChatbotFather,self.dictSentences,self.jsonFileCurrentChatbot)

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


