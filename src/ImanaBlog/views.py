from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bienvenu sur mon site web avec Django et bientot je deviens dev django<h1/>")