from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dict = {}

    for w in words:
        if w in word_dict:
            #증가
            word_dict[w]+=1
        else:
            #추가
            word_dict[w]=1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dict':word_dict.items()}) #키값 dict 설정 {'키값임의로정하기':텍스트가담긴변수}