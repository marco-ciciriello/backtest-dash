import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

# Define section layouts
left_column = html.Div([
    html.Div([
        html.Div('Symbols:'),
        dcc.Dropdown(
            id='symbols',
            options=['AAPL', 'AMZN', 'GOOGL', 'MSFT'],
            multi=True
        )
    ])
])

centre_column = html.Div([
    html.Div([
        dcc.Graph(id='charts')
    ])
])

right_column = html.Div([
    html.Div(
        html.Div([
            html.Div([
                html.Div([
                    html.Button('Backtest'),
                    html.Button('Save'), 
                    html.Button('Load')
                ]),
                html.Div(id='status-area')
            ]),
            html.Div(id='stat-block')
        ])
    )
])

bottom = html.Div([
    html.Div('Logs')
])

# Define app layout using sections
app.layout = html.Div([
    html.Div(
        html.Div(html.H1('backtest-dash'))
    ),
    html.Div([
        left_column, centre_column, right_column
    ]),
    html.Div(
        bottom
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
