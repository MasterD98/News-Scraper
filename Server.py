from flask import Flask
from flask import render_template
import Scraper
app=Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    news=Scraper.create_custom_hn()
    return render_template('index.html', news=news  )