# Missoula Ready

The project is a custom instance of the [Disaster Preparedness](https://github.com/missoula-ready/disaster-preparedness) project, which is an adaptation of [a pioneering project from Oregon](https://github.com/Oregon-Public-Broadcasting/earthquake-preparedness) but has been generalized to make it easy to clone and tailor to other regions.

# To set it up, follow the instructions in the [Disaster Preparedness project README](https://github.com/missoula-ready/disaster-preparedness/blob/master/README.md).

The data for this app is in `disasterinfosite/data`. This data includes shapefiles and related data for Missoula County, Montana, USA, to get you started. When you use `python import.py` to process these shapefiles and update some Django code to fit, the script will prompt you for which field to use to look up snuggets. Use the field name `lookup_val` for every shapefile.

Note that the `python manage.py makemigrations` step will probably tell you there's nothing to add.  Don't worry - this is not an error!

# Values to put in Django Admin

### Important links

###### Evacuation Information
`In the case of an emergency you may need to evacuate, learn more <a href="http://www.missoulacounty.us/government/public-safety/office-of-emergency-management/evacuation-information" target="_blank">here</a>.`

###### Neighborhood Council
`Find out more about getting your neighborhood ready <a href="http://www.ci.missoula.mt.us/1591/My-Neighborhood-Council" target="_blank">here</a>.`

###### Real-time Alerts
`Sign up for <a href="http://www.smart911.com">Smart911</a> to help your family during emergencies. <img class="smart911-logo" src="//www.ravemobilesafety.com/downloads/smart911logos/smart911_logo_lightbgs.png" />`

### Supply kit

###### days
  3
###### text
`For more information check out the <a href="ftp://www.co.missoula.mt.us/911advisory/Emergency_Supply_List.pdf">Missoula County Emergency Kit Checklist</a> and the <a href="ftp://www.co.missoula.mt.us/911advisory/Winter_Ready_Checklist.pdf">Winter Ready Kit Checklist</a>.`

### Location Information

###### Area Name
Missoula County

###### Community Leaders
In the event of an emergency the Office of Emergency Management for Missoula County will be your place to go for information. Call 406-258-INFO (4636). This line is either recorded with a disaster specific message or is manned by live people depending on the situation.

### Settings
###### Site title
Missoula ready

###### URL
http://hazardready.org/

###### Site description
A disaster preparedness website

###### Intro Text
A natural disaster could strike your area at any time. Find out about where you live, work, or play in Missoula County, MT.

###### Who Made This
`This is based on <a href="http://www.opb.org/news/widget/aftershock-find-your-cascadia-earthquake-story/">Aftershock</a>, an earthquake preparedness application for Oregon residents. Carson MacPherson-Krutsky and <a href="http://www.hs.umt.edu/geosciences/faculty/bendick/">Dr. Rebecca Bendick</a>, a graduate student and her advisor at the Unversity of Montana, had the idea to expand it for other locales and types of disasters. <a href="https://github.com/nein09">Melinda Minch</a> and <a href="https://github.com/eldang">Eldan Goldenberg</a> adapted it for that purpose.`

###### Data Download
https://github.com/missoula-ready/missoula-ready/blob/master/disasterinfosite/data.zip

###### Past Events Photos
Upload photos to show in a photo gallery in the search results, under Past Events. Make sure that the heading you enter here matches the heading that the photos will appear under.

###### Data Overview Images
In the box at the bottom of every page, there's a section called 'Quick Data Overview'. That's where these will show up, as links that open in a new tab or window. The link_text field is what the link says, like 'Earthquakes: Distance from a Fault', and you can upload the appropriate image here.

### Deploying to the web via Apache
There are directories called 'photos' and 'data' in disasterinfosite/img. This is where images go when you upload them via Django Admin, under 'Photos of Past Events' and 'Data Overview Images'. In order for that upload to work, you need to change the owner (chown) those directories to whatever user Apache is running as (www-data, perhaps).

#### Linode-specific instructions

If you have a default Linode configuration running Ubuntu 15.04, you can follow these very specific instructions. For any other system, skip this subsection.

1. `aptitude install libapache2-mod-wsgi-py3`
2. Edit `/etc/apache2/apache2.conf` adding the following (replace all-caps entries as appropriate):
`RedirectMatch ^/WEBSITE_SUBDIRECTORY$ /WEBSITE_SUBDIRECTORY/`
`WSGIScriptAlias /SUBDIRECTORY /home/USERNAME/INSTALLDIRECTORY/disasterinfosite/wsgi.py`
`WSGIPythonPath /home/USERNAME/INSTALLDIRECTORY:/home/USERNAME/INSTALLDIRECTORY/venv/lib/python3.4/site-packages`
`<Directory /home/USERNAME/INSTALLDIRECTORY/disasterinfosite>`
`<Files wsgi.py>`
`Require all granted`
`</Files>`
`</Directory>`
3. Edit the default apache website (usually `/etc/apache2/sites-available/000-default` to add: `Alias /WEBSITE_SUBDIRECTORY/static/ /home/USERNAME/INSTALLDIRECTORY/disasterinfosite/static/`
`<Directory /home/USERNAME/INSTALLDIRECTORY/disasterinfosite/static>`
`Require all granted`
`</Directory>`
`WSGIScriptAlias /zr /home/USERNAME/INSTALLDIRECTORY/disasterinfosite/wsgi.py`
`<Directory /home/USERNAME/INSTALLDIRECTORY/disasterinfosite>`
`<Files wsgi.py>`
`Require all granted`
`</Files>`
`</Directory>`
4. Edit `disasterinfosite/settings.py` to remove the first forward slash from the value of `STATIC_URL`, leaving the relevant line as: `STATIC_URL = 'static/'`

#### General instructions

1. Install a version of `mod_wsgi` that is compiled for Python 3. On Debian/Ubuntu you can do this with `aptitude install libapache2-mod-wsgi-py3`. On other systems it may be easier to use `pip` as per [these instructions](https://pypi.python.org/pypi/mod_wsgi).
2. Use [these instructions](https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/modwsgi/) to configure Apache. Note in particular:
    1. You'll need `WSGIScriptAlias` to point to `disasterinfosite/wsgi.py`
    2. You'll need to apply the "Using a virtualenv" addition.
    3. You'll need to set up a `/static/` alias pointing to `disasterinfosite/static`
    4. Depending on your server configuration, you *may* also need to set up a redirect rule to add trailing slashes to URLs, to get the static files (CSS, images etc) included.
    5. You may also need to alter the `STATIC_URL` constant in `settings.py` based on your server setup.
3. Set up the environment values from above (`DJANGO_SECRET_KEY` and `DATABASE_URL`) for all users by putting their declarations in `/etc/environment/` and rebooting the machine.

### Use foreman to run the server Heroku-style
*Not tested by the current maintainers*

* `foreman start`
  * Any errors that pop up are probably from missing modules or missing environmental variables. Read the errors!

## Adding new data

### What you need

1. At least one shapefile, meeting the following requirements:
    1. Each shapefile's attribute table must contain a column with a unique identifier for each set of text to display (e.g. all the areas for which you want to display "Expected ground shaking: severe" have one ID, and all the areas for which you want to display "Expected ground shaking: moderate" have another). This column will be used to look up text when a user selects a location.
    2. That column's name must comply with the [Django field name restrictions](https://docs.djangoproject.com/en/1.9/topics/db/models/#field-name-restrictions), including not being one of the [Python 3 reserved words](https://stackoverflow.com/questions/22864221/is-the-list-of-python-reserved-words-and-builtins-available-in-a-library/22864250#22864250). For example, if the column is called `id`, `object`, `map`, `property` or `type`, you'll have to rename it.
    3. It doesn't matter which coordinate reference system the shapefile has been saved with, but if you're making them yourself then we recommend using EPSG:4326, because the import pipeline will reproject it to that anyway.
    4. If you have multiple shapefiles, clip them all to cover the same area. Otherwise, if users click on a location that is covered by some shapefiles but not others they will see partial data without a clear explanation that there is missing data.
    5. Multiple shapes may overlap, but each shape may only have one value for the lookup field. If you have multiple shapes with the same lookup value, the import process will combine them.
2. Some text content to display when a user chooses a location in one or more of your shapefiles. In this project, the text content is referred to as **snuggets**, from "story nuggets".

If you have raster data, first convert it to a shapefile.  See [Converting raster files](#converting-raster-files) below for pointers if you don't already know how to do that.

To have the boundary of the area covered by your data display on the map, save it as a geoJSON LineString (not a polygon), in `/static/img/boundary.geojson`

**TODO**: Some automated processing of the boundary. The import pipeline ought to be able to compose it from the sum of all the included shapefiles.

### Fully automated pipeline

If the structure of your text content is simple enough, you can import shapefiles and snuggets automatically without having to do much manual work. We recommend using this pathway if possible, because it makes moving the site to a new server significantly easier. To do this, you will need a `snuggets.csv` file with the same columns as the example one we've included in `data.zip`.  The columns can be in any order, but the headings must be exactly as typed here:

* `section` : A section name that will be displayed on the page (must not be empty)
* `subsection` : A subsection name (must not be empty)
* `shapefile` : The file name for the shapefile this row corresponds to, without the extenstion. For example: `EQ_GroundShaking_MostLike` for text that relates to the content of `EQ_GroundShaking_MostLike.shp`. (must not be empty; must correspond exactly to the available shapefiles)
* `heading` : A human-readable heading that describes the content of this shapefile, to be displayed on the page.
* `lookup_value` : The value of the unique identifier in the shapefile (e.g. an intensity value or a hazard classification). This field can be empty; if it is then the rest of this row will be applied to every available value.
* `intensity` : Relative severity scaled from 0-100, to display graphically on the page. If this is empty, or if a value is provided for `image`, it will simply not be displayed.
* `image` : The file name for an image, stored in `disasterinfosite/static/img`, that illustrates the severity. If this is empty it won't be displayed. If there is a value here (including '0' or NULL), it overrides the value of `intensity`.
* `text` : The explanatory text to be displayed in the relevant section and subsection when the user chooses a location that matches this row's criteria. It's okay to use HTML in these- be sure that you close all your tags, though!

You can have any number of sections and subsections, but every row must be a unique combination of `shapefile`, `section`, `subsection` and `lookup_value`. If you define more than one row for the same permutation, only the last one in the file will actually be used. Note that this allows you to create a default value for a given section, subsection and shapefile, by having a row with `lookup_value` blank (so it applies to all values present in the shapefile), followed by rows with specified `lookup_value`s which will overwrite the default for that value only.

Blank rows or additional columns won't cause problems. Any row that is missing any of the required fields will be skipped and a warning will be printed.

Once `snuggets.csv` is ready, simply put it and the relevant shapefiles in `disasterinfosite/data` (and remove any other files or subdirectories from there), and follow the instructions in [Load Some Data](#load-some-data) above.

#### Updating existing data

If you make changes to `snuggets.csv` you should only need to re-run `python snugget_load.py` and restart your web server.

If you make changes to the shapefiles, or change which field from the shapefiles you want to use as the ID, then before running `python import.py` you will also need to remove the `disasterinfosite/data/reprojected` and `word/data/simplified` directories that the importer had created. It uses these to avoid having to repeat the time-consuming reprojection and simplification of the shapefiles every time it is run, but that means changes to the shapefiles themselves won't be picked up unless they are removed.

If you have existing data that needs to be removed—perhaps because you are replacing our sample data, or retiring a shapefile you previously used—you may have to clear the database first.  To do this:

1. `psql -d [DBNAME] -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public; CREATE EXTENSION postgis;"`
2. `python manage.py migrate` - if this step throws errors, delete all the .py files in `disasterinfosite/migrations` **except** `__init__.py` and `0001_initial.py`, and try again.

Then continue with the instructions in [Load Some Data](#load-some-data) above.

### Working with more complex text templates

You may want to use multiple fields from a shapefile to fill in blanks from a template, such as "In year [YEAR] the [FIRENAME] fire burned [AREA] acres here". The automated import pipeline is not sophisticated enough to do this for you, so you have two options:

#### If you can edit the shapefile

Using QGIS or ArcGIS, add two columns to the shapefile: one with a lookup value composed of all the variables you're using (e.g. `[FIRENAME]_[YEAR]_[AREA]`), and one with the complete text. You can create both of these using calculdated fields in either program. Then copy-paste the attribute table into Excel or an equivalent, and use the complete texts to populate the `text` column of `snuggets.csv` and the lookup values for the `lookup_value` column. With this, you can use the automated pipeline to do the rest.

#### If you can't edit the shapefile, or are more comfortable editing code

Take a look at `disasterinfosite/models.py`, `disasterinfosite/load.py` and `disasterinfosite/admin.py` after running the automated pipeline on some sample data, and write appropriate equivalents for all of the generated code (marked by prominent comments) that fit your data and text model. You may also need to edit `disasterinfosite/templates/found_content.html` which is the page template to be displayed when there is at least one snugget available for a location. Then run just the `manage.py` parts of the [Load Some Data](#load-some-data), and use the Django admin panel to enter snuggets by hand.

If you have some data that fits that automated import model and some that does not, you can combine the two. Just watch for three things:

1. You'll have to reproject the shapefiles that aren't going through the import pipeline to EPSG:4326 yourself.
2. Put the shapefiles that aren't being manually imported somewhere other than `disasterinfosite/data` to keep them out of the automated pipeline.
3. Be very careful to avoid putting any of your manually edited code between the `# GENERATED CODE GOES HERE` and `# END OF GENERATED CODE BLOCK` comment pairs in the Python files, because that part gets overwritten by `import.py` each time.

### Converting raster files

The import pipeline doesn't currently have a way to handle raster data. Instead you'll have to convert the file to vector data first, and save the shapefile this creates in `disasterinfosite/data`. Here are three ways to do that:

#### Using GDAL from the command line

GDAL includes a [polygonize](http://www.gdal.org/gdal_polygonize.html) tool. If you have this available, then simply run:

```shell
gdal_polygonize.py RASTERFILENAME.tif -f 'ESRI Shapefile' OUTPUTFILENAME.shp
```

This is the preferred method if you already have GDAL installed, but if you don't then be aware that installing GDAL can be complicated.

The output file will have an attribute `DN` that contains the pixel values from the raster file.

#### Using QGIS

* Open the raster file in QGIS
* Choose `Raster > Conversion > Polygonize` from the menus
* Use the Select button by "Output file" to give this a destination in `disasterinfosite/data`, and leave the other options as they are
* Click "OK" and be warned that it may take a while
* When it's finished, check the shapefile it's created.  It likes to create lines instead of polygons - if it did that, then use `Vector > Geometry Tools > Lines to Polygons` to make an actual polygons file, and take the lines file out of `disasterinfosite/data`.

The output file will have an attribute `DN` that contains the pixel values from the raster file.

#### Using ArcGIS

Try [these instructions](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/Raster_to_Polygon/001200000008000000/).


