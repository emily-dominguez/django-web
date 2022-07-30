# was created by me and not given or created by default; what the userface sees 

from turtle import pu
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    

    # content = { 
    #     "Data": "There is data",
    #     "Roll_number": [1,2,3,4,5,6,7,8,9,10], 
    #     "first_name": "Emily",
    #     "last_name": "Dominguez",
    #     "variable_name": "What is your name?"
    # 
    # }

    return render(request,"textutils-2.html") # have imported card render, will take the request anything in the code and then print html
#     return HttpResponse('''<a href="www.google.com">Google</a>
# <a href="www.facebook.com">Facebook</a>
# <a href="www.youtube.com">Youtube</a>
# <a href="www.apple.com">Apple</a>''')
 
def removepunctuations(request):
    # asked to get the text written inside of itgetting w/e is stored in text.utilities
    inputtext = request.POST.get('text', 'default') 
    # asks about the removepunctuations button 
    removepunctuations = request.POST.get('removepunctuations', 'off') 
    capitalize = request.POST.get('capitalize', 'off')
    spaceremover = request.POST.get('spaceremover', 'ff')
    # if the user has clicked it: 
    if removepunctuations == "on":
        punctuations = '''!@$%^&*()_+-={}[]:;><,.?/#'''
        # analyzed does not contain anything
        analyzed = ""
        for char in inputtext: 
            # if there is no punctuations, then we do not do anything 
            if char not in punctuations: 
                analyzed = analyzed + char 
        # other wise inside a new variable make it = to task which is to remove punctuation, analyzed task
        user_text = {'Task': 'Removed Punctuations','analyzed_text': analyzed }
        inputtext = analyzed
    # if the user did not click it
    if capitalize == "on":
        analyzed = "" 
        for char in inputtext:
            analyzed = analyzed + char.upper()
        user_text = {'Task': 'Capitalized','analyzed_text': analyzed }
        inputtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        # enumurate mean can run the loop acroding to it's values
        for index, char in enumerate(inputtext):
            if not (inputtext[index] == " " and inputtext[index + 1]== " "):
                analyzed = analyzed + char
        user_text = {'Task': 'Sorted','analyzed_text': analyzed }
        inputtext = analyzed
    
    if (removepunctuations != "on" and capitalize != "on" and spaceremover != "on"):
        return HttpResponse("You have not selected any responses")
    
    return render(request, 'analyzed.html', user_text)

    # else: 
        # return HttpResponse('ERROR: YOUR TEXT HAS NOT BEEN ANALYZED')

''' #1 created functions in views file 
#2 in utlities created a form, bc if you want user to enter text want a form,
 inside form, posted action, as they sumbit the value of form is sent to 'removepunctuations
 method a way in by which we can access the text; everyhting below is about the style
 #3 created abother html to show the outout, analyzed
 #4 backend section: removefunctions function  '''


def about(request):
    return HttpResponse("about this web page")

def home(request):
    return HttpResponse("welcome to the home page of this website")

def about(request):
    return HttpResponse("about this web page")
