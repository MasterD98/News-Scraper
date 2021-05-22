# News-Scraper

Getting Started

1.Installation

1.1.Create an environment

Create a project folder and a venv folder within:

Windows: \
mkdir myproject \
cd myproject \
py -3 -m venv venv

macOS/Linux: \
$ mkdir myproject \
$ cd myproject \
$ python3 -m venv venv

1.2 Activate the environment

Before you work on your project, activate the corresponding environment:

Windows: \
venv\Scripts\activate

macOS/Linux: \
$ . venv/bin/activate

Your shell prompt will change to show the name of the activated environment.
1.3 Install Flask

Within the activated environment, use the following command to install Flask:

$ pip install Flask

1.4 Install Requests and Beautiful Soup 

$ pip install requests \
$ pip install beautifulsoup4 

2.Deploy website locally

Powershell: \
$env:FLASK_APP = "server.py" \
flask run 

CMD: \
set FLASK_APP=server \
flask run 

Bash:
$ export FLASK_APP=server \
$ flask run 

website is Running on http://127.0.0.1:5000/


