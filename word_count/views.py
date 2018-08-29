from django.http import HttpResponse
from django.shortcuts import render

import operator

def home(request):
    return render(request, 'home.html', {'greeting':'This is Nez project'})

def count(request):
    fullText = request.GET['fullText']
    words = fullText.split()
    wordLst = {}
    for word in words:
        if word.capitalize() in wordLst.keys():
            wordLst[word.capitalize()] += 1
        else:
            wordLst[word.capitalize()] = 1

    sortedLst = sorted(wordLst.items(), key=operator.itemgetter(0), reverse=False)
    #itemgetter(position) ex. ('Nez':5) position 0 will be 'Nez'
    return render(request, 'count.html', {'result' : sortedLst, 'word_length': len(words)})

def about(request):
    return render(request, 'about.html', {'pageName' : 'About page:'})
