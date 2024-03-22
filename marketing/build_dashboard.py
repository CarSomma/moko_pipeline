from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


dash_app = Dash(__name__,
                external_stylesheets=[dbc.themes.MINTY], # PULSE
                suppress_callback_exceptions=True,
                meta_tags=
                [
                    {"name": "viewport", 
                     "content": """width=device-width, initial-scale=1"""
                     },
                     ]
        )
server = dash_app.server  

dash_app.title = "e-nMF Marketing Analytics: Understanding some nMFlings"


dash_app.layout = dbc.Container(
    [
        dcc.Store(id='store'),
        html.Img(src="./assets/logo_nmf4.jpeg",alt="e-nMF",width=55),
        html.H1("Marketing Analytics Dashboard"),
        html.P("Understanding e-nMFlings"),
        html.Hr(),
        # html.Div([
        #     tabs,html.Div(id='tab-content', className='p-4')]),
        
    ],
    fluid=False,
    
)

if __name__ == '__main__':
    dash_app.run(debug=True, port=5000)
