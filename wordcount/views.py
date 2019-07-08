# -*- coding: utf-8 -*-

#defining a view

from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request) :
    return render(request,'home.html')

def count(request) :
    fulltext = request.GET['fulltext']
    splitwordlist = fulltext.split()
    worddictionary = {}
   #counting the words in the text
    for word in splitwordlist:
        if word in worddictionary:
            #increase the count
             worddictionary[word] += 1
        else:
            #Add to the dictionary
            worddictionary[word] = 1
         
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse = True )
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(splitwordlist),'sortedwords':sortedwords})

def about(request) :
    return render(request,'about.html')