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

### Tabs / Shapefile Groups

######wildfire
    Display Name: Wildfire
    Order: 0

######flood
    Display Name: Flood
    Order: 1

######winter
    Display Name: Winter Weather
    Order: 2
    Note: Please note: Because weather hazards change daily, this section contains a region-wide report. To view real-time weather and hazards for a specific location, visit the <a href="https://www.weather.gov/" target="_blank" rel="noopener">National Weather Service website. All non-weather sections have information specific to the location you searched.

######summer
    Display Name: Summer Weather
    Order: 3
    Note: Please note: Because weather hazards change daily, this section contains a region-wide report. To view real-time weather and hazards for a specific location, visit the <a href="https://www.weather.gov/" target="_blank" rel="noopener">National Weather Service website. All non-weather sections have information specific to the location you searched.

######quake
    Display Name: Earthquake
    Order: 4

### Section orders

###### Snugget Section
What you can expect: 0, not collapsible
What's the worst that could happen: 1, not collapsible
Be ready, get prepared: 2, not collapsible
Other important details for your location: 3
During a / an (disaster): 4
Past (disaster)s in the region: 5


### Site Settings

###### About Text
This site is a collaboration between HazardReady, the University of Montana, Missoula County, and the City of Missoula.

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
