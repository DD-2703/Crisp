"""
All the functions are located here.
"""

import requests as rq
import exceptions as exp
from packages import package_names, package_urls, package_extensions


def download(app: str):
    if app not in package_names:
        raise exp.CrispUnknownPackageError(f"Could not find package {app} in bucket. Please recheck the spelling.")

    print(f"[INFO]   Found package {app}")
    index = package_names.index(app)
    url = package_urls[index]
    extension = package_extensions[index]

    try:
        r = rq.get(url, stream=True)
    except rq.exceptions.ConnectionError:
        raise exp.CrispConnectionError("Could not connect to the Internet. Please try again in a few moments.")

    print("[INFO]   Starting Download")

    packet: int = 0

    with open(app + extension, "wb") as f:
        for chunk in r.iter_content(1024):
            if chunk:
                packet += 1
                print(f"[INFO]   Downloading packet {str(packet)}")
                f.write(chunk)

    print("\nDownloaded successfully.")
    return 0


def download32():
    raise exp.CrispNotImplementedError("32 bit applications are not implemented yet.")


def search(app):
    print(f"[INFO]  Searching for package {app} in {len(package_names)} packages...")
    if app not in package_names:
        raise exp.CrispUnknownPackageError(f"Not found package {app}")
    print(f"Found package {app}. Use the download command to download the package.\n")
    return 0


def show_all():
    print("The following items are in the crisp bucket.")
    for _ in package_names:
        print(_)
    print("")
    return 0
