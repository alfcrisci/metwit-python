from .rest import Resource, RestApi


class Metwit(RestApi):
    #base_url = "https://api.metwit.com/"
    #token_url = 'https://api.metwit.com/token/'
    dialog_url = "https://metwit.com/oauth/authorize/"
    base_url = "http://127.0.0.1:8000/"
    token_url = 'http://127.0.0.1:8000/token/'

    weather = Resource('/v2/weather/')
    metags = Resource('/v2/metags/')
    users = Resource('/v2/users/')
