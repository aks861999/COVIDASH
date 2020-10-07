from c_list import country_list
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html




corona_layout=html.Div([
        html.Div(
        [html.H1(children='Progression of COVID-19 Spread Around the Globe')],
        style={'textAlign': 'center','background-color': '#000000','color':'#FFDF00','font-weight':'bold'}),




#################### starting of world data visualisation  ###################
        
        html.Div(
        [html.H2('Would You Like to Select A Country Of Your Choice  !!!!!!')],
            style={'textAlign': 'center','background-color': '#000000','color':'#BFFF00','font-weight':'bold'}),
        
        
        
        dbc.Container(
        html.Div([dbc.Container(children = [html.Div(dcc.Dropdown(id = 'select-country', options = country_list, value='Global Result',
        style={'background-color': '#FFFDD0','width':'3','textAlign': 'center','color':'black'}),
        style={'background-color': '#FFFDD0','width':'3','textAlign': 'center','color':'black'})
                                        
        ])])),


###################### Subplots ###################################
############## Confirmed	Deaths	Recovered	Active	Incident_Rate	Mortality_Rate ###################









        dbc.Container(
        html.Div([

        dcc.Loading(
            id="loading-1",
            type="default",


        children=dcc.Graph(id='fig of world',
        hoverData=None,
        figure={
                #hoverData=None,
                'layout': go.Layout(                                
                    xaxis =  {                                     
                        'showgrid': False
                                },
                    yaxis = {                              
                        'showgrid': True
                            },                                                                
                    ),
                    'zeroline': False
        }
        ))],
        style={'display': 'inline-block','background-color': '#000000','width': '820','textAlign': 'center'})),

        #,'padding-left':'1%', 'padding-right':'1%'









    
    
    
    dbc.Container(html.Div([html.H2(children='If You Like The Dashboard, Do Not Forget To Subscribe To Stay Upadated')],
            style={'textAlign': 'center','color':'#DA70D6','font-weight':'bold','font-family':'courgette'})),
        
    
    html.Div([html.H4(children='Type Your E-mail ID')],style={'textAlign': 'center','color':'#FF4500','font-weight':'bold','font-family':'courgette'}),
    
    dbc.Container(html.Div([dcc.Input(id='input-on-submit',type='email',
                                      style={'display': 'inline-block','width': '50%', 'font-family':'orbitron','textAlign': 'center','background-color':'#FBCEB1'})],
                       style={'textAlign': 'center'}  )),
    
    
    
    dbc.Container(html.Div([html.Button('Click Me And Wait A Bit !', id='submit-val', n_clicks=0,
style={'width': '35%','textAlign': 'center','font-weight':'bold','background-color': '#003153','color':'#FFFFFF'})],style={'color':'#FFFFFF','textAlign': 'center','font-weight':'bold'})),
    
    
    html.Div(id='container-button-basic',
             children='',
            style={'textAlign': 'center','color':'#FFFF00','font-style':'italic'}),



    #dbc.Container(html.Div([html.H1( id = 'text for user loginn' children='Please Login To Unlock Different Status based on Current Your Location')],
     #       style={'textAlign': 'center','color':'#FFAA1D','font-weight':'bold','font-family':'courgette'})),
    
             
    html.Br(),
    html.Br(),
    html.Br(),

    ########## "The Visualisation of Corona-Trend for Different Cases in\n" ###########
    html.Div(html.H2(id="text for indiv graph",children=''),
    style={'textAlign': 'center','font-weight': 'bold','color':'#FF007F'}),



    dbc.Container(
    html.Div([

        dcc.Loading(
            id="loading-2",
            type="default",
            children= dcc.Graph(id='fig for indiv graph')
        )],
    style={'display': 'inline-block','background-color': '#000000','width': '820','textAlign': 'center'})
    ),

    #,'padding-left':'5%', 'padding-right':'3%'
    
    





    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),   

    
    
    
    
    
    
    html.Div([html.H4(children='Dear Valuable Visitor, Is there anything that you found missing in the Dashboard and want us to add in near future ? ..... Do not think twice to put your VALUABLE Feedback, We will be overwhelmingly pleased to serve your desired solution')],
    style={'textAlign': 'center','color':'#7FFF00','font-weight':'bold','font-family':'courgette'}),
    
    dbc.Container(html.Div([dcc.Textarea(id='input-on',
    style={'display': 'inline-block','width': '100%','height': '300', 'font-family':'orbitron','textAlign': 'center','background-color':'#FBCEB1'})],
    style={'textAlign': 'center'}  )),
    
    
    
    dbc.Container(html.Div([html.Button('Click Me', id='submit1', n_clicks=0,
    style={'width': '35%','textAlign': 'center','font-weight':'bold','background-color': '#003153','color':'#FFFFFF'})],
    style={'color':'#FFFFFF','textAlign': 'center','font-weight':'bold'})),
    
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.Div([
    html.Footer(children='Made With ðŸ’– by Akash Biswas, Only for You'),],style={'background-color': '#0000FF','color':'#7FFF00','textAlign': 'center','font-weight': 'bold','width':'750'})
],style={'background-color': '#000000','color':'#FFFFFF','font-weight':'bold','width':'820'})