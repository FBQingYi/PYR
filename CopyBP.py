import mc
import json
import time

formidlist = [{}]
global lista
def qingyi_comm(e):
    if e["cmd"] == '/copybp':
        op = e["player"].perm
        if op == 1:
            qingyi_form1(e)
            return False

def qingyi_form1(e):
    global lista
    lista = playerlist()
    formid = e["player"].sendSimpleForm('玩家列表', '请选择:', json.dumps(lista))
    formidlist[0][e["player"].name] = formid

def playerlist():
    playerlist = mc.getPlayerList()
    list=[]
    for i in playerlist:
        list.append({"text":i.name})
    return list

def qingyi_form(e):
    global lista
    if e["selected"] == 'null':
        return False
    if e['formid'] == formidlist[0][e["player"].name]:
        name = lista[eval(e['selected'])]['text']
        data = player(name).getAllItem()
        e['player'].setAllItem(data)
        e['player'].sendTextPacket('复制成功！')
        return False

def player(name):
    playerlist = mc.getPlayerList()
    for i in playerlist:
        if i.name == name:
            return i

mc.setCommandDescription('copybp','复制玩家背包到自己身上（会清除自己背包）')
print('['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) +' INFO] [CopyBP] --> 复制玩家数据插件已加载！ v0.0.1')
mc.setListener('输入指令', qingyi_comm)
mc.setListener('选择表单', qingyi_form)