# -- coding: utf-8 -
import itchat
from itchat.content import *
import time
itchat.auto_login()
friendlist = itchat.get_friends(update=True)[1:]

@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    if msg['ToUserName'] == 'filehelper' and msg['Text'] != []:
        for friend in friendlist:
            print('亲爱的{my_friend},{receive_word}'.format(receive_word = msg['Text'],my_friend = friend['DisplayName'] or friend['NickName']))
            #itchat.send('亲爱的{my_friend},{receive_word}.'.format(receive_word = msg['Text'],my_friend = friend['DisplayName'] or friend['NickName']), friend['UserName'])
            #itchat.send_image('shehuiren.jpg',friend['UserName'])
            time.sleep(0.3)
        itchat.send('发送完毕！', toUserName='filehelper')
itchat.run()
