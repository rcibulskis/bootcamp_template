def index():
    return dict()


def get_data():
    import simutils as su
    import pandas as pd
    import numpy as np
    import os
    import json

    wd = os.getcwd()
    privateDir = wd + '/applications/bootcamp_template/private/data/dataset_1/'

    df = su.read_csv(in_path=privateDir + 'Video_Games_Sales_as_at_22_Dec_2016.csv',
                     sep=',', weight_col='', verbose=False)

    publisher_selected = request.vars

    publisher = str(publisher_selected['publisherselected'])

    if publisher == "Sony":
        publisher = "Sony Computer Entertainment"
    if publisher == "Microsoft":
        publisher = "Microsoft Game Studios"

    systems_array = df.platform.loc[df.publisher == publisher].unique()

    df_temp = df.loc[df['platform'].isin(systems_array)]

    output = {}

    output = df_temp.groupby('platform')[
        ['global_sales', 'na_sales']].sum().to_dict()

    output2 = df_temp.groupby(
        'genre')[['critic_score']].mean().dropna().to_dict()

    output3 = df_temp.groupby(
        'rating')[['critic_score']].mean().dropna().to_dict()

    full_dict = json.dumps(dict(sales=output, genre=output2, ratings=output3))

    return full_dict


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
