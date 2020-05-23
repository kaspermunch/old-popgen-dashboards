import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2, arg



def make_subheader(text):
    content = dbc.Container(
                    [
                        html.H4(text),

                    ], fluid=True, style={#'background': 'white', 
                                        'padding-left': 40,
                                        'padding-top': 20,
                                        'padding-bottom': 0,
                                        }               
                )
    return content

def make_card(text, image, page):
    content = dbc.Card(
                [
                    dcc.Link(
                        dbc.CardImg(src=image, top=True),
                            href=f'/apps/{page}', style={'border': 10}
                        ),
                    dbc.CardBody(
                        html.P(text, className="card-text")
                    ),
                ], className='pretty_container', style={'margin': 10},
            )
    return content

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [                
                        dbc.Container(
                            [
                                html.H1("Population Genetic Dashboards"),
                                html.P("Kasper Munch"),
                            ], fluid=True, style={#'background': 'white', 
                                                'padding-left': 40,
                                                'padding-top': 20,
                                                'padding-bottom': 0,
                                                }               
                        ),
                    ]
                ),
                # dbc.Col(
                #     [
                #         dbc.Container(
                #             [
                #                html.H3("Kasper Munch"),
                #             ], fluid=True, style={#'background': 'white', 
                #                                 'text-align': 'right',
                #                                 'padding-right': 40,
                #                                 'padding-top': 20,
                #                                 'padding-bottom': 0,
                #                                 'color': 'lightgrey',
                #                                 }               
                #         ),
                #     ], width=5
                # )                
            ]

        ),
        dbc.Row(
            [
                dbc.Col(
                    [                
                        make_subheader('Genetic drift')
                    ]
                ),
            ], no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        make_card("Drift in large populations", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("Drift in finite populations", "/assets/images/placeholder286x180.png", 'app2'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("Effective population size", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
            ], style={'padding-left': 20 }, no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [                
                        make_subheader('Selection')
                    ]
                ),
            ], no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        make_card("Strong positive selection", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("Weak positive selection", "/assets/images/placeholder286x180.png", 'arg'),

                    ], width=3
                ),
                dbc.Col(
                    [

                    ], width=3
                ),
            ], style={'padding-left': 20 }, no_gutters=True
        ),        
        dbc.Row(
            [
                dbc.Col(
                    [                
                        make_subheader('The coalescent')
                    ]
                ),
            ], no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        make_card("The coalescent", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("The coalescent in two populations", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("The coalescent and demography", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("Pool-Nielsen effect", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
            ], style={'padding-left': 20 }, no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [                
                        make_subheader('The coalescent with recombination')
                    ]
                ),
            ], no_gutters=True
        ), 
        dbc.Row(
            [
                dbc.Col(
                    [
                        make_card("The ancestral recombination graph", "/assets/images/arg.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [

                    ], width=3
                ),
                dbc.Col(
                    [

                    ], width=3
                ),
            ], style={'padding-left': 20 }, no_gutters=True
        ),                 
        dbc.Row(
            [
                dbc.Col(
                    [                
                        make_subheader('Lineage sorting')
                    ]
                ),
            ], no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        make_card("Lineage sorting", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [
                        make_card("Incomplete lineage sorting", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [

                    ], width=3
                ),
            ], style={'padding-left': 20 }, no_gutters=True
        ),          
        dbc.Row(
            [
                dbc.Col(
                    [                
                        make_subheader('Admixture')
                    ]
                ),
            ], no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        make_card("Distribution of admixture segments", "/assets/images/placeholder286x180.png", 'arg'),
                    ], width=3
                ),
                dbc.Col(
                    [

                    ], width=3
                ),
                dbc.Col(
                    [

                    ], width=3
                ),
            ], style={'padding-left': 20 }, no_gutters=True
        ),                        
    ], id='cards', #style={'padding': 10}
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),
               ])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    if pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/arg':
        return arg.layout
    else:
        return layout

if __name__ == '__main__':
    app.run_server(debug=True)