from django.contrib import admin
from django.forms import TextInput, Textarea
from tinymce.models import HTMLField

# from .models import Project, Category  # , Genre
from .models import Project_Images, Projects, SiteSettings

from django.contrib import admin
# from sorl.thumbnail.admin import AdminImageMixin

# from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from adminsortable.admin import SortableAdmin, SortableTabularInline


# , SortableStackedInline, SortableGenericStackedInline, NonSortableParentAdmin)


class ProjectImagesInline(SortableTabularInline):
    model = Project_Images
    extra = 1

    # ordering = ('order',)


class ProjectsAdmin(SortableAdmin):
    # ordering = ('order',)
    inlines = [ProjectImagesInline,
               ]

    prepopulated_fields = {'slug': ('title',)}

    list_display = ('title',)
    # list_display = ['__str__', 'category']


class SiteSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
