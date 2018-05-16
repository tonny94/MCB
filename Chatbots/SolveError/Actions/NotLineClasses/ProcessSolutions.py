from Abstract.AActionSubclasses.ActionLine import ActionLine
import json

class CProcessSolutions(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot
        self.chatbotToProcess = self.chatbot.chatbot

    def exec(self,):
        if self.chatbot.listResolvedErrors == {}:
            self.chatbot.output.exec('No hay soluciones para procesar/resolver.')
        else:
            with open(self.chatbotToProcess.jsonPath, 'r+') as f:
                data = json.load(f)
                intents = data[self.chatbotToProcess.name]
                for sentence,intent in self.chatbot.listResolvedErrors.items():
                    for i in intents:
                        # find a tag matching the first result
                        if i['tag'] == intent:
                            i['patterns'].append(sentence)
                            break

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

            # Reiniciar la lista de errores resueltos
            #listResolvedErrors = []
            copyResolvedErrores = self.chatbot.listResolvedErrors.copy()
            stringToPRint = ''
            for k in copyResolvedErrores:
                #listResolvedErrors.append(k)
                stringToPRint += k

                del(self.chatbot.listResolvedErrors[k])

            self.chatbot.output.exec('Se han resuelto los errores: '+stringToPRint)





    """
    para editar json

    with open('pruebaEdicionJSON.json','r+') as f:
    data = json.load(f)
    intents = data['chatbotprocessor']        
    intent = intents[0]
    intent['patterns'].append('123asd123')
    f.seek(0)
    json.dump(data,f,indent=4)
    f.truncate() 

    """