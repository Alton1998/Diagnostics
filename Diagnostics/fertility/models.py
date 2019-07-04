from django.db import models
import pandas as pd
from tensorflow import  keras
# Create your models here.
class Fertility(models.Model):
    season_choices=((1,'spring'),
                    (2,'fall'),
                    (3,'winter'),
                    (4,'summer'),
                    )
    season=models.PositiveIntegerField(choices=season_choices)
    age=models.PositiveIntegerField()
    cd_choices=((0,'no'),(1,'yes'))
    childish_diseases=models.PositiveIntegerField(choices=cd_choices)
    accident_or_serious_trauma=models.PositiveIntegerField(choices=cd_choices)
    surgical_intervention=models.PositiveIntegerField(choices=cd_choices)
    high_fevers_choices=((1,'more than 3 months ago'),(2,'less than 3 months ago'),(3,'no'))
    high_fevers_in_last_year=models.PositiveIntegerField(choices=high_fevers_choices)
    frequency_of_alcohol_consumption_choiced=((1,'once a week'),(2,'hardly ever or never'),(3,'several times a week'),(4,'several times a day'),(5,'every day'))
    frequency_of_alcohol_consumption=models.PositiveIntegerField(choices=frequency_of_alcohol_consumption_choiced)
    smoking_habit_choices=((1,'occasional'),(2,'daily'),(3,'never'))
    smoking_habit=models.PositiveIntegerField(choices=smoking_habit_choices)
    no_of_hours_spent_sitting_per_day=models.PositiveIntegerField()
    confidence=models.FloatField()

    def save(self, *args, **kwargs):
        df = pd.DataFrame(
            columns=['Season','Age','Childish diseases','Accident or serious trauma','Surgical intervention','High fevers in the last year','Frequency of alcohol consumption','Smoking habit','Number of hours spent sitting per day',], data=[
                [self.season,self.age,self.childish_diseases,self.accident_or_serious_trauma,self.surgical_intervention,self.high_fevers_in_last_year,self.frequency_of_alcohol_consumption,self.smoking_habit,self.no_of_hours_spent_sitting_per_day]])
        NEW_MODEL = keras.models.load_model('my_model_fertility.h5')
        self.confidence=NEW_MODEL.predict(x=df)[0][0]*100
        super().save(*args, **kwargs)