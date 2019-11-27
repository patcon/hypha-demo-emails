# Demo Mailcow Auth Proxy

The purpose of this app is to allow a custom restricted token to only
allow a small subset of actions within the MailCow API.

Specifically, this proxy currently only allows listing, editing, and
creating of aliases.

## Usage

```
# See: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-node-js-application-for-production-on-ubuntu-14-04
npm install pm2 -g
pm2 start server.js
```
