from django.contrib import admin

# Register your models here.
from .models import Fertility
# Register your models here.
@admin.register(Fertility)
class FertilityAdmin(admin.ModelAdmin):
    exclude = ['confidence']
    search_fields = ['age','childish_diseases','accident_or_serious_trauma','surgical_intervention','high_fevers_in_last_year','frequency_of_alcohol_consumption','smoking_habit','no_of_hours_spent_sitting_per_day','confidence']
    list_display =['age','childish_diseases','accident_or_serious_trauma','surgical_intervention','high_fevers_in_last_year','frequency_of_alcohol_consumption','smoking_habit','no_of_hours_spent_sitting_per_day','confidence']
    list_filter =['age','childish_diseases','accident_or_serious_trauma','surgical_intervention','high_fevers_in_last_year','frequency_of_alcohol_consumption','smoking_habit','no_of_hours_spent_sitting_per_day','confidence']
