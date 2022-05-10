#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from functions import subsample, words_distribution


df_kaggle = pd.read_csv('data/emotion_final.csv')
df_world = pd.read_csv('data/text_emotion.csv')

# Figure 1 Kaggle emotions distribution
trace = go.Histogram(x=df_kaggle['Emotion'], xbins=dict(), marker=dict(color='#119DFF'))
layout = go.Layout(title='Kaggle')
fig1 = go.Figure(data=trace, layout=layout)

# Figure 2 Data World emotions distribution
trace = go.Histogram(x=df_world['sentiment'], xbins=dict(), marker=dict(color='#C40030'))
layout = go.Layout(title='data.World')
fig2 = go.Figure(data=trace, layout=layout)
fig2.update_layout(xaxis={'tickangle': -45})

# Figure 3 Kaggle words distribution
x_kaggle = np.array(df_kaggle['Text'])
y_kaggle = np.array(df_kaggle['Emotion'])

ranks_kaggle, freqs_kaggle, words_kaggle = words_distribution(x_kaggle)

fig3 = px.bar(x=ranks_kaggle, y=freqs_kaggle)
fig3.update_traces(marker_color='#119DFF', marker_line_color='black', marker_line_width=1.5)
fig3.update_layout(
    title='Kaggle',
    yaxis={'title_text': ''},
    xaxis={'tickmode': 'array', 'title_text': '', 'tickangle': -45,
           'tickvals': ranks_kaggle, 'ticktext': subsample(words_kaggle),
           },
)

# Figure 4 Data World words distribution
x_world = np.array(df_world['content'])
y_world = np.array(df_world['sentiment'])

ranks_world, freqs_world, words_world = words_distribution(x_world)

fig4 = px.bar(x=ranks_world, y=freqs_world)
fig4.update_traces(marker_color='#C40030', marker_line_color='black', marker_line_width=1.5)
fig4.update_layout(
    title='data.World',
    yaxis={'title_text': ''},
    xaxis={'tickmode': 'array', 'title_text': '', 'tickangle': -45,
           'tickvals': ranks_world, 'ticktext': subsample(words_world),
           },
)

# Figure 5 Kaggle emotions repartition
fig5 = go.Figure(
    data=[go.Pie(
        labels=df_kaggle.Emotion.unique(),
        values=df_kaggle.groupby('Emotion').Text.nunique(),
        textinfo='label+percent')
    ],
    layout={'title': 'Kaggle', 'font_color': 'grey'}
)

# Figure 6 Data World emotions repartition
fig6 = go.Figure(
    data=[go.Pie(
        labels=df_world.sentiment.unique(),
        values=df_world.groupby('sentiment').content.nunique(),
        textinfo='label+percent'
    )],
    layout={'title': 'data.World', 'font_color': 'grey'}
)

# Tables
tab1_content = dash_table.DataTable(
    id='container-button-timestamp',
    data=df_kaggle.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df_kaggle.columns],
    export_format='csv',
    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_table={'overflowX': 'auto', 'width': '1200px', 'height': '400px'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'textAlign': 'left',
        'padding-left': '5px'
    }
)

tab2_content = dash_table.DataTable(
    id='container-button-timestamp',
    data=df_world.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df_world.columns],
    export_format='csv',
    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_table={'overflowX': 'auto', 'width': '1200px', 'height': '400px'},
    style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white', 'textAlign': 'left'},
    css=[{'selector': '.row', 'rule': 'margin: 0'}]
)

# Layout
layout = html.Div([
    dbc.Container([
        dbc.Row([dbc.Col(html.H2(children='Datasets'), className="mb-2")]),

        dbc.Row([dbc.Tabs([
            dbc.Tab(tab1_content, label="Kaggle", label_style={"color": "#119DFF"}),
            dbc.Tab(tab2_content, label="data.World", label_style={"color": "#C40030"}),
        ])]),

        dbc.Row([dbc.Col(html.H2(children='Emotions distribution'), className="mb-2")]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='graph-1', figure=fig1)),
            dbc.Col(dcc.Graph(id='graph-2', figure=fig2), className="mb-2")
        ]),

        dbc.Row([
            dbc.Col(
                html.H6(
                    children='We can observe that HAPPYNESS and SADNESS are very important in Kaggle dataset, \
                    but in the middle for data.World in which NEUTRAL and WORRY are dominant. \
                    Two emotions that do not exist in Kaggle data set. \
                    The two datasets are distributed so differently !'
                ),
                className="mb-4"
            )
        ]),

        dbc.Row([dbc.Col(html.H2(children='Emotions repartition'), className="mb-2")]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='graph-5', figure=fig5), className="mb-4"),
            dbc.Col(dcc.Graph(id='graph-6', figure=fig6), className="mb-4")
        ]),
        dbc.Col(
            html.H6(
                children='Classes are not distributed homogenously in both datasets : \
                hard point for relevant prediction. And classes are not the same between each datasets ...'
            ),
            className="mb-4"
        ),

        dbc.Row(
            [
                dbc.Col(html.H2(children='Words distribution'), width=5, className="mb-2"),
                dbc.Col(html.H5(children='(first 30ths + last 10ths)'), align='center', className="pl-0 ml-0")
            ]
        ),

        dbc.Row([
            dbc.Col(dcc.Graph(id='graph-3', figure=fig3), className="mb-2"),
            dbc.Col(dcc.Graph(id='graph-4', figure=fig4), className="mb-2")
        ]),

        dbc.Row([
            dbc.Col(
                html.H6(children='Taking into account words that appear more than 500 times, \
                we can observe that most of them express no emotion, and that in both datasets, \
                we have to remove them with stopwords so as to make our model more relevant.'),
                className="mb-4"
            )
        ]),
    ],
        className="mb-5"
    )
])
