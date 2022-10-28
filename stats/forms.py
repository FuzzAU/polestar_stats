from django import forms


class CSVFileForm(forms.Form):
    polestar_log_file = forms.FileField(label='Polestar Log', required=True)