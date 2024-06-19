# Generated by Django 4.0.7 on 2022-08-31 00:35

import disasterinfosite.models
from django.conf import settings
import django.contrib.postgres.validators
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        CreateExtension(name='postgis'),
        CreateExtension(name='postgis_raster'),
        migrations.CreateModel(
            name='DataOverviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(
                    storage=disasterinfosite.models.OverwriteStorage(), upload_to='data')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Location Information',
            },
        ),
        migrations.CreateModel(
            name='PreparednessAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('image', models.ImageField(upload_to='prepare_images')),
                ('cost', models.IntegerField(default=0, validators=[django.contrib.postgres.validators.RangeMinValueValidator(
                    0), django.contrib.postgres.validators.RangeMaxValueValidator(4)])),
                ('happy_text', models.TextField(default='')),
                ('useful_text', models.TextField(default='')),
                ('property_text', models.TextField(default='')),
                ('content_text', models.TextField(default='')),
                ('link_text', models.TextField(default='')),
                ('link_icon', models.ImageField(upload_to='prepare_images')),
                ('link', models.URLField(default='')),
                ('slug', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ShapefileGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(default='', max_length=50)),
                ('order_of_appearance', models.IntegerField(
                    default=0, help_text='The order, from top to bottom, in which you would like this group to appear, when applicable.')),
                ('note', models.TextField(
                    blank=True, help_text='A note that appears above all snuggets in this section. Use for data caveats or warnings.')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(default='the affected area',
                                               help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'.", max_length=100)),
                ('about_text', models.TextField(default='Information about your organization goes here.',
                                                help_text='Describe the data and the agencies that it came from.')),
                ('contact_email', models.EmailField(
                    blank=True, help_text='Put a contact email for the maintainer of this site here.', max_length=254)),
                ('site_url', models.URLField(default='https://www.example.com',
                                             help_text='Put the URL to this site here.')),
                ('site_title', models.CharField(
                    default='Your Title Here!', max_length=50)),
                ('site_description', models.CharField(default='A disaster preparedness website',
                                                      help_text='A small, catchy description for this site.', max_length=200)),
                ('intro_text', models.TextField(default='A natural disaster could strike your area at any time.',
                                                help_text='A description of what we are trying to help people prepare for, or the goal of your site.')),
                ('who_made_this', models.TextField(default='Information about the creators and maintainers of this particular site.',
                                                   help_text='Include information about who you are and how to contact you.')),
                ('data_download', models.URLField(
                    blank=True, help_text='A link where people can download a zipfile of all the data that powers this site.')),
            ],
            options={
                'verbose_name': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='Snugget',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(null=True)),
                ('order', models.IntegerField(default=0)),
                ('group', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetPopOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('image', models.ImageField(upload_to='popout_images')),
                ('link', models.TextField(default='', max_length=255)),
                ('alt_text', models.TextField(default='', max_length=255)),
                ('video', embed_video.fields.EmbedVideoField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(default='',
                                                  help_text='The name to show for this section', max_length=50)),
                ('collapsible', models.BooleanField(default=True,
                                                    help_text='Whether this section of the data is collapsible')),
                ('order_of_appearance', models.IntegerField(
                    default=0, help_text="The order in which you'd like this to appear in the tab. 0 is at the top.")),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model_name', models.CharField(choices=[('SNUG_TEXT', 'TextSnugget'), (
                    'SNUG_VIDEO', 'EmbedSnugget'), ('SNUG_SLIDESHOW', 'SlideshowSnugget')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmbedSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                     parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.snugget')),
                ('text', models.TextField(default='')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='SlideshowSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                     parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.snugget')),
                ('text', models.TextField(default='')),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='TextSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                     parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.snugget')),
                ('content', models.TextField()),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(blank=True, max_length=50)),
                ('actions_taken', models.ManyToManyField(
                    blank=True, to='disasterinfosite.preparednessaction')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
        migrations.AddField(
            model_name='snugget',
            name='pop_out',
            field=models.OneToOneField(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.snuggetpopout'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='+', to='disasterinfosite.snuggetsection'),
        ),
        migrations.CreateModel(
            name='PastEventsPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('caption', models.TextField(default='', max_length=200)),
                ('snugget', models.ForeignKey(
                    default=None, on_delete=django.db.models.deletion.CASCADE, to='disasterinfosite.slideshowsnugget')),
            ],
        ),
    ]
