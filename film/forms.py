from django import forms
from django.contrib.auth.models import User
from .models import film_profile, Review, Essay, Comment
from django.forms import ModelForm

class FilmRegisterForm(ModelForm):
    class Meta:
        model = film_profile
        fields = ['film_name', 'film_summary', 'film_image']

class ReviewForm(forms.Form):
    contents = forms.CharField(max_length=100)
    
    class Meta:
        model = Review

class DelReviewForm(forms.Form):
    deleteid = forms.CharField(max_length=100)
    
class EditReviewForm(forms.Form):
    reviewid = forms.CharField(max_length=100)
    changecontents = forms.CharField(max_length=100)

class EssayForm(forms.Form):
    contents = forms.CharField(max_length=100)
    
    class Meta:
        model = Essay

class DelEssayForm(forms.Form):
    deleteid = forms.CharField(max_length=100)
    
class EditEssayForm(forms.Form):
    reviewid = forms.CharField(max_length=100)
    changecontents = forms.CharField(max_length=100)

class CommentForm(forms.Form):
    commentparent = forms.CharField(max_length=100)
    commentmasteressay = forms.CharField(max_length=100)
    commentcontents = forms.CharField(max_length=100)
    class Meta:
        model = Comment

class DelCommetForm(forms.Form):
    commentdeleteid = forms.CharField(max_length=100)
    
class EditCommentForm(forms.Form):
    commentreviewid = forms.CharField(max_length=100)
    commentchangecontents = forms.CharField(max_length=100)