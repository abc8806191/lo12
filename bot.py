# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy
from threading import Thread

####################################################
botStart = time.time()
####################################################

####################################################
cl = LINE("EOSwdGQN0ZWq8XShAiN4.UFe28xSfjCVNPNanltOLLa.0YgDSkbVqs/uSlAXqk1bfBFNQubIddcaTtW4A0DJ9ok=")
####################################################
clMID = cl.profile.mid
profile = cl.getProfile()
status = str(profile.statusMessage)
lock = _name = "Yuan βộṱ ℟ǕÑing...\n\nYuan-ŁĪŃĘβộṱ\n\n✔已運行24høüř\n\n✔βộṱ  ℟ǕÑing...."
if lock not in status:
    profile.statusMessage = lock + status
    cl.updateProfile(profile)
else:
    pass
####################################################
####################################################

####################################################
oepoll = OEPoll(cl)
####################################################

####################################################
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
####################################################
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
####################################################
redOpen = codecs.open("red.json","r","utf-8")
red = json.load(redOpen)
####################################################
jgOpen = codecs.open("jg.json","r","utf-8")
jg = json.load(jgOpen)
####################################################

####################################################
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
####################################################

####################################################
lineSettings = cl.getSettings()
clMID = cl.profile.mid
clProfile = cl.getProfile()
clSetting = cl.getSettings()
####################################################

####################################################
bl = ["MID"]
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
####################################################

####################################################
admin=['ub6f9d53713c5869f0d78e71febe13837',clMID]
King = "MID"
####################################################

####################################################
msg_dict = {}
msg_dictt = {}
####################################################

####################################################
wait = {
    'logout': {},
    'rapidFire': {},
    'group': "",
    'getmid': True,
    'um': True,#收回高速
    'cvp': True,#更換頭貼
    'gbc':{},
    'resset': False#偵測更新
    }
####################################################

####################################################
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
####################################################

####################################################
setTime = {}
setTime = wait2['setTime']
####################################################

####################################################
profile = cl.getProfile()
####################################################

####################################################
msg_dict = {}
msg_dictt = {}
####################################################
if "ub6f9d53713c5869f0d78e71febe13837" not in admin:
    admin.append("ub6f9d53713c5869f0d78e71febe13837")
if "ub6f9d53713c5869f0d78e71febe13837" not in admin:
    admin.append("ub6f9d53713c5869f0d78e71febe13837")
####################################################
mulai = time.time()
####################################################

def Runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天\n%02d 時\n%02d 鐘\n%02d 秒\n以上為半垢機体運行時間\n半垢 運行時間測試' % (days, hours, mins, secs)
def Rtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天 %02d 時 %02d 鐘 %02d 秒' % (days, hours, mins, secs)
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重新啟動中...")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = jg
        f = codecs.open('jg.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  出來面對'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageTag(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  此人在群組(私聊)標住您'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessagegat(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  157.9出來'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@MiliSun "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mid")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 
def ytdl(url):
    video = pafy.new(url)
    best = video.getbest() 
    best.download(filepath="test.mp4")
def gettoken(to):
    try:
        k1 = LINE() 
        cl.sendMessage(to,str(k1.authToken))
    except:
        pass
    return True
def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt', 'r') as f:
        text = f.read()
    help = text.format(key=key.title())
    return help
def help1():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help1.txt', 'r') as f:
        text = f.read()
    help1 = text.format(key=key.title())
    return help1
def help2():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help2.txt', 'r') as f:
        text = f.read()
    help2 = text.format(key=key.title())
    return help2
def help3():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help3.txt', 'r') as f:
        text = f.read()
    help3 = text.format(key=key.title())
    return help3
def help4():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help4.txt', 'r') as f:
        text = f.read()
    help4 = text.format(key=key.title())
    return help4
def help5():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help5.txt', 'r') as f:
        text = f.read()
    help5 = text.format(key=key.title())
    return help5
def unsend(msgid):
    sleep(1)
    cl.unsendMessage(msgid)
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == False:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "安安！{} 感謝您加我為好友！半垢V4.0 Su Bot運行中(๑′ᴗ‵๑)！Çręätør:Yuan".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == False:
                if op.param2 in admin:
                    pass
                else:
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
                    cl.sendMessage("MID",cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if op.param2 in admin or op.param2 in owners:
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[提示]\n')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "真心感謝您一直以來的陪伴\n\n但是\n離開了就再也回不來了☺️\n\n拜拜👋".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@yuan "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "歡迎加入1️⃣0️⃣元群組🎉🎉\n\n🔸進群請先看記事本重要事宜\n\n🔸版媽平常白天在忙碌，期間如有問題，請私訊小幫手即可，沒有馬上回復代表在忙碌，感謝！\n\n🔸非必要版媽與小幫手不會介入各位交易.若有跑單.棄單.喊了不要等行為.可私訊介入協商.\n\n🔸請勿更改群組內的設定，如被機器人踢出，是不給予加回來的唷，請多多配合唷❤️\n\n本群版媽為 👉 嬣🍋\n\n小幫手為 👉◡̈  馥、魚🐟、Yu🧸".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
            if op.param1 in jg["JoinGroup"]:
                if op.param2 not in admin:
                    try:
                        contact = cl.getContact(op.param2)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@yuan "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@yuan "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@yuan "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@yuan "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if sender in admin:
                pass 
            else:
                if msg.to in wait["rapidFire"]:
                    if time.time() - wait["rapidFire"][msg.to] < 2:
                        return
                    else:
                        wait["rapidFire"][msg.to] = time.time()
                else:
                    wait["rapidFire"][msg.to] = time.time()       
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 1:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'pic':
                    image = cl.downloadObjectMsg(msg.id )
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《圖片》\n" + wait['gbc'][sender]['text'] )
                            cl.sendImage(manusia,image)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    cl.deleteFile(image)
                    del wait['gbc'][sender]
            if msg.contentType == 13:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'contact':
                    mid =msg.contentMetadata["mid"]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《友資》\n" + wait['gbc'][sender]['text'] )
                            cl.sendContact(manusia,mid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if msg.contentType == 16:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'post':
                    postid =str(msg.contentMetadata['postEndUrl']).split("&postId=")[1]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《貼文》\n" + wait['gbc'][sender]['text'] )
                            cl.sendPostToTalk(manusia,postid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if sender in admin:
                if text.lower() == 'help':
                        cl.sendMessage(to, help())
                elif msg.text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    cl.sendMessage(to, "管理員已增加！")
                elif msg.text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    cl.sendMessage(to, "已移除權限！")
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("info "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName +"\n[ 個簽 ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                            cl.sendImageWithURL(msg.to, str("http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus)) 
                            cl.sendImageWithURL(msg.to, str(cl.getProfileCoverURL(ls)))
                elif msg.text.lower().startswith("adminadd ") or msg.text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"] and inkey not in ban["blacklist"] and inkey not in ban["owners"]: 
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "已獲得權限！")
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                elif msg.text.lower().startswith("admindel ") or msg.text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                elif text.lower().startswith('prank '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    sep = msg.text.split(" ")
                    text = sep[2]
                    contact = cl.getContact(inkey)
                    path = "http://dl.profile.line-cdn.net/" + str(contact.pictureStatus)
                    cl.sendMessage(to, text, {'MSG_SENDER_NAME': str(contact.displayName),'MSG_SENDER_ICON': str(path)})
                elif text.lower().startswith('tr-jp '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower() in ['ginfo']:		
                    G = cl.getGroup(msg.to)
                    group = cl.getGroup(to)
                    contact = cl.getContact(sender)
                    gtime = group.createdTime
                    gtimee = int(round(gtime/1000))
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "創群者已砍帳"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                         gPending = str(len(group.invitee))				
                    ret_ ="☲☲☲☲☲群組☲☲☲☲☲"
                    ret_ +="\n成員數量\n【"+(str(len(group.members)))+"】"
                    ret_ +="\n邀請數量\n【"+(gPending)+"】"
                    ret_ +="\n☲☲☲☲☲群組☲☲☲☲☲"
                    ret_ +="\n群組名稱\n【{}】".format(str(group.name))
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    ret_ +="\n群組建立時間\n【{}】".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(gtimee)))
                    ret_ +="\n☲☲☲☲☲說明☲☲☲☲☲"
                    ret_ +="\n群主創建者"
                    ret_ +="\n【"+(str(gCreator))+"】"
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    ret_ +="\n群組Gid"
                    ret_ +="\n【{}】".format(group.id)
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    cl.sendMessage(to, str(ret_))
                elif text.lower() == 'rlb':
                    a = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    b = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    c = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    d = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    e = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    f = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    g = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    h = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    i = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    j = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    k = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    l = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    m = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    n = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    o = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    slot = "拉霸機拉霸一次\n第一行==>{}  {}  {}<==\n第二行==>{}  {}  {}<==\n第三行==>{}  {}  {}<==\n第四行==>{}  {}  {}<==\n第五行==>{}  {}  {}<==\n以上是您的拉霸結果".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"[自動回覆]\n恭喜中獎~~")
                        return
                    cl.sendMessage(to,"[自動回覆]\n再試一次吧QQ")
                elif msg.text.lower().startswith("fk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendMessage(to,"Error")
         
                elif msg.text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"來回一次")
                            cl.findAndAddContactsByMid(target)
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.sendMessage(to,"Error")
                elif msg.text in ["本日運勢","rls"]:
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.sendMessage(to,slot)
                    cl.sendMessage(to,"[自動回覆]\n在玩一次吧！ヽ(✿ﾟ▽ﾟ)ノ")	
                #防翻保護
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
			    #少數重要功能
                elif text.lower() == 'rs':
                    cl.sendMessage(to, "重新啟動中....")	
                    restartBot()
                elif text.lower() == 'rt':
                    eltime = time.time() - mulai
                    bot = "運行時間長達\n" +Runtime(eltime)
                    cl.sendMessage(to,bot)	
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
                elif text.lower() == 'bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            cl.leaveGroup(to)
                        except:
                            pass
				#進群退群退副本
                elif text.lower() == 'aj on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟 ✔")	
                elif text.lower() == 'aj off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉 ✘")	
                elif text.lower() == 'qj off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址自動入群已關閉 ✘")	
				#其餘加好友收回自動已讀
                elif text.lower() == 'ad on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟 ✔")	
                elif text.lower() == 'ad off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉 ✘")	
                elif text.lower() == 'rr on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟 ✔")	
                elif text.lower() == 'rr off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉 ✘")	
                elif text.lower() == 'rd on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟 ✔")	
                elif text.lower() == 'rd off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉 ✘")	
				#更改顯示
	
				#踢人顯示
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "踢人標註已開啟 ✔═")	
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "踢人標註已關閉 ✘═")	
				#進群退群
                elif text.lower() == 'sj on':
                    settings["seeJoin"] = True
                    cl.sendMessage(to, "入群通知已開啟 ✔═")	
                elif text.lower() == 'sj off':
                    settings["seeJoin"] = False
                    cl.sendMessage(to, "入群通知已關閉 ✘═")	
                elif text.lower() == 'sl on':
                    settings["seeLeave"] = True
                    cl.sendMessage(to, "退群通知已開啟 ✔═")	
                elif text.lower() == 'sl off':
                    settings["seeLeave"] = False
                    cl.sendMessage(to, "退群通知已關閉 ✘═")	
                elif text.lower() == 'm on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已開啟 ✔")	
                elif text.lower() == 'm off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已關閉 ✘")	
                elif text.lower() == 'ru on':
                    wait["um"] = True
                    cl.sendMessage(to, "收回已開啟 ✔")	
                elif text.lower() == 'ru off':
                    wait["um"] = False
                    cl.sendMessage(to, "收回已關閉 ✘")	
				#保護項目
                elif text.lower() == 'pro on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開啟 ✔")
                elif text.lower() == 'pro off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關閉 ✘")
                elif text.lower() == 'ip on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開啟 ✔")
                elif text.lower() == 'ip off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關閉 ✘")
                elif text.lower() == 'qp on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開啟 ✔")
                elif text.lower() == 'qp off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關閉 ✘")
                elif text.lower() == 'set':
                    try:
                        ret_ = "Capoo Set List"
                        ret_ += "\n進群類型 開關"
                        if settings["autoJoin"] == True: ret_ += "\n自動入群 ✅"
                        else: ret_ += "\n自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n網址入群 ✅"
                        else: ret_ += "\n網址入群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n自離副本 ✅"
                        else: ret_ += "\n自離副本 ❌"
                        ret_ += "\n其餘功能 開關"
                        if settings["autoAdd"] == True: ret_ += "\n自動加友 ✅"
                        else: ret_ += "\n自動加友 ❌"
                        if settings["autoRead"] == True: ret_ += "\n自動已讀 ✅"
                        else: ret_ += "\n自動已讀 ❌"
                        if settings["reread"] == True: ret_ += "\n查詢收回 ✅"
                        else: ret_ += "\n查詢收回 ❌"
                        if wait["resset"] == True: ret_ += "\n偵測更改 ✅"
                        else: ret_ += "\n偵測更改 ❌"
                        ret_ += "\n保護類型 開關"
                        if settings["protect"] == True: ret_ += "\n群組保護 ✅"
                        else: ret_ += "\n群組保護 ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n邀請保護 ✅"
                        else: ret_ += "\n邀請保護 ❌"
                        if settings["qrprotect"] == True: ret_ += "\n網址保護 ✅"
                        else: ret_ += "\n網址保護 ❌"
                        ret_ += "\n通知類型 開關"
                        if settings["seeJoin"] == True: ret_ += "\n入群通知開啟 ✅"
                        else: ret_ += "\n入群通知關閉 ❌"
                        if settings["seeLeave"] == True: ret_ += "\n退群通知開啟 ✅"
                        else: ret_ += "\n退群通知關閉 ❌"
                        ret_ += "\n作者: Su"
                        ret_ += "\nID: bat920301"
                        ret_ += "\nQR:https://sutw.xyz/profile"
                        ret_ += "\n<查詢完畢>"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
				#機器簡介
                elif text.lower() == 'about':
                        arr = []
                        t1 = time.time()
                        t2 = (time.time() - t1)/100
                        owner = "u74ae03c94243a7d57373d156e2068ed7"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(owner)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        eltime = time.time() - mulai
                        bot = Rtime(eltime)
                        ret_ = "《關於自己》"
                        ret_ += "\n➲群組數量: {}".format(str(len(grouplist)))
                        ret_ += "\n➲好友人數: {}".format(str(len(contactlist)))
                        ret_ += "\n➲封鎖人數: {}".format(str(len(blockedlist)))
                        ret_ += "\n➲個簽字數: {}".format(str(len(clProfile.statusMessage)))
                        ret_ += "\n➲最愛人數: {}".format(str(len(cl.getFavoriteMids())))
                        ret_ += "\n➲封鎖好友: {}".format(str(len(cl.getBlockedContactIds())))
                        ret_ += "\n➲邀請群組: {}".format(str(len(cl.getGroupIdsInvited())))
                        ret_ += "\n➲LineID:{}".format(clProfile.userid)
                        ret_ += "\n《個人開關》"
                        if settings["autoJoin"] == True: ret_ += "\n➲自動入群 ✅"
                        else: ret_ += "\n➲自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n➲網址入群 ✅"
                        else: ret_ += "\n➲網址入群 ❌"
                        if settings["reread"] == True: ret_ += "\n➲防止收回 ✅"
                        else: ret_ += "\n➲防止收回 ❌"
                        if settings["autoRead"] == True: ret_ += "\n➲自動已讀 ✅"
                        else: ret_ += "\n➲自動已讀 ❌"
                        ret_ += "\n《關於半垢》"
                        ret_ += "\n➲Su Bot v8.7"
                        ret_ += "\n➲半垢主人:Yuan" .format(creator.displayName)
                        ret_ += "\n➲半垢極限速度:\n➲{}".format(str(t2))
                        ret_ += "\n➲半垢運行時間:\n➲l─────●────l\n➲{}\n➲⇆ ㅤㅤ◁  ❚ ❚  ▷    ↻".format(bot)
                        cl.sendMessage(to, str(ret_))
                        cl.relatedMessage(msg.to, str(e))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "開啟成功")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "關閉成功")
                elif text.lower().startswith("rt:"):
                    id = text[3:].split(':')
                    for x in range(int(id[1])):
                        cl.sendPostToTalk(to,id[0])
                    cl.sendMessage(to, "文章分享完畢")
                elif text.lower().startswith("rpc:"):
                    separate = text.split(":")
                    bctxt = text.replace(separate[0] + ":","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,bctxt[1])
                elif text.lower().startswith("rgb:"):
                    data = text[4:].lower().split(':')
                    if len(data) == 2:data.append("0")
                    elif len(data) >3 or len(data) <2:return
                    try:int(data[2])
                    except:return
                    if data[0] == 'text':
                        n = cl.getGroupIdsJoined()
                        g = 0
                        for manusia in n:
                            group = cl.getGroup(manusia)
                            nama =[contact.mid for contact in group.members]
                            if len(nama) >int(data[2]):
                                cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《文字》\n" + data[1])
                                g+=1
                            else:
                                pass
                        cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    elif data[0] in ['pic', 'contact', 'post']:
                        wait['gbc'][sender] = {'type':data[0],'text':data[1],'over':data[2]}
                        cl.sendMessage(to,'請發送你要廣播的東西~')
				#測速功能
				 
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "趴搭趴搭.....")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + " 秒")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + ' seconds')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'spt':
                    start = time.time()
                    cl.sendMessage(to, "速度約為......")
                    elapsed_time = (time.time() - start)/100
                    cl.sendMessage(to,format(str(elapsed_time)) + " 秒")
                elif text.lower() == 'spk':
                    start = time.time()
                    cl.sendMessage(to, "Test Speed......")
                    elapsed_time = (time.time() - start)/100
                    cl.sendMessage(to,"Kick One\n" + format(str(elapsed_time)) + " 秒")
                elif msg.text in ["/sp","/speed"]:
                    t1 = time.time()
                    cl.sendMessage(to, "第一次")
                    t2 = time.time() - t1
                    time.sleep(0.01)
                    t3 = time.time()
                    cl.sendMessage(to, "第二次")
                    t4 = time.time() - t3
                    time.sleep(0.01)
                    t5 = time.time()
                    cl.sendMessage(to, "第三次")
                    t6 = time.time() - t5
                    time.sleep(0.01)
                    t7 = time.time()
                    cl.sendMessage(to, "第四次")
                    t8 = time.time() - t7
                    time.sleep(0.01)
                    t9 = time.time()
                    cl.sendMessage(to, "第五次")
                    t10 = time.time() - t9
                    time.sleep(0.01)
                    a1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b1 = str(a1)
                    a2 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b2 = str(a2)
                    a3 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b3 = str(a3)
                    a4 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b4 = str(a4)
                    a5 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b5 = str(a5)
                    ret_ = "     [反應速度]\n"
                    ret_ += "第1次:{}秒\n".format(str(t2))
                    ret_ += "第2次:{}秒\n".format(str(t4))
                    ret_ += "第3次:{}秒\n".format(str(t6))
                    ret_ += "第4次:{}秒\n".format(str(t8))
                    ret_ += "第5次:{}秒\n     [處理速度]\n".format(str(t10))
                    ret_ += "第1次:{}秒\n".format(str(b1))
                    ret_ += "第2次:{}秒\n".format(str(b2))
                    ret_ += "第3次:{}秒\n".format(str(b3))
                    ret_ += "第4次:{}秒\n".format(str(b4))
                    ret_ += "第5:{}秒\n".format(str(b5))
                    ret_ += "     [以上為Capoo速度測試]"
                    cl.sendMessage(to, str(ret_))
                    cl.relatedMessage("MID", str(ret_))
				#踢人指令
                elif text.lower().startswith("ri:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("ti:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("vk:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif msg.text.lower().startswith("kt "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制中")
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.relatedMessage(msg.to, str(ret_))
               				#mid或其餘方式功能
                elif text.lower().startswith("mc:"):
                        separate = text.split(":")
                        mmid = text.replace(separate[0] + ":","")
                        cl.sendContact(to, mmid)
                        cl.sendMessage(to,"幫您丟出友資\n友資MID\n"+mmid+"\n幫您生成完畢")
                elif text.lower().startswith("inv:"):
                        separate = text.split(":")
                        midd = text.replace(separate[0] + ":","")
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(msg.to,[midd])
                        cl.sendMessage(to,"已經幫您邀請\n"+midd+"\n邀請完畢\n或可能此人已經在群組")
                elif text.lower().startswith("ce:"):
                        separate = text.split(":")
                        txt = text.replace(separate[0] + ":","")
                        cl.createPost(txt)
                        cl.sendMessage(to,"正在幫您生成貼文\n貼文創建內容:\n" + txt + "\n貼文創建完畢")
                elif text.lower().startswith("cn:"):
                        separate = text.split(":")
                        string = text.replace(separate[0] + ":","")
                        if len(string) <= 20:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(to,"名稱已更改為\n=>" + string + "")
                        if len(string) >= 21:
                            cl.sendMessage(to,"[警告]\n名稱不能突破20字喔!!\n超過20字強制更改\n將會凍帳一小時\n以下是您想突破的文字名稱\n" + string + "")
				#發送文字指令
                elif text.lower().startswith("say "):
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.sendMessage(to,x[1])
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.sendMessage(to,x[1])
                        except:
                            cl.sendMessage(to,"無法正確執行此指令")
				#標註指令
                elif text.lower().startswith('tag '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    start = time.time()
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessageWithMention(to, inkey)
                        elapsed_time = time.time() - start
                    cl.sendMessage(to, "標註完畢 共標註了{}次".format(number))
                    cl.sendMessage(to, "標註完畢\n標註共計: %s秒" % (elapsed_time))
                elif text.lower().startswith('tg '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessagegat(to, inkey)
                    cl.sendMessage(to, "標註完畢 共標註了{}次".format(number))
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Mili \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'rgone':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//1
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*1 : (a+1)*1]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Mili \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
				#更改個簽指令
                elif text.lower().startswith("cb:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    if len(string) <= 10000000000:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendMessage(to,"個簽狀態已更改為 :  \n" + string)                       
                elif text.lower() == '抽':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.sendMessage(to,slot)                            
    #====================================================================================================================================================================遊客
    #===================================================================================================================================================================
            if sender not in admin:
                if msg.text in ["幹","淦","fuck","肏","幹你娘","操","靠","靠腰","靠北","靠杯"]:
                    a = random.choice(["ヽ(✿ﾟ▽ﾟ)ノ","(ﾟ∀ﾟ)","(`・ω・´)","ò∀ó","(´･ω･`)","(つд⊂)","｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "不要講髒話辣\n{}".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == '本日運勢':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == '抽':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == 'rls':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.sendMessage(to,slot)

                elif text.lower() == 'rlb':
                    a = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    b = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    c = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    d = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    e = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    f = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    g = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    h = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    i = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    j = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    k = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    l = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    m = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    n = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    o = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    slot = "拉霸機拉霸一次\n第一行==>{}  {}  {}<==\n第二行==>{}  {}  {}<==\n第三行==>{}  {}  {}<==\n第四行==>{}  {}  {}<==\n第五行==>{}  {}  {}<==\n以上是您的拉霸結果".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"[自動回覆]\n恭喜中獎~~")
                        return
                    cl.sendMessage(to,"[自動回覆]\n再試一次吧QQ")
                elif text.lower() == 'help':
                    cl.sendMessage(to, help1())
    #===========================================================================================================================================================================遊客
    #=============================================================================================================================================================================
        if op.type == 26:
            try:
                msg = op.message
                msg_id = msg.id
                sender = msg._from
                if msg.toType == 0:
                    cl.log("[%s]"%(msg._from)+msg.text)
                else:
                    if msg.contentType == 0:#文字
                        cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 7:#貼圖
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata['STKID'])
                    elif msg.contentType == 13:#友資
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["mid"]+' '+msg.contentMetadata["displayName"])
                    elif msg.contentType == 14:#檔案
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["FILE_NAME"]+'檔案下載完成')
                    else:#若是都沒有則是錯誤
                        cl.log("[%s] [E]"%(msg.to)+msg.text)
                if msg.contentType == 0:#文字
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                #elif msg.contentType == 1:#圖片
                    #image = cl.downloadObjectMsg(msg_id, saveAs="檔案/圖片/{}-jpg.jpg".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime}
                #elif msg.contentType == 2:#影片
                    #Video = cl.downloadObjectMsg(msg_id, saveAs="檔案/影片/{}-Video.mp4".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":msg.createdTime}
                #elif msg.contentType == 3:#錄音檔
                    #sound = cl.downloadObjectMsg(msg_id, saveAs="檔案/音檔/{}-sound.mp3".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime}
                elif msg.contentType == 7:#貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime}
                elif msg.contentType == 13:#友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime}
                elif msg.contentType == 14:#檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="檔案/檔案/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime}
                else:#若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime}
            except Exception as e:
                print(e)
#==============================================================================# #偵測收回
        if op.type == 65:
            at = "MID"
            msg_id = op.param2
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in bl:
                    if msg_dict[msg_id]["from"] not in red["reread"]:
                        if at not in red["reread"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                    ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                    cl.sendImageWithURL(at, ok)
                                    del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendContact(at,msg_dict[msg_id]["mid"])
                                    del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                    del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendFile(at, msg_dict[msg_id]["file"])
                                    del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendImage(at, msg_dict[msg_id]["image"])
                                    del msg_dict[msg_id]
                                elif 'Video' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                    cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                    del msg_dict[msg_id]
                                else:
                                    pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    sendMessageTag("MID", contact.mid)
                                break
            if "/ti/g/" in msg.text.lower():
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.sendMessage(to, "使用網址成功淺入《%s》群組" % str(group.name))
                            cl.sendMessage(to, "群組網址\n《https://line.me/R/ti/g/》\n《%s》" % str(ticket_id))
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
