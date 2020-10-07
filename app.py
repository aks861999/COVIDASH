from corona_layout import corona_layout
from search_navbar_layout import search_navbar_layout
from c_list import codes
from firebase import firebase
import smtplib 
import time
firebase = firebase.FirebaseApplication('https://covid-dash-ak.firebaseio.com/', None)
import json
import requests
import pandas as pd


############### https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings  ###############
import urllib3
urllib3.disable_warnings()




from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pycountry
import plotly.express as px
from plotly.subplots import make_subplots

import pyrebase
from flask import *
from flask import request
from gtts import gTTS
import base64
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

country_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/country_df.csv')
confirmed_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/confirmed_df.csv')
death_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/death_df.csv')
recovered_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/recovered_df.csv')
daily_new_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/daily_new_df.csv')
daily_death_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/daily_death_df.csv')
daily_recov_df=pd.read_csv('https://raw.githubusercontent.com/aks861999/COVIDASH/master/covidash_backend_files/daily_recov_df.csv')



				


country_df_top10_Confirmed=country_df.sort_values(by=['Confirmed'],ascending=False)
country_df_top10_Confirmed=country_df_top10_Confirmed.head(10)
country_df_top10_Confirmed=country_df_top10_Confirmed.sort_values(by=['Confirmed'])


country_df_top10_Deaths=country_df.sort_values(by=['Deaths'],ascending=False)
country_df_top10_Deaths=country_df_top10_Deaths.head(10)
country_df_top10_Deaths=country_df_top10_Deaths.sort_values(by=['Deaths'])


country_df_top10_Recovered=country_df.sort_values(by=['Recovered'],ascending=False)
country_df_top10_Recovered=country_df_top10_Recovered.head(10)
country_df_top10_Recovered=country_df_top10_Recovered.sort_values(by=['Recovered'])



country_df_top10_Active=country_df.sort_values(by=['Active'],ascending=False)
country_df_top10_Active=country_df_top10_Active.head(10)
country_df_top10_Active=country_df_top10_Active.sort_values(by=['Active'])


country_df_top10_Incident_Rate=country_df.sort_values(by=['Incident_Rate'],ascending=False)
country_df_top10_Incident_Rate=country_df_top10_Incident_Rate.head(10)
country_df_top10_Incident_Rate=country_df_top10_Incident_Rate.sort_values(by=['Incident_Rate'])

country_df_top10_Mortality_Rate=country_df.sort_values(by=['Mortality_Rate'],ascending=False)
country_df_top10_Mortality_Rate=country_df_top10_Mortality_Rate.head(10)
country_df_top10_Mortality_Rate=country_df_top10_Mortality_Rate.sort_values(by=['Mortality_Rate'])








global_flag="https://raw.githubusercontent.com/aks861999/COVIDASH/master/Country%20Flags/global.jpg"










fig_without_login={
    "layout": {



        #"template" : 'plotly_dark',
        "height":50,
        "width":820,
        "autosize":False,
        "showlegend":False,
        #"plot_bgcolor":'#000000',
        'color':'#BFFF00',
        'textAlign': 'center',
        "align":"center",



        "xaxis": {
            "visible": False
        },
        "yaxis": {
            "visible": False
        },
        "annotations": [
            {
                "text": "Please Login to unlock this plot dedicated to your location",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {
                    "size": 22
                },
                'textAlign': 'center','font-weight':'bold','font-family':'courgette',
                 #"template" : 'plotly_dark',
        "height":50,
        "width":820,
        "autosize":False,
        "showlegend":False,
        #"plot_bgcolor":'#000000',
        'color':'#BFFF00',
        "align":"center"




            }
        ]
    }
}







server = Flask(__name__)

config={
    "apiKey": "**********************************",
    "authDomain": "*************************",
    "databaseURL": "****************************",
    "projectId": "************",
    "storageBucket": "*********************",
    "messagingSenderId": "***********",
    "appId": "***************************************",
    "measurementId": "***********"
}

firebase1 = pyrebase.initialize_app(config)

auth = firebase1.auth()




@server.route('/reset_password/', methods=['GET', 'POST'])

