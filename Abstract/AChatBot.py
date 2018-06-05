
from Abstract.AActionSubclasses.NotLineClasses.FinishRunningCB import CFinishRunningCB
import TrainerPredictor

from Abstract.AActionSubclasses.NotLineClasses.SaveSentence import CSaveSentence
from Abstract.AActionSubclasses.NotLineClasses.DontSaveSentence import CDontSaveSentence
from Abstract.AActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence


from Abstract.AOutputSubclasses.Screen import CScreen
from Abstract.AInputSubclasses.Keyboard import CKeyboard
from Abstract.AInteractor import IInteractor
import os,json


class CChatBot(object):

    def __init__(self):
        self.name = ''
        self.intents = []

        # variable que cancela la ejecucion de un chatbot
        self.runChatBot = True

        self.jsonPath = ''
        self.generalPath = ''
        self.actionsPath = ''
        self.errorFilePath = ''

        self.errorDict = {}

        self.currentSentence = None
        self.currentIntent = None

        self.unrecognizedSentence = None
        self.unrecognizeIntent = None

        self.listGeneralActions = ['finishRunningChatbot','saveSentence','dontSaveSentence']
        self.actions = {
            'finishRunningChatbot': CFinishRunningCB(self),

            'saveSentence': CSaveSentence(self),
            'dontSaveSentence': CDontSaveSentence(self)
        }
        self.TrainerAndPredictor = None
        
        self.input = IInteractor.input
        self.output = IInteractor.output


    def initializePaths(self):
        pass

    def isEmpty(self,sentence):
        return sentence in ['',None,""]

    def saveUnrecognizedSentence(self,key,value):
        self.errorDict[key] = value

    def showRandomResponse(self):
        self.output.exec(self.TrainerAndPredictor.randomResponse)

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
            value = '"No se le asoció una intención"'
            if not valorClasificacion == []:
               value = valorClasificacion[0][0] #self.currentRunningChatbot.TrainerAndPredictor.getIntent(valorClasificacion[0][0])
            self.setUnrecognizedIntent(value)
            CNotRecognizedSentence(self.unrecognizedSentence).exec()

    def setUnrecognizedSentence(self, sentence):
        self.unrecognizedSentence = sentence

    def setUnrecognizedIntent(self, intent):
        self.unrecognizeIntent = intent

    def setCurrentSentence(self, sentence):
        self.currentSentence = sentence

    def setCurrentIntent(self, intent):
        self.currentIntent = intent

    def existModel(self,path):
        return os.path.exists(os.path.join(os.path.sep,path,'model.h5'))

    def startModel(self):
        if not (os.path.exists(self.jsonPath)):
            self.output.exec('No existe el fichero JSON "'+self.jsonPath+'".')
        else:
            if not self.existModel(self.generalPath):
                self.output.exec('running Trainer')
                self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
                self.TrainerAndPredictor.readJSON(self.jsonPath,self.name)
                self.TrainerAndPredictor.createElementsToModel()
                value = self.TrainerAndPredictor.trainingModel(self.generalPath)
                if not value:
                    self.output.exec('No se ha podido generar el Modelo porque se necesita más de 1 Intent con Patterns creados.')
                else:
                    self.TrainerAndPredictor.doPickle()
                    # self.TrainerAndPredictor.closeResource()
                self.output.exec('end to train')
            else:
                self.output.exec('El modelo ya existe')


    def startPredictor(self):
        if not (os.path.exists(self.jsonPath)):
            self.output.exec('No existe el fichero JSON "'+self.jsonPath+'".')
        else:
            self.output.exec('running Predictor')
            if self.TrainerAndPredictor is None:
                self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
                self.TrainerAndPredictor.loadArrays(self.generalPath)
                self.TrainerAndPredictor.readJSON(self.jsonPath,self.name)
                self.TrainerAndPredictor.buildNetwork()
                self.TrainerAndPredictor.loadModel()
            # self.TrainerAndPredictor.closeResource()
            self.setIntentsList()
            self.setErrorDict()
            self.output.exec('end to predict')

    def setIntentsList(self):
        self.intents = self.TrainerAndPredictor.classes

    def setErrorDict(self):
        with open(self.errorFilePath, 'r', encoding='utf-8') as json_data:
            self.errorDict = json.load(json_data)