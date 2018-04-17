from StructureChatBot.StructureIntent import CStructureIntent

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

