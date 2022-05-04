#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([dbc.Col(html.H1('Emotions Wheel', className='text-center'), className='mb-5 mt-5')]),
        dbc.Row([dbc.Col(html.H5(
            children='This site, through NLP (Natural Language Processing), aims to detect emotions in text. \
            Some usefull resources are available in GitHub link at the top of this page.'),
            className='mt-4'
        )]),
        dbc.Row([dbc.Col(html.H5(children='To do so, 3 dashboards are available :'), className='mt-4')]),
        dbc.Row([dbc.Button('Datasets', href='/data', color='primary', className='mt-3')]),
        dbc.Row([dbc.Col(html.H5(
            children='Datasets analysis from Kaggle & Data World, our base for NLP.'),
            className='mt-4'
        )]),
        dbc.Row([dbc.Button('Classifiers', href='/classification', color='primary', className='mt-3')]),
        dbc.Row([dbc.Col(html.H5(
            children='Studies of different ML (Machine Learning) models to pick up the BEST one.'),
            className='mt-4'
        )]),
        dbc.Row([dbc.Button('Prediction', href='prediction', color='primary', className='mt-3')]),
        dbc.Row([dbc.Col(html.H5(
            children='An API in which text can be entered for emotion detection.'),
            className='mt-4'
        )]),
        html.Br(),
        dbc.Row([dbc.Col(html.Img(src='/assets/wheel.png', height='500px'), className='mb-5 text-center')]),
    ], className='mb-5')
])
