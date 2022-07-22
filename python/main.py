from google_play_scraper import app
from google_play_scraper import search
from google_play_scraper import permissions


def search_apps(query):

    result = search(query, country="in", n_hits=200)
    return result


def get_permissions(app_id):

    result = permissions(app_id)
    return result


def filter_currency_developer(orglist):

    result = []
    for app in orglist:
        if(app['currency'] == 'INR'):
            if(app['developer'] == '' or app['developer'].endswith('@gmail.com') or app['developer'].endswith('@hotmail.com') or app['developer'].endswith('@yahoo.com')):
                result.append(app)
    return result

def filter_permissions(orglist):

    # result = []
    for app in orglist:
        # print(app['appId'])
        # print(type(app['appId']))
        perms = get_permissions(app['appId'])
        # if(perms):
            # print(perms)
        # result.append(perms)
    # return result


keywords_file = open("keywords.txt", "r")
terms = keywords_file.read().splitlines()
appslist = []
for term in terms:
    for app in search_apps(term):
        appslist.append(app)

filter_permissions(appslist)

# print(get_permissions("com.google.android.apps.translate"))

filtered_list = []




