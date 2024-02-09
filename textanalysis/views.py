from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'front.html')

def upper(request):
    r = " "

    if request.method == "POST":
        text = request.POST.get('message')
        up = request.POST.get('upper','off')
        lo = request.POST.get('lower','off')
        sy = request.POST.get('punc','off')
        no = request.POST.get('number','off')
        word = request.POST.get('word','off')
        s = request.POST.get('s')
        cw = request.POST.get('cw','off')
        ci = request.POST.get('icw')


        if up == 'on' :
            a = "Upper Case Text:"

            r = text.upper()
        elif lo == 'on':
            a = "Lower Case Text:"
            r = text.lower()
        elif sy == 'on':
            a = "Text With Removed Symbols:"
            symb =''',?!:;'()"[]{}.../\&%$@=_|~<>.*+-'''
            for i in text:
                if i not in symb:
                    r = r + i
        elif no == 'on':
            a = "Text With Removed Numbers:"
            num = "1234567890"
            for i in text:
                if i not in num:
                    r +=i
        elif word == 'on':
            a = f"Text With Removed Word {s}:"
            b = text.split(" ")
            for i in b:
                if i == s:
                    b.remove(s)
                    r = ' '.join(b)
        elif cw == 'on':
            a = f"count of {ci}:"
            b = text.split(" ")
            count = 0
            for i in b:
                if i == ci:
                    count+=1
                    r = f"Count of {ci} is: {count}"
        else:
            a = "Error:"
            r = "Please Select The One Check Box When Enterig Your Text"


        

            
    return render(request,'result.html',{'r':r ,'a':a})