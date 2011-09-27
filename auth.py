#!/usr/bin/env python
# coding:utf-8

import urlparse
import oauth.oauth as oauth
import logging
import time
import ConfigParser
import httplib

logging.basicConfig(level=0,format="%(asctime)s %(levelname)s %(message)s")

class BaseOAuthClient(oauth.OAuthClient):
    """Base OAuth Client Wrapper"""

    def __init__(self, server, port=httplib.HTTP_PORT, request_token_url='', access_token_url='', authorization_url=''):
        self.server = server
        self.port = port
        self.request_token_url = request_token_url
        self.access_token_url = access_token_url
        self.authorization_url = authorization_url
        self.connection = httplib.HTTPConnection("%s:%d" % (self.server, self.port))

    def fetch_request_token(self, oauth_request):
        # via headers
        # -> OAuthToken
        self.connection.request(oauth_request.http_method, self.request_token_url, headers=oauth_request.to_header())
        response = self.connection.getresponse()
        print response.read()
        return oauth.OAuthToken.from_string(response.read())

    def fetch_access_token(self, oauth_request):
        # via headers
        # -> OAuthToken
        self.connection.request(oauth_request.http_method, self.access_token_url, headers=oauth_request.to_header())
        response = self.connection.getresponse()
        return oauth.OAuthToken.from_string(response.read())

    def authorize_token(self, oauth_request):
        # via url
        # -> typically just some okay response
        self.connection.request(oauth_request.http_method, oauth_request.to_url())
        response = self.connection.getresponse()
        return response.read()

    def access_resource(self, oauth_request):
        # via post body
        # -> some protected resources
        headers = {'Content-Type' :'application/x-www-form-urlencoded'}
        self.connection.request('POST', RESOURCE_URL, body=oauth_request.to_postdata(), headers=headers)
        response = self.connection.getresponse()
        return response.read()

def do_oauth(weibo_type):
    config=ConfigParser.ConfigParser()
    config.read('config.ini')

    #get config

    server=config.get(weibo_type,'server')
    port=config.getint(weibo_type,'port')
    request_token_url=config.get(weibo_type,'request_token_url')
    authorize_url=config.get(weibo_type,'authorize_url')
    access_token_url=config.get(weibo_type,'access_token_url')
    app_key=config.get(weibo_type,'app_key')
    app_secret=config.get(weibo_type,'app_secret')
    callback_url=config.get('common','callback_url')

    #setup
    client = BaseOAuthClient(server, port, request_token_url, access_token_url, authorize_url)
    consumer = oauth.OAuthConsumer(app_key, app_secret)
    signature_method_plaintext = oauth.OAuthSignatureMethod_PLAINTEXT()
    signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, callback=callback_url, http_url=client.request_token_url)
    oauth_request.sign_request(signature_method_hmac_sha1, consumer, None)

    print 'REQUEST (via headers)'
    print 'parameters: %s' % str(oauth_request.parameters)
    token = client.fetch_request_token(oauth_request)
    print 'GOT'
    print 'key: %s' % str(token.key)
    print 'secret: %s' % str(token.secret)
    print 'callback confirmed? %s' % str(token.callback_confirmed)