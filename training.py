# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:04:38 2018

@author: Shabnam Rani
"""


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize


from os import listdir
from os.path import isfile, join


nltk.data.path = ['nltk_data']

stopwords = set(stopwords.words('english'))


spam_path = 'data/spam/'
easy_ham_path = 'data/easy_ham/'

def get_words(message):

   
    all_words = set(wordpunct_tokenize(message.replace('=\\n', '').lower()))
    
  
    msg_words = [word for word in all_words if word not in stopwords and len(word) > 2]
    
    return msg_words
    
def get_mail_from_file(file_name):
    
    """
    Returns the entire mail as a string from the given file.
    """
    
    message = ''
    
    with open(file_name, 'r') as mail_file:
        
        for line in mail_file:
           
            if line == '\n':
              
                for line in mail_file:
                    message += line
                    
    return message
    
    
    
def make_training_set(path):
 
    training_set = {}

    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]
    
    
    cmds_count = 0
 
    total_file_count = len(mails_in_dir)
    
    for mail_name in mails_in_dir:
        
        if mail_name == 'cmds':
            cmds_count += 1
            continue
        
        message = get_mail_from_file(path + mail_name)
        
        
        terms = get_words(message)
                    
      
        for term in terms:
            if term in training_set:
                training_set[term] = training_set[term] + 1
            else:
                training_set[term] = 1
    
 
    total_file_count -= cmds_count
   
    for term in training_set.keys():
        training_set[term] = float(training_set[term]) / total_file_count
                            
    return training_set

 
print "(Loading training sets...)",
spam_training_set = make_training_set(spam_path)
ham_training_set = make_training_set(easy_ham_path)
print "(done.)"
