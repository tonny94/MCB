from Interfaces.IActionSubclasses.ActionLine import ActionLine
import json

class CProcessSolutions(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot
        self.chatbotToProcess = self.chatbot.chatbot

    def exec(self,):
        if self.chatbot.listResolvedErrors == {}:
            print('No hay soluciones para procesar/resolver.')
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
            listResolvedErrors = []
            for k in self.chatbot.listResolvedErrors.keys():
                listResolvedErrors.append(k)
                del(self.chatbot.listResolvedErrors[k])

            print('Se han resuelto los errores: ',listResolvedErrors)





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