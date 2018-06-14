import os
from ChatBotProcessor import CBProcessor
from Chatbots.MetaChatBot.MetaChatBot import CMetaChatBot
from Chatbots.SolveError.SolveError import CSolveError

#META CHATBOT
mcb = CMetaChatBot()
cbp = CBProcessor(mcb)
cbp.startModel()
cbp.startPredictor()
cbp.run()



#SOLVE ERROR
# se = CSolveError()
# cbp = CBProcessor(se)
# cbp.startModel()
# cbp.startPredictor()
# cbp.run()


"""
interaction
    -2 atributos : input, output  - SEGUIR PROBANDO

ejecutar nuevo chatbot desde metachatbot. - SEGUIR PROBARNDO

realizar un SolveError separado. - TERMINAR DE PROBAR

crear un ejemplo de "Lista_Compra" funcional. - PROBAR

el nombre del chatbot, acciones -> quitar tildes, ñ, y espacios. - POSIBLES PROBLEMAS

1.- Que se muestre la solucion (sentencia e intent) del SolveError - PROBAR
2.- no admitir vacios en las acciones que esperan una sentencia - PROBAR
"""




"""
cambiar en MetaChatBot : loadChatbots -> para cargar el nombre del fichero json         -> LISTO
cambiar en SolveError : a la hora de cargar la lista de chatbots                        -> LISTO
cambiar en structurechatbot a la hora de generar el string de ficheros .py "toCode"     
cambiar createmodel del trainerandpredictor, chatbotName
"""