from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from time import sleep 
from mongodb import count_actions

sleep(3)


dash_app = Dash(__name__,
                external_stylesheets=[dbc.themes.MINTY], # PULSE
                suppress_callback_exceptions=True,
                requests_pathname_prefix='/real-time-monitoring/',
                meta_tags=
                [
                    {"name": "viewport", 
                     "content": """width=device-width, initial-scale=1"""
                     },
                     ]
        )
server_monitor = dash_app.server  

dash_app.title = "e-nMF Marketing Analytics: Understanding some nMFlings"

# tab1_content = dbc.Card(
#     dbc.CardBody(
#         [
#             html.P("Here we consider only those data whose utm is not null!", className="card-text"),
#             html.Div(
#                 [
                    
#                     dcc.Graph(figure={}, id='controls-and-graph-tab1')
#                 ],
#             )

#         ]
#     ),
#     className="mt-3",
# )

dash_app.layout = dbc.Container(
    [
        dcc.Store(id='store'),
        html.Img(src="./assets/logo_nmf4.jpeg",alt="e-nMF",width=55),
        html.H1("Real Time Dashboard"),
        html.P("Monitoring e-nMFlings"),
        html.Hr(),
        html.Div([ 
            dcc.Graph(id='click-chart'),
            dcc.Interval(
                id='interval-component',
                interval=5*1000,  # in milliseconds
                n_intervals=0
                )
                ])
        # html.Div([
        #     tabs,html.Div(id='tab-content', className='p-4')]),
        
    ],
    fluid=False,
    
)

# Define callback to update the chart
@dash_app.callback(
    Output('click-chart', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_chart(n):
    # Generate new data point
    _, actions, counts = count_actions()

    colors = ['blue','green','crimson']

    # Create plotly figure
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=actions,y=counts,opacity=0.5, 
        texttemplate=counts, marker_color=colors
        ))

    fig.update_layout(
        title=dict(text=f'User Web-Interaction Count ({sum(counts)})',
                   xanchor="center",
                   yanchor='top',
                   y=0.9,
                   x=0.5,
                   font=dict(family="Rockwell",
                             size= 20)),
        plot_bgcolor="white",
        barcornerradius="20%",
        width=500, height=500
        
    )

    fig.update_xaxes(
    ticks='outside',
    showline=False,
    linecolor='black',
    tickfont=dict(family='Rockwell', size=14)
)
    fig.update_yaxes(
        mirror=True,
        ticks='outside',
        showline=False,
        linecolor='black',
        visible=False
        
    )

    return fig



if __name__ == '__main__':
    dash_app.run(debug=True, port=5000)