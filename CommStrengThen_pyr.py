import mc
import time


def qingyi_a(e):
    if '/give' in e["cmd"]:
        op = mc.getPlayerPerm(e["player"])
        if op == 1:
            qingyi_comm2(e)
            return False


def qingyi_comm2(e):
    cmd = e["cmd"].split(' ')
    if cmd[1] == '@s':
        if cmd[4] != 'addon':
            if '[{' in cmd[5]:
                jdata = cmd[5].replace('n', '"id2"')
                jdata1 = jdata.replace('l', '"lvl2"')
                mc.addItemEx(e["player"], '{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"minecraft:'+cmd[2] +
                             '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')
                mc.tellraw(e["player"], '§g§l给予'+cmd[3] +
                           '个 '+cmd[4] + ' 附魔物品成功！')
            else:
                mc.tellraw(e["player"], '§4§l此版本暂不支持特殊值')
        elif cmd[4] == 'addon':
            jdata = cmd[6].replace('n', '"id2"')
            jdata1 = jdata.replace('l', '"lvl2"')
            mc.addItemEx(e["player"], '{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"'+cmd[2] +
                         '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[5]+'"},"ench9":'+jdata1+'}}')
            mc.tellraw(e["player"], '§g§l给予'+cmd[3]+'个 '+cmd[5] + ' 附魔物品成功！')
    else:
        mc.tellraw(e["player"], '§4§l此版本暂不支持当前功能')


def qingyi_commblock(e):
    if e["style"] == 'title':
        cmd = e["msg"].split(' ')
        if cmd[0] == 'give':
            play = player(e["target"])
            if cmd[3] != 'addon':
                if '[{' in cmd[4]:
                    jdata = cmd[4].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    mc.addItemEx(play, '{"Count1": '+cmd[2]+',"Damage2":0,"Name8":"minecraft:'+cmd[1] +
                                 '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[3]+'"},"ench9":'+jdata1+'}}')
            elif cmd[3] == 'addon':
                if '[{' in cmd[5]:
                    jdata = cmd[5].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    mc.addItemEx(play, '{"Count1": '+cmd[2]+',"Damage2":0,"Name8":"'+cmd[1] +
                                 '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')


def player(name):
    online = mc.getPlayerList()
    for key in online:
        if name == mc.getPlayerInfo(key)['playername']:
            return key


mc.setListener('聊天消息', qingyi_commblock)
mc.setListener('输入指令', qingyi_a)
