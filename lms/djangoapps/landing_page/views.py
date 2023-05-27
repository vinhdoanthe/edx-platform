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
    # mission_image = generate_image_url(mission[0]['image'].id, 'fill-1920x1080')
    mission_image = ''

    context.update({
        'homepage': home,
        'menu': menu,
        'banner': list_to_dict(banner),
        'features': list_to_dict(features),
        'why': list_to_dict(why),
        'mission': list_to_dict(mission),
        'proof_points': list_to_dict(proof_points),
        'services': list_to_dict(services),
        'case_studies': list_to_dict(case_studies),
        'testimonials': list_to_dict(testimonials),
        'subscription_form': list_to_dict(subscription_form),
        'footer': list_to_dict(footer),
        'mission_image': mission_image,
        'missing_home': False
        })

    return render(request, 'landing_page/index.html', context=context)
