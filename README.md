# Scaling a Flask Application with Memcache

This is an example of a Flask app that uses the [MemCachier add-on](https://addons.heroku.com/memcachier) on [Heroku](http://www.heroku.com/). A running version of this app can be found [here](https://mighty-beyond-15012.herokuapp.com).

Inspired by: [this article](https://devcenter.heroku.com/articles/flask-memcache).
Credit goes to: [memcachier](https://github.com/memcachier/examples-flask).

## Deploy to Heroku

Deploy this app on Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Running Locally

Run the following commands to get started running this app locally:

```sh
$ git clone https://github.com/dungnv2602/flask_memcache.git
$ cd flask_memcache
$ mkdir instance
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ FLASK_APP=task_list flask db upgrade
(venv) $ FLASK_APP=task_list FLASK_ENV=development flask run
```

Then visit `http://localhost:5000` to checkout locally.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/dungnv2602/flask_memcache.git
$ cd flask_memcache
$ heroku create
Creating app... done, ⬢ mighty-beyond-15012
https://mighty-beyond-15012.herokuapp.com/ | https://git.heroku.com/mighty-beyond-15012.git
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku addons:create memcachier:dev
$ heroku config:set FLASK_APP=task_list
$ heroku config:set SECRET_KEY="`< /dev/urandom tr -dc 'a-zA-Z0-9' | head -c16`"
$ git push heroku master
$ heroku open
```

## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).
