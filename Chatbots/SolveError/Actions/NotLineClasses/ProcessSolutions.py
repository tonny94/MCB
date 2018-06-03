from Abstract.AActionSubclasses.ActionLine import ActionLine
import os,json
from TrainerPredictor import CTrainerPredictor

class CProcessSolutions(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):

        if self.chatbot.nameChatbotToSolve == '':
            self.chatbot.output.exec('No hay un chatbot seleccionado.')
        elif not (self.chatbot.nameChatbotToSolve == '') and self.chatbot.listResolvedErrors == {}:
            self.chatbot.output.exec('El chatbot "'+self.chatbot.nameChatbotToSolve+'" no tiene soluciones que aplicar.')
        else:
            with open(self.chatbot.pathJSONChatbotToSolve, 'r+',encoding='utf-8') as f:
                data = json.load(f)
                intents = data[self.chatbot.nameChatbotToSolve]
                for sentence,intent in self.chatbot.listResolvedErrors.items():
                    for i in intents:
                        # find a tag matching the first result
                        if i['tag'] == intent:
                            i['patterns'].append(sentence)
                            break

                f.seek(0)
                json.dump(data, f, ensure_ascii=False,indent=4)
                f.truncate()

            listSolvedErros = []
            with open(self.chatbot.pathErrorFileChatbotToSolve, 'r+', encoding='utf-8') as f:
                json_data = json.load(f)

                copyResolvedErrores = self.chatbot.listResolvedErrors.copy()
                for k, v in copyResolvedErrores.items():
                    listSolvedErros.append(k)
                    del (json_data[k])
                    del (self.chatbot.listResolvedErrors[k])
                result = ", ".join(str(value) for value in listSolvedErros)

                f.seek(0)
                json.dump(json_data, f, ensure_ascii=False, indent=4)
                f.truncate()

            self.rebuildModel()
            self.chatbot.output.exec('Se han resuelto los errores: '+result)


    def rebuildModel(self):
        if not (os.path.exists(self.chatbot.pathJSONChatbotToSolve)):
            self.chatbot.output.exec('No existe el fichero JSON "'+self.chatbot.pathJSONChatbotToSolve+'".')
        else:
            self.chatbot.output.exec('running Trainer')
            TrainerAndPredictor = CTrainerPredictor()
            TrainerAndPredictor.readJSON(self.chatbot.pathJSONChatbotToSolve,self.chatbot.nameChatbotToSolve)
            TrainerAndPredictor.createElementsToModel()
            pathModelChatbotToSolve = os.path.join(os.path.sep,self.chatbot.generalPathChatbotToSolve,self.chatbot.nameChatbotToSolve)
            value = TrainerAndPredictor.trainingModel(pathModelChatbotToSolve)
            if not value:
                self.chatbot.output.exec('No se ha podido generar el Modelo porque se necesita más de 1 Intent con Patterns creados.')
            else:
                TrainerAndPredictor.doPickle()
                # self.TrainerAndPredictor.closeResource()
            self.chatbot.output.exec('end to train')


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