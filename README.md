# Demo: Email config syncer

The purpose of this repo is to demo:

- a script for syncing a configuration file describing our email aliases, [`sync-email-aliases.py`](/sync-email-aliases.py). This could be the full set, or a subset of the whole. It could also be public or private. The config file could be managed via pull request.
- a small proxy app to restrict access to the mailserver API, so that only a subset of actions and domains can be modified via the API.

## Script

### Usage

```
pipenv install
pipenv run python parse-email-config.py email-aliases.yml
```

## Proxy App

### Usage

```
git clone https://github.com/patcon/hypha-demo-emails && cd hypha-demo-emails
cp proxy-app/sample.env proxy-app/.env
vim proxy-app/.env

heroku create MY-APP-NAME
heroku config:set $(cat proxy-app/.env)
heroku buildpacks:set https://github.com/negativetwelve/heroku-buildpack-subdir
git push heroku master
```
