from modeltranslation.translator import (register,
                                         translator,
                                         TranslationOptions)
from .models import (SiteSettings,
                     ShapefileGroup,
                     PastEventsPhoto,
                     DataOverviewImage,
                     TextSnugget,
                     EmbedSnugget,
                     SlideshowSnugget,
                     SnuggetPopOut,
                     SnuggetSection,
                     PreparednessAction,
                     PreparednessLink)

# To translate these models, uncomment the following lines and make / run migrations.

# @register(SiteSettings)
# class SiteSettingsTranslationOptions(TranslationOptions):
#     fields = ('about_text',
#               'site_title', 'site_description',
#               'intro_text', 'who_made_this', 'area_name')


# @register(ShapefileGroup)
# class ShapefileGroupTranslationOptions(TranslationOptions):
#     fields = ('display_name', 'note')


# @register(PastEventsPhoto)
# class PastEventsPhotoTranslationOptions(TranslationOptions):
#     fields = ('caption',)


# @register(DataOverviewImage)
# class DataOverviewImageTranslationOptions(TranslationOptions):
#     fields = ('link_text',)


# @register(TextSnugget)
# class TextSnuggetTranslationOptions(TranslationOptions):
#     fields = ('content',)


# @register(EmbedSnugget)
# class EmbedSnuggetTranslationOptions(TranslationOptions):
#     fields = ('text',)


# @register(SlideshowSnugget)
# class SlideshowSnuggetTranslationOptions(TranslationOptions):
#     fields = ('text',)


# @register(SnuggetPopOut)
# class SnuggetPopOutTranslationOptions(TranslationOptions):
#     fields = ('text', 'alt_text')


# @register(SnuggetSection)
# class SnuggetSectionTranslationOptions(TranslationOptions):
#     fields = ('display_name',)


# @register(PreparednessAction)
# class PreparednessActionTranslationOptions(TranslationOptions):
#     fields = ('title', 'content_text',
#               'happy_text', 'useful_text', 'property_text')


# @register(PreparednessLink)
# class PreparednessActionTranslationOptions(TranslationOptions):
#     fields = ('text',)