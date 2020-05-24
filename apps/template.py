import plotly.graph_objects as go

import json
from textwrap import dedent as d

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

from app import app

import json

import numpy as np
import pandas as pd

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                html.H3("TEMPLATE HEADER"),
                            ], fluid=True, style={'padding-left': 20,
                                                  'padding-top': 10,
                                                  'padding-bottom': 0,
                                                 }               
                        ),
                    ], width=8
                ),
                dbc.Col(
                    [
                        dbc.Container(
                            [
                            dcc.Link(
                               html.H3("Dashboards"),
                               href='/',
                               style={'color': 'lightgrey'}
                            ),
                            ], fluid=True, style={'text-align': 'right',
                                                  'padding-right': 40,
                                                  'padding-top': 10,
                                                  'padding-bottom': 0,
                                                  'color': 'lightgrey',
                                                 }               
                        ),
                    ], width=4
                )
            ], justify='center', no_gutters=True,
        ),

        # Hidden div inside the app that stores the intermediate value
        html.Div(id='TEMPLATE-intermediate-value', style={'display': 'none'}),

        # row for arg and marginal trees
        dbc.Row(
            [
                # column for arg 
                dbc.Col(
                    [
                        # arg
                        dbc.Container(
                            [
                                dbc.Container(
                                    [

                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.B("Dropdown one:"),
                                                        dcc.Dropdown(
                                                            id='TEMPLATE-dropdown-one',
                                                            options=[
                                                                {'label': "choice one", 'value': 'one'},
                                                                {'label': "choice two'", 'value': 'two'}
                                                            ],
                                                            value='arg', searchable=False, clearable=False
                                                        ),
                                                    ], width=2
                                                ),                                                        
                                                dbc.Col(
                                                    [
                                                        html.B("Dropdown two"),
                                                        dcc.Dropdown(
                                                            id='TEMPLATE-dropdown-two',
                                                            options=[
                                                                {'label': "3", 'value': 3},
                                                                {'label': "4", 'value': 4},
                                                                {'label': "5", 'value': 5}
                                                            ],
                                                            value=5, searchable=False, clearable=False,
                                                            style={
                                                                    # 'height': '20px', 
                                                                    # 'width': '80px', 
                                                                    'font-size': "0.85rem",
                                                                    # 'min-height': '1px',
                                                                    },
                                                        ),
                                                    ], width=2
                                                ),  
                                                dbc.Col(
                                                    [
                                                        html.B("Dropdown three:"),
                                                        dcc.Dropdown(
                                                            id='TEMPLATE-dropdown-three',
                                                            options=[
                                                                {'label': "1kb", 'value': 1e+3},
                                                                {'label': "2kb", 'value': 2e+3},
                                                                {'label': "4kb", 'value': 4e+3}
                                                            ],
                                                            value=2e+3, searchable=False, clearable=False,
                                                            style={
                                                                    # 'height': '20px', 
                                                                    # 'width': '80px', 
                                                                    'font-size': "0.85rem",
                                                                    # 'min-height': '1px',
                                                                    },
                                                        ),
                                                    ], width=2
                                                ),                                                                                                        
                                                dbc.Col(
                                                    [ 
                                                        dbc.Button('New data', 
                                                            id='TEMPLATE-new-data-button', 
                                                            color="primary", #size="sm", #outline=True,
                                                            style={'height': 35, 'font-size': "0.85rem"},
                                                            className="mr-1"
                                                            )
                                                    ], width=3
                                                ),    
                                                dbc.Col(
                                                    [
                                                        html.Div(id='TEMPLATE-dynamic-header'),

                                                        # dcc.Markdown(d("""
                                                        # **Ancestral recombination graph:**   
                                                        # Nodes are colored by amount of ancestral sequence.
                                                        # """), ),                    
                                                    ], width=3
                                                ),                                                                                                                                                    
                                                # dbc.Col(
                                                #     [ 
                                                #         dcc.Loading(
                                                #             id="loading-1",
                                                #             type="default",
                                                #             children=html.Div(id="arg-figure"),
                                                #         ),  
                                                #     ], width=1
                                                # )
                                                    
                                            ], justify="between", align="end", #no_gutters=True, 
                                        ),


                                        dcc.Graph(id='TEMPLATE-main-figure',
                                                clear_on_unhover=True,
                                                figure={'layout': {
                                                            'height': 570,
                                                            # 'margin': {'l': 0, 'b': 0, 't': 0, 'r': 0},
                                                                }
                                                            },
                                                    ),

  

                                    ], className='pretty_container', fluid=True,
                                ),
                            ], style={'padding': 20}
                        ),
                    ], width=8, 
                ),

                # column for marginal trees
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                dbc.Container(
                                    [
                                        dcc.Markdown(d("""
                                        **Marginal tree(s):** Hover over an ARG node.
                                        """), ),                    
                                        dcc.Graph(id='TEMPLATE-side-figure-one',
                                                    figure={'layout': {
                                                            # 'title': 'Marginal tree',
                                                            'height': 250,
                                                            # 'margin': {'l': 0, 'b': 0, 't': 0, 'r': 0},
                                                                }
                                                            },),
                                    ], className='pretty_container'
                                ),
                            ], style={'padding': 20, 'padding-left': 0, 'padding-bottom': 0}
                        ),
                        dbc.Container(
                            [
                                dbc.Container(
                                    [
                                        dcc.Markdown(d("""
                                        **Ancestral sequences:** Hover over an ARG node.
                                        """), ),                    
                                        dcc.Graph(id='TEMPLATE-side-figure-two',
                                                figure={'layout': {
                                                    'height': 250,
                                                        }
                                                        },),
                                    ], className='pretty_container'
                                ),            
                            ], style={'padding': 20, 'padding-left': 0}
                        ),            
                    ], width=4, 
                ),        
            ], no_gutters=True
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                dbc.Container(
                                    [
                                        dbc.Container(
                                            [
                                                dcc.Markdown(d("""
                                                **Coalesce and recombination events:** 
                                                Slide to see progression of events.
                                                """)),
                                            ], 
                                        ),
                                        dbc.Container(
                                            [
                                                dcc.Slider(
                                                    id='TEMPLATE-discrete-slider',
                                                    min=0, max=40, value=0, 
                                                    marks={str(i): str(i) for i in range(0, 40)}, 
                                                    step=None,
                                                    ),
                                            ], style={'padding-bottom': 20}
                                        )
                                    ], className='pretty_container'
                                )
                            ], style={'padding': 20, 'padding-top': 0},
                        )
                    ], width=6
                ),  
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                dbc.Container(
                                    [
                                        dbc.Container(
                                            [
                                                dcc.Markdown(d("""
                                                    **Recombination points:** 
                                                    Slide to see graph for only part of the sequence.
                                                """)),
                                            ]
                                        ),
                                        dbc.Container(
                                            [
                                                dcc.RangeSlider(
                                                    id='TEMPLATE-continuous-slider',
                                                    min=0,
                                                    max=1000,
                                                    value=[0, 1000],
                                                    # step=None,
                                                    marks={0: '0', 1000: '1'},
                                                    pushable=30,
                                                )
                                            ], style={'padding-bottom': 20}
                                        ),
                                    ], className='pretty_container', 
                                ),
                            ], style={'padding': 20, 'padding-left': 0, 'padding-top': 0}
                        ),
                    ], width=6, align='start',
                ),
            ], no_gutters=True, 
        ),
    ], style={'padding': 20}
)


