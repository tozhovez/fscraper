import requests
import json

ACCESS_TOKEN = "EAAEocXFQnlMBALHENQtLvSQv3wv2BuTZBvoRHBCfSylwnvgqQyzZCZBQVfSBmjhkfeDuEYb4Kp21ZB4XFiABxaxRSZAprbGj7IE4xbd0ZCkrzbLQkHZBBUjswEseMS4l2ImfPTOOnxIVZCak3eFS888XT9aRpZBbDCg0VyAtpqufWrZA3ke931FFB6oAs0icKEmY4Bn6Js5QhKp2Ljh2sXZCMdo"
URL = f"https://graph.facebook.com/v7.0/natgeo/feed?access_token={ACCESS_TOKEN}"
max_posts = 500

def pages(url):
    receive = requests.get(url)
    data = receive.json()
    data = data["data"]
    paging = data["paging"]["next"]
    posts = {}
    for i in data:
        posts[i["id"]] = i
    return posts, paging


def scraper(n=max_posts, url=URL):
    data = {}
    while True:
        posts, next_page = pages(url)
        data.update(posts)
        if len(data.keys()) >= n:
            break
        url = next_page
    return data.values()

if __name__ == "__main__":
    result = scraper()
    for i in result:
        print(i)
