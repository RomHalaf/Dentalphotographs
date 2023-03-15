from django import forms
import datetime

class patientForm(forms.Form):
    branch=forms.CharField(initial="ראשון לציון")
    date=forms.DateField(initial=datetime.datetime.today)
    first_name=forms.CharField(initial="רום")
    last_name=forms.CharField(initial="חלף")
    id_number=forms.IntegerField(initial=212212740)
    doctor=forms.CharField(initial="דזן")
    photo_type=forms.CharField(initial="פנורמי")
    deal_number=forms.IntegerField(initial=0)
    price_type=forms.CharField(initial="אשראי")
    credit=forms.IntegerField(initial=150)
    cash=forms.IntegerField(initial=0)
    reimbursement_from_insurance=forms.IntegerField(initial=0)
    reference_number=forms.CharField(initial="0")
    invoicing_number=forms.IntegerField(initial=15246)
    way=forms.CharField(initial="רופא")
    photographer_name=forms.CharField(initial="מני")


    



    