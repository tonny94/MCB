# things we need for NLP
import nltk
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')
#from nltk.stem.lancaster import LancasterStemmer
#stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random

# import the class actions for modify the chatbots
from actions import Action
from MetaChatBot import MetaChatBot
import pickle
import json


class Response:
    def __init__(self):
        self.model = None
        self.data = pickle.load( open( "training_data", "rb" ) )
        self.words = self.data['words']
        self.classes = self.data['classes']
        self.train_x = self.data['train_x']
        self.train_y = self.data['train_y']
        self.ERROR_THRESHOLD = 0.25
        self.context = {}
        self.intens = {}#listIntens
        self.action = ''


    def setIntens(self,json):
        self.intens = json

    """
    def setIntens(self,listIntens, intentName):
        with open(listIntens[intentName]) as json_data:
            self.intens = json.load(json_data)
"""

    def buildNetwork(self):
        net = tflearn.input_data(shape=[None, len(self.train_x[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(self.train_y[0]), activation='softmax')
        net = tflearn.regression(net)

        # Define model and setup tensorboard
        self.model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

        # instance of MetaChatBot object
        #myMetaChatBot = MetaChatBot()
        # instance of Action object
        #myAction = Action()
        #myAction.setMetaChatBot(myMetaChatBot)

    def loadModel(self):
        self.model.load('./model.tflearn')

    def clean_up_sentence(self,sentence):
        # tokenize the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(self,sentence, words, show_details=False):
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
        # bag of words
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return (np.array(bag))

    def classify(self,sentence):
        # generate probabilities from the model
        results = self.model.predict([self.bow(sentence, self.words)])[0]
        # filter out predictions below a threshold
        results = [[i, r] for i, r in enumerate(results) if r > self.ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((self.classes[r[0]], r[1]))
        # return tuple of intent and probability
        return return_list


    def response(self,sentence, userID='123', show_details=False):

        results = self.classify(sentence)

        # if we have a classification then find the matching intent tag
        if results:
            # loop as long as there are matches to process
            while results:
                for i in self.intens['lista_compra']:
                    # find a tag matching the first result
                    if i['tag'] == results[0][0]:

                        if 'action' in i:
                            # myAction.selectOption(sentence, i['tag'])
                            self.action = i['action']

                        # set context for this intent if necessary
                        if 'context_set' in i:
                            if show_details: print('context:', i['context_set'])
                            self.context[userID] = i['context_set']

                        # check if this intent is contextual and applies to this user's conversation
                        if (userID in self.context and 'context_filter' in i and i['context_filter'] == self.context[userID]):
                            if show_details: print('tag:', i['tag'])

                        # a random response from the intent
                        return (random.choice(i['responses']))

                results.pop(0)

"""


if __name__ == "__main__":
    intens = {}
    def setInten(chatbotName, jsonFile):
        if '.json' in jsonFile:
            if chatbotName in intens:
                return print('El nombre del chatbot ya existe.')
            else:
                intens[chatbotName] = jsonFile
        else:
            return print('Se necesita introducir un fichero en formato JSON')


    myResponse = Response()
    setInten('lista_compra','lista_compra.json')
    myResponse.setIntens(intens, 'lista_compra')
    myResponse.buildNetwork()
    myResponse.loadModel()

    print(myResponse.classify('Hola'))
    print(myResponse.classify('Quiero introducir un item'))

    #fallara porque no le paso el json, solo la ruta y el nombre, peo no la estructura JSON
    print(myResponse.response('Quiero anhadir un item'))

"""

############################################

"""

# restore all of our data structures
import pickle
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']
listaCompra=[]

# import our chat-bot intents file
import json
with open('lista_compra.json') as json_data:
    intents = json.load(json_data)

"""
############################################

"""
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

#instance of MetaChatBot object
myMetaChatBot = MetaChatBot()
#instance of Action object
myAction = Action()
myAction.setMetaChatBot(myMetaChatBot)
"""

############################################

"""
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))
"""

############################################

"""
p = bow("Quiero ver los items de la cesta", words)
print (p)
print (classes)
"""
############################################

"""
# load our saved model
model.load('./model.tflearn')
"""

############################################

"""
# create a data structure to hold user context
context = {}#None
modoChatbot = 'modo_chatbot'# {}
currentAction = {}#None

ERROR_THRESHOLD = 0.25


def classify(sentence):
	# generate probabilities from the model
	results = model.predict([bow(sentence, words)])[0]
	# filter out predictions below a threshold
	results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
	# sort by strength of probability
	results.sort(key=lambda x: x[1], reverse=True)
	return_list = []
	for r in results:
		return_list.append((classes[r[0]], r[1]))
	# return tuple of intent and probability
	return return_list


def response(sentence, userID='123', show_details=False):
    global modoChatbot
    global listaCompra
    ##modificar el itens.json para "lista de compra"
    # if modo=chatbot
    # ejecutar normalmente el chatbot
    # guardo en currentAction la accion que me encuentre en al intencion
    # elif modo=texto
    # ejecuto la accion dispatchAction(sentence,currentAction)
    print (modoChatbot)

    if modoChatbot == 'modo_chatbot' :
        results = classify(sentence)

        # if we have a classification then find the matching intent tag
        if results:
            # loop as long as there are matches to process
            while results:
                for i in intents['lista_compra']:
                    # find a tag matching the first result
                    if i['tag'] == results[0][0]:

                        # do an action
                        if 'action' in i:
                            #myAction.selectOption(sentence, i['tag'])
                            currentAction['1'] = i['action']
                            modoChatbot = 'modo_texto'

                        # set context for this intent if necessary
                        if 'context_set' in i:
                            if show_details: print('context:', i['context_set'])
                            context[userID] = i['context_set']

                        # check if this intent is contextual and applies to this user's conversation
                        if (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                            if show_details: print('tag:', i['tag'])

                        # a random response from the intent
                        return print(random.choice(i['responses']))

                results.pop(0)

    elif modoChatbot == 'modo_texto':
        #respuesta = myAction.selectOption(sentence, currentAction['1'])
        modoChatbot = 'modo_chatbot'
        if currentAction['1'] == 'anhadirItem':
            listaCompra.append(sentence)

        return print('anhadido')
"""


"""
classify('Anhadir elemento a la cesta')
response('Anhadir elemento a la cesta')
response('arroz')
print(listaCompra)
"""



