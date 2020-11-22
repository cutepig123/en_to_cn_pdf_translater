# 导入模块
from wxpy import *
import datetime

import pandas as pd
from pandas_datareader import data, wb
import datetime

import matplotlib.pyplot as plt

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

# test code
now = datetime.datetime.now()
print('Hello WeChat! %s' % now)

asmpt = data.DataReader("0522.hk", "yahoo", start, end)

def AsmptStock():
	return str(asmpt.tail())
print('AsmptStock is: %s' % AsmptStock())
	
def AsmptStockFigure():
	asmpt["Adj Close"].plot(grid = True)
	plt.savefig('test.png')
	plt.show()

AsmptStockFigure()

# 初始化机器人，扫码登陆
bot = Bot()
my_friend =bot.friends().search('hjs')[0]
my_friend2 = bot.friends().search('李晶晶')[0]

now = datetime.datetime.now()
for my_friend in [my_friend, my_friend2]:
	my_friend.send('Hello WeChat! Now is: %s' % now)
	my_friend.send('AsmptStock is: %s' % AsmptStock())
	my_friend.send_image('test.png')

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')
	
embed()
	