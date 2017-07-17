import json
import requests
from fb_THUMBot import key
from pprint import pprint

class Facebook_API():
    FANPAGE_ACCESS_TOKEN = key.Fanpage_Access_Token

    def post_facebook_message(self, fbid, recevied_message):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + self.FANPAGE_ACCESS_TOKEN
        response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": recevied_message}})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        if status.status_code != 200:
            print "Error ", status.status_code, fbid, recevied_message
        pprint(status.json())

    def get_info_user(self, fbid):
        get_info_url = 'https://graph.facebook.com/v2.8/'
        params = {
            'id': fbid,
            'access_token': self.FANPAGE_ACCESS_TOKEN,
        }
        r = requests.get(get_info_url, params)
        if r.status_code == 200:
            response_data = r.json()
            if response_data.has_key('name'):
                return {
                    'fbid': fbid,
                    'name': response_data['name'],
                    'is_female': True if response_data['gender'] == 'female' else False,
                }
        return None