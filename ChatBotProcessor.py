import Response
#import Trainer

class CBProcessor:

    def __init__(self):
        self.intens = {}
        self.sentence = ''
        #self.actions = {'añadirItem' : self.añadirItem, 'eliminarItem' : self.eliminarItem}
        self.mode = 'chatbot'
        self.currentAction = ''
        self.context = ''
        #self.chatbotModel = Trainer.Model()
        self.chatbotResponse = None

    """
    def preparateModel(self,chatbotName,jsonFile,pathModel):


        if not ('.json' in jsonFile)  or (chatbotName == ''):
            print('Se necesita especificar la ruta del fichero JSON.')
        else:
            self.chatbotModel.readJSON(jsonFile,chatbotName)
            self.chatbotModel.createElementsToModel()
            self.chatbotModel.trainingModel(pathModel)
            self.chatbotModel.doPickle()

    """

    def preparateResponse(self,chatbotName,jsonFile,pathModel):


        if not ('.json' in jsonFile)  or (chatbotName == ''):
            print('Se necesita especificar la ruta del fichero JSON.')
        else:
            self.chatbotResponse = Response.Response(pathModel)
            self.chatbotResponse.readJSON(jsonFile,chatbotName)
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
            #self.actions[self.currentAction](sentence)

    def getAction(self):
        return self.currentAction

    def resetAction(self):
        self.currentAction = ''

    """
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
    """


    #def addAction(self,clave, valor):

    #def dispatchAction(self):

    def añadirItem(self,sentence):
        return print('El item '+sentence+' se ha anhadido correctamente a la cesta.')


    def eliminarItem(self,sentence):
        return print('El item '+sentence+' se ha anhadido correctamente a la cesta.')

