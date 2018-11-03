from django import forms

class FeedbackForm(forms.Form):
    feedback_name = forms.CharField(required=True)
    feedback_text = forms.CharField(
        required = True ,
        widget = forms.Textarea
    )
