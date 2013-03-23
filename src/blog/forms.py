from django import forms


class Blog(forms.Form):
    title = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size':'40'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'resizable'}))