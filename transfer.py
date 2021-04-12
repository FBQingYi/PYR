# 引入模板
import mc
import json
import os
import codecs
import datetime

# 判断文件夹是否存在，不存在则创建
dirs1 = 'plugins/transfer'
if not os.path.exists(dirs1):
    os.makedirs(dirs1)

# 判断文件是否存在，不存在则创建
file1 = 'plugins/transfer/transfer.json'
if not os.path.exists(file1):
    with codecs.open(file1, 'w+', encoding='utf-8') as f:
        f.write(json.dumps({"content":"服务器列表","buttons":[{"image":{"type":"path","data":"textures/items/book_writable.png"},"text":"XXX服务器"},{"image":{"type":"path","data":"textures/items/iron_sword.png"},"text":"ZZZ服务器"},{"text": "§c关闭"}],"type":"form","title":"跨服传送"}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))
file1 = 'plugins/transfer/transfer_cmd.json'
if not os.path.exists(file1):
    with codecs.open(file1, 'w+', encoding='utf-8') as f:
        f.write(json.dumps([{"method":"cmd","data":"第一个服务器ip","cata":"端口"},{"method":"cmd","data":"第二个服务器ip","cata":"端口"},{"method":"custom_cmd","data":".","cata":"."}], ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))

def qingyi_tr_comm(e):
    with open('plugins/transfer/transfer.json', 'r', encoding='utf-8') as tr_n:
        tr_name = json.load(tr_n)
        tr_name1 = json.dumps(tr_name)
        while ' ' in tr_n:
            tr_name1.remove(' ')
        online = mc.getOnLinePlayers()
        t = mc.sendForm(online[e["playername"]][0],tr_name1)

def qingyi_tr_form(e):
    with open('plugins/transfer/transfer_cmd.json', 'r', encoding='utf-8') as tr_c:
        tr_name = json.load(tr_c)
        dk = tr_name[0]["cata"]
        ip = tr_name[0]["data"]
        if(dk != "."):
            mc.transferServer(e["uuid"], ip, int(dk))

# 指令判断函数
def qingyi_comm(e):
    cmd = e["cmd"]
    if(cmd == '/tr'):
        qingyi_tr_comm(e)
        print(e)

# 设置监听
mc.setListener(19, qingyi_comm)
mc.setListener(3, qingyi_tr_form)