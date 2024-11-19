import requests
from bs4 import BeautifulSoup as bs4


def img_load_flag_emblem(country_name):
    imgs = {
        "flag": "",
        "emblem": "",
    }
    URL = f"https://en.wikipedia.org/wiki/{country_name}"
    req = requests.get(URL)

    soup = bs4(req.text, "html.parser")

    p_imgs = soup.find_all("img")
    for img in p_imgs:
        if img.get("alt") and img:
            if img["alt"] == f"Flag of {country_name}":
                imgs["flag"] = img["src"].replace("//", "")
            if img["alt"] == f"Emblem of {country_name}":
                imgs["emblem"] = img["src"].replace("//", "")
    return imgs
