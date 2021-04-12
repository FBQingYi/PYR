import mc
import json
import os
import datetime
import time
import codecs

global data
# 判断文件夹是否存在，不存在则创建
dirs1 = 'plugins/Inventory_Sync'
if not os.path.exists(dirs1):
    os.makedirs(dirs1)

def fn():
    time.sleep(3)
    print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [Inventory_Sync] >>测试版本加载成功，不推荐用于正式服！')
    print('['+datetime.datetime.now().strftime('%F %T')+' WARN] [Inventory_Sync] >>此插件数据不能使用jsr版的数据！')
    print('['+datetime.datetime.now().strftime('%F %T')+' WARN] [Inventory_Sync] >>受限于PYR目前不支持末影箱数据，末影箱部分功能不可用！')


# 判断文件是否存在，不存在则创建
file1 = 'plugins/Inventory_Sync/deploy.json'
if not os.path.exists(file1):
    with codecs.open(file1, 'w+', encoding='utf-8') as f:
        f.write(json.dumps({"玩家末影箱同步（on/off）":"off","玩家背包同步（on/off）":"off(当前版本不可用，不建议开启)","玩家背包储存路径":"../player-data/player-ltems","玩家末影箱储存路径":"../player-data/player-enitem","提示":"../为返回上层目录，需要返回多少次就加多少个"}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))
        print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [Inventory_Sync] >>插件第一次运行，配置好deploy.json文件后再开服！')
        exit()
else:
    fn()
    with open('plugins/Inventory_Sync/deploy.json', 'r', encoding='utf-8') as tr_n:
        global data
        data = json.load(tr_n)
        if not os.path.exists(data["玩家背包储存路径"]):
            os.makedirs(data["玩家背包储存路径"])
        if not os.path.exists(data["玩家末影箱储存路径"]):
            os.makedirs(data["玩家末影箱储存路径"])

#下线处理
def qingyi_ouitem(e):
    if data["玩家背包同步（on/off）"] == "on":
        qingyi_ouitem1(data,e)
    if data["玩家末影箱同步（on/off）"] == "on":
        qingyi_ouenitem1(data,e)

#上线处理
def qingyi_onitem(e):
    if data["玩家背包同步（on/off）"] == "on":
        qingyi_onitem1(data,e)
    if data["玩家末影箱同步（on/off）"] == "on":
        qingyi_onenitem1(data,e)

#背包数据写文件
def qingyi_ouitem1(data,e):
    item = e.getAllItem()
    name = qingyi_player(e)["playername"]
    with codecs.open(data["玩家背包储存路径"]+'/'+name+'.json', 'w+', encoding='utf-8') as f:
        f.write(item)


#末影箱数据写文件
def qingyi_ouenitem1(data,e):
    enitem = mc.getPlayerEnderChests(e)
    name = qingyi_player(e)["playername"]
    with codecs.open(data["玩家末影箱储存路径"]+'/'+name+'.json', 'w+', encoding='utf-8') as f:
        f.write(enitem)

#设置玩家背包数据
def qingyi_onitem1(data,e):
    name = qingyi_player(e)["playername"]
    file1 = data["玩家背包储存路径"]+'/'+name+'.json'
    if not os.path.exists(file1):
        print('未找到玩家'+name+'背包数据，停止同步！')
    else:
        idata = open(data["玩家背包储存路径"]+'/'+name+'.json', 'r', encoding='utf-8')
        idata1 = idata.read()
        if idata1 !='':
            e.setAllItem(idata1)

#设置玩家末影箱数据
def qingyi_onenitem1(data,e):
    name = qingyi_player(e)["playername"]
    file1 = data["玩家末影箱储存路径"]+'/'+name+'.json'
    if not os.path.exists(file1):
        print('未找到玩家'+name+'背包数据，停止同步！')
    else:
        idata = open(data["玩家背包储存路径"]+'/'+name+'.json', 'r', encoding='utf-8')
        idata1 = idata.read()
        if idata1 !='':
            mc.setPlayerEnderChests(e,idata1)


#获取玩家信息
def qingyi_player(player):
    return mc.Entity
        
mc.setListener('离开游戏', qingyi_ouitem)
mc.setListener('加入游戏', qingyi_onitem)