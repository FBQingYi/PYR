import sys
sys.path.append('C:/Users/tangs/OneDrive/Desktop/其他/MC/PYR测试/MCPE/plugins/py/HGuild_Runtime')
import datetime
import mc
import json
import time
import requests

global locala
global clouda
locala =0
clouda =0

def UPDATE(name, version):
    data = {"plugin": name}
    res = requests.post(url=url, data=data)
    if res.text != '':
        if '链接' in res.text:
            bb = res.text.index('链接：')
            bb1 = res.text.index('版本：')
            gurl = res.text[bb+3:]
            banben = res.text[bb1+3:bb]
            b = banben.split('.')
            a = version.split('.')
            qingyi_pd(a, b, gurl, banben, version, name)
    else:
        print('['+datetime.datetime.now().strftime('%F %T') +
              ' ERROR] [' + name + '] >> 加载成功，云端未找到相关信息，当前版本：' + version)


def OFUPDATE(name, version):
    print('['+datetime.datetime.now().strftime('%F %T') +
          ' INFO] [' + name + '] >> 加载成功，无法检测更新，当前版本：' + version)
    print('-------------------------------------')


def qingyi_pd(a, b, upurll, vers, version, name):
    if(a[0] == b[0] and a[1] == b[1] and a[2] == b[2]):
	    print('['+datetime.datetime.now().strftime('%F %T') +
	          ' INFO] ['+name+']插件加载成功，当前版本：'+version)
	    print('-------------------------------------')
    else:
        if(a[0] < b[0]):
            localup(name, upurll, vers, version)
        elif(a[0] == b[0]):
            if(a[1] < b[1]):
                localup(name, upurll, vers, version)
            elif(a[1] == b[1]):
                if(a[2] < b[2]):
                    localup(name, upurll, vers, version)
                elif(a[2] > b[2]):
                    cloudup(name, version, vers)
                elif(a[1] > b[1]):
                    cloudup(name, version, vers)
        elif(a[0] > b[0]):
            cloudup(name, version, vers)

def localup(name, upurll, vers, version):
    global locala
    locala += 1
    print('['+datetime.datetime.now().strftime('%F %T') +
          ' UPDATE] [' + name + '] >> 当前版本：' + version + ',最新版本：' + vers)
    print('['+datetime.datetime.now().strftime('%F %T') +
          ' UPDATE] [' + name + '] >> 请前往 ' + upurll + ' 更新！')
    print('-------------------------------------')


def cloudup(name, version, vers):
    global clouda
    clouda += 1
    print('['+datetime.datetime.now().strftime('%F %T') +
          ' ERROR] [' + name + '] >> 云端版本过低，请联系作者更新云端数据！')
    print('['+datetime.datetime.now().strftime('%F %T') + ' ERROR] [' +
          name + '] >> 加载成功，当前版本：' + version + '，云端版本：' + vers)
    print('-------------------------------------')


url = 'http://up.qingyimc.cn/home/api/check.php'
data = ''
res = requests.post(url=url, data=data)
if res.text == '':
    print('['+datetime.datetime.now().strftime('%F %T') +
          ' INFO] 数据库链接成功！即将开始检测服务器插件版本！')
    mc.setShareData('_PluginCheck', UPDATE)
else:
    print('['+datetime.datetime.now().strftime('%F %T')+' INFO] 数据库链接链接失败，暂停检测更新！')
    mc.setShareData('_PluginCheck', OFUPDATE)


def qingyi_ti():
    time.sleep(12)
    if(locala >= 1 and clouda >= 1):
        print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [版本检测] >> 更新检测完毕，本次检测到您有 ' + str(locala) + ' 个插件需要更新，' + str(clouda) + ' 个插件数据库没更新，请联系作者更新数据库！')
    elif(clouda >= 1):
        print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [版本检测] >> 更新检测完毕，本次检测到您有 ' + str(clouda) + ' 个插件数据库没有更新，请联系作者更新数据库！')
    elif(locala >= 1):
        print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [版本检测] >> 更新检测完毕，本次检测到您有 ' + str(locala) + ' 个插件需要更新，为了您的更好的体验，请速去更新！')
    else:
        print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [版本检测] >> 更新检测完毕，您没有需要更新的插件！')

mc.newThread(qingyi_ti)
