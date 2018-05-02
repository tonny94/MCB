# -*- coding: utf-8 -*-

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
import json
import os
import pickle
#*obser = unicode(self.edit_observ.toPlainText())*
#* obser1 = obser.encode('utf-8')*

############################################

class CTrainerPredictor:

    def __init__(self):
        self.jsonFile = ''
        self.chatbotName = ''
        self.intents = []#toda la estructura 'metachatbot':{...}
        self.model = None
        self.pathModel = ''

        self.words = []
        self.classes = []#tag's
        self.documents = []

        self.ignore_words = ['?']
        self.training = []
        self.output = []

        self.train_x = []
        self.train_y = []

        self.action = ''
        self.intent = ''
        self.ERROR_THRESHOLD = 0.25
        self.context = {}




    #lee el json y inicializa el atributo 'intents'
    def readJSON(self,jsonFile,chatbotName):
        self.jsonFile = jsonFile
        self.chatbotName = chatbotName
        with open(self.jsonFile) as json_data:
            self.intents = json.load(json_data)

    #inicializa las listas que se necesita para el modelo: words,clasees,documents
    def createElementsToModel(self):

        for intent in self.intents[self.chatbotName]:  # selecciona el chatbot
            for pattern in intent['patterns']:  # selecciona las preguntas del chatbot
                # tokenize each word in the sentence
                w = nltk.word_tokenize(pattern)  # selecciona las palabras
                # add to our words list
                self.words.extend(w)  # anhade las palabras a una lista
                # add to documents in our corpus
                self.documents.append((w, intent['tag']))  # relaciona cada palabra con su TAG
                # add to our classes list
                if intent['tag'] not in self.classes:  # selecciona los TAG'S
                    self.classes.append(intent['tag'])

        # stem and lower each word and remove duplicates
        self.words = [stemmer.stem(w.lower()) for w in self.words if w not in self.ignore_words]  # selecciona raiz de las palabras
        self.words = sorted(list(set(self.words)))

        # remove duplicates
        self.classes = sorted(list(set(self.classes)))

        print(len(self.documents), "documents")
        print(len(self.classes), "classes", self.classes)
        print(len(self.words), "unique stemmed words", self.words)

    #entrena el modelo
    def trainingModel(self,pathModel):

        self.pathModel = pathModel
        if not os.path.isdir(pathModel):
            os.makedirs(pathModel) #mkdir


        output_empty = [0] * len(self.classes)

        # training set, bag of words for each sentence
        for doc in self.documents:
            # initialize our bag of words
            bag = []
            # list of tokenized words for the pattern
            pattern_words = doc[0]
            # stem each word
            pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
            # create our bag of words array
            for w in self.words:
                bag.append(1) if w in pattern_words else bag.append(0)

            # output is a '0' for each tag and '1' for current tag
            output_row = list(output_empty)
            output_row[self.classes.index(doc[1])] = 1

            self.training.append([bag,output_row])

        # shuffle our features and turn into np.array
        random.shuffle(self.training)
        self.training = np.array(self.training)

        # create train and test lists
        self.train_x = list(self.training[:, 0])
        self.train_y = list(self.training[:, 1])

        ############################################


        # reset underlying graph data
        tf.reset_default_graph()
        # Build neural network
        net = tflearn.input_data(shape=[None, len(self.train_x[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(self.train_y[0]), activation='softmax')
        net = tflearn.regression(net)

        # Define model and setup tensorboard
        # listSplit = self.pathModel.split(os.sep)
        # pathTrainingData = self.pathModel.replace(listSplit[len(listSplit) - 1], '')
        #tf.reset_default_graph()
        self.model = tflearn.DNN(net, tensorboard_dir=self.pathModel)
        # Start training (apply gradient descent algorithm)
        self.model.fit(self.train_x, self.train_y, n_epoch=1000, batch_size=8, show_metric=True)
        self.model.save(os.path.join(os.path.sep,self.pathModel,'model.tflearn'))

    def clean_up_sentence(self,sentence):
        # tokenize the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(self,sentence, words, show_details=False):

        sentence_words =  self.clean_up_sentence(sentence)
        # bag of words
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return (np.array(bag))

    #guarda los datos de entrenamiento
    def doPickle(self):
        # list = self.pathModel.split(os.sep)
        # pathTrainingData = self.pathModel.replace(list[len(list)-1],'')
        import pickle
        pickle.dump({'words': self.words, 'classes': self.classes, 'train_x': self.train_x, 'train_y': self.train_y},
                    open(os.path.join(os.path.sep,self.pathModel,"training_data"), "wb"))

    #cierra la secion del model
    def closeResource(self):
        self.model.session.close()










#
# PARTE DE PPREDICTOR
#

    def loadArrays(self,pathModel):
        self.pathModel = pathModel
        # listSplit = self.pathModel.split(os.sep)
        # pathTrainingData = self.pathModel.replace(listSplit[len(listSplit) - 1], '')

        self.data = pickle.load(open(os.path.join(os.path.sep,self.pathModel, "training_data"), "rb"))
        self.words = self.data['words']
        self.classes = self.data['classes']
        self.train_x = self.data['train_x']
        self.train_y = self.data['train_y']

    #lee el fichero json y actualiza el atributo 'intents'
    # def readJSON(self,jsonFile,chatbotName):
    #     self.jsonFile = jsonFile
    #     self.chatbotName = chatbotName
    #     with open(self.jsonFile) as json_data:
    #         self.intents = json.load(json_data)

    #construye la red
    def buildNetwork(self):
        net = tflearn.input_data(shape=[None, len(self.train_x[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(self.train_y[0]), activation='softmax')
        net = tflearn.regression(net)
        # Define model and setup tensorboard
        self.model = tflearn.DNN(net, tensorboard_dir = self.pathModel)

    #carga el objeto 'model'
    def loadModel(self):
        # listSplit = self.pathModel.split(os.sep)
        # pathModelFiles = self.pathModel.replace(listSplit[len(listSplit) - 1], '')
        self.model.load(os.path.join(os.path.sep,self.pathModel,'model.tflearn'))


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

    #da una respuesta acorde a la frase introducida
    def predict(self, sentence, userID='123', show_details=False):

        results = self.classify(sentence)

        # if we have a classification then find the matching intent tag
        if results:
            # loop as long as there are matches to process
            while results:
                for i in self.intents[self.chatbotName]:
                    # find a tag matching the first result
                    if i['tag'] == results[0][0]:

                        if 'action' in i:
                            # myAction.selectOption(sentence, i['tag'])
                            self.action = i['action']


                        if self.context == {}:
                            # set context for this intent if necessary
                            if 'context_set' in i:
                                if show_details: print('context:', i['context_set'])
                                self.context[userID] = i['context_set']

                            # check if this intent is contextual and applies to this user's conversation
                            # if (not 'context_filter' in i) or (userID in self.context and 'context_filter' in i and i['context_filter'] == self.context[userID]):
                            #     if show_details: print('tag:', i['tag'])


                            self.intent = i

                            # a random predict from the intent - si no hay respuestas no se imprime nada
                            if not len(i['responses']) == 0:
                                return print( (random.choice(i['responses'])) )
                            else:
                                return
                        #comprobacion de que la intencion, si tiene context_filter, concuerde con el context_set
                        elif 'context_filter' in i and self.context[userID] == i['context_filter']:
                            #reinicia en contexto
                            self.context = {}

                            # a random predict from the intent - si no hay respuestas no se imprime nada
                            if not len(i['responses']) == 0:
                                return print((random.choice(i['responses'])))
                            else:
                                return

                results.pop(0)

    def getIntent(self,intent):
        for i in self.intents[self.chatbotName]:
            # find a tag matching the first result
            if i['tag'] == intent:
                return i
            else:
                return None