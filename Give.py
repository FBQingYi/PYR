import mc
import time

def qingyi_a(e):
    if '/give' in e["cmd"]:
        op = e["player"].perm
        if op == 1:
            qingyi_comm2(e)
            return False

def qingyi_comm2(e):
    cmd = e["cmd"].split(' ')
    player2 = e['player']
    if cmd[1] == '@s':
        if cmd[4] != 'addon':
            if '[{' in cmd[5]:
                jdata = cmd[5].replace('n', '"id2"')
                jdata1 = jdata.replace('l', '"lvl2"')
                player2.addItem('{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"minecraft:'+cmd[2] +
                             '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')
                player2.sendTextPacket('§g§l给予'+cmd[3] +
                           '个 '+cmd[4] + ' 附魔物品成功！')
            else:
                player2.sendTextPacket('§4§l此版本暂不支持特殊值')
        elif cmd[4] == 'addon':
            jdata = cmd[6].replace('n', '"id2"')
            jdata1 = jdata.replace('l', '"lvl2"')
            player2.addItem('{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"'+cmd[2] +
                         '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[5]+'"},"ench9":'+jdata1+'}}')
            player2.sendTextPacket('§g§l给予'+cmd[3]+'个 '+cmd[5] + ' 附魔物品成功！')
    

def qingyi_commblock(e):
    if e["style"] == 'title':
        cmd = e["msg"].split(' ')
        if cmd[0] == 'give':
            play = player(e["target"])
            if cmd[3] != 'addon':
                if '[{' in cmd[4]:
                    jdata = cmd[4].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    play.addItem('{"Count1": '+cmd[2]+',"Damage2":0,"Name8":"minecraft:'+cmd[1] +
                                 '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[3]+'"},"ench9":'+jdata1+'}}')
            elif cmd[3] == 'addon':
                if '[{' in cmd[5]:
                    jdata = cmd[5].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    play.addItem('{"Count1": '+cmd[2]+',"Damage2":0,"Name8":"'+cmd[1] +
                                 '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')


def player(name):
    playerlist = mc.getPlayerList()
    for i in playerlist:
        if i.name == name:
            return i

print('['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) +' INFO] [Give] --> give增强已加载，目前暂不支持特殊值（懒 v0.0.1')
mc.setListener('聊天消息', qingyi_commblock)
mc.setListener('输入指令', qingyi_a)