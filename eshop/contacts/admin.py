from django.contrib import admin
from django.forms import forms
from django.urls import path
from django.shortcuts import render, redirect
from .models import Contact

import csv
import codecs


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    change_list_template = "admin/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv, name='import-csv'),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.DictReader(codecs.iterdecode(csv_file, 'utf-8'))
            cnt = 0
            for row in reader:
                Contact.objects.create(
                    address=row['address'],
                    email=row['email'],
                    state=row['state'],
                    phone=row['phone']
                )
                cnt += 1

            self.message_user(request, "Your csv file has been imported (%d items)" % cnt)
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
