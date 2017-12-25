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

############################################

class Model:

    def __init__(self):
        self.jsonFile = None
        self.chatbotName = None
        self.intents = None
        self.words = []
        self.classes = []#tag's
        self.documents = []  #
        self.ignore_words = ['?']
        self.training = []
        self.output = []
        self.train_x = []
        self.train_y = []
        #self.output_empty = None#[0] * len(classes)

    def setPropertiesJSON(self,jsonFile,chatbotName):
        self.jsonFile = jsonFile
        self.chatbotName = chatbotName

    def readJSON(self):
        if self.jsonFile == None:
            print('Se necesita especificar la ruta del fichero JSON.')
        else:
            with open(self.jsonFile) as json_data:
                self.intents = json.load(json_data)

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

    def trainingModel(self):

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

            self.training.append([bag, output_row])

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
        model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
        # Start training (apply gradient descent algorithm)
        model.fit(self.train_x, self.train_y, n_epoch=1000, batch_size=8, show_metric=True)
        model.save('model.tflearn')

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

    def doPickle(self):
        import pickle
        pickle.dump({'words': self.words, 'classes': self.classes, 'train_x': self.train_x, 'train_y': self.train_y},
                    open("training_data", "wb"))


"""
if __name__ == "__main__":
    myModel = Model()
    myModel.setPropertiesJSON('lista_compra.json', 'lista_compra')
    myModel.readJSON()
    myModel.createElementsToModel()
    myModel.trainingModel()
    myModel.doPickle()

"""










# import our chat-bot intents file

"""
with open('lista_compra.json') as json_data:
    intents = json.load(json_data)
"""

############################################

"""


words = []#palabras
classes = []#tag's
documents = []#
ignore_words = ['?']
# loop through each sentence in our intents patterns
for intent in intents['lista_compra']:#selecciona el chatbot
    for pattern in intent['patterns']:#selecciona las preguntas del chatbot
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)#selecciona las palabras
        # add to our words list
        words.extend(w)#anhade las palabras a una lista
        # add to documents in our corpus
        documents.append((w, intent['tag']))#relaciona cada palabra con su TAG
        # add to our classes list
        if intent['tag'] not in classes:#selecciona los TAG'S
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]#selecciona raiz de las palabras
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)
"""

############################################


"""
# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])


############################################


# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')
"""

############################################
"""
def clean_up_sentence(self, sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words
"""



"""

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


#p = bow("quiero ver los chatbots que hay", words)
#print (p)
#print (classes)

############################################

#print(model.predict([p]))

############################################


"""
# save all of our data structures
import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )
"""