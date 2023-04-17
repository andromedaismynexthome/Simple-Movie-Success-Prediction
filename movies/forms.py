from django import forms
from django.forms import ModelForm
from .models import Movies

#Create a Movies form
class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = {'name','year','imdb_meta','genres','runtime','director','stars','yt_trailer_views','ph_credit','yt_trailer_like'}
        labels = {
            'name':'',
            'year':'',
            #'link':'',
            'director':'select anyone',
            #'outline':'',
            'imdb_meta':'Imdb metascore',
            'genres':'select multi',
            'stars':'',
            'runtime':'enter movie runtime',
            #'yt_trailer_title':'',
            #'yt_trailer_url':'',
            'yt_trailer_views':'',
            'yt_trailer_like':'',
            #'yt_trailer_dislike':'',
            #'yt_trailer_uploader':'',
            'ph_credit':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'add movie name'}),
            'year':forms.TextInput(attrs={'class':'form-control','placeholder':'add movie release year'}),
            #'link':forms.TextInput(attrs={'class':'form-control','placeholder':'add movie imdb link'}),
            'director':forms.Select(attrs={'class':'form-select','placeholder':'add movie director'}),
            #'outline':forms.TextInput(attrs={'class':'form-control','placeholder':'add discription'}),
            'imdb_meta':forms.TextInput(attrs={'class':'form-control','placeholder':'add imdb meta score'}),
            'genres':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'select genre'}),
            'stars':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'add movie star name'}),
            'runtime':forms.TextInput(attrs={'class':'form-control','placeholder':'write movie runtime'}),
            #'yt_trailer_title':forms.TextInput(attrs={'class':'form-control','placeholder':'add youtube movie title'}),
            #'yt_trailer_url':forms.TextInput(attrs={'class':'form-control','placeholder':'add youtube movie embed url'}),
            'yt_trailer_views':forms.TextInput(attrs={'class':'form-control','placeholder':'add youtube movie views'}),
            'yt_trailer_like':forms.TextInput(attrs={'class':'form-control','placeholder':'add youtube movie like'}),
            #'yt_trailer_dislike':forms.TextInput(attrs={'class':'form-control','placeholder':'add youtube movie dislike'}),
            #'yt_trailer_uploader':forms.TextInput(attrs={'class':'form-control','placeholder':'add youtube movie uploader name'}),
            'ph_credit':forms.TextInput(attrs={'class':'form-control','placeholder':'add production house credits'}),

        }
