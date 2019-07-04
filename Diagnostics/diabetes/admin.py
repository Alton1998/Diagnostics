from django.contrib import admin
from .models import Diabetes
# Register your models here.
@admin.register(Diabetes)
class DiabetesAdmin(admin.ModelAdmin):
    exclude = ['outcome']
    search_fields = ['pregnancies','glucose','blood_pressure','skin_thickness','insulin','b_m_i','diabetes_pedigree_function','age','outcome']
    list_display =['pregnancies','glucose','blood_pressure','skin_thickness','insulin','b_m_i','diabetes_pedigree_function','age','outcome']
    list_filter = ['pregnancies','glucose','blood_pressure','skin_thickness','insulin','b_m_i','diabetes_pedigree_function','age','outcome']