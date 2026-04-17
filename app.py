import pandas
from dash import Dash, html, dcc, callback, Output, Input
from plotly.express import line

DATA_PATH = "./formatted_data.csv"

data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

dash_app = Dash(__name__)

header = html.H1(
    "Soul Foods Pink Morsel Sales Visualiser",
    id="header",
    style={
        "backgroundColor": "#2B3329",
        "color": "#FFFFFF",
        "textAlign": "center",
        "padding": "20px",
        "margin": "0",
        "fontFamily": "Arial, sans-serif",
        "letterSpacing": "2px"
    }
)

radio_button = dcc.RadioItems(
    id="region-filter",
    options=[
        {"label": "All", "value": "all"},
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
    ],
    value="all",
    inline=True,
    style={
        "backgroundColor": "#4F5C4C",
        "color": "#FFFFFF",
        "padding": "15px",
        "textAlign": "center",
        "fontFamily": "Arial, sans-serif",
        "fontSize": "18px",
    }
)

visualization = dcc.Graph(id="visualization")

dash_app.layout = html.Div([
    header,
    radio_button,
    visualization
], style={
    "backgroundColor": "#243320",
    "minHeight": "100vh",
    "margin": "0",
    "padding": "0"
})

@callback(
    Output("visualization", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = data
    else:
        filtered = data[data["region"] == region]

    fig = line(
        filtered,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales ($)"},
        color_discrete_sequence=["#61DB48"]
    )
    fig.update_layout(
        paper_bgcolor="#243320",
        plot_bgcolor="#2B3329",
        font={"color": "#FFFFFF"},
    )
    return fig

if __name__ == '__main__':
    dash_app.run()