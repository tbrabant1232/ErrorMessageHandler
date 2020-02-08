import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import date

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

today = date.today()
# dateStr = today.strftime("%d-%b-%Y")
dateStr = today.isoformat()
csvfile = (dateStr + "processed.csv")
inputFile = csvfile

df = pd.read_csv(inputFile)

app.layout = html.Div([
    dcc.Graph(
        id='Master Consol RELEASE Build Failures '+ dateStr,
        figure={
            'data': [
                dict(
                    x=df[df['Code'] == i]['Line Number'],
                    y=df[df['Code'] == i]['Scenario'],
                    # z=df[df['Code'] == i]['Mode'],
                    text=df[df['Code'] == i]['Error Summary'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.Code.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'Line Number'},
                yaxis={'title': 'Scenario'},
                margin={'l': 200, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'

            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)