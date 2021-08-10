import mc
import time

def qingyi_a(e):
    if '/give' in e["cmd"] and "[{n" in e["cmd"]:
        op = e["player"].perm
        if op == 1:
            qingyi_comm2(e)
            return False

def qingyi_comm2(e):
    cmd = e["cmd"].split(' ')
    player2 = e['player']
    try:
        if cmd[1] == '@s' and "[" in e["cmd"]:
            if cmd[4] != 'addon':
                if '[{' in cmd[5]:
                    jdata = cmd[5].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    player2.addItem('{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"minecraft:'+cmd[2] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')
                    player2.sendTextPacket('§g§l给予'+cmd[3] +'个 '+cmd[4] + ' 附魔物品成功！')
                    return False
                elif '[{' in cmd[6]:
                    jdata = cmd[6].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    player2.addItem('{"Count1": '+cmd[3]+',"Damage2":'+cmd[5]+',"Name8":"minecraft:'+cmd[2] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')
                    player2.sendTextPacket('§g§l给予'+cmd[3] +'个 '+cmd[4] + ' 附魔物品成功！')
                    return False
            elif cmd[4] == 'addon':
                jdata = cmd[6].replace('n', '"id2"')
                jdata1 = jdata.replace('l', '"lvl2"')
                player2.addItem('{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"'+cmd[2] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[5]+'"},"ench9":'+jdata1+'}}')
                player2.sendTextPacket('§g§l给予'+cmd[3]+'个 '+cmd[5] + ' 附魔物品成功！')
                return False
    except:
        player2.sendTextPacket('§g§l格式错误！！')

def qingyi_commblock(e):
    if e["style"] == 'title':
        cmd = e["msg"].split(' ')
        if cmd[0] == 'give':
            play = player(e["target"])
            if cmd[3] != 'addon':
                if '[{' in cmd[4]:
                    jdata = cmd[4].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    play.addItem('{"Count1": '+cmd[2]+',"Damage2":0,"Name8":"minecraft:'+cmd[1] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[3]+'"},"ench9":'+jdata1+'}}')
                elif '[{' in cmd[5]:
                    jdata = cmd[5].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    play.addItem('{"Count1": '+cmd[2]+',"Damage2":'+cmd[4]+',"Name8":"minecraft:'+cmd[1] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[3]+'"},"ench9":'+jdata1+'}}')
            elif cmd[3] == 'addon':
                if '[{' in cmd[5]:
                    jdata = cmd[5].replace('n', '"id2"')
                    jdata1 = jdata.replace('l', '"lvl2"')
                    play.addItem('{"Count1": '+cmd[2]+',"Damage2":0,"Name8":"'+cmd[1] +
                                 '","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')


def qingyi_cmdcomm(e):
    print(e)
    if 'give' in e:
        if '[{' in e:
            if '"' in e:
                cmd1 = e.split('"')
                name = cmd1[1].split('"')[0]
                cmd = cmd1[2].split('"')
                try:
                    player3 = player(name)
                    if player3 == 'off':
                        mc.logout('玩家不在线！')
                    elif cmd[2] != 'addon':
                        if '[{' in cmd[3]:
                            jdata = cmd[3].replace('n', '"id2"')
                            jdata1 = jdata.replace('l', '"lvl2"')
                            player3.addItem('{"Count1": '+cmd[1]+',"Damage2":0,"Name8":"minecraft:'+cmd[0] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[2]+'"},"ench9":'+jdata1+'}}')
                            player3.sendTextPacket('§g§l给予'+cmd[1] +'个 '+cmd[2] + ' 附魔物品成功！')
                            mc.logout('ok')
                            return False
                        elif '[{' in cmd[4]:
                            jdata = cmd[4].replace('n', '"id2"')
                            jdata1 = jdata.replace('l', '"lvl2"')
                            player3.addItem('{"Count1": '+cmd[1]+',"Damage2":'+cmd[3]+',"Name8":"minecraft:'+cmd[0] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[2]+'"},"ench9":'+jdata1+'}}')
                            player3.sendTextPacket('§g§l给予'+cmd[1] +'个 '+cmd[2] + ' 附魔物品成功！')
                            mc.logout('ok')
                            return False
                    elif cmd[2] == 'addon':
                        jdata = cmd[4].replace('n', '"id2"')
                        jdata1 = jdata.replace('l', '"lvl2"')
                        player3.addItem('{"Count1": '+cmd[1]+',"Damage2":0,"Name8":"'+cmd[0] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[3]+'"},"ench9":'+jdata1+'}}')
                        player3.sendTextPacket('§g§l给予'+cmd[1]+'个 '+cmd[3] + ' 附魔物品成功！')
                        mc.logout('ok')
                        return False
                except Exception as e:
                    print(str(e))
                return False
            else:
                cmd = e.split(' ')
                try:
                    print(cmd[1])
                    player3 = player(cmd[1])
                    print('指针测试 ：玩家名字为：'+player3.name)
                    if player3 == 'off':
                        mc.logout('玩家不在线！')
                    elif cmd[4] != 'addon':
                        if '[{' in cmd[5]:
                            jdata = cmd[5].replace('n', '"id2"')
                            jdata1 = jdata.replace('l', '"lvl2"')
                            player3.addItem('{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"minecraft:'+cmd[2] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')
                            player3.sendTextPacket('§g§l给予'+cmd[3] +'个 '+cmd[4] + ' 附魔物品成功！')
                            mc.logout('ok')
                            return False
                        elif '[{' in cmd[6]:
                            jdata = cmd[6].replace('n', '"id2"')
                            jdata1 = jdata.replace('l', '"lvl2"')
                            player3.addItem('{"Count1": '+cmd[3]+',"Damage2":'+cmd[5]+',"Name8":"minecraft:'+cmd[2] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[4]+'"},"ench9":'+jdata1+'}}')
                            player3.sendTextPacket('§g§l给予'+cmd[3] +'个 '+cmd[4] + ' 附魔物品成功！')
                            mc.logout('ok')
                            return False
                    elif cmd[4] == 'addon':
                        jdata = cmd[6].replace('n', '"id2"')
                        jdata1 = jdata.replace('l', '"lvl2"')
                        player3.addItem('{"Count1": '+cmd[3]+',"Damage2":0,"Name8":"'+cmd[2] +'","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"'+cmd[5]+'"},"ench9":'+jdata1+'}}')
                        player3.sendTextPacket('§g§l给予'+cmd[3]+'个 '+cmd[5] + ' 附魔物品成功！')
                        mc.logout('ok')
                        return False
                except Exception as e:
                    print(str(e))
                    mc.logout('格式错误')
                return False

def player(name):
    playerlist = mc.getPlayerList()
    cs = 'off'
    for i in playerlist:
        if i.name == name:
            cs = i
    return cs


print('['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) +' INFO] [Give] --> give增强已加载v0.2.2')
mc.setListener('聊天消息', qingyi_commblock)
mc.setListener('输入指令', qingyi_a)
mc.setListener('onConsoleInput',qingyi_cmdcomm)