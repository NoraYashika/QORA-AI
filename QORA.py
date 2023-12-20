# ai imports
import  random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

#import os for filepaths
import os

lemmatizer = WordNetLemmatizer()
intents = json.load(open(f'{os.getcwd()}\\intents.json', 'r'))

words = pickle.load(open(f'{os.getcwd()}\\network\\words.pkl', 'rb'))
classes = pickle.load(open(f'{os.getcwd()}\\network\\classes.pkl', 'rb'))
model = load_model(f"{os.getcwd()}\\network\\qora_neural_network.keras")

def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict(sentence):
    bag = bag_of_words(sentence)
    res = model.predict(np.array([bag]))[0]
    ERROR_THRESHOLD = 0.50  # 50 %
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key = lambda x: x[1], reverse = True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_lst, intents_json):
    tag  = intents_lst[0]['intent']
    intents_lst = intents_json['intents']
    for i in intents_lst:
        if i['tag'] == tag:
            answer = random.choice(i['responses'])
            break
    return answer

print("Hello, I am QORA, how may I help you?")

while True:
    message = input("")
    ints = predict(message)
    res = get_response(ints, intents)
    print(res)