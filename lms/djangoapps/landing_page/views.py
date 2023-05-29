from django.shortcuts import render
from openedx.core.djangoapps.user_authn.toggles import (
        should_redirect_to_authn_microfrontend
        )

from .models import HomePage
from .services import (
        get_stream_field_data,
        list_to_dict
)

from wagtail.images.views.serve import generate_image_url

# Create your views here.


def index(request):
    should_redirect_to_authn_mfe = should_redirect_to_authn_microfrontend()

    home = HomePage.objects.first()

    context = {
        'should_redirect_to_authn_mfe': should_redirect_to_authn_mfe,
        'missing_home': False
    }

    if not home:
        context['missing_home'] = True

        return render(request, 'landing_page/index.html', context=context)

    menu = get_stream_field_data(home, 'menu')
    banner = get_stream_field_data(home, 'banner')
    features = get_stream_field_data(home, 'features')
    why = get_stream_field_data(home, 'why')
    mission = get_stream_field_data(home, 'mission')
    proof_points = get_stream_field_data(home, 'proof_points')
    services = get_stream_field_data(home, 'services')
    case_studies = get_stream_field_data(home, 'case_studies')
    testimonials = get_stream_field_data(home, 'testimonials')
    subscription_form = get_stream_field_data(home, 'subscription_form')
    footer = get_stream_field_data(home, 'footer')

    context.update({
        'homepage': home,
        'menu': menu,
        'banner': banner,
        'features': features,
        'why': why,
        'mission': mission,
        'proof_points': proof_points,
        'services': services,
        'case_studies': case_studies,
        'testimonials': testimonials,
        'subscription_form': subscription_form,
        'footer': footer,
        'missing_home': False
        })

    return render(request, 'landing_page/index.html', context=context)
