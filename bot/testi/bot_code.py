from flask import Flask, request
import telepot;import urllib3;import time
import datetime;import difflib; #import re #import mmap
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=10),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=10))

secret = "***"
token='**********';chatid1='?';c
bot = telepot.Bot(token)
bot.setWebhook("https://???.pythonanywhere.com/{}".format(secret), max_connections=1)
with open('/home/???/mysite/text/chatuq.txt','r') as chatid:
    k=chatid.read()
with open('/home/???/mysite/text/Number.txt','r') as m:
    pop=eval(m.read())
temp=[chatid1];exc=0
#tehrancity='http://31.24.237.150/TTCCTrafficWebSite/UploadedFiles/WebTrafficImages/Web0.png'
#iranroad='http://t15.ir/images/mypictures/iran_map.jpg'
tam="تمام استانها به ترتیب الفبا";
mon="استانهای منتخب";
bazdid="پر بازديدترين استانها";
#tehter="شهر تهران"
os=["آذربایجان‌شرقی", "آذربایجان‌غربی", "اردبیل" ,"اصفهان", "البرز", "ایلام", "بوشهر", "تهران", "چهارمحال‌بختیاری", "خراسان‌جنوبی", "خراسان‌رضوی", "خراسان‌شمالی", "خوزستان", "زنجان", "سمنان" ,"سیستان‌وبلوچستان", "فارس", "قزوین", "قم", "کردستان", "کرمان", "کرمانشاه", "کهکیلویه‌وبویراحمد", "گلستان", "گیلان", "لرستان", "مازندران", "مرکزی", "هرمزگان", "همدان", "یزد"]
pr=["AzarbayjanSharghi","AzarbayjanGharbi","Ardebil","Esfehan","Alborz","Ilam","Boshehr","tehran","chaharmahalbakhtiari","KhorasanJonoobi","KhorasanRazavi","KhorasanShomali","Khozestan","Zanjan","Semnan","SistanBalochestan","Fars","Ghazvin","qom","Kordestan","Kerman","KermanShah","kohkilooyehVaBoyerAhmad","Golestan","Gilan","Lorestan","Mazandaran","Markazi","Hormozgan","Hamedan","Yazd"]
key='{"keyboard":[["'+tam+'"],["'+bazdid+'"],["'+os[18]+'","'+os[17]+'","'+os[4]+'","'+os[7]+'"],["'+os[26]+'","'+os[24]+'","'+os[10]+'"]]}'
#keys='{"keyboard":[["'+os[2]+'","'+os[1]+'","'+os[0]+'"],["'+os[5]+'","'+os[4]+'","'+os[3]+'"],["'+os[8]+'","'+os[7]+'","'+os[6]+'"],["'+os[11]+'","'+os[10]+'","'+os[9]+'"],["'+os[14]+'","'+os[13]+'","'+os[12]+'"],["'+os[17]+'","'+os[16]+'","'+os[15]+'"],["'+os[20]+'","'+os[19]+'","'+os[18]+'"],["'+os[23]+'","'+os[22]+'","'+os[21]+'"],["'+os[26]+'","'+os[25]+'","'+os[24]+'"],["'+os[28]+'","'+os[27]+'"],["'+os[30]+'","'+os[29]+'"]]}'
keys='{"keyboard":[["'+bazdid+'"],["'+os[1]+'","'+os[0]+'"],["'+os[4]+'","'+os[3]+'","'+os[2]+'"],["'+os[7]+'","'+os[6]+'","'+os[5]+'"],["'+os[9]+'","'+os[8]+'"],["'+os[11]+'","'+os[10]+'"],["'+os[14]+'","'+os[13]+'","'+os[12]+'"],["'+os[16]+'","'+os[15]+'"],["'+os[19]+'","'+os[18]+'","'+os[17]+'"],["'+os[21]+'","'+os[20]+'"],["'+os[23]+'","'+os[22]+'"],["'+os[26]+'","'+os[25]+'","'+os[24]+'"],["'+os[28]+'","'+os[27]+'"],["'+os[30]+'","'+os[29]+'"],["'+mon+'"]]}'
#keys='{"keyboard":[["'+bazdid+'"],["'+os[2]+'","'+os[1]+'","'+s[0]+'"],["'+os[5]+'","'+os[4]+'","'+os[3]+'"],["'+os[8]+'","'+os[7]+'","'+os[6]+'"],["'+os[10]+'","'+os[9]+'"],["'+os[11]+'","'+os[10]+'"],["'+os[14]+'","'+os[13]+'","'+os[12]+'"],["'+os[16]+'","'+os[15]+'"],["'+os[19]+'","'+os[18]+'","'+os[17]+'"],["'+os[18]+'","'+os[17]+'","'+s[16]+'"],["'+os[21]+'","'+os[20]+'","'+s[19]+'"],["'+os[24]+'","'+os[23]+'","'+os[22]+'"],["'+os[27]+'","'+os[26]+'","'+s[25]+'"],["'+os[30]+'","'+os[29]+'","'+s[28]+'"],["استانهای منتخب"]]}'
pops=sorted(range(len(pop)), key=lambda k: pop[k])
pkey='{"keyboard":[["'+os[pops[-1]]+'"],["'+os[pops[-2]]+'","'+os[pops[-3]]+'"],["'+os[pops[-4]]+'","'+os[pops[-5]]+'"],["'+tam+'"]]}'
start='خوش آمديد.'+'\n'+"کافی است از میان گزینه ها استان موردنظر خود را انتخاب کنید."
helpp="کافی است از میان گزینه ها استان موردنظر خود را انتخاب کنید یا نام استان موردنظر خود را وارد نمایید."
contact='نظر یا پیشنهاد خود را برای @ad_141 ارسال کنید.'
ent= 'استان موردنظر خود را انتخاب کنيد.'
pages=["/start","/help",'/contact',tam,mon]
res=[start,helpp,contact,ent,ent]
Key=[key,keys,keys,keys,key]
app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    global temp
    exc=0;
    update = request.get_json()
    if "message" in update:
        try:
            message=update["message"]
            content_type, chat_type, chid, date, msgid = telepot.glance(message,long=True)
            chid = str(chid);#message["chat"]["id"])
            #msgid=message["message_id"]
            if chat_type!='private':
                raise Exception
            if (chid not in k) and (chid not in temp):
                exc=0.1
                temp=[chid]+temp
                bot.sendSticker(chid,'CAADBAAD3ggAAlx6nwM35DbE1wFKUAI')#saleno!
                #bot.sendSticker(chid,'CAADBAADXgEAAmtCkQWpknVsBSpU7wI')#khoshamdid!
                bot.forwardMessage(chatid1,chid,msgid)
                exc=0.2
                with open('/home/???/mysite/text/chatuq.txt',"a") as u:
                    u.write('\n'+chid)
                exc=0.3
            if 'text' in message:
                msg = message["text"]#.encode('UTF-8');#print (msg)
                exc=1;
                if msg in pages:
                    bot.sendMessage(chid,res[pages.index(msg)] , reply_markup=Key[pages.index(msg)])
                elif (chid==chatid1) and ('reply_to_message' in message):
                    if msg=='chatid':
                        bot.sendMessage(chatid1,message['reply_to_message']['forward_from']['id'])
                    elif msg=='fileid':
                        if 'photo' in message['reply_to_message']:
                            bot.sendMessage(chatid1,message['reply_to_message']['photo'][0]['file_id'])
                        elif 'audio' in message['reply_to_message']:
                            bot.sendMessage(chatid1,message['reply_to_message']['audio']['file_id'])
                        elif 'document' in message['reply_to_message']:
                            bot.sendMessage(chatid1,message['reply_to_message']['document']['file_id'])
                        elif 'sticker' in message['reply_to_message']:
                            bot.sendMessage(chatid1,message['reply_to_message']['sticker']['file_id'])
                        elif 'video' in message['reply_to_message']:
                            bot.sendMessage(chatid1,message['reply_to_message']['video']['file_id'])
                        elif 'voice' in message['reply_to_message']:
                            bot.sendMessage(chatid1,message['reply_to_message']['voice']['file_id'])
                    #if (msg=='ALLL'):
                    #    with open('/home/???/mysite/text/chatuq.txt',"a") as alll:
                    #        all=alll.read()
                    #    all=re.findall('\d+', all);
                    #    for i in all:
                    #        bot.sendMessage(i,message['text'])
                    else:
                        bot.sendChatAction(message['reply_to_message']['forward_from']['id'],'typing')
                        bot.sendMessage(message['reply_to_message']['forward_from']['id'],message['text'])
                elif (chid==chatid1) and ((msg=='pop')or (msg=='Pop')):
                    bot.sendChatAction(chid, 'typing')
                    pops=sorted(range(len(pop)), key=lambda k: pop[k])
                    pkey='{"keyboard":[["'+os[pops[-1]]+'"],["'+os[pops[-3]]+'","'+os[pops[-2]]+'"],["'+os[pops[-5]]+'","'+os[pops[-4]]+'"],["'+tam+'"]]}'
                    bot.sendMessage(chatid1,os[pops[-1]]+':'+str(pop[pops[-1]])+'\n'+os[pops[-2]]+':'+str(pop[pops[-2]])+'\n'+os[pops[-3]]+':'+str(pop[pops[-3]])+'\n'+os[pops[-4]]+':'+str(pop[pops[-4]])+'\n'+os[pops[-5]]+':'+str(pop[pops[-5]]))
                    bot.sendMessage(chatid1,str(pop), reply_markup=pkey)
                elif (chid==chatid1) and ((msg=='pops')or (msg=='Pops')):
                    bot.sendChatAction(chid, 'typing')
                    pops=sorted(range(len(pop)), key=lambda k: pop[k])
                    pkey='{"keyboard":[["'+os[pops[-1]]+'"],["'+os[pops[-3]]+'","'+os[pops[-2]]+'"],["'+os[pops[-5]]+'","'+os[pops[-4]]+'"],["'+tam+'"]]}'
                    bot.sendMessage(chatid1,os[pops[-1]]+':'+str(pop[pops[-1]])+'\n'+os[pops[-2]]+':'+str(pop[pops[-2]])+'\n'+os[pops[-3]]+':'+str(pop[pops[-3]])+'\n'+os[pops[-4]]+':'+str(pop[pops[-4]])+'\n'+os[pops[-5]]+':'+str(pop[pops[-5]])+'\n'+os[pops[-6]]+':'+str(pop[pops[-6]])+'\n'+os[pops[-7]]+':'+str(pop[pops[-7]])+'\n'+os[pops[-8]]+':'+str(pop[pops[-8]])+'\n'+os[pops[-9]]+':'+str(pop[pops[-9]])+'\n'+os[pops[-10]]+':'+str(pop[pops[-10]]))
                    bot.sendMessage(chatid1,os[pops[-11]]+':'+str(pop[pops[-11]])+'\n'+os[pops[-12]]+':'+str(pop[pops[-12]])+'\n'+os[pops[-13]]+':'+str(pop[pops[-13]])+'\n'+os[pops[-14]]+':'+str(pop[pops[-14]])+'\n'+os[pops[-15]]+':'+str(pop[pops[-15]])+'\n'+os[pops[-16]]+':'+str(pop[pops[-16]])+'\n'+os[pops[-17]]+':'+str(pop[pops[-17]])+'\n'+os[pops[-18]]+':'+str(pop[pops[-18]])+'\n'+os[pops[-19]]+':'+str(pop[pops[-19]])+'\n'+os[pops[-20]]+':'+str(pop[pops[-20]]))
                    bot.sendMessage(chatid1,os[pops[-21]]+':'+str(pop[pops[-21]])+'\n'+os[pops[-22]]+':'+str(pop[pops[-22]])+'\n'+os[pops[-23]]+':'+str(pop[pops[-23]])+'\n'+os[pops[-24]]+':'+str(pop[pops[-24]])+'\n'+os[pops[-25]]+':'+str(pop[pops[-25]])+'\n'+os[pops[-26]]+':'+str(pop[pops[-26]])+'\n'+os[pops[-27]]+':'+str(pop[pops[-27]])+'\n'+os[pops[-28]]+':'+str(pop[pops[-28]])+'\n'+os[pops[-29]]+':'+str(pop[pops[-29]])+'\n'+os[pops[-30]]+':'+str(pop[pops[-30]])+'\n'+os[pops[-31]]+':'+str(pop[pops[-31]]))
                    bot.sendMessage(chatid1,str(pop), reply_markup=pkey)
                elif (chid==chatid1) and ((msg=='sum')or(msg=='Sum')):
                    bot.sendChatAction(chid, 'typing')
                    bot.sendMessage(chatid1,"تعداد کل:"+str(len(k.splitlines())+len(temp)-1)+'\nدفعات کل:'+str(sum(pop)))
                elif (chid==chatid1) & (msg=='Archive!'):
                    bot.sendChatAction(chid,'upload_document')
                    bot.sendDocument(chid,open('/home/???/mysite/text/messages.xls',"rb"))
                elif msg in os:#ind!=[]:
                    if chid=='126447371':#Maman
                       # bot.sendSticker(chid,'CAADBAADAwIAAn_CDgXQr4iJw1RlYQI')#flowers
                        bot.sendSticker(chid,'CAADBAADxw0AAhPwPAKVYeflVKlCdAI')#Heart
                    if chid=='68692710':#Maryam
                        bot.sendSticker(chid,'CAADBAADdA4AAhPwPALs9mcpfY4uSAI')#Heart
                    bot.sendChatAction(chid, 'upload_photo')
                    #bot.sendMessage(chid, 'http://images.141.ir/Province/'+pr[os.index(msg)]+'.jpg'+'?='+str(datetime.datetime.now())[0:10]+'-'+str(datetime.datetime.now())[11:13]+'-'+str(datetime.datetime.now())[14:16])
                    bot.sendPhoto(chid,'http://images.141.ir/Province/'+pr[os.index(msg)]+'.jpg'+'?='+str(datetime.datetime.now())[0:10]+'-'+str(datetime.datetime.now())[11:13]+'-'+str(datetime.datetime.now())[14:16])
                    pop[os.index(msg)]+=1;
                elif msg==bazdid:
                    bot.sendChatAction(chid, 'typing')
                    pops=sorted(range(len(pop)), key=lambda k: pop[k])
                    pkey='{"keyboard":[["'+os[pops[-1]]+'"],["'+os[pops[-3]]+'","'+os[pops[-2]]+'"],["'+os[pops[-5]]+'","'+os[pops[-4]]+'"],["'+tam+'"]]}'
                    bot.sendMessage(chid, ent, reply_markup=pkey)
                else:
                    T=os+pr;
                    ind=[T.index(i) for i in T if msg in i]
                    if ind==[]:
                        J=difflib.get_close_matches(msg,T,len(T),0.6)
                        ind=[T.index(i) for i in J]
                    for i in range(min(3,len(ind))):
                        if ind[i]>=31:
                            ind[i]=ind[i]-31
                    if len(ind)==1:
                        bot.sendMessage(chid, 'استان موردنظر شما:'+'\n'+os[ind[0]], reply_markup='{"keyboard":[["'+os[ind[0]]+'"],["'+tam+'"]]}')
                        bot.sendPhoto(chid,'http://images.141.ir/Province/'+pr[ind[0]]+'.jpg'+'?='+str(datetime.datetime.now())[0:10]+'-'+str(datetime.datetime.now())[11:13]+'-'+str(datetime.datetime.now())[14:16])
                        pop[ind[0]]+=1;
                    elif len(ind)==2:
                        bot.sendMessage(chid,ent, reply_markup='{"keyboard":[["'+os[ind[1]]+'","'+os[ind[0]]+'"],["'+tam+'"]]}')
                    elif len(ind)>=3:
                        bot.sendMessage(chid, ent, reply_markup='{"keyboard":[["'+os[ind[0]]+'"],["'+os[ind[2]]+'","'+os[ind[1]]+'"],["'+tam+'"]]}')
                    else:
                        bot.sendChatAction(chid, 'typing')
                        bot.forwardMessage(chatid1,chid,msgid)
                        bot.sendMessage(chid,'بابت ارسال نظرتان ممنونیم.')
                exc="Writing text message details in file.\n"
                #n.seek(0);#n.write(str(pop))
                with open('/home/???/mysite/text/messages.xls',"a") as g:
                    g.write('\n'+str(datetime.datetime.now())[:-7]+'\t'+chid+'\t'+str(msgid)+'\t'+str(msg).replace('\n', '/').replace('\t', ' ')+'\t\t'+str(message['chat']['first_name']))
                    exc=2.1
                    if 'username' in message ['chat']:
                        g.write('\t@'+str(message['chat']['username']))
            else:
                exc="Other that text!"
                bot.forwardMessage(chatid1,chid,msgid);
                content_type = telepot.glance(message,long=False)[0]
                with open('/home/???/mysite/text/messages.xls',"a") as g:
                    g.write('\n'+str(datetime.datetime.now())[:-7]+'\t'+chid+'\t'+str(msgid)+'\t'+str(content_type).replace('\n', '/').replace('\t', ' ')+'\t\t'+str(message['chat']['first_name']))
                    exc=3.1
                    if 'username' in message ['chat']:
                        g.write('\t@'+str(message['chat']['username']))
            exc=4
            with open('/home/???/mysite/text/Number.txt','w') as n:
                n.write(str(pop))
        except Exception as err:
            print ('Error',str(datetime.datetime.now())[:-7])
            print (exc)
            bot.forwardMessage(chatid1,chid,msgid)
            bot.sendMessage(chatid1,str(err)+'\nError:'+str(exc)+str(msg))
            with open('/home/???/mysite/text/Number.txt','w') as n:
                n.write(str(pop))
    print (str(datetime.datetime.now())[:-7])
    return "OK"
