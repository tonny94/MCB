from StructureChatBot.StructureIntent import CStructureIntent
from Abstract.AOutputSubclasses.Screen import CScreen

import os,json

class CStructureChatBot:
    """Son class"""
    def __init__(self):
        self.name = ''
        self.dicIntents = {}
        self.currentIntent = None
        self.ouput = CScreen()

    #para inicializar el atributo 'Name'
    def setName(self, name):
        self.name = name

    def printCurrentIntent(self):
        if self.currentIntent is None:
            self.ouput.exec('No hay un Intent actual para el chatbot "'+self.name+'".')
        else:
            self.ouput.exec('"'+self.currentIntent.tag+'"')

    def printDictIntents(self):
        result = ", ".join(str(value.tag) for key, value in self.dicIntents.items())
        self.ouput.exec('Los Intents del chatbot "'+self.name+'" son:'+result)

    #añade in intetn a la lista y actualiza el intent actual, devuelve un estado según cómo haya ido la insercion
    def addIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            self.ouput.exec('Ya existe "'+ nameIntent+ '" en la lista de Intents del chatbot "'+ self.name+ '".')
            return False
        else:
            myIntent = CStructureIntent()
            myIntent.setTag(nameIntent)
            self.dicIntents[nameIntent] = myIntent
            self.currentIntent = myIntent
            return True

    #elimina el intent de la lista, si existe, y si es actual reinicia el atributo 'currentIntent'
    def deleteIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            del self.dicIntents[nameIntent]
            self.ouput.exec('Se ha eliminado "'+nameIntent+'" de la lista de Intents del cahtbot "'+self.name+'".')

            if not(self.currentIntent is None) and nameIntent == self.currentIntent.tag:
                self.currentIntent = None
                self.ouput.exec('"'+nameIntent+'" ha dejado se ser la intencion actual.')
        else:
            self.ouput.exec('No existe "'+nameIntent+'" en la lista de Intents del cahtbot "'+self.name+'".')

    #cambia la intencion actual si existe en la lista
    def setCurrentIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            if not self.currentIntent is None:
                self.ouput.exec('Se ha cambiado "'+ self.currentIntent.tag+ '" por "'+nameIntent+'".')
            else:
                self.ouput.exec('Ahora "'+nameIntent+'" es el actual Intent.')
            self.currentIntent = self.dicIntents[nameIntent]
        else:
            self.ouput.exec('No existe "'+ nameIntent+ '" en la lista de Intents del cahtbot "'+ self.name+ '".')

    #pasa el diccionario de intenciones en formato JSON
    def dicToJSON(self,dicIntents):
        if len(dicIntents) > 0:
            length = 0
            strJSON = '\n\t\t[\n\t\t\t'
            for intent in dicIntents:
                if length == len(dicIntents)-1:
                    strJSON += dicIntents[intent].toJSON()+'\n\t\t]'
                else:
                    strJSON += dicIntents[intent].toJSON()+',\n\t\t\t'
                length += 1
            return strJSON
        else:
            return '[]'

    #pasa el objeto 'Chatbot' a formato JSON
    def toJSON(self):
        strJson = '{"' + self.name + '":'
        strJson += self.dicToJSON(self.dicIntents)+'\n\t'
        strJson += '}'
        return strJson

    def toCode(self,listGeneralActions,pathAction):
        lengDict = 1
        strImports = 'import os,inspect \nfrom Abstract.AChatBot import CChatBot\nfrom Abstract.AActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence\n'
        strActions = 'self.actionsCB = {'

        #seleccionar acciones que no sean las acciones generales y aquellos intens que si tengan acciones
        listActions = []
        for tag in self.dicIntents:
            if not tag in listGeneralActions:
                intent = self.dicIntents[tag]
                if not intent.action == '':
                    listActions.append(intent.action)

        for action in listActions:
            nameActionFile = action.title()
            nameActionClass = 'C'+action.title()

            #crea los ficheros .py de cada accion
            self.createActions(pathAction,nameActionFile,nameActionClass)

            #construye el diccionario de acciones
            if lengDict == 1:
                strActions += '\''+action+'\':'+nameActionClass+'(self)'
                lengDict = 0
            else:
                strActions += ', \''+action+'\':'+nameActionClass+'(self)'

            #construye el string de todos los import para las acciones
            strImports += 'from Chatbots.'+self.name+'.Actions.'+nameActionFile+' import '+nameActionClass+'\n'

            

        strActions += ' }'
        strChatbotClass = 'C'+self.name
        strChatbotCode = strImports+'\nclass '+strChatbotClass+'(CChatBot):\n'
        strChatbotCode += '\tdef __init__(self):\n'
        strChatbotCode += '\t\tsuper('+strChatbotClass+', self).__init__()\n'
        strChatbotCode += '\t\t'+strActions+'\n'
        strChatbotCode += '\t\tself.initializePaths()\n\n'

        #initializePaths
        strChatbotCode +='\tdef initializePaths(self):\n'
        strChatbotCode += '\t\tstrSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)\n'
        strChatbotCode += '\t\tself.name = strSplit[len(strSplit)-1]\n'
        strChatbotCode += '\t\tself.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))\n'
        strChatbotCode += '\t\tself.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+\'.json\')\n\n'

        #saveUnrecognizedSentence
        strChatbotCode += '\tdef saveUnrecognizedSentence(self,key,value):\n'
        strChatbotCode += '\t\tnewDict = {key:value}\n'
        strChatbotCode += '\t\tself.errorDict.update(newDict)\n\n'

        #execPrediction
        strChatbotCode += '\tdef execPrediction(self,sentence):\n'
        strChatbotCode += '\t\tvalorClasificacion = self.TrainerAndPredictor.classify(sentence)\n'
        strChatbotCode += '\t\tif (not valorClasificacion == []) and valorClasificacion[0][1] >= 0.9:\n'
        strChatbotCode += '\t\t\tself.TrainerAndPredictor.predict(sentence)\n'
        strChatbotCode += '\t\t\tself.currentAction = self.TrainerAndPredictor.action\n'
        strChatbotCode += '\t\t\tif not self.currentAction == \'\':\n'
        strChatbotCode += '\t\t\t\tself.actions[self.currentAction].exec()\n'
        strChatbotCode += '\t\t\t\tself.TrainerAndPredictor.action = \'\'\n'
        strChatbotCode += '\t\telse:\n'
        strChatbotCode += '\t\t\tCNotRecognizedSentence(self.unrecognizedSentence).exec()\n'
        self.ouput.exec(strChatbotCode)
        return strChatbotCode

    def createActions(self,pathAction,nameActionFile,nameActionClass):
        codeFile = open(os.path.join(os.path.sep,pathAction,nameActionFile+'.py'), 'w')
        codeFile.write(self.actionToCode(nameActionClass))
        codeFile.close()

    def actionToCode(self,nameActionClass):
        str = 'from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine\n'
        str +='class '+nameActionClass+'(ActionNotLine):\n\n'
        str += '\tdef __init__(self,chatbot):\n'
        str += '\t\tself.chatbot = chatbot\n\n'
        str += '\tdef exec(self,):\n'
        str += '\t\tpass'
        return str




    def codeToStructureChatbot(self,chatbot,jsonFile):

        with open(jsonFile) as json_data:
            chatbotJsonStructure = json.load(json_data)
        listIntenst = chatbotJsonStructure[chatbot.name]

        lastIntent = 1
        for intent in listIntenst:
            structureIntent = CStructureIntent()
            structureIntent.codeToStructureIntent(intent)
            chatbot.dicIntents[structureIntent.tag]=structureIntent
            if lastIntent == len(listIntenst):
                chatbot.setCurrentIntent(structureIntent.tag)
            lastIntent += 1






















