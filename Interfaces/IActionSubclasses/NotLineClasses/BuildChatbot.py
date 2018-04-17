#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales
import os
from TrainerPredictor import CTrainerPredictor


class CBuildChatbot(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot
        self.structureChatbot = self.chatbot.currentStructureChatBot
        self.generalPath = os.path.join(os.path.sep,os.getcwd(),'Chatbots')
        self.structureChatbotPath = ''
        self.structureDirJsonFile = ''

    def exec(self,):
        if self.structureChatbot is None:
            print('ERROR: No hay un Chatbot actual para construir.')
        else:
            #inicializa las variables
            self.structureChatbotPath = os.path.join(os.path.sep,self.generalPath,self.structureChatbot.name)
            self.structureDirJsonFile = os.path.join(os.path.sep,self.structureChatbotPath,self.structureChatbot.name+'.json')

            if os.path.exists(self.generalPath) and not (os.path.isdir(self.generalPath)):
                print('ERROR: La ruta debe ser un directorio(carpeta).')
            else:
                if not os.path.isdir(self.structureChatbotPath):
                    os.makedirs(self.structureChatbotPath)
                self.crearJSON()
                print('Se ha construido el chatbot "',self.structureChatbot.name, '" correctamente.')

    def crearJSON(self):
        jsonFile = open(self.structureDirJsonFile, 'w')
        jsonFile.write(self.chatbotToJson())
        jsonFile.close()
        self.startTrainer()

    def chatbotToJson(self):
        strJSON = self.chatbot[1].toJSON()
        return strJSON

    def startTrainer(self):
        VTrainer = CTrainerPredictor()
        VTrainer.readJSON(self.structureDirJsonFile,self.structureChatbot.name)
        VTrainer.createElementsToModel()
        VTrainer.trainingModel(self.structureChatbotPath)
        VTrainer.doPickle()
        VTrainer.closeResource()
        print('Modelo de "',self.structureChatbot.name,'" creado.')

    # def startResponse(self):
    #     VResponse = Response()
    #     VResponse.loadArrays(self.structureChatbotPath)
    #     VResponse.readJSON(self.structureDirJsonFile,self.structureChatbot.name)
    #     VResponse.buildNetwork()
    #     VResponse.loadModel()
    #     print('Response de "',self.structureChatbot.name,'" creado.')



