from django.shortcuts import render
from django.urls import reverse

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
    menu_order = {
            "key_selling_points": 0,
            "why": 1,
            "mission": 2,
            "proof_points": 3,
            "services": 4,
            "courses": 5,
            "case_studies": 6,
            "testimonials": 7,
            "subscription_form": 8,
            }
    course_url = request.build_absolute_uri(reverse('courses'))
    menu.update({'courses': {'enable': True, 'title': 'Courses', 'url': course_url}})

    for k, v in menu.items():
        if k == 'logo':
            continue
        v['order'] = menu_order[k]

    logo = menu['logo']
    del menu['logo']
    menu_data = dict(sorted(menu.items(), key=lambda item: item[1]['order']))
    menu_data.update({'logo': logo})

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
        'menu': menu_data,
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
