# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nltk as nlp


def code1():
    t = "Twinkel Twinkle little star, how i wonder what you are?"
    tlist = t.split()
    print(tlist)
    manuallist = token1(t)
    print(manuallist)
    token = nlp.word_tokenize(t)
    print(token)
    
   
def token(t):
    r = len(t)
    new_t = " "
    for c in range(r):
        c=t[c]
        if str(c).isalpha() or str(c).isdigit() or c == " ":
            new_t = new_t + str(c)
        else:
            new_t = new_t + " " + str(c)
    new_t = new_t.split()
    return new_t


def token1(t):
    r = len(t)
    new_t = " "
    ka = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    kd = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for c in range(r):
        c=t[c]
        if str(c) in ka or str(c) in kd or c == " ":
            new_t = new_t + str(c)
        else:
            new_t = new_t + " " + str(c)
    new_t = new_t.split()
    return new_t    

code1()
