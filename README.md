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
heroku create my-proxy-app
heroku buildpacks:set https://github.com/negativetwelve/heroku-buildpack-subdir
git push heroku master
```
