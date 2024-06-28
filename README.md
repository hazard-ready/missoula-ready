# Missoula Ready

The project is a custom instance of the [Disaster Preparedness](https://github.com/missoula-ready/disaster-preparedness) project, which is an adaptation of [a pioneering project from Oregon](https://github.com/Oregon-Public-Broadcasting/earthquake-preparedness) but has been generalized to make it easy to clone and tailor to other regions.

# To set it up, follow the instructions in the [Disaster Preparedness project README](https://github.com/missoula-ready/disaster-preparedness/blob/master/README.md).

Information that is unique to this instance of Hazard Ready is below.

# Values for importing

### All county shapefiles have the following groups: `wildfire, winter, summer, quake, flood`
### fire_wui_wmt: `wildfire`
### Burned_perimeter: `wildfire`
### WHP_FINAL: `wildfire`
### MergedEQs: `quake`
### FloodMaps_MT: `flood`
### CMZ_mt: `flood`

Note that there is no *prepare* page in this instance of Hazard Ready.

# Values to put in Django Admin

### Tabs

######wildfire
    Display Name: Wildfire
    Order: 0
    Likely Scenario Title: Likely Wildfire Scenario
    Likely Scenario Text: Wildfire season stretches from spring to fall in Missoula County. In a low snowpack year the potential for fires increases. Is the area where you live at risk for a potential burn?

######flood
    Display Name: Flood
    Order: 1
    Likely Scenario Title: Likely Flood Scenario
    Likely Scenario Text: It’s springtime in Missoula County and the temperature has been steadily rising causing the snowpack to melt. It has been raining for many days and the rivers begin flooding. Will you feel the flood effects?

######winter
    Display Name: Winter Weather
    Order: 2
    Likely Scenario Title: Likely Winter Storm Scenario
    Likely Scenario Text: In the wintertime in Missoula County you can expect to see low temperatures, inches to feet of snow, and inversions causing poor air quality in the valleys. This can stretch from October to May depending on the year. Go get some good winter boots and bundle up! What might your winter look like?

######summer
    Display Name: Summer Weather
    Order: 3
    Likely Scenario Title: Likely Summer Storm Scenario
    Likely Scenario Text: In the summertime temperatures rise in Missoula County, sometimes into the 100s! There is potential for thunderstorms, high winds, and heat waves.  Besides planning your summer adventures, what should you prepare for?

######quake
    Display Name: Earthquake
    Order: 4
    Likely Scenario Title: Earthquake
    Likely Scenario Text: Earthquakes can happen anytime. In Missoula County there are five faults that are considered active. It is most likely that a small earthquake of magnitude 4 to 5 would strike here. What kind of shaking might you experience?

### Section orders

###### Snugget Section
What to expect: 0
How to prepare: 1
Past events: 2

###### Snugget Subsection
potential: 0
flood zones: 1
ground shaking: 1
worst case scenario: 2
safety issues: 3
historic events: 0
get earthquake ready: 0
get flood ready: 0
get wildfire ready: 0
get landslide ready: 0
stay tuned: 1
a word from your emergency managers: 2
get summer weather ready: 0
get winter weather ready: 0


### Settings

###### About Text
This site is a collaboration of HazardReady, the University of Montana, Missoula County, and the City of Missoula.

###### Area Name
Montana

###### Site title
Montana Ready

###### URL
https://hazardready.org/

###### Site description
A disaster preparedness website

###### Intro Text
A natural disaster could strike your area at any time. Find out about where you live, work, or play in Montana.

###### Who Made This
Have questions? View the <a href="/about" target="_blank">About</a> page or <a href="mailto:software@hazardready.org">email the Hazard Ready creators</a> for more information.


###### Data Download
https://github.com/missoula-ready/missoula-ready/blob/master/disasterinfosite/data.zip


### Deploying to the web via Docker
This repository has a Dockerfile that lets you build a Docker image of the Django app. It needs you to have `DATABASE_URL` and `DJANGO_SECRET_KEY` set in your environment, but it is also able to guess sensible defaults for these values.

Do `docker build . --tag missoula-ready` and you can run it. It will set up the Python environment for you. Depending on the state of the database you're connecting to, you will likely need to start at the `python manage.py migrate` step under "Load some data".

For an example of a working production environment, see the `docker-compose.yml` in the [base repository](https://github.com/hazard-ready/disaster-preparedness)
