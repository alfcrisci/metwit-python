Metwit API for Python
=====

A Python client for [Metwit weather API](http://metwit.com/developers/).

It's as simple as this:

    from metwit import Metwit

    weather = Metwit.weather.get(location_lat=45.45,
                                 location_lng=9.18)

Good! Hope it's not raining.

    # weather[0] is the real-time weather in a location
    if weather[0]['weather']['status'] == 'rainy':
        print 'Better take my umbrella with me'

What if I want to authenticate my app?

    from metwit import Metwit

    CLIENT_ID = '111111'
    CLIENT_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    metwit = Metwit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    metwit.token_client_credentials()

    metwit.weather.get(location_lat=45.45, location_lng=9.18)

Fine. This will allow me to use credits from my plan and make more API calls.

Posting data
-----

Metwit API plans come with a number of `weather` calls you can make daily. You can overcome the limit by posting data. Every time you post meaningful data to Metwit, your limits will extend.

How? Post a `Metag`:

    metag = {
        'geo': {
            'lat': 45.45,
            'lng': 9.18,
        }
        'weather': {
            'status': 'rainy',
        },
    }
    metwit.metags.post(metag)

`geo` is the only mandatory field. As an overview, a `Metag` object may contain weather status, measured data (temperature, pressure, humidity, etc) and sensory info (I feel hot/warm/etc). Detailed reference is available on the [Metwit API documentation page for metags](http://metwit.com/developers/docs/resources/metags/).

Reference
----

All you need is the `Metwit` class.

### class **`metwit.Metwit`**`([client_id], [client_secret], [access_token], [refresh_token])`

*`client_id`* and *`client_secret`* come from the [Developer Dashboard](https://metwit.com/developers/dashboard/). You only need those if you registered an application. You shouldn't include a client secret if you are going to distribute the code of your application (as opposed to application code hosted on a server, or running on your machine, for example).

If you stored an *`access_token`* (and *`refresh_token`*) elsewhere you can pass them to the constructor, otherwise you can make unauthenticated calls, or obtain a token with `get_token()` or one of the shortcut methods.

#### `Metwit.metags`
#### `Metwit.weather`
#### `Metwit.users`
These are the API resources. You can `.get()` and `.post()` these, or get
individual items with the subscript operator (e.g. `Metwit.metag['123456'].get()`).

#### `Metwit.get_token(grant_type, **kwargs)`
Calls the token endpoint to obtain an access token. The `Metwit` object stores the access token for you, so API calls after this will be authenticated.

#### `Metwit.dialog(redirect_uri, [scope], [state], [implicit])`
Returns the URL for the OAuth 2.0 authorization dialog. If you want to act in behalf of the users, you should redirect their browser to this URL.

#### `Metwit.token_auth_code(code, redirect_uri)`
This is a shortcut to `get_token()`. Use it when your users go through the
authorization dialog and you get the authorization code back.

#### `Metwit.token_client_credentials()`
This is a shortcut to `get_token()`. Use it when you just want to query the
weather and don't need to act in behalf of a user.

#### `Metwit.token_password(username, password, [scope])`
This is a shortcut to `get_token()`. Use it when you have the username and
the password of a Metwit user.

#### `Metwit.resource(uri)`
Use this when you have the URI of a resource and need to access it. E.g.
`metwit.resource('/v2/metags/123456/').get()`.
