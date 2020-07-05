from django.http import HttpResponse


def home(request):
    return HttpResponse(''
                        '<html>'
                        '<title>Projeto Django</title>'
                        '<body>'
                        '<h1>Olá, Django!</h1>'
                        '</body>'
                        '</html>',
                        content_type='text/html')
