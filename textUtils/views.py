#this file is created my me-Vanshaj
from django.http import HttpResponse #we import this to return http response to server
from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')
        
def analyze(request):
    djtext=request.POST.get('text','default')

    #check checkbox value
    removepunc=request.POST.get('removepunc','off')
    capf=request.POST.get('capFirst','off')
    newline=request.POST.get('newlineremove','off')
    space=request.POST.get('spaceremove','off')
    fullcaps=request.POST.get('fullcaps','off')
    charcount=request.POST.get('charcount','off')

    analyzed=""
    purp=""
    punctuations='''!()@#$%^&*_+=[]{;}:'",./<>?`~|'''
    
    #check which checkbox is on
    if(removepunc=='on'):
        purp=purp+"Remove Punctuations"
        for char in djtext:
            if(char not in punctuations):
                
                analyzed=analyzed+char
    else:
        analyzed=djtext


    if(capf=='on'):
        purp=purp+"+Capital First"
        analyzed=analyzed.capitalize()
   

    if(newline=='on'):
        purp=purp+"+New Line remove"
        st=''
        for char in analyzed:
            if(char!='\n' and char!='\r'):
                st=st+char
        analyzed=st

    

    if(space=='on'):
        purp=purp+" +Space Remove"
        analyzed=analyzed.replace(' ','')

    if(fullcaps=='on'):
        purp=purp+" +UPPERCASE"
        str1=""
        for i in analyzed:
            str1=str1+i.upper()
        analyzed=str1

    if(charcount=='on'):
        purp=purp+" +Count Characters"
        count=0
        for i in analyzed:
            if(i.isalpha()):
                count+=1
        count=str(count)
        analyzed=analyzed+"\nThe number of characters are"+count

        
    params={'purpose':purp,'analyzed_text':analyzed}
    if(removepunc=='off' and charcount=='off' and fullcaps=='off' and space=='off' and capf=='off' and newline=='off'):
        return HttpResponse("Error")
    return render(request,'analyze.html',params)

