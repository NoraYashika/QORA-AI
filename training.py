# ai imports
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import LearningRateScheduler

# os for filepaths
import os

def learning_rate_schedule(epoch):
    initial_learning_rate = 0.01
    decay = 1e-6
    lr = initial_learning_rate / (1 + decay * epoch)
    return lr

lemmatizer = WordNetLemmatizer()

intents = json.load(open(f'{os.getcwd()}\\intents.json', 'r'))

batch = 3
epochs = 500
losstype = 'categorical_crossentropy' #tf.compat.v1.losses.sparse_softmax_cross_entropy()

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open(f'{os.getcwd()}\\network\\words.pkl', 'wb'))
pickle.dump(classes, open(f'{os.getcwd()}\\network\\classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype = object)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape = (len(train_x[0]),), activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = 'softmax'))

lr_scheduler = LearningRateScheduler(learning_rate_schedule)

sgd = SGD(learning_rate = 0.01, momentum = 0.9, nesterov = True)

model.compile(loss = losstype, optimizer = sgd, metrics = ['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs = epochs, batch_size = batch, verbose = 1, callbacks = [lr_scheduler])

model.save(f'{os.getcwd()}\\network\\qora_neural_network.keras', hist)

print("Done")
input("Press any Button to close the training program...")
exit()