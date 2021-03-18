from django import forms
from .models import Binss


class BinForm(forms.ModelForm):
	class Meta:
		model = Binss
		fields = [
			'title', 
			'text'
		]