def basic1():
	if request.method == 'POST':
		email = request.form['email']
		print(email)
		try:
			user=auth.send_password_reset_email(email)
			return render_template('reset.html',s='Please Check Your Inbox, An Email Has been Sent Shortly')
			
		except Exception as e:
			x=str(e)
			z=x.find(']')
			x=x[z+1:]
			t=json.loads(x)
			t=t['error']['message']
			if t == "EMAIL_NOT_FOUND":
				return render_template('reset.html',s='We regret that you have not registered yet')
			else:
				return render_template('reset.html',s='Uknown Error')
	return render_template('reset.html')















@server.route('/new=True/', methods=['GET', 'POST'])

def basic():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        print(email,password)
        try:
            user=auth.create_user_with_email_and_password(email,password)
            auth.send_email_verification(user['idToken'])
            no_of_users =firebase.get('/no_of_users/no_of_users/', '')
            no_of_users+=1
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("*************@gmail.com", "***********") 
            SUBJECT="New Member Registered"   
            TEXT=  "Hello !!!, Akash This is COVIDASH, A NEW USER HAS REGISTERED, Total No Of Users is "+str(no_of_users)
            message='Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s.sendmail("************", "************", message) 
            s.quit() 
            firebase.put('/no_of_users/',"no_of_users",no_of_users)
            return render_template('index.html',s='Please Check Your Inbox, Verification mail has been sent successfully')

        except Exception as e:
            x=str(e)
            z=x.find(']')
            x=x[z+1:]
            t=json.loads(x)
            t=t['error']['message']
            if t == 'WEAK_PASSWORD : Password should be at least 6 characters':
                return render_template('index.html',s='You Have Entered a weak password')
            elif t == 'INVALID_EMAIL':
                return render_template('index.html',s='You have entered an invalid email-ID')
            elif t=="EMAIL_EXISTS":
                return render_template('index.html',s='This mail ID is already registered')
            else:
                return render_template('index.html',s='Uknown Error')


    return render_template('index.html')

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    update_title="Please Wait . . . ."
)

app.title="COVIDASH by Akash"

lay=[search_navbar_layout,
corona_layout
    ]

app.layout = html.Div(
    lay,
    style={'textAlign': 'center','background-color':'#000000','width':'820'}
)

@app.callback(
    
[   
    Output("se_img","src"),        
    Output("text for indiv graph","children"),
    Output('fig for indiv graph','figure'),
    Output("sound", "children"),
     Output('logged-in','children'),
    Output('error','children'),
     Output('email', 'value'),
    Output('password', 'value'),
    Output("testing", "children"),
    Output("forgo", "children"),
    Output("to_reg", "children"),
    Output("logout", "children")],
      [Input('submit', 'n_clicks')],
      [State('email', 'value'),
       State('password', 'value'),
       State("testing", "children")])
