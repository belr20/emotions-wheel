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


SIMPLON_LOGO = "./assets/images/simplon-logo.png"
server = app.server

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=SIMPLON_LOGO, height='40px')),
                        dbc.Col(dbc.NavbarBrand('Home', className='ms-2')),
                    ],
                    align='center',
                    className='g-0',
                ),
                href='/home'
            ),
            dbc.NavbarToggler(id='navbar-toggler', n_clicks=0),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(dbc.NavItem(dbc.NavLink("DATA", href='/data'))),
                    navbar=True,
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(dbc.NavItem(dbc.NavLink("CLASSIFICATION", href='/classification'))),
                    navbar=True,
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(dbc.NavItem(dbc.NavLink("PREDICTION", href='/prediction'))),
                    navbar=True,
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Container(dbc.NavItem(dbc.NavLink(
                        "GitHub Source Code",
                        href="https://github.com/belr20/dev-ia-simplon/tree/main/RNCP34757E2/emotions-wheel",
                    ))),
                    navbar=True,
                ),
                width="auto",
            ),
        ]
    ),
    dark=True,
    color='primary',
    className='mb-5'
)

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='page-content')
    ]
)


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
    app.run_server(host='0.0.0.0', port=8050, debug=False)
