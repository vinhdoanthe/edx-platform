from django.shortcuts import render
from common.djangoapps.edxmako.shortcuts import render_to_response


# Create your views here.
def index(request):
    context = {}
    return render(request, 'landing_page/index.html', context=context)
