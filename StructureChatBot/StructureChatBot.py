from StructureChatBot.StructureIntent import CStructureIntent
import os

class CStructureChatBot:
    """Son class"""
    def __init__(self):
        self.name = ''
        self.dicIntents = {}
        self.currentIntent = None

    #para inicializar el atributo 'Name'
    def setName(self, name):
        self.name = name

    def printCurrentIntent(self):
        if self.currentIntent is None:
            print('No hay un Intent actual para el chatbot "',self.name,'".')
        else:
            print('"',self.currentIntent.tag,'"')

    def printDictIntents(self):
        result = ", ".join(str(value.tag) for key, value in self.dicIntents.items())
        print('Los Intents del chatbot "',self.name,'" son:',result)

    #añade in intetn a la lista y actualiza el intent actual, devuelve un estado según cómo haya ido la insercion
    def addIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            print('Ya existe "', nameIntent, '" en la lista de Intents del chatbot "', self.name, '".')
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
            print('Se ha eliminado "',nameIntent,'" de la lista de Intents del cahtbot "',self.name,'".')

            if not(self.currentIntent is None) and nameIntent == self.currentIntent.tag:
                self.currentIntent = None
                print('"',nameIntent,'" ha dejado se ser la intencion actual.')
        else:
            print('No existe "',nameIntent,'" en la lista de Intents del cahtbot "',self.name,'".')

    #cambia la intencion actual si existe en la lista
    def setCurrentIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            if not self.currentIntent is None:
                nameIntent = self.currentIntent.tag
                print('Se ha cambiado "', nameIntent, '" por "', nameIntent, '".')
            else:
                print('Ahora "', nameIntent, '" es el actual Intent.')
            self.currentIntent = self.dicIntents[nameIntent]
        else:
            print('No existe "', nameIntent, '" en la lista de Intents del cahtbot "', self.name, '".')



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

    def  toCode(self,listGeneralActions,pathAction):
        lengDict = 1
        strImports = 'import os,inspect \nfrom Interfaces.IChatBot import CChatBot\nfrom Interfaces.IActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence\n'
        strActions = 'self.actionsCB = {'
        for tag in self.dicIntents:
            if not tag in listGeneralActions:
                intent = self.dicIntents[tag]
                if not intent.action == '':
                    nameActionFile = intent.action.title()
                    nameActionClass = 'C'+intent.action.title()

                    #crea los ficheros .py de cada accion
                    self.createActions(pathAction,nameActionFile,nameActionClass)

                    #construye el diccionario de acciones
                    if lengDict == 1:
                        strActions += '\''+intent.action+'\':'+nameActionClass+'(self)'
                    else:
                        strActions += ', \''+intent.action+'\':'+nameActionClass+'(self)'

                    #construye el string de todos los import para las acciones
                    strImports += 'from Chatbots.'+self.name+'.Actions.'+nameActionFile+' import '+nameActionClass+'\n'

            lengDict += 1

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
        print(strChatbotCode)
        return strChatbotCode





    def createActions(self,pathAction,nameActionFile,nameActionClass):
        codeFile = open(os.path.join(os.path.sep,pathAction,nameActionFile+'.py'), 'w')
        codeFile.write(self.actionToCode(nameActionClass))
        codeFile.close()

    def actionToCode(self,nameActionClass):
        str = 'from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine\n'
        str +='class '+nameActionClass+'(ActionNotLine):\n\n'
        str += '\tdef __init__(self,chatbot):\n'
        str += '\t\tself.chatbot = chatbot\n\n'
        str += '\tdef exec(self,):\n'
        str += '\t\tpass'
        return str



















