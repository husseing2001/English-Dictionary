from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antynoms = dictionary.antonym(search)
    
    context = {
        'meaning' : meaning,
        'synonyms' : synonyms,
        'antynoms' : antynoms
    }
    return render(request,'word.html',context)