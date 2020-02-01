import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import date

today = date.today()
dateStr = today.strftime("%d-%b-%Y")
csvfile = (dateStr + "raw.csv")
inputFile = csvfile

df = pd.read_csv(inputFile)


def generate_table(dataframe, max_rows=40):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]


    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4('Master Consol RELEASE Build Failures '+ dateStr),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