def update_output(n_clicks, email, password,box):
    
    if n_clicks:
        
    
        import pyrebase

        config={
            "apiKey": "**********************************",
            "authDomain": "*************************",
            "databaseURL": "****************************",
            "projectId": "************",
            "storageBucket": "*********************",
            "messagingSenderId": "***********",
            "appId": "***************************************",
            "measurementId": "***********"
        }

        firebase = pyrebase.initialize_app(config)

        auth = firebase.auth()

        try:
            print(email,password)
            auth.sign_in_with_email_and_password(email, password)
            print("successful")
            
            text = 'You have successfully Logged in'
            tts = gTTS(text ) #Provide the string to convert to speech

            #print("all okay 1")

            language = 'zh'
            tts.save('m.mp3') #save the string converted to speech as a .wav file
            sound_filename ='m.mp3'
            
            encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

            #print("all okay 2")
            
            sound=html.Audio(src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                          controls=False,
                          autoPlay=True,
                          )

            #print("all okay 3")


            

            if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
                print(request.environ['REMOTE_ADDR'])
                print(request.environ)
                ip=request.environ['REMOTE_ADDR']

            else:
                print(request.environ['REMOTE_ADDR'])
                print(request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
                ip=request.environ['HTTP_X_FORWARDED_FOR']




            try:
                res=requests.get('https://ipinfo.io/'+ip+'?token=**************')
                data=res.json()
                print(data)
            except:
                res=requests.get('https://ipinfo.io/'+ip+'?token=**************')
                data=res.json()
                print(data)    

            email=email+" ("+data['city']+")"

            country_name_location=codes[data['country']]
            country_flag="https://raw.githubusercontent.com/aks861999/COVIDASH/master/Country%20Flags/"+data['country']+".jpg"


            ########### track user's location ############
            c_n=country_name_location

            print(c_n)


            stri="Visualisation of Corona-Trend for Different Cases in your Country "

            ler=len(confirmed_df)

            con=(confirmed_df.iloc[ler-1][c_n]-confirmed_df.iloc[ler-2][c_n])*100/confirmed_df.iloc[ler-2][c_n]
            con="%.2f" %con
            if(float(con))>0:
                con='+'+con
                

            det=(death_df.iloc[ler-1][c_n]-death_df.iloc[ler-2][c_n])*100/death_df.iloc[ler-2][c_n]
            det="%.2f" %det
            if(float(det))>0:
                det='+'+det

            rec=(recovered_df.iloc[ler-1][c_n]-recovered_df.iloc[ler-2][c_n])*100/recovered_df.iloc[ler-2][c_n]
            rec="%.2f" %rec
            if(float(rec))>0:
                rec='+'+rec

                
            d_con=(daily_new_df.iloc[ler-1][c_n]-daily_new_df.iloc[ler-2][c_n])*100/daily_new_df.iloc[ler-2][c_n]
            d_con="%.2f" %d_con
            if(float(d_con))>0:
                d_con='+'+d_con

            d_det=(daily_death_df.iloc[ler-1][c_n]-daily_death_df.iloc[ler-2][c_n])*100/daily_death_df.iloc[ler-2][c_n]
            d_det="%.2f" %d_det
            if(float(d_det))>0:
                d_det='+'+d_det
            
            d_rec=(daily_recov_df.iloc[ler-1][c_n]-daily_recov_df.iloc[ler-2][c_n])*100/daily_recov_df.iloc[ler-2][c_n]
            d_rec="%.2f" %d_rec
            if(float(d_rec))>0:
                d_rec='+'+d_rec


            #print("all okay 4")

            t1="Total Confirmed("+con+"%)"
            t2="Total Death("+det+"%)"
            t3="Total Recovered("+rec+"%)"
            t4="Daily New("+d_con+"%)"
            t5="Daily Death("+d_det+"%)"
            t6="Daily Recovered("+d_rec+"%)"

            

            fig = make_subplots(
                rows=2, cols=3,
                subplot_titles=(t1,t2,t3,t4,t5,t6))

            fig.add_trace(go.Scatter(x=confirmed_df['Date'], y=confirmed_df[c_n]),
                        row=1, col=1)

            
            fig.add_trace(go.Scatter(x=death_df['Date'], y=death_df[c_n]),
                        row=1, col=2)
            
            
            fig.add_trace(go.Scatter(x=recovered_df['Date'], y=recovered_df[c_n]),
                        row=1, col=3)


            fig.add_trace(go.Scatter(x=daily_new_df['Date'], y=daily_new_df[c_n]),
                        row=2, col=1)

            
            fig.add_trace(go.Scatter(x=daily_death_df['Date'], y=daily_death_df[c_n]),
                        row=2, col=2)
            
            
            fig.add_trace(go.Scatter(x=daily_recov_df['Date'], y=daily_recov_df[c_n]),
                        row=2, col=3)



            #print("all okay 5")

            

            fig.update_layout(template='plotly_dark',height=700,width=820,
                                autosize=False,
                                showlegend=False,
                                plot_bgcolor='#000000'
                    )

            fig.update_yaxes(showgrid=False,zeroline=False) 


            fig.update_xaxes(showgrid=False,
                        tickfont=dict(
                        family='Arial',
                        size=15,
                        color='rgb(255, 255, 0)',
                    )) 








            
            print(country_flag)


            return(country_flag,stri,fig,sound,email,"","","","","","","Logout")

        except:
            print("unsuccessful")
        
            text = 'You have entered invalid credentials,please check'
            tts = gTTS(text ) #Provide the string to convert to speech
            language = 'zh'
            tts.save('m.mp3') #save the string converted to speech as a .wav file
            sound_filename ='m.mp3'
            
            encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

            sound=html.Audio(src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                          controls=False,
                          autoPlay=True,
                          )
            return(global_flag,"",fig_without_login,sound,"","âš ï¸ Invalid Credentials âš ï¸","","",box,"Forgot Password ?","Register","")
    else:
        return(global_flag,"",fig_without_login,"","","","","",box,"Forgot Password ?","Register","")
 #######dash.no_update   
@app.callback(
    dash.dependencies.Output('input-on', 'value'),
    [dash.dependencies.Input('submit1', 'n_clicks')],
    [dash.dependencies.State('input-on', 'value')])
    
def fun1(n_clicks,value):
    if n_clicks==0:
        return("")
    
    firebase.post('/feedbacks/',value)
    
    return("")
        
##### Email CallBack ######


@app.callback(
    [dash.dependencies.Output('input-on-submit', 'value'),
     dash.dependencies.Output('container-button-basic', 'children')],
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])
def update_output(n_clicks, value):
    if n_clicks==0:
        return(value,"")
    
    
    
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("********@gmail.com", "************") 
    SUBJECT="Subscription Successful"   
    TEXT=  """Hello !! User, Your Email-ID Has Been Successfully Added in Our Database, Now You Are Good To Get Daily Update About COVID-19 Scenario"""
    message='Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    
    
    #yield("",'Verifying Your Email Address')
    
    
    try:
        s.sendmail("***********@gmail.com", value, message) 
        xj=0
        
    except:
        xj=1
    
    
    if(xj==0):
        s.quit() 
        firebase.post('/emails/',value)
        value=""
        return(value,'HOLA!! You Have Been Subscribed')
    else:
        return("",('âŒâš ï¸âŒ'+str(value)+' Is An Invalid Email Address âŒâš ï¸âŒ'))


