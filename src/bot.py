import pyjokes

from twython import Twython

from auth import *

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def main():
    joke = pyjokes.get_joke()
    twitter.update_status(status=joke)

if __name__ == '__main__':
    main()
