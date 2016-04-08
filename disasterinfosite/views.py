from django.shortcuts import render
from collections import OrderedDict
from .models import Snugget, Location, SiteSettings, SupplyKit, ImportantLink, PastEventsPhoto, DataOverviewImage, UserProfile
from .fire_dial import make_icon
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.db.utils import IntegrityError

def create_user(request):
    if request.method == 'POST':

        try:
            user = User.objects.create_user(
                username=request.POST.get('username'),
                email=request.POST.get('username'),
                password=request.POST.get('password')
            )
        except IntegrityError:
            return HttpResponse(status=409, reason="That user already exists.")

        profile = UserProfile(
            user=user,
            address1=request.POST.get('address1'),
            address2=request.POST.get('address2'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip_code=request.POST.get('zip_code')
        )
        profile.save()
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        login(request, user)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=403)

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    profile = None
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("#user-info-container")
    else:
        # Show an error page
        return HttpResponseRedirect("#user-info-container--invalid")

def update_profile(request):
    if request.method == 'POST' and request.user.is_authenticated():
        username = request.user.username
        profile = UserProfile.objects.get(user=request.user)
        profile.address1 = request.POST.get('address1')
        profile.address2 = request.POST.get('address2')
        profile.city = request.POST.get('city')
        profile.state = request.POST.get('state')
        profile.zip_code = request.POST.get('zip_code')

        profile.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=403)

def app_view(request):
    location = Location.get_solo()
    important_links = ImportantLink.objects.all()
    settings = SiteSettings.get_solo()
    data_bounds = Location.get_data_bounds()
    supply_kit = SupplyKit.get_solo()
    supply_kit.meals = 3 * supply_kit.days
    quick_data_overview = DataOverviewImage.objects.all()
    username = None
    profile = None
    if request.user.is_authenticated():
        username = request.user.username
        profile = UserProfile.objects.get(user=request.user)

    template = "no_content_found.html"

    likely_scenarios = {
        'Wildfire': {
            'title': 'Likely Wildfire Scenario',
            'text': "Wildfire season stretches from spring to fall in Missoula County. In a low snowpack year the potential for fires increases. Is the area where you live at risk for a potential burn?"
        },
        'Flooding': {
            'title': 'Likely Flood Scenario',
            'text': "It’s springtime in Missoula County and the temperature has been steadily rising causing the snowpack to melt. It has been raining for many days and the rivers begin flooding. Will you feel the flood effects?"
        },
        'Landslide': {
            'title': 'Landslide',
            'text': "Landslides typically happen after rainstorms come through and especially in burned areas without vegetation to stabilize the slopes. Find out if you should be concerned in your area."
        },
        'Earthquake': {
            'title': 'Earthquake',
            'text': "Earthquakes can happen anytime. In Missoula County there are five faults that are considered active. It is most likely that a small earthquake of magnitude 4 to 5 would strike here. What kind of shaking might you experience?"
        },
        'Winter Weather': {
            'title': 'Likely Winter Storm Scenario',
            'text': "In the wintertime in Missoula County you can expect to see low temperatures, inches to feet of snow, and inversions causing poor air quality in the valleys. This can stretch from October to May depending on the year. Go get some good winter boots and bundle up! What might your winter look like?"
        },
        'Summer Weather': {
            'title': 'Likely Summer Storm Scenario',
            'text': " In the summertime temperatures rise in Missoula County, sometimes into the 100s! There is potential for thunderstorms, high winds, and heat waves.  Besides planning your summer adventures, what should you prepare for?"
        }
    }

    # Make sure that sections and subsections are always in the same order.
    section_order = {
        'what to expect': 0,
        'past events': 2,
        'how to prepare': 1
    }

    # Some of these are in different sections or are mutually exclusive, hence the non-unique values.
    sub_section_order = {
        'potential': 0,
        'flood zones': 1,
        'ground shaking': 1,
        'worst case scenario': 2,
        'safety issues': 3,
        'historic events': 0,
        'get earthquake ready': 0,
        'get flood ready': 0,
        'get wildfire ready': 0,
        'get landslide ready': 0,
        'stay tuned': 1,
        'a word from your emergency managers': 2,
        'get summer weather ready': 0,
        'get winter weather ready': 0
    }

    heading_tab_order = {
        'wildfire': 0,
        'flooding': 1,
        'winter weather': 2,
        'summer weather': 3,
        'earthquake': 4,
        'landslide': 5
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

                        photos = []
                        for p in PastEventsPhoto.objects.filter(heading__iexact=heading):
                            photos.append(str(p))

                        data[key] = {
                            'heading': heading,
                            'sections': OrderedDict(sorted(sections.items(), key=lambda t: sort_by_name(t, section_order))),
                            'likely_scenario_title': likely_scenarios[heading]['title'] if heading in likely_scenarios else "",
                            'likely_scenario_text': likely_scenarios[heading]['text'] if heading in likely_scenarios else "",
                            'photos': photos
                        }

        return render(request, template, {
            'location': location,
            'settings': settings,
            'supply_kit': supply_kit,
            'important_links': important_links,
            'data_bounds': data_bounds,
            'data': OrderedDict(sorted(data.items(), key=lambda t: heading_tab_order[t[1]['heading'].lower()] )),
            'quick_data_overview': quick_data_overview,
            'username': username,
            'profile': profile
        })


    # if not, we'll still serve up the same template without data
    else:
        return render(request, 'index.html', {
            'location': location,
            'settings': settings,
            'data_bounds': data_bounds,
            'quick_data_overview': quick_data_overview,
            'username': username,
            'profile': profile
        })
