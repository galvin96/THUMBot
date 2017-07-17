import json
from pprint import pprint

from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from bot import Bot
from fb_THUMBot.api.FB_Api import Facebook_API
from fb_THUMBot import key

class THUMBotView(generic.View):
    fbapi = Facebook_API()
    bot = Bot()

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == key.Verify_Token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    pprint(message)
                    self.bot.handle(message)
        return HttpResponse()

