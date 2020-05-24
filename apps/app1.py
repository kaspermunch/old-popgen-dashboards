import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# layout = html.Div([
#     html.H3('App 1'),
#     dcc.Dropdown(
#         id='app-1-dropdown',
#         options=[
#             {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
#                 'NYC', 'MTL', 'LA'
#             ]
#         ]
#     ),
#     html.Div(id='app-1-display-value'),
#     dcc.Link('Go to App 2', href='/apps/app2')
# ])


# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

layout = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Ancestral recombination graph", 
                        tab_id="tab-1",
                        label_style={"color": "black", 'font-size': '200%'},
                        tab_style={"color": 'blue'},
                        ),
                    dbc.Tab(label="Explore", tab_id="tab-2",
                        label_style={"color": "lightgrey", 'font-size': '200%'}
                    ),
                ],
                id="card-tabs",
                card=True,
                active_tab="tab-1",
                style={'border': 10},
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text"), 
        # style={'background-color': 'green'}
        ),
    ]
)


@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    return "This is tab {}".format(active_tab)