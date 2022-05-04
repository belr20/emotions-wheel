#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle

import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from functions import print_table


filename = 'data/analysis-results/logreg-kaggle.sav'
res_logreg = pickle.load(open(filename, 'rb'))
res_logreg = print_table(res_logreg)

filename = 'data/analysis-results/sgd-kaggle.sav'
res_sgd = pickle.load(open(filename, 'rb'))
res_sgd = print_table(res_sgd)

filename = 'data/analysis-results/knn-kaggle.sav'
res_knn = pickle.load(open(filename, 'rb'))
res_knn = print_table(res_knn)

filename = 'data/analysis-results/dtree-kaggle.sav'
res_dtree = pickle.load(open(filename, 'rb'))
res_dtree = print_table(res_dtree)

filename = 'data/analysis-results/data-world.sav'
res_world = pickle.load(open(filename, 'rb'))
res_world = print_table(res_world)

filename = 'data/analysis-results/roccurve-kaggle.sav'
res_roc = pickle.load(open(filename, 'rb'))

# Tables
table_logreg_results = dbc.Row([
    dash_table.DataTable(
        id='container-button-timestamp',
        data=res_logreg.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in res_logreg.columns],
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_table={'overflowX': 'auto', 'width': '1200px', 'margin-bot': '100px'},
        style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white', 'textAlign': 'left', 'padding-left': '5px'},
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    ),
    html.H6(
        children='With a long execution time, STOPWORDS + NGRAM is the best vectorization for LOGISTIC REGRESSION.',
        className="mt-4"
    )
])

table_sgd_results = dbc.Row([
    dash_table.DataTable(
        id='container-button-timestamp',
        data=res_sgd.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in res_sgd.columns],
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_table={'overflowX': 'auto', 'width': '1200px'},
        style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white', 'textAlign': 'left', 'padding-left': '5px'},
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    ),
    html.H6(
        children='One more time, STOP-WORDS + NGRAM is the best vectorization for STOCHASTIC GRADIENT DESCENT model, \
         others are also quite good.',
        className="mt-4"
    )
])

table_knn_results = dbc.Row([
    dash_table.DataTable(
        id='container-button-timestamp',
        data=res_knn.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in res_knn.columns],
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_table={'overflowX': 'auto', 'width': '1200px'},
        style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white', 'textAlign': 'left', 'padding-left': '5px'},
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    ),
    html.H6(
        children='KNNeighbors is not suitable for NLP. Results are not good at all !',
        className='mt-4'
    )
])

table_dtree_results = dbc.Row([
    dash_table.DataTable(
        id='container-button-timestamp',
        data=res_dtree.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in res_dtree.columns],
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_table={'overflowX': 'auto', 'width': '1200px'},
        style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white', 'textAlign': 'left', 'padding-left': '5px'},
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    ),
    html.H6(
        children='Decision TREE has good scores, STOP-WORDS + NGRAM is one more time the best vectorization.',
        className='mt-4')
])

# Figure ROC curve
fig_roc_results = res_roc

# Layout
layout = html.Div([
    dbc.Container([
        dbc.Row([dbc.Col(html.H1(children='Classification'), className='mb-2')]),

        dbc.Row([dbc.Col(html.H6(
            children='We will compare & analyze different ML models with different vectorization techniques \
            for Kaggle dataset, which seems to be the best one.'),
            className='mb-4'
        )
        ]),

        dbc.Row([dbc.Col(html.H6(
            children='Different words vectorizations are performed to compare 4 machine learning classifiers : \
                     LOGISTIC REGRESSION, STOCHASTIC GRADIENT DESCENT, KNNEIGHBORS, & DECISION TREE.'),
            className='mb-4'
        )
        ]),

        dbc.Row([dbc.Col(html.H6(
            children='Legend : SW=STOP-WORDS, NG=N-GRAM, idf=TFIDF \
            (see GitHub link at top of this page for more information)'),
            className='mb-2'
        )
        ]),

        dbc.Row([dbc.Tabs([
            dbc.Tab(table_logreg_results, label='LOGREG', label_style={'color': '#119DFF'}),
            dbc.Tab(table_sgd_results, label='SGD', label_style={'color': '#C40030'}),
            dbc.Tab(table_knn_results, label='KNN', label_style={'color': '#119DFF'}),
            dbc.Tab(table_dtree_results, label='DTREE', label_style={'color': '#C40030'})
        ])],
            className='mb-4'
        ),

        dbc.Row([
            dbc.Col(html.H4(
                children='With classification report, let\'s compare best vectorization of each classifier \
                to determine the best one for Kaggle dataset'),
                className="mt-4 mb-4"
            )
        ]),

        dbc.Row([
            dbc.Col(html.Img(src='/assets/classification-reports/logreg-cr.png', height='240px'), width=4.5),
            dbc.Col(html.Img(src='/assets/classification-reports/sgd-cr.png', height='240px'), width=4.5),
            dbc.Col([
                dbc.Row([html.H5(
                    children='The distribution of scores is homogeneous for all models : \
                    LOVE & SURPRISED are the most difficult to detect.')],
                    className='mb-4'
                ),
                dbc.Row([html.H5(
                    children='HAPPY & SADNESS are well detected : it is surely because \
                    they are the most represented emotions in dataset.')],
                    className='mb-4'
                )
            ], className='mt-4 mb-4')
        ]),

        dbc.Row([
            dbc.Col(html.Img(src='/assets/classification-reports/knn-cr.png', height='240px'), width=4.5),
            dbc.Col(html.Img(src='/assets/classification-reports/dtree-cr.png', height='240px'), width=4.5),
            dbc.Col([
                dbc.Row([html.H5(
                    children='If we keep focus on score, SGD model is really the best \
                  in addition to being the fastest !')],
                    className='mb-4'
                ),
                dbc.Row([html.H5(
                    children='LOGREG is quite well too, with DTREE and after comes KNN.')],
                    className='mb-4')
            ], className='mt-4 mb-4'),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Row([html.H4(children='Stochastic Gradient Descent ROC curve')], className='mb-4'),
                dbc.Row([html.H5(
                    children='The Best Classifier is SGD with a F1 average at 0.9, \
                and it is the fastest with 2,91 seconds.')],
                    className='mb-4'),
                dbc.Row([html.H5(
                    children='With ROC curve, we can observe the true positives and false positives \
                to evaluate its performance.')],
                    className='mb-4'),
                dbc.Row([html.H5(children="We will use this model for our prediction API.")])
            ]),
            dbc.Col(dcc.Graph(id='graph-21', figure=fig_roc_results)),
        ]),

        dbc.Row([dbc.Col(html.H4(children='Data World scores'), className='mt-4 mb-4')]),

        dbc.Row([
            dash_table.DataTable(
                id='container-button-timestamp',
                data=res_world.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in res_world.columns],
                style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                style_table={'overflowX': 'auto',
                             'width': '1200px',
                             'margin-bot': '100px'},
                style_cell={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                    'textAlign': 'left',
                    'padding-left': '5px'
                },
                css=[{'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='Scores with Data World dataset are really bad !', className='mt-4 mb-4'),
        ]),

        dbc.Row([dbc.Col(html.H4(children='SGD classifier, with STOP-WORDS + N-GRAM vectorization, applied to \
        Kaggle dataset is the winner for the prediction API !'), className='mt-4 mb-4')]),
    ],
        className="mb-5")
])
