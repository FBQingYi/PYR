import mc
import datetime
import json
import os

path = "plugins/GiveClock/"
folder = os.path.exists(path)
if not folder:
	os.makedirs(path)
if not os.path.exists("plugins/GiveClock/deploy.txt"):
    open("plugins/GiveClock/deploy.txt",'w')

def qingyi_join(e):
    with open('plugins/GiveClock/deploy.txt', 'r') as f:
        t=f.read()
        name = e.name
        if name in t:
            print('[GiveClock] >>玩家已领取过！')
        else:
            e.addItem('{"Count1":1,"Damage2":0,"Name8":"minecraft:clock","WasPickedUp1":0,"tag10":{"minecraft:item_lock1" : 2,"minecraft:keep_on_death1" : 1,"RepairCost3":3,"display10":{"Name8":"钟表菜单"},"ench9":[]}}')
            file = 'plugins/GiveClock/deploy.txt'
            with open(file, 'a+') as f:
                f.write(e.name+'\n') 

def qingyi_uitem(e):
    playdata = e["player"].getAllItem()
    jsondata = json.loads(playdata)
    je = jsondata["Hand"]
    pd = json.dumps(je)
    if "\\u949f\\u8868\\u83dc\\u5355"in pd:
        if e["blockname"] == "minecraft:frame" or e["blockname"] == "minecraft:glow_frame":
            if je["Name8"] == "minecraft:clock" and je["tag10"]["display10"]["Name8"] == "钟表菜单":
                return False

mc.setListener('onUseItem',qingyi_uitem)
mc.setListener('onRespawn', qingyi_join)
print('['+datetime.datetime.now().strftime('%F %T')+' INFO] [GiveClock] >>插件加载成功，当前版本：V0.0.2！')