@app.callback(
     Output('fig of world', 'figure'),
     [Input('select-country', 'value')]
)
def display_number(c_n):


    if c_n=='Global Result':


        t1="Confirmed Case"
        t2="Death Case"
        t3="Recovered Case"
        t4="Active Case"
        t5="Incident_Rate"
        t6="Mortality_Rate"

        #fig = make_subplots(rows=1, cols=2, shared_yaxes=False)
        

        fig = make_subplots(
            rows=2, cols=3,
            subplot_titles=(t1,t2,t3,t4,t5,t6),
            shared_yaxes=False
            )

    
####### country_df_top10_Deaths country_df_top10_Recovered 
# 
# country_df_top10_Active country_df_top10_Incident_Rate 
# country_df_top10_Mortality_Rate


        fig.add_trace(go.Bar(x=country_df_top10_Confirmed['Confirmed'], y=country_df_top10_Confirmed['Country_Region'],orientation='h',
                    marker=dict(color=country_df_top10_Confirmed['Confirmed'])),
              1, 1)
            

        fig.add_trace(go.Bar(x=country_df_top10_Deaths['Deaths'], y=country_df_top10_Deaths['Country_Region'],orientation='h',
                    marker=dict(color=country_df_top10_Deaths['Deaths'])),
              1, 2)

        fig.add_trace(go.Bar(x=country_df_top10_Recovered['Recovered'], y=country_df_top10_Recovered['Country_Region'],orientation='h',
                    marker=dict(color=country_df_top10_Recovered['Recovered'])),
              1, 3)



        fig.add_trace(go.Bar(x=country_df_top10_Active['Active'], y=country_df_top10_Active['Country_Region'],orientation='h',
                    marker=dict(color=country_df_top10_Active['Active'])),
              2, 1)
            

        fig.add_trace(go.Bar(x=country_df_top10_Incident_Rate['Incident_Rate'], y=country_df_top10_Incident_Rate['Country_Region'],orientation='h',
                    marker=dict(color=country_df_top10_Incident_Rate['Incident_Rate'])),
              2, 2)

        fig.add_trace(go.Bar(x=country_df_top10_Mortality_Rate['Mortality_Rate'], y=country_df_top10_Mortality_Rate['Country_Region'],orientation='h',
                    marker=dict(color=country_df_top10_Mortality_Rate['Mortality_Rate'])),
              2, 3)


        fig.update_layout(template='plotly_dark',height=1000,width=820,
                        autosize=False,
                        showlegend=False,
                        plot_bgcolor='#000000'
            )

        fig.update_yaxes(showgrid=False,zeroline=False) 
        fig.update_xaxes(showgrid=False,
                    tickfont=dict(
                    family='Arial',
                    size=20,
                    color='rgb(255, 255, 0)',
                )) 

        return(fig)

    else:



        ler=len(confirmed_df)

        con=(confirmed_df.iloc[ler-1][c_n]-confirmed_df.iloc[ler-2][c_n])*100/confirmed_df.iloc[ler-2][c_n]
        con="%.2f" %con
        if(float(con))>0:
            con='+'+con
            

        det=(death_df.iloc[ler-1][c_n]-death_df.iloc[ler-2][c_n])*100/death_df.iloc[ler-2][c_n]
        det="%.2f" %det
        if(float(det))>0:
            det='+'+det

        rec=(recovered_df.iloc[ler-1][c_n]-recovered_df.iloc[ler-2][c_n])*100/recovered_df.iloc[ler-2][c_n]
        rec="%.2f" %rec
        if(float(rec))>0:
            rec='+'+rec

            
        d_con=(daily_new_df.iloc[ler-1][c_n]-daily_new_df.iloc[ler-2][c_n])*100/daily_new_df.iloc[ler-2][c_n]
        d_con="%.2f" %d_con
        if(float(d_con))>0:
            d_con='+'+d_con

        d_det=(daily_death_df.iloc[ler-1][c_n]-daily_death_df.iloc[ler-2][c_n])*100/daily_death_df.iloc[ler-2][c_n]
        d_det="%.2f" %d_det
        if(float(d_det))>0:
            d_det='+'+d_det
        
        d_rec=(daily_recov_df.iloc[ler-1][c_n]-daily_recov_df.iloc[ler-2][c_n])*100/daily_recov_df.iloc[ler-2][c_n]
        d_rec="%.2f" %d_rec
        if(float(d_rec))>0:
            d_rec='+'+d_rec
        
        t1="Total Confirmed("+con+"%)"
        t2="Total Death("+det+"%)"
        t3="Total Recovered("+rec+"%)"
        t4="Daily New("+d_con+"%)"
        t5="Daily Death("+d_det+"%)"
        t6="Daily Recovered("+d_rec+"%)"
        

        fig = make_subplots(
            rows=2, cols=3,
            subplot_titles=(t1,t2,t3,t4,t5,t6))

        fig.add_trace(go.Scatter(x=confirmed_df['Date'], y=confirmed_df[c_n]),
                    row=1, col=1)

        
        fig.add_trace(go.Scatter(x=death_df['Date'], y=death_df[c_n]),
                    row=1, col=2)
        
        
        fig.add_trace(go.Scatter(x=recovered_df['Date'], y=recovered_df[c_n]),
                    row=1, col=3)


        fig.add_trace(go.Scatter(x=daily_new_df['Date'], y=daily_new_df[c_n]),
                    row=2, col=1)

        
        fig.add_trace(go.Scatter(x=daily_death_df['Date'], y=daily_death_df[c_n]),
                    row=2, col=2)
        
        
        fig.add_trace(go.Scatter(x=daily_recov_df['Date'], y=daily_recov_df[c_n]),
                    row=2, col=3)

        

        fig.update_layout(template='plotly_dark',height=700,width=820,
                            autosize=False,
                            showlegend=False,
                            plot_bgcolor='#000000'
                )

        fig.update_yaxes(showgrid=False,zeroline=False) 
        fig.update_xaxes(showgrid=False,
                    tickfont=dict(
                    family='Arial',
                    size=15,
                    color='rgb(255, 255, 0)',
                )) 

        return(fig)

if __name__ == "__main__":
    app.run_server(debug=False)