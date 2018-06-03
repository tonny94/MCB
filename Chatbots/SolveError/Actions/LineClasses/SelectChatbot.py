from Abstract.AActionSubclasses.ActionLine import ActionLine
import os,json

class CSelectChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.showRandomResponse()
        sentence = self.chatbot.input.exec()
        if not (self.checkCancellation(sentence)):

            if not(sentence in self.chatbot.listChatbots):
                self.chatbot.output.exec('El chatbot "'+sentence+'" no existe.')
            elif not os.path.exists(os.path.join(os.path.sep,self.chatbot.generalPathChatbotToSolve,sentence,sentence+'_ErrorFile.json')):
                self.chatbot.output.exec('El chatbot "' + sentence + '" no tiene un fichero de errores.')
            else:
                self.chatbot.pathErrorFileChatbotToSolve = os.path.join(os.path.sep,self.chatbot.generalPathChatbotToSolve,sentence,sentence+'_ErrorFile.json')
                self.chatbot.pathJSONChatbotToSolve = os.path.join(os.path.sep,self.chatbot.generalPathChatbotToSolve,sentence, sentence + '.json')

                with open(self.chatbot.pathErrorFileChatbotToSolve, 'r', encoding='utf-8') as json_data:
                    self.chatbot.listUnresolvedErrors = json.load(json_data)

                if self.chatbot.listUnresolvedErrors == {}:
                    self.chatbot.output.exec('El chatbot "'+sentence+'" ya no tiene sentencias que resolver.')
                    # self.chatbot.nameChatbotToSolve = ''
                else:
                    self.chatbot.nameChatbotToSolve = sentence
                    listIntents = []
                    with open(self.chatbot.pathJSONChatbotToSolve, 'r', encoding='utf-8') as json_data:
                        jsonChatbot = json.load(json_data)
                        for i in jsonChatbot[sentence]:
                            listIntents.append(i['tag'])
                    self.chatbot.listIntens = listIntents
                    self.chatbot.output.exec('Se ha seleccionado el chatbot "'+ sentence+ '".')

    def checkCancellation(self, sentence):
        if (sentence.lower()  in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False
