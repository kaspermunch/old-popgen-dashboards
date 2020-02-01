import plotly.graph_objects as go

import json
from textwrap import dedent as d

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

import pandas as pd

import networkx as nx

G = nx.random_geometric_graph(20, 0.125)


edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
layout = html.Div([
      html.Div([
        dcc.Markdown(d("""
            **ARG:**
        """)),
        dcc.Graph(id='graph-with-slider'),
    ], className='six columns'),#style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
   html.Div([
        dcc.Markdown(d("""
            **Trees:** Click on coalescent to see below or click recombination to see tree on either side.
        """)),
        dcc.Graph(id='extra'),
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
        html.Div([
            dcc.Markdown(d("""
                **Event time line:**
            """)),
        dcc.Slider(
            id='year-slider',
            min=0,
            max=20,
            value=0,
            marks={str(i): str(i) for i in range(0, 20)},
            step=None
        )
        ], className='six columns'),#style={'width': '90%', 'display': 'inline-block', 'padding': '1em'}),

    html.Div([
        dcc.Markdown(d("""
            **Hover Data**

            Mouse over values in the graph.
        """)),
        html.Pre(id='hover-data', style=styles['pre'])
    ], className='two columns'),
    html.Div([
        dcc.Markdown(d("""
            **Click Data**

            Click values in the graph.
        """)),
        html.Pre(id='click-data', style=styles['pre'])
    ], className='two columns'),    
])

@app.callback(
    Output('hover-data', 'children'),
    [Input('graph-with-slider', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output('click-data', 'children'),
    [Input('graph-with-slider', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    traces = []

    traces.append(dict(
        x=edge_x[:selected_year*3],
        y=edge_y[:selected_year*3],
        # text=df_by_continent['country'],
        #mode='lines+markers',
        mode='lines',
        opacity=0.7,
        line={
            'color': 'grey',
        },
        name='kasper'
    ))
    traces.append(dict(
        x=node_x[:selected_year],
        y=node_y[:selected_year],
        text='coalescent',
        #mode='lines+markers',
        mode='markers',
        opacity=1,
        marker={
            'size': 10,
            'color': node_adjacencies[:selected_year],

            'line': {'width': 0.5, 'color': 'white'}
        },
        name='kasper'
    ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'range':[0, 1]},
            yaxis={'range': [0, 1]},
            hovermode='closest',
            transition = {'duration': 100},
        )
    }

# fig = go.Figure(data=[edge_trace, node_trace],
#              layout=go.Layout(
#                 title='<br>Network graph made with Python',
#                 titlefont_size=16,
#                 showlegend=False,
#                 hovermode='closest',
#                 margin=dict(b=20,l=5,r=5,t=40),
#                 annotations=[ dict(
#                     text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
#                     showarrow=False,
#                     xref="paper", yref="paper",
#                     x=0.005, y=-0.002 ) ],
#                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
#                 )
# fig.show()


# if __name__ == '__main__':
#     app.run_server(debug=True)