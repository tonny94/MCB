import os
from ChatBotProcessor import CBProcessor
from Chatbots.MetaChatBot.MetaChatBot import CMetaChatBot
from Chatbots.Lista_Compra.Lista_Compra import CLista_Compra
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

#LISTA_COMPRA
# lc = CLista_Compra()
# cbp = CBProcessor(lc)
# cbp.startModel()
# cbp.startPredictor()
# cbp.run()