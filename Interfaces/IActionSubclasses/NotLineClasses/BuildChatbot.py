#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales
import os
from Response import Response
from Trainer import Model


class CBuildChatbot(ActionNotLine):

    def __init__(self,chatbot,path):
        self.chatbot = chatbot
        self.generalPath = path
        self.chatbotPath = os.path.join(self.generalPath,self.chatbot.name)
        self.dirJsonFile = ''

    def exec(self,):
        if not os.path.isdir(self.generalPath):
            print('La ruta debe ser un directorio(carpeta).')
        else:
            if not os.path.isdir(self.chatbotPath):
                os.makedirs(self.chatbotPath)
            self.crearJSON()
            print('Se ha construido el chatbot "', self.chatbot.name, '" correctamente.')

    def crearJSON(self):
        self.dirJsonFile = os.path.join(os.sep, self.chatbotPath, self.chatbot.name + '.json')
        jsonFile = open(self.dirJsonFile, 'w')
        jsonFile.write(self.chatbotToJson())
        # jsonFile.write(self.dicToJSON(self.dicChatBots) )
        jsonFile.close()
        self.startTrainer()
        #self.startResponse()

    def chatbotToJson(self):
        strJSON = self.chatbot.toJSON()
        return strJSON

    def startTrainer(self):
        VTrainer = Model()
        VTrainer.readJSON(self.dirJsonFile,self.chatbot.name)
        VTrainer.createElementsToModel()
        VTrainer.trainingModel(self.chatbotPath)
        VTrainer.doPickle()
        VTrainer.closeResource()
        print('Modelo de "',self.chatbot.name,'" creado.')

    def startResponse(self):
        VResponse = Response()
        VResponse.loadArrays(self.chatbotPath)
        VResponse.readJSON(self.dirJsonFile, self.chatbot.name)
        VResponse.buildNetwork()
        VResponse.loadModel()
        print('Response de "',self.chatbot.name,'" creado.')

# print(os.getcwd())
# print (os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir, os.pardir, 'CreatedChatbots')))