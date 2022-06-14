"""
All the functions are here.

"""

from packages import data
from json import loads

d = loads(data)


def download(app_name):
    import requests as rq
    from sys import exit as sysexit

    app_url = None

    for package in d["packages"].values():
        if package["name"] == app_name:
            app_url = package["url"]

    if app_url is None:
        print(f"Fatal Error: Failed to find package '{app_name}'")
        sysexit(1)

    try:
        r = rq.get(app_url, stream=True)
    except rq.exceptions.ConnectionError:
        print("Fatal Error: Cannot connect to the Internet. Check your Internet connection and try a few moments later.")
        sysexit(1)

    with open(app_name + package["file_extension"], "wb") as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)


def _make_array():
    global app_list
    app_list = []
    for package in d["packages"].values():
        app_list += [package["name"]]


def search(app_name):
    _make_array()
    for app in app_list:
        if app == app_name:
            print(f"Package '{app_name}' found. Use `crisp download {app_name}` to download it.")
            return

    from sys import exit as sysexit
    print(f"Fatal Error: Package {app_name} not found.")
    sysexit(1)


def show_all():
    _make_array()
    for app in app_list:
        print(app)
