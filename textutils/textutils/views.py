#I have created this file, not generated - Sanath#
from django.http import HttpResponse
# def index(request):
#     return HttpResponse('''<h1>Hello Sanath</h1> <a href = "https://fmovies.hn/tv/watch-family-guy-full-39549">Best
#     Family Show </a>''')
#
# def about(req):
#     return HttpResponse("About Sanath")
from django.shortcuts import render
def index(req):
    # return HttpResponse("Home")

    return render(req,'index.html')
def analyze(req):
    djtext = req.POST.get('text','default')
    removepunc = req.POST.get('removepunc','off')
    fullcaps = req.POST.get('fullcaps', 'off')
    newlineremover = req.POST.get('newlineremover', 'off')
    extraspaceremover = req.POST.get('extraspaceremover', 'off')
    params = {}
    if djtext == "":
        return HttpResponse("Go back and insert the text you want to analyze in the text area")


    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params = {'purpose': 'Punctuations Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(req, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(req, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(req, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(req, 'analyze.html', params)
    if removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on":
        return HttpResponse("Go back and select atleast one operation to perform on your text")
    return render(req, 'analyze.html', params)



