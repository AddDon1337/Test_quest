from django import forms


class CsvForm(forms.Form):
    name = forms.CharField()

    csv_fields = forms.FilePathField(path="C:/Users/admin/Desktop/Testdirection/test_page_root/data", match='deals. * /. csv $')
