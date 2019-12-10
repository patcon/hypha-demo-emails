# Demo: Email config syncer

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
heroku buildpacks:set https://github.com/Pagedraw/heroku-buildpack-select-subdir
git push heroku master
```
