from django.shortcuts import render
from common.djangoapps.edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.user_authn.toggles import should_redirect_to_authn_microfrontend

# Create your views here.
def index(request):
    should_redirect_to_authn_mfe = should_redirect_to_authn_microfrontend()

    context = {
        'should_redirect_to_authn_mfe': should_redirect_to_authn_mfe,
    }
    return render(request, 'landing_page/index.html', context=context)
