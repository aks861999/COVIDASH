import pandas as pd
import numpy as np 
from apscheduler.schedulers.blocking import BlockingScheduler
from github import Github
from github import InputGitTreeElement
import re


sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=3)

def scheduled_job():



    def do_fuzzy_search(country):
        try:
            result = pycountry.countries.search_fuzzy(country)
        except Exception:
            return np.nan
        else:
            return result[0].alpha_2







    ##################################
    ############GitHUB################

    death_df =  pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')




    confirmed_df.drop(columns=['Lat','Long'],axis=1,inplace=True)
    death_df.drop(columns=['Lat','Long'],axis=1,inplace=True)
    recovered_df.drop(columns=['Lat','Long'],axis=1,inplace=True)
    country_df.drop(columns=['People_Tested','People_Hospitalized','Lat','Long_','Last_Update','UID'],axis=1,inplace=True)




    confirmed_df=confirmed_df.groupby(['Country/Region']).sum()
    death_df=death_df.groupby(['Country/Region']).sum()
    recovered_df=recovered_df.groupby(['Country/Region']).sum()



    confirmed_df=confirmed_df.reset_index()
    death_df=death_df.reset_index()
    recovered_df=recovered_df.reset_index()

    dfg=country_df['Country_Region']
    dfg=list(dfg)


    dfg.remove('MS Zaandam')
    dfg.remove('Diamond Princess')

    olo={}
    for i in dfg:
        olo[i]=do_fuzzy_search(i)

    olo['Burma']='MMR'
    olo['Congo (Brazzaville)']='COG'
    olo['Congo (Brazzaville)']='COD'
    olo['Korea, South']='KOR'
    olo['Laos']='LA'
    olo['Taiwan*']='TWN'
    olo['West Bank and Gaza']='PS'



    country_df.sort_values(by=['Confirmed'],ascending=False,inplace=True)
    country_df=country_df.reset_index()
    country_df.drop(columns=['index'],inplace=True)
    #country_df=country_df.head(10)



    l=country_df['Country_Region']
    l=list(l)

    l.remove('MS Zaandam')
    l.remove('Diamond Princess')

    """
    confirmed_df=confirmed_df.loc[confirmed_df['Country/Region'].isin(l) ]
    death_df=death_df.loc[death_df['Country/Region'].isin(l) ]
    recovered_df=recovered_df.loc[recovered_df['Country/Region'].isin(l) ]
    """

    confirmed_df=pd.melt(confirmed_df,id_vars='Country/Region',var_name='Date',value_name='No. Of Confirmed Cases')
    death_df=pd.melt(death_df,id_vars='Country/Region',var_name='Date',value_name='No. Of Death Cases')
    recovered_df=pd.melt(recovered_df,id_vars='Country/Region',var_name='Date',value_name='No. Of Recovered Cases')





    confirmed_df=confirmed_df.pivot(index='Date', columns='Country/Region', values='No. Of Confirmed Cases')

    death_df=death_df.pivot(index='Date', columns='Country/Region', values='No. Of Death Cases')

    recovered_df=recovered_df.pivot(index='Date', columns='Country/Region', values='No. Of Recovered Cases')




    confirmed_df=confirmed_df.reset_index()
    death_df=death_df.reset_index()
    recovered_df=recovered_df.reset_index()





    death_df['Date']=pd.to_datetime(death_df['Date'])
    confirmed_df['Date']=pd.to_datetime(confirmed_df['Date'])
    recovered_df['Date']=pd.to_datetime(recovered_df['Date'])



    confirmed_df.sort_values(by=['Date'],inplace=True)
    death_df.sort_values(by=['Date'],inplace=True)
    recovered_df.sort_values(by=['Date'],inplace=True)



    l1=[]
    l1.append('Date')
    for i in range(len(country_df['Country_Region'])):
        l1.append(country_df['Country_Region'][i])





    confirmed_df=confirmed_df[l1]
    death_df=death_df[l1]
    recovered_df=recovered_df[l1]



    osama=list(confirmed_df.loc[0])
    osama_d=list(confirmed_df['Date'])
    daily_new_df=confirmed_df.diff()
    daily_new_df.loc[0]=osama
    daily_new_df['Date']=osama_d

    osama=list(recovered_df.loc[0])
    osama_d=list(recovered_df['Date'])
    daily_recov_df=recovered_df.diff()
    daily_recov_df.loc[0]=osama
    daily_recov_df['Date']=osama_d

    osama=list(death_df.loc[0])
    osama_d=list(death_df['Date'])
    daily_death_df=death_df.diff()
    daily_death_df.loc[0]=osama
    daily_death_df['Date']=osama_d




    #confirmed_df,death_df,recovered_df,daily_new_df,daily_death_df,daily_recov_df


    confirmed_df.to_csv('confirmed_df.csv')
    death_df.to_csv('death_df.csv')
    recovered_df.to_csv('recovered_df.csv')
    daily_new_df.to_csv('daily_new_df.csv')
    daily_death_df.to_csv('daily_death_df.csv')
    daily_recov_df.to_csv('daily_recov_df.csv')




    user = "XXXXXXXXX"
    password = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    g = Github(user,password)
    repo = g.get_user().get_repo('COVIDASH')



    commit_message = 'inti'
    master_ref = repo.get_git_ref('heads/master')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)
    element_list = list()


    l=[r'confirmed_df.csv',r'death_df.csv',r'recovered_df.csv',r'daily_new_df.csv',r'daily_death_df.csv',r'daily_recov_df.csv']
    for i in range(len(l)):
        file_name ='covidash_backend_files/'+l[i]
        with open(l[i],errors='ignore') as input_file:
            data = input_file.read()   
        file = repo.get_contents("covidash_backend_files/"+l[i])
        repo.update_file("covidash_backend_files/"+l[i], commit_message,data, file.sha)

sched.start()
