#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Response
import Trainer
import curses

class CBProcessor(object):

    def __init__(self):
        #self.intens = {}
        self.sentence = ''
        self.mode = 'chatbot'
        self.currentAction = ''
        self.actions = {'error':self.error ,
                        'listarError':self.listarError#,'listarErrorProcesados':self.listarErrorProcesados
                        }
        self.dicPattersnNoReconocidos = {}
        self.context = ''
        self.chatbotModel = None
        self.chatbotResponse = None #Response.Response()

        self.name = ''
        self.sentenciaAnterior = ''
        self.currentChatbotName = None


    def error(self,sentence,nombChatbot):
        if self.dicPattersnNoReconocidos is {}:
            #la primera lista es para los NO reconoidos, la sengunda es para los que YA han sido reconocidos
            self.dicPattersnNoReconocidos = {nombChatbot:[[],[]]}
        elif not nombChatbot in self.dicPattersnNoReconocidos:
            self.dicPattersnNoReconocidos = {nombChatbot: [[], []]}

        self.addNoReconocido(nombChatbot,sentence)

    def addNoReconocido(self,nombChatbot,sentence):
        listNoRec = self.dicPattersnNoReconocidos[nombChatbot][0]
        listNoRec.append(sentence)
        print('Se ha anhadido la sentencia a la lista de error')

    def addYaReconocido(self,nombChatbot,sentence):
        listNoRec = self.dicPattersnNoReconocidos[nombChatbot][0]
        listNoRec.remove(sentence)
        listYaRec = self.dicPattersnNoReconocidos[nombChatbot][1]

    def listarError(self):
        print(self.dicPattersnNoReconocidos)


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
            self.name = chatbotName
            self.chatbotResponse = Response.Response()
            self.chatbotResponse.cargarArrays(pathModel)
            self.chatbotResponse.readJSON(jsonFile,chatbotName)
            self.chatbotResponse.buildNetwork()
            self.chatbotResponse.loadModel()
            print('fin response')

    ## Encuentra las posibles respuestas ##
    def classify(self,sentence):
        print(self.chatbotResponse.classify(sentence))

    ## Genera la respuesta ##

    def opcionGuardar(self,sentencia):
        self.error(sentencia,self.name)

    def opcionNada(self):
        print('Se ha descartado la sentencia.')

    def response(self,sentence):

        if self.mode == 'modoOpciones':
            if sentence == 'G':
                self.opcionGuardar(self.sentenciaAnterior)
                self.mode = 'chatbot'
            elif sentence == 'N':
                self.opcionNada()
                self.mode = 'chatbot'
            else:
                print('No se ha reconocido la opcion escogida')

        elif self.mode == 'chatbot':
            self.sentenciaAnterior = sentence
            valorClasificacion = self.chatbotResponse.classify(sentence)

            if valorClasificacion[0][1] >= 0.9:

                self.chatbotResponse.response(sentence)
                if 'toJSON' in self.chatbotResponse.action:
                    self.actions[self.chatbotResponse.action](self.currentChatbotName)
                    return True
                elif 'listar' in self.chatbotResponse.action or 'mostrar' in self.chatbotResponse.action:
                    self.currentAction = self.chatbotResponse.action
                    self.actions[self.currentAction]()
                    self.currentAction = ''
                    return True
                elif 'resolver' in self.chatbotResponse.action:
                    self.actions[self.chatbotResponse.action]()
                elif not (self.chatbotResponse.action == '') : # ha encontrado una accion que espera un literal
                    self.currentAction = self.chatbotResponse.action
                    self.mode = 'modoTexto'
                    return True

            else:
                print('No se ha reconocido la frase.')
                print('Que queire hacer: \nG -> guardar la frase \nN -> no hacer nada ')
                self.mode = 'modoOpciones'


        elif self.mode == 'modoTexto': # ha encontrado una accion
            #se hace el response para ver si se ha introducido "error" y ejecutar su respuesta
            classifyError = self.chatbotResponse.classify(sentence)

            if 'error' in classifyError[0][0] and classifyError[0][1]>=0.9:
                # se ejecuta la accion del error -> guardar la sentencia
                self.actions['error'](self.sentenciaAnterior, self.name)

            # si no se ha encontrado la accion de "error" se ejecuta la accion que se había guardado previamente
            else:
                # self.actions[self.chatbotResponse.action]()
                self.actions[self.currentAction](sentence)

            #en cualquier caso se reinicia el modo y la accion actual, la diferencia de controlar la palabra "error" es el de mostrar un mensaje.
            self.mode = 'chatbot'  # reinicia el valor
            self.currentAction = ''

    def getAction(self):
        return self.currentAction

    def resetAction(self):
        self.currentAction = ''
