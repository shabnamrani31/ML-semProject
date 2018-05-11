# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:04:36 2018

@author: Shabnam Rani
"""



from training import *


def classify(message, training_set, prior = 0.5, c = 3.7e-4):
    
   
    
    msg_terms = get_words(message)
    
    msg_probability = 1
    
    for term in msg_terms:        
        if term in training_set:
            msg_probability *= training_set[term]
        else:
            msg_probability *= c
            
    return msg_probability * prior


mail_msg=("shabnam")

spam_probability = classify(mail_msg, spam_training_set, 0.2)
ham_probability = classify(mail_msg, ham_training_set, 0.8)
if spam_probability > ham_probability:
    print ("Your mail has been classified as SPAM.")
else:
    print ("Your mail has been classified as HAM.")
print ("")