def main_figure_data(data):

    # use `data` as source for plot:

    node_color = np.random.randint(1, 10, size=10)

    traces = []
    traces.append(dict(
        x=np.random.randint(1, 10, size=10),
        y=np.random.randint(1, 10, size=10),
        # mode='lines',
        # line={
        #     'color': 'grey',
        # },        mode='markers',
        mode='markers',
        marker={
            'size': 10,
            'color': node_color,
            # 'cmin': 0,
            # 'cmax': 1,
            # 'line': {'width': 0.5, 'color': 'white'},
#            'colorscale': 'Viridis',
            # 'colorbar': {'title': 'Fraction<br>ancestral<br>sequence',
            #             'titleside': 'top',
            #             'thickness': 15,
            #             'len': 0.5,
            #             # 'tickmode': 'array',
            #             'tickvals': [0, 0.5, 1],
            #             # 'ticktext': ['0', '1'],
            #             'ticks': 'outside',
            #             },
        },
        opacity=1,
        hoverinfo ='text',
        # hoverinfo ='skip',
        name='TEMPLATE'
    ))

    return dict(data=traces,
                layout=dict(xaxis=dict(fixedrange=True, 
                                    #    range=[0, 6],
                                       title='X label',
                                    #    showgrid=False, showline=False, 
                                    #    zeroline=False, showticklabels=False
                                       ),
                            yaxis=dict(fixedrange=True, 
                                    #    range=[0, 6],
                                       title='Y label',
                                    #    showgrid=False, showline=False, 
                                    #    zeroline=False, showticklabels=False
                                       ),
                            hovermode='closest',
                            # range_color=[0,1],
                            margin= {'l': 50, 'b': 50, 't': 20, 'r': 20},
                            transition = {'duration': 10},
                            showlegend=False
                            )
                )


@app.callback(
    Output('TEMPLATE-dynamic-header', 'children'),
    [Input('TEMPLATE-new-data-button', 'n_clicks')])
