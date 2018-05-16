#! /bin/bash
# -*- coding: utf-8 -*-


import nltk
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')

import numpy as np
import random
import json
import os
import pickle

import h5py
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.models import load_model

from Abstract.AOutputSubclasses.Screen import CScreen

class CTrainerPredictor:

    def __init__(self):
        self.ouput = CScreen()
        
        self.jsonFile = ''
        self.chatbotName = ''
        self.intents = []
        self.model = None
        self.pathModel = ''

        self.words = []
        self.classes = []
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

    def readJSON(self,jsonFile,chatbotName):
        self.jsonFile = jsonFile
        self.chatbotName = chatbotName
        with open(self.jsonFile) as json_data:
            self.intents = json.load(json_data)

    #inicializa las listas que se necesita para el modelo: words,clasees,documents
    def createElementsToModel(self):

        for intent in self.intents[self.chatbotName]:
            for pattern in intent['patterns']:
                # tokenize each word in the sentence
                w = nltk.word_tokenize(pattern)
                # add to our words list
                self.words.extend(w)
                # add to documents in our corpus
                self.documents.append((w, intent['tag']))
                # add to our classes list
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        # stem and lower each word and remove duplicates
        self.words = [stemmer.stem(w.lower()) for w in self.words if w not in self.ignore_words]
        self.words = sorted(list(set(self.words)))

        # remove duplicates
        self.classes = sorted(list(set(self.classes)))

        self.ouput.exec( str(len(self.documents))+ ' documents')
        self.ouput.exec( str(len(self.classes))+ "classes ["+ ', '.join(self.classes) +']' )
        self.ouput.exec( str(len(self.words)) + "unique stemmed words ["+', '.join(self.words) + ']')

    #entrena el modelo
    def trainingModel(self,pathModel):

        self.pathModel = pathModel
        if not os.path.isdir(pathModel):
            os.makedirs(pathModel)

        self.train_x = []
        self.train_y = []
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

            self.train_x.append(np.array(bag))
            self.train_y.append(np.array(output_row))

        # create train and test lists
        self.train_x = np.array(self.train_x)
        self.train_y = np.array(self.train_y)
        self.ouput.exec(self.train_y)

        #comprueba de que hayan datos de salida > 1
        if self.train_y.shape[1] == 1:
            return False
        else:
            self.model = Sequential()
            # Dense(64) is a fully-connected layer with 64 hidden units.
            # in the first layer, you must specify the expected input data shape:
            # here, 20-dimensional vectors.
            self.model.add(Dense(25, input_dim=self.train_x.shape[1]))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(25))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(self.train_y.shape[1], activation='softmax'))

            sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
            self.model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

            self.model.fit(self.train_x, self.train_y, epochs=1000, batch_size=8)
            self.model.save(os.path.join(os.path.sep,self.pathModel,'model.h5'))
            return True

    #guarda los datos de entrenamiento
    def doPickle(self):
        import pickle
        pickle.dump({'words': self.words, 'classes': self.classes},
                    open(os.path.join(os.path.sep,self.pathModel,"training_data"), "wb"))

    #cierra la secion del model
    def closeResource(self):
        self.model.session.close()

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

#
# PARTE DE PPREDICTOR
#

    def loadArrays(self,pathModel):
        self.pathModel = pathModel
        self.data = pickle.load(open(os.path.join(os.path.sep,self.pathModel, "training_data"), "rb"))
        self.words = self.data['words']
        self.classes = self.data['classes']

    #construye la red
    def buildNetwork(self):
        pass

    #carga el objeto 'model'
    def loadModel(self):
        self.model = load_model(os.path.join(os.path.sep,self.pathModel,'model.h5'))

    def classify(self,sentence):
        # generate probabilities from the model
        results = self.model.predict(np.array([self.bow(sentence, self.words)]))[0]
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
                            self.intent = i
                            # a random predict from the intent - si no hay respuestas no se imprime nada
                            if not len(i['responses']) == 0:
                                return self.ouput.exec( (random.choice(i['responses'])) )
                            else:
                                return
                        #comprobacion de que la intencion, si tiene context_filter, concuerde con el context_set
                        elif 'context_filter' in i and self.context[userID] == i['context_filter']:
                            #reinicia en contexto
                            self.context = {}
                            if not len(i['responses']) == 0:
                                return self.ouput.exec((random.choice(i['responses'])))
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