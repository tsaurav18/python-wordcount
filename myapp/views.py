from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def result(request):
    text=request.GET['fulltext']
    words=text.split()
    dictionary={}
    for word in words:
        if word in dictionary:
             #increase
             dictionary[word]+=1
        else:
             #add in dictionary
             dictionary[word]=1
      
    return render(request, 'result.html',{'full':text,'total':len(words),'dictt':dictionary.items()})