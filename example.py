from metwit import Metwit
from requests import HTTPError


# In order to get client id and client secret go to:
# http://metwit.com/developers/dashboard/
CLIENT_ID = '129380294'
CLIENT_SECRET = 'EoylKe-RXIc-D0Gfu0YR-ZzSuD0Xeax4kbcMPIfe'


metwit = Metwit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# this is an unauthenticated call
print metwit.weather.get(location_lat=45.45,
                         location_lng=9.18)

try:
    metwit.token_password(username='foo', password='bar')
except HTTPError as exc:
    print "can't authenticate", exc.response.text

# this is an authenticated call
metag = metwit.metags.post(
    dict(weather=dict(status="clear"),
         geo=dict(lat=45.45, lng=9.18),
         )
)

print metwit.resource(metag['user']['resource_uri']).get()
