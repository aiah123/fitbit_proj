import base64
import configparser
import requests

# fitbit tutorial to create the right urls to get tokens:
# https://dev.fitbit.com/apps/oauthinteractivetutorial

################### Implicit grant flow (doesn't use client secret) ##############################
# authorization url (must be done from the browser when logged in):
# https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=<client_id>&redirect_uri=https%3A%2F%2Fwww.github.com%2Fcallback&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800
    # https://www.fitbit.com/oauth2/authorize?
    # response_type=token&
    # client_id=<client id>&
    # redirect_uri=https%3A%2F%2Fwww.github.com%2Fcallback&
    # scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&
    # expires_in=604800
#
# response to the above url is a redirect to the callback defined by the app. The redirect:
# https://github.com/callback#access_token=<access_token>&user_id=<user_id>&scope=nutrition+heartrate+activity+social+profile+sleep+weight+settings+location&token_type=Bearer&expires_in=464568
    # https://github.com/callback#
    # access_token=<access_token>&
    # user_id=<user_id>
    # scope=nutrition+heartrate+activity+social+profile+sleep+weight+settings+location&
    # token_type=Bearer&
    # expires_in=464568
#
# the access token will be used in the api call. Api call will look like the below curl command.
# Authorization header will user the access_token from the redirect url:
    # curl -i
    # -H "Authorization: Bearer <access_token>
    # https://api.fitbit.com/1/user/-/profile.json


################### Authorization Code Flow ##############################
# authorization url: (must be done from the browser when logged in):
    # https://www.fitbit.com/oauth2/authorize?
    # response_type=code&
    # client_id=<client id>&
    # redirect_uri=https%3A%2F%2Fwww.github.com%2Fcallback&
    # scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&
    # expires_in=604800
# That url will redirect to the callback url with a code as parameter
# https://github.com/callback?code=<code>#_=__
# The code is used to create the token request. The authorization header uses the client id and the client secret
# in base 64:
    # secret = CLIENT_ID + ":" + CLIENT_SECRET
    # b64secret = base64.b64encode(secret.encode())
# The request:
    # curl	-X POST -i
    # -H 'Authorization: Basic MjJDWFlHOmE0NTNkNTUyNzliNDBlODcyNTMyYzliN2Y5NzZkNTg0'
    # -H 'Content-Type: application/x-www-form-urlencoded'
    # -d "clientId=<client_id>"
    # -d "grant_type=authorization_code"
    # -d "redirect_uri=https%3A%2F%2Fwww.github.com%2Fcallback"
    # -d "code=8cd2f62cbc281add91c2fa7edc5ef65c3c77bd6f"
    # https://api.fitbit.com/oauth2/token
# the response will contain the access token and then the api can be used
from src.ConfigReader import ConfigReader

class FitbitAuthorization:

    def __init__(self, config):
        self.token = 0
        #config = ConfigReader()

        # TODO config file should be encrypted
#        self.client_id = config['client_id']
#        self.client_secret = config['client_secret']
#        self.redirect_url = config['redirect_url']
        self.access_token = config.get_access_token()

    def get_access_token(self):
        return self.access_token

    # create the authorization. doesn't work when not logged in
    # def get_acces_token_with_code_authorization_flow(self):
    #     secret = self.client_id + ":" + self.secret
    #     b64secret = base64.b64encode(secret.encode())
    #     # Pass encoded ID and Secrets to header and decode
    #     header = {'Authorization': 'Basic ' + b64secret.decode()}
    #
    #     # https://www.fitbit.com/login?disableThirdPartyLogin=true&redirect=%2Foauth2%2Fauthorize%3Fclient_id%3D<clinet_id>%26redirect_uri%3Dhttps%253A%252F%252Fwww.github.com%252Fcallback%26response_type%3Dcode%26scope%3Dactivity%2Bnutrition%2Bheartrate%2Blocation%2Bnutrition%2Bprofile%2Bsettings%2Bsleep%2Bsocial%2Bweight%26state
    #     # https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=22942C&redirect_uri=http%3A%2F%2Fexample.com%2Fcallback&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight
    #     resp_type = 'token'
    #     scope = 'activity nutrition heartrate location nutrition profile settings sleep social weight'
    #     params = {'response_type': resp_type, 'client_id': self.client_id,
    #               'redirect_uri': self.redirect_url, 'scope': scope}
    #     response = requests.post('https://www.fitbit.com/oauth2/authorize', data=params, headers=header)
    #     print(response.text)
    #
    #

# def get_token():
#     headers = {'Authorization': 'Basic ' + access_token, 'Content-Type': 'application/x-www-form-urlencoded'}
#     grant_type = 'authorization_code'
#     code = '4f2275f76b6f2fcbd57c4b515ea4c12c644b3e6d'
#     token_url = "https://api.fitbit.com/oauth2/token"
#     params = {'clientId': CLIENT_ID, 'grant_type': grant_type, 'redirect_uri': redirect_url, 'code': code}
#     res = requests.post(token_url, params, headers=headers)
#     print(res.request.url)
#     print(res.content)

