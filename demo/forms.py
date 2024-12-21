from django import forms

class PMSBaseForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = '' # Get rid of : after the labels

class DoctorForm(PMSBaseForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=[('M','Male'), ('F','Female')])
    speciality = forms.CharField(max_length=20)
    contact_no = forms.CharField(max_length=15)
    board_reg_no = forms.CharField(max_length=100)
    system_reg_no = forms.CharField(max_length=20, disabled=True, required=False)
    average_time_per_patient = forms.IntegerField(initial=20)
    active = forms.ChoiceField(widget=forms.RadioSelect, choices=[('Y','Yes'), ('N','No')],initial='Y')
    # profile_pic = forms.ImageField(required=False)
    board_reg_cert = forms.FileField(required=False)

