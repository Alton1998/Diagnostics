from django.db import models
import pandas as pd
from tensorflow import  keras




# Create your models here.
class Diabetes(models.Model):
    pregnancies = models.PositiveIntegerField()
    glucose = models.PositiveIntegerField()
    blood_pressure = models.PositiveIntegerField()
    skin_thickness = models.PositiveIntegerField()
    insulin = models.PositiveIntegerField()
    b_m_i = models.PositiveIntegerField()
    diabetes_pedigree_function = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    outcome=models.FloatField()

    def save(self, *args, **kwargs):
        df = pd.DataFrame(
            columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'], data=[
                [self.pregnancies,self.glucose,self.blood_pressure,self.skin_thickness,self.insulin,self.b_m_i,self.diabetes_pedigree_function,self.age]])
        NEW_MODEL = keras.models.load_model('my_model_diabetes.h5')
        self.outcome=NEW_MODEL.predict(x=df)[0][0]*100
        super().save(*args, **kwargs)  # Call the "real" save() method.