from Intent import Intent

class ChatBot:
    """Son class"""
    def __init__(self):
        self.name = None
        self.dicIntents = {}
        self.currentIntent = None

    #para inicializar el atributo 'Name'
    def setName(self, name):
        if self.name == None:
            self.name = name

    #para cambiar el atributo 'Name'
    def changeName(self, name):
        if self.name != None:
            self.name = name

    #añade in intetn a la lista y actualiza el intent actual
    def addIntent(self, nameIntent):
        myIntent = Intent()
        myIntent.setTag(nameIntent)
        self.dicIntents[nameIntent] = myIntent
        self.currentIntent = nameIntent
        return myIntent

    #elimina el intent de la lista, si existe, y si es actual reinicia el atributo 'currentIntent'
    def removeIntent(self, nameIntent):
        myIntent = None

        if nameIntent in self.dicIntents:
            myIntent = self.dicIntents[nameIntent]
            del self.dicIntents[nameIntent]

        if nameIntent is self.currentIntent:
            self.currentIntent = None

        return myIntent

    #cambia la intencion actual si existe en la lista
    def setCurrentIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            self.currentIntent = nameIntent
            return self.dicIntents[nameIntent]
        else:
            return None

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





    #devuelve el intent si existe y actualiza el atributo 'currentIntent'
    # def selectIntent(self, nameIntent):
    #     if nameIntent in self.dicIntents:
    #         self.currentIntent = nameIntent
    #         return self.dicIntents[nameIntent]
    #
    #     return None

