#! /bin/bash
# -*- coding: utf-8 -*-
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
import Response
import Trainer
from Interfaces.IActionSubclasses.NotLineClasses.SaveSentenceAfirmative import CSaveSentenceAfirmative

class CBProcessor(object):

    def __init__(self):
        #para guardar sentencia no reconocida
        self.errorSentence = ''
        self.dictSentences = {}

        self.pathChildrenChatbots = ''
        self.currentChatbotChild = None
        self.currentChatbotFather = ''

        self.sentence = ''
        self.mode = 'chatbot'
        self.currentAction = ''
        self.actions = {'saveSentence':self.updateErrorSentence,'saveSentenceAfirmative':self.saveSentenceAfirmativeMetachatbot

                        }

        self.context = ''
        self.chatbotModel = None
        self.chatbotResponse = None #Response.Response()

        self.name = ''
        self.sentenciaAnterior = ''


    """
        Metodos para guardar las sentencias no reconocidas
    """
    def updateErrorSentence(self):
        if not self.errorSentence is '':
            print('Desea guardar la sentencia "',self.errorSentence,'" ?.')
        else:
            print('Hubo un error con la sentencia no reconocida.')

    def saveSentenceAfirmativeMetachatbot(self):
        CSaveSentenceAfirmative(self.currentChatbotFather, self.errorSentence, self.dictSentences).exec()




    #"""
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
    #"""

    def preparateResponse(self,chatbotName,jsonFile,pathModel):
        # if self.chatbotModel == None:
        #     print('Se necesita crear el Modelo primero.')
        if not ('.json' in jsonFile) or (chatbotName == ''):
            print('Se necesita especificar la ruta del fichero JSON.')
        else:
            print('inicio response')
            self.currentChatbotFather = chatbotName
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
                self.actions[self.chatbotResponse.action]()

            #reinicia el atributo
            self.chatbotResponse.action = ''
        else:
            # guarda la sentencia que no se reconocio
            self.errorSentence = sentence
            print('No se ha reconocido la frase "',sentence,'".')



        # if self.mode == 'modoOpciones':
        #     if sentence == 'G':
        #         self.opcionGuardar(self.sentenciaAnterior)
        #         self.mode = 'chatbot'
        #     elif sentence == 'N':
        #         self.opcionNada()
        #         self.mode = 'chatbot'
        #     else:
        #         print('No se ha reconocido la opcion escogida')
        #
        # elif self.mode == 'chatbot':
        #     self.sentenciaAnterior = sentence
        #     valorClasificacion = self.chatbotResponse.classify(sentence)
        #
        #     if valorClasificacion[0][1] >= 0.9:
        #
        #         self.chatbotResponse.response(sentence)
        #         if 'toJSON' in self.chatbotResponse.action:
        #             self.actions[self.chatbotResponse.action](self.currentChatbotName)
        #             return True
        #         elif 'listar' in self.chatbotResponse.action or 'mostrar' in self.chatbotResponse.action:
        #             self.currentAction = self.chatbotResponse.action
        #             self.actions[self.currentAction]()
        #             self.currentAction = ''
        #             return True
        #         elif 'resolver' in self.chatbotResponse.action:
        #             self.actions[self.chatbotResponse.action]()
        #         elif not (self.chatbotResponse.action == '') : # ha encontrado una accion que espera un literal
        #             self.currentAction = self.chatbotResponse.action
        #             self.mode = 'modoTexto'
        #             return True
        #
        #     else:
        #         print('No se ha reconocido la frase.')
        #         print('Que queire hacer: \nG -> guardar la frase \nN -> no hacer nada ')
        #         self.mode = 'modoOpciones'
        #
        #
        # elif self.mode == 'modoTexto': # ha encontrado una accion
        #     #se hace el response para ver si se ha introducido "error" y ejecutar su respuesta
        #     classifyError = self.chatbotResponse.classify(sentence)
        #
        #     if 'error' in classifyError[0][0] and classifyError[0][1]>=0.9:
        #         # se ejecuta la accion del error -> guardar la sentencia
        #         self.actions['error'](self.sentenciaAnterior, self.name)
        #
        #     # si no se ha encontrado la accion de "error" se ejecuta la accion que se había guardado previamente
        #     else:
        #         # self.actions[self.chatbotResponse.action]()
        #         self.actions[self.currentAction](sentence)
        #
        #     #en cualquier caso se reinicia el modo y la accion actual, la diferencia de controlar la palabra "error" es el de mostrar un mensaje.
        #     self.mode = 'chatbot'  # reinicia el valor
        #     self.currentAction = ''

    def getAction(self):
        return self.currentAction

    def resetAction(self):
        self.currentAction = ''
