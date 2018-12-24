from django.contrib import admin
from django.forms import forms
from django.urls import path
from django.shortcuts import render, redirect
from django.apps import apps
from .models import Product

import os
import csv
import codecs


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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
            image_class = apps.get_model('images.ProductImage')
            for row in reader:
                try:
                    img_obj = image_class.objects.get(name=os.path.basename(row['image']))
                except image_class.DoesNotExist:
                    img_obj = None

                Product.objects.create(
                    name=row['name'],
                    desc=row['desc'],
                    is_promo=bool(row['is_promo']),
                    in_trend=bool(row['in_trend']),
                    exclusive=bool(row['exclusive']),
                    image=img_obj,
                )
                cnt += 1

            self.message_user(request, "Your csv file has been imported (%d items)" % cnt)
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
