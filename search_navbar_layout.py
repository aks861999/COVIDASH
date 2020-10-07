import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import requests




global_flag="https://raw.githubusercontent.com/aks861999/COVIDASH/master/Country%20Flags/global.jpg"




search_navbar_layout = dbc.Navbar(

        [
            #https://cdn.britannica.com/97/1597-004-05816F4E/Flag-India.jpg
            #"https://assets.teenvogue.com/photos/5e8df9bf6a53960008b4ee3b/16:9/w_2560%2Cc_limit/GettyImages-1208742706.jpg"
            
            
            dbc.Collapse(
                dbc.Row(
                    [
                        html.Div(dbc.Col(html.Img(id="se_img", src=global_flag, 
                             height="100px",
                            width='130px'),
                            align="left"
                                    )),
            
                        dbc.NavbarToggler(id="navbar-toggler"),
                        
                        
                        
                        
                        html.Div(id = "testing", children = 
                        [
                            #dbc.Row([
                                dbc.Col(
                                    dbc.Input(id='email'  ,type="email", placeholder="Enter email",
                                             
                                              style={
                                                  'width':'300px',
                                                  'textAlign': 'center'
                                              }
                                             
                                             ),
                                ),
                            dbc.Col(
                                dbc.Input(id='password',type="password", placeholder="Enter password",
                                         
                                         style={
                                                  'width':'300px',
                                                 'textAlign': 'center'
                                              }
                                         ),
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "LogIn", id='submit', color="primary", className="ml-2"
                                ),
                                width="auto",
                            ),]
                         ),
                     html.Div(
                            dbc.Col([
                            html.Div(id='error')
                         ]),
                             style={
                                'textAlign': 'center',
                                'color': '#FF5470',
                                'font-weight':'bold'
                            }
                        ),
                        html.Div(id="sound", style={"display": "none"}),
                         html.Div(
                            dbc.Col([
                            html.Div(id="logged-in")
                         ]),
                                style={
                                'textAlign': 'center',
                                'color': '#FF5470',
                                'font-weight':'bold',
                                'font-family':'courgette',
                                'font-size':'20px'
                            }
                        ),
        html.Div(
            dbc.Col([
            html.A(children=html.Div(id='forgo'), href='https://covidash-ak.herokuapp.com/reset_password/', target="_blank",
                  
                  style={
            'textAlign': 'center',
            'color': '#FF5470',
            'font-weight':'bold',
            'font-size':'20px'
            
            }
           )
            ]),

        ),
         html.Div(
                    dbc.Col([
                    html.A(children= html.Div(id="to_reg"), href='https://covidash-ak.herokuapp.com/new=True/', target="_blank",
                        style={
                            'textAlign': 'center',
                            'color': '#FF5470',
                            'font-weight':'bold',
                            'font-size':'20px'
                            }
                        )
                    ]),
                                
                        ),
                        html.Div(
                            dbc.Col([
                            html.A(children=html.Div(id='logout'), href='https://covidash-ak.herokuapp.com/', target="_blank",
                                  
                                  
                                   style={
                                        'textAlign': 'center',
                                        'color': '#FF5470',
                                        'font-weight':'bold',
                                        'font-size':'20px'

                                        }
                                  )
                            ]),
                                
                        ),
                        ],
                    no_gutters=True,
                    className="ml-auto flex-nowrap mt-3 mt-md-0",
                    align="left"
                ),
                id="navbar-collapse",
                navbar=True ),
        ],
        
        style={
            'textAlign': 'center',
            'color': '#FF5470',
            'font-weight':'bold',
            'font-family':'courgette',
            'width':'1500'
            }
)