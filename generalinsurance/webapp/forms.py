'''
from django import forms
from datetime import datetime
from .models import GenAgentMaster,genProductMaster

class ProductsMasterForm(forms.ModelForm):
    prod_start_date = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today)
    prod_end_date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = genProductMaster
        fields =[
            'prod_code',
            'prod_description',
            'prod_start_date',
            'prod_end_date',
            'created_by',
            'last_updated_by'
        ]
        exclude = ['created_by',
            'last_updated_by']


    def clean_prod_code(self, *args, **kwargs):  # syntax for filed validate is clean_<fildName>
        data = self.cleaned_data['prod_code']
        if not data.isupper():
            raise forms.ValidationError("prod code should be in UpperCase")
        if '@' in data or '*' in data or '|' in data:
            raise forms.ValidationError("prod code should not have special characters. @,*,|")

        if len(data) < 5:
            self._errors['prod_code'] = self.error_class([
                'Minimum 5 characters required'])
        return data

    def clean(self):

        # data from the form is fetched using super function
        super(ProductsMasterForm, self).clean()
        prod_desc = self.cleaned_data.get('prod_description')
        if len(prod_desc) < 10:
            self._errors['prod_description'] = self.error_class([
                'Description Should Contain minimum 10 characters'])
            # return any errors if found
        return self.cleaned_data
'''
