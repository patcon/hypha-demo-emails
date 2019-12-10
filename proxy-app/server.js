var argo = require('argo');

var BASE_URL = process.env.MAILCOW_BASE_URL || 'https://private-anon-1c4eb966d2-mailcow.apiary-mock.com';
var MAILCOW_TOKEN_FULL = process.env.MAILCOW_TOKEN_FULL || 'xxxxxxxxxxxx';
var HYPHA_TOKEN_RESTRICTED = process.env.HYPHA_TOKEN_RESTRICTED || '1234567890';

var restricted_token = function(handle) {
  handle('request', function(env, next) {
    if (env.request.headers['x-api-key'] == HYPHA_TOKEN_RESTRICTED) {
      console.log("Successful X-API-Key header for restricted access. Passing through with full token.";
      env.request.headers['x-api-key'] = MAILCOW_TOKEN_FULL;
    } else {
      console.log("Incorrect or missing X-API-Key header. Passing through without special access.";
    }
    console.log("Proxying request to " + BASE_URL;);
    next(env);
  })
}

argo()
  .target(BASE_URL)
  // list
  .get('^/api/v1/get/alias/(all|\\d+)', restricted_token)
  // add or edit
  .post('^/api/v1/(edit|add)/alias', restricted_token)
  .listen(process.env.PORT || 1337)
