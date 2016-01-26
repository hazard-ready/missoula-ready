from django.shortcuts import render
from collections import OrderedDict
from .models import Snugget, Location, SiteSettings, SupplyKit, ImportantLink
from .fire_dial import make_icon

likely_scenarios = {
    'fire': {
        'title': 'Likely Wildfire Scenario',
        'text': "Wildfire season stretches from spring to fall in Missoula County. In a low snowpack year the potential for fires increases. Is the area where you live at risk for a potential burn?"
    },
    'flood': {
        'title': 'Likely Flood Scenario',
        'text': "It’s springtime in Missoula County and the temperature has been steadily rising causing the snowpack to melt. It has been raining for many days and the rivers begin flooding. Will you feel the flood effects?"
    },
    'landslide': {
        'title': 'Landslide',
        'text': "Landslides typically happen after rainstorms come through and especially in burned areas without vegetation to stabilize the slopes. Find out if you should be concerned in your area."
    },
    'earthquake': {
        'title': 'Earthquake',
        'text': {"Earthquakes can happen anytime. In Missoula County there are five faults that are considered active. It is most likely that a small earthquake of magnitude 4 to 5 would strike here. What kind of shaking might you experience?"
    }
}

def app_view(request):
    location = Location.get_solo()
    important_links = ImportantLink.objects.all()
    settings = SiteSettings.get_solo()
    data_bounds = Location.get_data_bounds()
    supply_kit = SupplyKit.get_solo()
    supply_kit.meals = 3 * supply_kit.days
    template = "no_content_found.html"

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

                        data[key] = {
                            'heading': heading,
                            'sections': sections
                        }

        return render(request, template, {
            'location': location,
            'settings': settings,
            'supply_kit': supply_kit,
            'important_links': important_links,
            'data_bounds': data_bounds,
            'data': OrderedDict(sorted(data.items(), key=lambda t: t[0])),
            'likely_scenarios': likely_scenarios
        })


    # if not, we'll still serve up the same template without data
    else:
        return render(request, 'index.html', {
            'location': location,
            'settings': settings,
            'data_bounds': data_bounds
            })
