def index():
    return dict()


def get_data():
    import simutils as su
    import pandas as pd
    import numpy as np
    import os

    wd = os.getcwd()
    privateDir = wd + '/applications/bootcamp_template/private/data/dataset_1/'

    df = su.read_csv(in_path=privateDir + 'Video_Games_Sales_as_at_22_Dec_2016.csv', sep=',', weight_col='', verbose=False)

    publisher = 'Nintendo'

    systems_array = df.platform.loc[df.publisher == publisher].unique()

    output = {}
    for x in range(0,len(systems_array)):

        output[systems_array[x]] = {}

        output[systems_array[x]]['Global_Sales'] = df.global_sales.loc[df['platform'] == systems_array[x]].sum()
        output[systems_array[x]]['NA_Sales'] = df.na_sales.loc[df['platform'] == systems_array[x]].sum()

    output = pd.DataFrame(output).to_json()

    return output

def get_data2():
    import simutils as su
    import pandas as pd
    import numpy as np
    import os

    wd = os.getcwd()
    privateDir = wd + '/applications/bootcamp_template/private/data/dataset_1/'

    df = su.read_csv(in_path=privateDir + 'Video_Games_Sales_as_at_22_Dec_2016.csv', sep=',', weight_col='', verbose=False)

    ratings_array = df.rating.dropna().unique()

    publisher = 'Nintendo'

    #critic score past 2005

    temp_df = df[df['year_of_release'] >= 2005]
    temp_df = df[df['publisher'] == publisher]
    temp_df = temp_df['critic_score'].dropna()

    output2 = {}
    
    for x in range(0,len(ratings_array)):

        output2[ratings_array[x]] = {}

        output2[ratings_array[x]]["Mean_Ratings"] = df.critic_score.loc[df['rating'] == ratings_array[x]].mean()

    #import ipdb;ipdb.set_trace()
    output2 = pd.DataFrame(output2).to_json()



    return output2

def get_data3():
    import simutils as su
    import pandas as pd
    import numpy as np
    import os

    wd = os.getcwd()
    privateDir = wd + '/applications/bootcamp_template/private/data/dataset_1/'

    df = su.read_csv(in_path=privateDir + 'Video_Games_Sales_as_at_22_Dec_2016.csv', sep=',', weight_col='', verbose=False)

    genre_array = df.genre.dropna().unique()

    publisher = 'Nintendo'

    #critic score past 2005

    temp_df = df[df['year_of_release'] >= 2005]
    temp_df = df[df['publisher'] == publisher]
    temp_df = temp_df['critic_score'].dropna()

    output3 = {}
    
    for x in range(0,len(genre_array)):

        output3[genre_array[x]] = {}

        output3[genre_array[x]]["Mean_Ratings"] = df.critic_score.loc[df['genre'] == genre_array[x]].mean()

    #import ipdb;ipdb.set_trace()
    output3 = pd.DataFrame(output3).to_json()
    
    return output3

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()





