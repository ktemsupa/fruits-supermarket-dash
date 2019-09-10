import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart

x_list=['Apples', 'Pineapples', 'Grapes', 'Pears', 'Bananas']
y_list=y=[4, 2, 8, 6, 10]
color1 = '#90ee90'
color2 = '#9370db'
color3 = '#ffa500'
color4 = '#C74A2F'
color5 = '#FEC227'

data = [go.Bar(
            x=x_list,
            y=y_list,
            marker={'color': [color1, color2, color3, color4, color5]}

)]

layout = go.Layout(
    title = 'My Favorite Fruits', # Graph title
    xaxis = dict(title = 'Type of Fruits'), # x-axis label
    yaxis = dict(title = 'Number in Supermarket'), # y-axis label

)
fig = go.Figure(data=data, layout=layout)


########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Fruits in the Supermarket'),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href='https://github.com/ktemsupa/fruits-supermarket-dash'),
    html.Br(),
    html.A('HTML Color Codes', href='https://htmlcolorcodes.com'),


    ]
)

if __name__ == '__main__':
    app.run_server()
