from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def wordcount(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    word_dictionary = {}
    total=len(word_list)
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    if total>=10:
        gnarstate=False
    else:
        gnarstate=True
    return render(request, 'wordcount.html', {'alltext': entered_text, 'dictionary': word_dictionary.items(),'total':total, 'gnarstate':gnarstate})