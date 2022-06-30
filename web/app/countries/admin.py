from django.contrib import admin
from django import forms

from .models import Country, HostCountry

class UploadForm(forms.Form):
    csv = forms.FileField()

class CountryAdmin(admin.ModelAdmin):
    template = 'admin/change_list.html'

    def changelist_view(self, request, extra_context = None):
        extra = extra_context or {}
        extra['csv']= UploadForm()

        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)

            if form.is_valid:
                file = request.FILES['csv']

                if file.name.endswith('csv'):
                    try:
                        self.insert_csv(file)
                    except Exception as e:
                        print("An error has occured:")
                        print(e)
                else:
                    print(f"Incorrect file type: {file.name.split('.')[1]}")

        return super(CountryAdmin, self).changelist_view(request, extra_context = extra)

    def insert_csv(self, file):
        pass

admin.site.register(Country, CountryAdmin)
admin.site.register(HostCountry)