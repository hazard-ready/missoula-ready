# Generated by Django 2.2.1 on 2019-05-24 21:01

import disasterinfosite.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name='ShapefileGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(default='', max_length=50)),
                ('order_of_appearance', models.IntegerField(default=0, help_text='The order, from top to bottom, in which you would like this group to appear, when applicable.')),
                ('likely_scenario_title', models.CharField(blank=True, max_length=80)),
                ('likely_scenario_text', models.TextField(blank=True)),
                ('display_name_es', models.CharField(default='', max_length=50, null=True)),
                ('display_name_en', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(default='', help_text='The name to show for this section', max_length=50)),
                ('collapsible', models.BooleanField(default=True, help_text='Whether this section of the data is collapsible')),
                ('order_of_appearance', models.IntegerField(default=0, help_text="The order in which you'd like this to appear in the tab. 0 is at the top.")),
                ('display_name_es', models.CharField(default='', help_text='The name to show for this section', max_length=50, null=True)),
                ('display_name_en', models.CharField(default='', help_text='The name to show for this section', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetPopOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.TextField(default='', max_length=255)),
                ('image', models.ImageField(upload_to='popout_images')),
                ('link', models.TextField(default='', max_length=255)),
                ('text', models.TextField(default='')),
                ('video', embed_video.fields.EmbedVideoField(null=True)),
                ('alt_text_es', models.TextField(default='', max_length=255, null=True)),
                ('text_es', models.TextField(default='', null=True)),
                ('alt_text_en', models.TextField(default='', max_length=255, null=True)),
                ('text_en', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snugget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.SnuggetSection')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup')),
                ('pop_out', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.SnuggetPopOut')),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SlideshowSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.Snugget')),
                ('text', models.TextField(default='')),
                ('text_es', models.TextField(default='', null=True)),
                ('text_en', models.TextField(default='', null=True)),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='SnuggetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model_name', models.CharField(choices=[('SNUG_TEXT', 'TextSnugget'), ('SNUG_VIDEO', 'EmbedSnugget'), ('SNUG_SLIDESHOW', 'SlideshowSnugget')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DataOverviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(storage=disasterinfosite.models.OverwriteStorage(), upload_to='data')),
                ('link_text_es', models.CharField(default='', max_length=100, null=True)),
                ('link_text_en', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmbedSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.Snugget')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('text', models.TextField(default='')),
                ('text_es', models.TextField(default='', null=True)),
                ('text_en', models.TextField(default='', null=True)),

            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(default='the affected area', help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'.", max_length=100)),
                ('community_leaders', models.TextField(default='Information about community leaders goes here.', help_text='Information about community leaders, how to contact them, and form groups.')),
                ('area_name_es', models.CharField(default='the affected area', help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'.", max_length=100, null=True)),
                ('community_leaders_es', models.TextField(default='Information about community leaders goes here.', help_text='Information about community leaders, how to contact them, and form groups.', null=True)),
                ('area_name_en', models.CharField(default='the affected area', help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'.", max_length=100, null=True)),
                ('community_leaders_en', models.TextField(default='Information about community leaders goes here.', help_text='Information about community leaders, how to contact them, and form groups.', null=True)),

            ],
            options={
                'verbose_name': 'Location Information',
            },
        ),
        migrations.CreateModel(
            name='PastEventsPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snugget', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='disasterinfosite.SlideshowSnugget')),
                ('image', models.ImageField(upload_to='photos')),
                ('caption', models.TextField(default='', max_length=200)),
                ('caption_es', models.TextField(default='', max_length=200, null=True)),
                ('caption_en', models.TextField(default='', max_length=200, null=True)),

            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField(default='Information about your organization goes here.', help_text='Describe the data and the agencies that it came from.')),
                ('contact_email', models.EmailField(blank=True, help_text='Put a contact email for the maintainer of this site here.', max_length=254)),
                ('site_url', models.URLField(default='https://www.example.com', help_text='Put the URL to this site here.')),
                ('site_title', models.CharField(default='Your Title Here!', max_length=50)),
                ('site_description', models.CharField(default='A disaster preparedness website', help_text='A small, catchy description for this site.', max_length=200)),
                ('data_download', models.URLField(blank=True, help_text='A link where people can download a zipfile of all the data that powers this site.')),
                ('intro_text', models.TextField(default='A natural disaster could strike your area at any time.', help_text='A description of what we are trying to help people prepare for, or the goal of your site.')),
                ('who_made_this', models.TextField(default='Information about the creators and maintainers of this particular site.', help_text='Include information about who you are and how to contact you.')),
                ('about_text_es', models.TextField(default='Information about your organization goes here.', help_text='Describe the data and the agencies that it came from.', null=True)),
                ('intro_text_es', models.TextField(default='A natural disaster could strike your area at any time.', help_text='A description of what we are trying to help people prepare for, or the goal of your site.', null=True)),
                ('site_description_es', models.CharField(default='A disaster preparedness website', help_text='A small, catchy description for this site.', max_length=200, null=True)),
                ('site_title_es', models.CharField(default='Your Title Here!', max_length=50, null=True)),
                ('who_made_this_es', models.TextField(default='Information about the creators and maintainers of this particular site.', help_text='Include information about who you are and how to contact you.', null=True)),
                ('about_text_en', models.TextField(default='Information about your organization goes here.', help_text='Describe the data and the agencies that it came from.', null=True)),
                ('intro_text_en', models.TextField(default='A natural disaster could strike your area at any time.', help_text='A description of what we are trying to help people prepare for, or the goal of your site.', null=True)),
                ('site_description_en', models.CharField(default='A disaster preparedness website', help_text='A small, catchy description for this site.', max_length=200, null=True)),
                ('site_title_en', models.CharField(default='Your Title Here!', max_length=50, null=True)),
                ('who_made_this_en', models.TextField(default='Information about the creators and maintainers of this particular site.', help_text='Include information about who you are and how to contact you.', null=True)),
            ],
            options={
                'verbose_name': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='TextSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.Snugget')),
                ('content', models.TextField()),
                ('content_es', models.TextField(null=True)),
                ('content_en', models.TextField(null=True)),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='PreparednessAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('image', models.ImageField(upload_to='prepare_images')),
                ('cost', models.IntegerField(default=0, validators=[django.contrib.postgres.validators.RangeMinValueValidator(0), django.contrib.postgres.validators.RangeMaxValueValidator(4)])),
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
    ]
