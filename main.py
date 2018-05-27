#! /bin/bash
# -*- coding: utf-8 -*-

import os
from ChatBotProcessor import CBProcessor
from Chatbots.MetaChatBot.MetaChatBot import CMetaChatBot

# import keras
# import sys
# import tensorflow as tf
# print("pyton: {}, keras: {}".format(sys.version,keras.__version__))

#METACHATBOT
mcb = CMetaChatBot()
cbp = CBProcessor(mcb)
cbp.startModel()
cbp.startPredictor()
cbp.run()

"""
FALLOS:
1.- Tras ejecutar un chatbot desde el MEtaChatbot, se sale de la ejecucion siempre que no sea una palabra del un pattern
"""








