from flask import Flask
import Scraper
app=Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    content=str(Scraper.create_custom_hn())
    return content