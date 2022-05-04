#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output

from app import app

# For Heroku hosting
from app import server

from apps import data, classification, prediction, home


server = app.server

navbar = dbc.Navbar(dbc.Container([
        html.A(dbc.Row([
            dbc.Col(html.Img(src='/assets/simplon-logo.png', height='40px')),
            dbc.Col(dbc.NavbarBrand('Home', className='ml-2')),
        ], align='center'), href='/home'),
        dbc.NavbarToggler(id='navbar-toggler2'),
        dbc.NavItem([dbc.NavLink('Datasets', href='/data')]),
        dbc.NavItem([dbc.NavLink('Classifiers', href='/classification')]),
        dbc.NavItem([dbc.NavLink('Prediction', href='/prediction')]),
        dbc.NavItem([dbc.NavLink(
            'GitHub Source Code',
            href='https://github.com/belr20/dev-ia-simplon/tree/main/RNCP34757E2/emotions-wheel')]),
        ]
    ),
    color='dark',
    dark=True,
    className='mb-4'
)

app.layout = html.Div([dcc.Location(id='url', refresh=False), navbar, html.Div(id='page-content')])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/data':
        return data.layout
    elif pathname == '/classification':
        return classification.layout
    elif pathname == '/prediction':
        return prediction.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)
