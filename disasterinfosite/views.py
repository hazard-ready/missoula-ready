from django.shortcuts import render
from collections import OrderedDict
from .models import Snugget, Location, SiteSettings, SupplyKit, ImportantLink
from .fire_dial import make_icon

def app_view(request):
    location = Location.get_solo()
    important_links = ImportantLink.objects.all()
    settings = SiteSettings.get_solo()
    data_bounds = Location.get_data_bounds()
    supply_kit = SupplyKit.get_solo()
    supply_kit.meals = 3 * supply_kit.days
    template = "no_content_found.html"

    # Make sure that sections and subsections are always in the same order.
    section_order = {
        'what to expect': 0,
        'past events': 1,
        'how to prepare': 2
    }

    # Some of these are in different sections or are mutually exclusive, hence the non-unique values.
    sub_section_order = {
        'intensity': 0,
        'flood zones': 1,
        'ground shaking': 1,
        'worst case scenario': 2,
        'safety issues': 3,
        'historic events': 0,
        'get earthquake ready': 0,
        'get flood ready': 0,
        'get fire ready': 0,
        'stay tuned': 1,
        'a word from your emergency managers': 2
    }

    # Clean up the syntax for the ordered dicts below.
    def sort_by_name(value, sorting_dict):
        return sorting_dict[value[0].__str__().lower()]

    # if user submitted lat/lng, find our snuggets and send them to our template
    if 'lat' and 'lng' in request.GET:
        lat = request.GET['lat']
        lng = request.GET['lng']

        if len(lat) > 0:
            snugget_content = Snugget.findSnuggetsForPoint(lat=float(lat), lng=float(lng))

            data = {}
            if snugget_content is not None:
                for key, values in snugget_content['groups'].items():
                    sections = {}
                    if values:
                        template = 'found_content.html'
                        heading = values[0].heading
                        for text_snugget in values:
                            if not text_snugget.image:
                                text_snugget.dynamic_image = make_icon(text_snugget.percentage)
                            if not text_snugget.section in sections:
                                sections[text_snugget.section] = {}
                            if text_snugget.sub_section in sections[text_snugget.section]:
                                sections[text_snugget.section][text_snugget.sub_section].append(text_snugget)
                            else:
                                sections[text_snugget.section][text_snugget.sub_section] = [text_snugget]

                        for section, sub_section_dict in sections.items():
                            sections[section] = OrderedDict(sorted(sub_section_dict.items(), key=lambda t: sort_by_name(t, sub_section_order)))

                        data[key] = {
                            'heading': heading,
                            'sections': OrderedDict(sorted(sections.items(), key=lambda t: sort_by_name(t, section_order)))
                        }

        return render(request, template, {
            'location': location,
            'settings': settings,
            'supply_kit': supply_kit,
            'important_links': important_links,
            'data_bounds': data_bounds,
            'data': OrderedDict(sorted(data.items(), key=lambda t: t[0]))
        })


    # if not, we'll still serve up the same template without data
    else:
        return render(request, 'index.html', {
            'location': location,
            'settings': settings,
            'data_bounds': data_bounds
            })
