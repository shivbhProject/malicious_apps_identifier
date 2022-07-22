from tkinter import N
from google_play_scraper import app
from google_play_scraper import search
from google_play_scraper import permissions


def search_apps(query):

    result = search(query, country="in", n_hits=100)
    return result


def get_permissions(app_id):

    result = permissions(app_id)
    return result


def filter_currency_developer(orglist):

    result = []
    for app in orglist:
        if(app['currency'] == 'INR'):
            if(app['developerEmail'] == '' or app['developerEmail'].endswith('@gmail.com') or app['developerEmail'].endswith('@hotmail.com') or app['developerEmail'].endswith('@yahoo.com')):
                result.append(app)
    return result

def filter_permissions(orglist):

    # result = []
    for app in orglist:
        # print(app['appId'])
        # print(type(app['appId']))
        get_permissions(app['appId'])

        # if(perms):
            # print(perms)
        # result.append(perms)
    # return result


keywords_file = open("keywords.txt", "r")
terms = keywords_file.read().splitlines()
appslist = []
for term in terms:
    for tempapp in search_apps(term):
        app_details = app(tempapp['appId'])
        appslist.append(app_details)

# filter_permissions(appslist)

# print(get_permissions("com.google.android.apps.translate"))


filtered_list = []


code_start = """
<html>
<head>
<title>Test</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<h1>Suspected Apps</h1>
<div class="mainParent">
"""

code_end = """
</div>
</body>
</html>
"""

# dynamic_content = f"<img src='{appslist[0]['icon']}' alt='Italian Trulli' >"
dynamic_content = ""

for apps in appslist:
    dynamic_content += f"""
    <div class="app">
        <div class="icon_box">
            <img src="{apps['icon']}">
        </div>
        <div class="details">
            <p><b>Title:</b> {apps['title']}</p>
            <p><b>Package Name:</b> {apps['appId']}</p>
            <p><b>Release Date:</b> {apps['released']}</p>
            <p><b>Installs:</b> {apps['installs']}</p>
            <p><b>Genre:</b> {apps['genre']}</p>
            <p><b>Summary:</b> {apps['summary']}</p>
            <p><b>Developer:</b> {apps['developer']}</p>
            <p><b>Developer ID:</b> {apps['developerId']}</p>
            <p><b>Developer EMail:</b> {apps['developerEmail']}</p>
            <p><b>Developer Website:</b> {apps['developerWebsite']}</p>
            <p><b>Developer Address:</b> {apps['developerAddress']}</p>
            <p><b>Ratings:</b> {apps['ratings']}</p>
            <p><b>Reviews:</b> {apps['reviews']}</p>
            <p><b>Description:</b> {apps['description']}</p>
        </div>
    </div>
"""




code = code_start + dynamic_content + code_end

file = open("test.html","w")
file.write(code)
file.close()