def update_header(n_clicks):

    if n_clicks is None:
        n_sim = 1
    else:
        n_sim = n_clicks + 1

    return dcc.Markdown(d("""
                **Simulation #{}:**   
                """.format(n_sim)))

@app.callback(Output('TEMPLATE-intermediate-value', 'children'), 
    [Input('TEMPLATE-new-data-button', 'n_clicks'),
     Input('TEMPLATE-dropdown-one', 'value'),
     Input('TEMPLATE-dropdown-two', 'value'),
     Input('TEMPLATE-dropdown-three', 'value')])
def new_data(n_clicks, sim, samples, length):
    
    json_str = '{}'
    return json_str

@app.callback(
    [Output(component_id='TEMPLATE-discrete-slider', component_property='min'),
     Output(component_id='TEMPLATE-discrete-slider', component_property='max'),
     Output(component_id='TEMPLATE-discrete-slider', component_property='step'),
     Output(component_id='TEMPLATE-discrete-slider', component_property='value')],
    [Input('TEMPLATE-intermediate-value', 'children')])    
def update_event_slider(jsonified_data):

    if jsonified_data:
        data = json.loads(jsonified_data)
    else:
        data = []

    nr_marks = 10
    return 0, nr_marks, 1, nr_marks

@app.callback(
    [Output(component_id='TEMPLATE-continuous-slider', component_property='min'),
     Output(component_id='TEMPLATE-continuous-slider', component_property='max'),
     Output(component_id='TEMPLATE-continuous-slider', component_property='value'),
     Output(component_id='TEMPLATE-continuous-slider', component_property='marks')],
    [Input('TEMPLATE-intermediate-value', 'children')])    
def update_continuous_slider(jsonified_data):
    if jsonified_data:
        data = json.loads(jsonified_data)
    else:
        data = []

    # modify / subset data
    data = data

    marks = dict((b*1000, str(i+1)) for i, b in enumerate([0.1, 0.7]))

    return 0, 1000, [0, 1000], marks

@app.callback(
    Output('TEMPLATE-main-figure', 'figure'),
    [Input('TEMPLATE-intermediate-value', 'children'),
     Input('TEMPLATE-discrete-slider', 'value'),
     Input('TEMPLATE-continuous-slider', 'value')])
def update_main_figure(jsonified_data, event, interval):

    if jsonified_data:
        data = json.loads(jsonified_data)
    else:
        data = []
    print(data)
    # modify / subset data
    data = data

    return main_figure_data(data)

@app.callback(
    Output('TEMPLATE-side-figure-one', 'figure'),
    [Input('TEMPLATE-discrete-slider', 'value'),
     Input('TEMPLATE-continuous-slider', 'value'),
     Input('TEMPLATE-main-figure', 'hoverData')])
def update_side_figure_one(node, interval, hover):

#    print(node, interval, hover)
    if hover is None:
        color='blue'
    else:
        color='red'#hover['points'][0]['x']
    return dict(data=[dict(x=[1,2,3], 
                            y=[1,2,3], 
                            mode='markers', 
                            marker={'color': color})],
                layout=dict(xaxis=dict(range=[0, 4], #title='Samples',
                                       showgrid=False, showline=False, 
                                       zeroline=False, showticklabels=False
                                       ),
                            yaxis=dict(range=[0, 4], #title='Time',
                                       showgrid=False, showline=False, 
                                       zeroline=False, showticklabels=False
                                       ),
                            hovermode='closest',
                            margin= {'l': 0, 'b': 0, 't': 20, 'r': 0},
                            transition = {'duration': 0},
                            showlegend=False
                            ))

@app.callback(
    Output('TEMPLATE-side-figure-two', 'figure'),
    [Input('TEMPLATE-discrete-slider', 'value'),
     Input('TEMPLATE-continuous-slider', 'value'),
     Input('TEMPLATE-main-figure', 'hoverData')])
def update_side_figure_two(node, interval, hover):
    # print(node, interval, hover)
    if hover is None:
        color='blue'
    else:
        color='red'#hover['points'][0]['x']
    return dict(data=[dict(x=[1,2,3], 
                            y=[1,2,3], 
                            mode='markers', 
                            marker={'color': color})],
                layout=dict(xaxis=dict(range=[0, 4], #title='Samples',
                                       showgrid=False, showline=False, 
                                       zeroline=False, showticklabels=False
                                       ),
                            yaxis=dict(range=[0, 4], #title='Time',
                                       showgrid=False, showline=False, 
                                       zeroline=False, showticklabels=False
                                       ),
                            hovermode='closest',
                            margin= {'l': 0, 'b': 0, 't': 20, 'r': 0},
                            transition = {'duration': 0},
                            showlegend=False
                            ))
