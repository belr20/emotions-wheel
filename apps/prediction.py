#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

from app import app, stopwords

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv("data/emotion_final.csv")

targets = list(df["Emotion"])
corpus = list(df["Text"])

X = corpus
y = targets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

pipe_for_api = Pipeline([('vect', CountVectorizer(stop_words=stopwords)), ('sgd', SGDClassifier())])
pipe_for_api.fit(X_train, y_train)

layout = html.Div([
    dbc.Container([
        dbc.Row([dbc.Col(html.H1(children='Prediction API'), className='mb-2 text-center')]),
        dbc.Row([dbc.Col(
            dcc.Input(id='user_input', type='text', placeholder='Enter text', debounce=True),
            className='mb-1 text-center')
        ]),
        dbc.Row([dbc.Col(html.H2(id='output'), className='mb-4 text-center')]),
        dbc.Row([dbc.Col(html.Img(src='/assets/wheel.png', height='500px'), className='mb-5 text-center')]),
        dbc.Row([dbc.Col(html.H5(
            children='Be aware that only ML AI (with a huge proportion of happyness emotion in the dataset) has \
            been implemented for the moment ... Next step will be \
            DL (Deep Learning) implementation for better prediction.'
        ),
            className='mt-4 text-center')]),
    ])
])


@app.callback(
    Output('output', 'children'),
    Input('user_input', 'value'),)
def update_output(emotion_to_detect):
    text = [emotion_to_detect]
    if emotion_to_detect is None or emotion_to_detect == '':
        return "Emotions Wheel"
    else:
        y_pred = pipe_for_api.predict(text)
        return u'{}'.format(str.upper(y_pred[0]))
