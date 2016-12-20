from django import forms

class ExpressionOfInterestForm(forms.Form):
	email = forms.EmailField()
	name = forms.CharField()
	what_interests_you = forms.CharField(widget=forms.Textarea(), required=False)
	sign_up_to_newsletter = forms.BooleanField(required=False)


class ImNotInterestedForm(forms.Form):
	email_address = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	reason_for_no_interest = forms.CharField(widget=forms.Textarea())
	telephone_number = forms.CharField()
	postal_address = forms.CharField(widget=forms.Textarea())
	signup_for_spam_emails = forms.BooleanField(required=True)