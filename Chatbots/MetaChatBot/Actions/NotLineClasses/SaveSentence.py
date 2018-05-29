#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine
import os
import json
class CSaveSentence(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot


    def exec(self,):
        if self.chatbot.unrecognizedSentence is None and self.chatbot.currentSentence is None:
            self.chatbot.output.exec('ERROR: No hay sentencia que guardar.')
        elif self.chatbot.unrecognizedSentence in self.chatbot.errorDict or self.chatbot.currentSentence in self.chatbot.errorDict:
            self.chatbot.output.exec('La sentencia reconocida ya existe en la lista.')
        else:
            key = ''
            value = ''
            if self.chatbot.unrecognizedSentence is None:
                value= self.chatbot.currentIntent.tag
                key = self.chatbot.currentSentence
            else:
                value = self.chatbot.unrecognizeIntent
                key = self.chatbot.unrecognizedSentence

            self.chatbot.saveUnrecognizedSentence(key,value)
            #----- guardar errores en su fichero -----------#
            with open(self.chatbot.errorFilePath, 'r+', encoding='utf-8') as f:
                json_data = json.load(f)
                json_data.update(self.chatbot.errorDict)
                f.seek(0)
                json.dump(json_data, f, ensure_ascii=False, indent=4)
                f.truncate()


            self.chatbot.output.exec('Se ha guardado la sentencia "' + key + '" que se le ha asociado erroneamente con la intención "'+value+'".')



            # ----- mostrar caracteres especiales -----------#
            # with open('p1.json', 'r', encoding='utf-8') as f:
            #     json_data = json.load(f)
            #     for k, v in json_data.items():
            #         print(k + '->' + v)


    def addNoReconocido(self, nombChatbot):
        #self.dictionary[nombChatbot][0].append(self.sentence)
        self.chatbot.output.exec('Se ha anhadido la sentencia a la lista de error.')
