# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from api.FB_Api import Facebook_API

from models.FacebookUsers import FacebookUser

class Bot():
    fbapi = Facebook_API()
    fbusers = FacebookUser.objects

    def handle(self, message):
        try:
            fbid = message['sender']['id']
            user = self.indentify_user(fbid)
            if not user:
                return
            mess_recv = message['message']['text']

            if message[0] == '#':
                try:
                    patterns = mess_recv.split(' ',1)
                    if len(patterns) == 1:
                        patterns.append('')
                except:
                    patterns = [mess_recv, '']
                self.classify(user, patterns[0], patterns[1])
            else:
                self.notdefine(user)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print exc_type, exc_value, exc_traceback

    def indentify_user(self, fbid):
        user = self.fbusers.filter(fbid=fbid)
        if len(user) == 0:
            data = self.fbapi.get_info_user(fbid=fbid)
            if data:
                user = self.fbusers.create(**data)
                user.save()
                return user
            else:
                return None
        return user.first()

    def classify(self, user, command, content):
        command = command.lower()
        if command in ["#help", "#trogiup"]:
            pass

    def notdefine(self, user):
        content = b"\xE2\x9C\x8C" + u''' Xin chào {0}, THUMBot không xác định được yêu cầu bạn. Để biết cách sử dụng THUMBot bạn có thể sử dụng cú pháp #TROGIUP 
'''.format(user.name)
        self.fbapi.post_facebook_message(user.fbid, content)

