# twitter-search
Simple twitter serach engine. Search top popular tweets.

##### Technology and libraries used:

1. [Python 3.6.6](https://www.python.org/)
2. [Django 2.1](https://www.djangoproject.com/)
3. [Python-twitter](https://github.com/bear/python-twitter)

#### Create twitter app
[Twitter app](https://apps.twitter.com/)
Get the access token and consumer key.
Add these keys in [settings file](https://github.com/sarvan-nov14/twitter-search/blob/master/twitter_search/settings.py#L124)

##### Setps to install
* Install pip
```console
  $ sudo apt-get install python3-pip
```
* Install virtualenv
```console
  $ sudo pip3 install virtualenv
```
* Create virtualenv
```console
  $ virtualenv -p python3 <envname>
```
* Go to created envname activate the virtualenv by entering following command
```console
  $ source bin/activate
```
* Now install the dependencies
```console
  $ pip install -r /path/to/requirements.txt
```
* Move to project root dir, run the server
```console
  $ python manage.py runserver
```
 
