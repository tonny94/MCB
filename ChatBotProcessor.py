# -*- coding: utf-8 -*-
import Tensorflow_chatbot_model
import Tensorflow_chatbot_response
###usarlo en cada caso que se use tildes o ñ###
import json
#*obser = unicode(self.edit_observ.toPlainText())*
#* obser1 = obser.encode('utf-8')*


class ChatBotProcessor:
    """Son class"""
    def __init__(self):
        self.intens = {}
        self.sentence = ''
        self.actions = {'añadirItem' : self.añadirItem, 'eliminarItem' : self.eliminarItem}
        self.mode = 'chatbot'
        self.currentAction = ''
        self.context = ''
        self.chatbotModel = Tensorflow_chatbot_model.Model()
        self.chatbotResponse = Tensorflow_chatbot_response.Response()


    def preparateModel(self,chatbotName,jsonFile):

        if chatbotName in self.intens:
            self.chatbotModel.setPropertiesJSON(jsonFile,chatbotName)
            self.chatbotModel.readJSON()
            self.chatbotModel.createElementsToModel()
            self.chatbotModel.trainingModel()
            self.chatbotModel.doPickle()
            #self.chatbotResponse = Tensorflow_chatbot_response.Response()
        else:
            print('El chatbot no existe en la lista de chatbots (intens)')


    def preparateResponse(self,nameIntent):
        if self.intens == {} :
            print('Se necesita tener al menos una intención guardada. ')
        else:
            self.chatbotResponse.setIntens(self.intens[nameIntent])
            self.chatbotResponse.buildNetwork()
            self.chatbotResponse.loadModel()


    ## Encuentra las posibles respuestas ##
    def classify(self,sentence):
        print(self.chatbotResponse.classify(sentence))


    ## Genera la respuesta ##

    def response(self,sentence):
        if self.mode == 'chatbot':
            print(self.chatbotResponse.response(sentence))
            if not (self.chatbotResponse.action == ''): # ha encontrado una accion
                self.mode = 'modoTexto'
                self.currentAction = self.chatbotResponse.action

        else: # ha encontrado una accion
            self.mode = 'chatbot' #reinicia el valor
            self.actions[self.currentAction](sentence)




    def setInten(self,chatbotName,jsonFile):
        if '.json' in jsonFile:
            if chatbotName in self.intens:
                return print('El nombre del chatbot ya existe.')
            else:
                with open(jsonFile) as json_data:
                    self.intens[chatbotName] = json.load(json_data)
                #self.intens[chatbotName] = jsonFile
        else:
            return print('Se necesita introducir un fichero en formato JSON')

    #def addAction(self,clave, valor):

    #def dispatchAction(self):

    def añadirItem(self,sentence):
        return print('El item '+sentence+' se ha anhadido correctamente a la cesta.')


    def eliminarItem(self,sentence):
        return print('El item '+sentence+' se ha anhadido correctamente a la cesta.')

