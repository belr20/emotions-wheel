#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
import dash
import dash_bootstrap_components as dbc

# bootstrap theme https://bootswatch.com/flatly/
external_stylesheets = [dbc.themes.FLATLY]
# external_stylesheets = [dbc.themes.SLATE]
# external_stylesheets = [dbc.themes.SUPERHERO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Emotions Wheel'

server = app.server
app.config.suppress_callback_exceptions = True

# nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

