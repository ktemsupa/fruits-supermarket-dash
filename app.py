import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart

myfavoritecolor='C74A2F'
x_list=['Apples', 'Pineapples', 'Grapes', 'Pears', 'Bananas]
y_list=y=[4, 2, 8, 6, 10]

data = [go.Bar(
            x=x_list,
            y=y_list,
            marker=dict(color=myfavoritecolor)
    )]

layout = go.Layout(
    title = 'My favorite animals', # Graph title
    xaxis = dict(title = 'Type of Fruits'), # x-axis label
    yaxis = dict(title = 'Number in Supermarket'), # y-axis label

)
fig = go.Figure(data=data, layout=layout)


########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Animals in the Zoo'),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href='https://github.com/austinlasseter/zoo-animals-dash'),
    html.Br(),
    html.A('HTML Color Codes', href='https://htmlcolorcodes.com'),


    ]
)

if __name__ == '__main__':
    app.run_server()
