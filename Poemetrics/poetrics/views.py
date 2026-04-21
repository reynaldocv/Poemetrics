from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template import RequestContext
from urllib.parse import unquote, quote
from poetrics.modules import metrica



def webpage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def analysis(request):
    data = {
        'output': 'Django User',
        'status': 'active',
        'items': [1, 2, 3]
    }
    return JsonResponse(data)

def test(request):
    output = ''
    
    if request.method == 'GET':
        output = (request.GET.get('input', 'No input provided'))
        output = output.replace("—", " ")
        
    verses = output.split('\n')
    newVerses = []
    
    for verse in verses:        
        newVerses.append(metrica.oracion(verse))
    
    ans = "".join(newVerses)
    
    ans = "<table>" + ans + "</table>"
        
    data = {
        'output': (ans if ans != "" else "No input provided"), 
        'status': 'success',
        'items': ['a', 'b', 'c']
    }
    return JsonResponse(data)





