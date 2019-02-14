#coding: utf8

'''
1. 搜索
http://www.xigua15.com/index.php?s=home-search-vod&q=%E9%AC%BC%E5%90%B9%E7%81%AF%E4%B9%8B%E6%80%92%E6%99%B4%E6%B9%98%E8%A5%BF&limit=12&timestamp=1549945342314
s: home-search-vod
q: 鬼吹灯之怒晴湘西
limit: 12
timestamp: 1549945342314
{"data":[{"vod_name":"鬼吹灯之怒晴湘西","vod_title":"第15集","vod_url":"\/guochanju\/guichuidengzhinuqingxiangxi\/"}],"info":"ok","status":1}

2. 详情页
http://www.xigua15.com/guochanju/guichuidengzhinuqingxiangxi/

<div class="vodplaybox" id="playm3u8-pl-list" style="display:block">
			<div class="wxts" style="margin:0px 20px 10px 20px;">
				<div class="snvtvb" ><span class="snvd">温馨提示：</span>[DVD：标准清晰版]&nbsp;[BD：高清无水印]&nbsp;[HD：高清版]&nbsp;[TS：抢先非清晰版] - 其中，BD和HD版本不太适合4M以下的宽带的用户和网速过慢的用户观看。</div>
        </div>
                     <p class="player_list">
                   <a target="_blank" href="/kehuanpian/liulangdiqiu/0-2.html" title="HD1280高清中字">HD1280高清中字<span class="new"></span></a>
                 <a target="_blank" href="/kehuanpian/liulangdiqiu/0-1.html" title="HD1280高清国语中字版">HD1280高清国语中字版</a>
        </p> 
   </div>  
	<div class="vodplaybox" id="m3u8-pl-list" style="display:none">
			<div class="wxts" style="margin:0px 20px 10px 20px;">
				<div class="snvtvb" ><span class="snvd">温馨提示：</span>[DVD：标准清晰版]&nbsp;[BD：高清无水印]&nbsp;[HD：高清版]&nbsp;[TS：抢先非清晰版] - 其中，BD和HD版本不太适合4M以下的宽带的用户和网速过慢的用户观看。</div>
        </div>
                     <p class="player_list">
                   <a target="_blank" href="/kehuanpian/liulangdiqiu/1-2.html" title="HD1280高清中字">HD1280高清中字<span class="new"></span></a>
                 <a target="_blank" href="/kehuanpian/liulangdiqiu/1-1.html" title="HD1280高清国语中字版">HD1280高清国语中字版</a>
        </p> 
   </div>  

3. 播放页

http://www.xigua15.com/kehuanpian/liulangdiqiu/0-2.html

<div style="height:442px; overflow:hidden;" id="zanpiancms_player"><script>var zanpiancms_player = {"url":"https:\/\/135zyv6.xw0371.com\/2019\/02\/07\/Fat6MQ8YeWsiCzt8\/playlist.m3u8","copyright":null,"name":"playm3u8","apiurl":"https:\/\/p.antns.com\/mdparse\/index.php?type=m3u8&id=","adtime":0,"adurl":"","next_path":null};</script><script src="/public/player/playm3u8.js"></script></div>

4. 
https://p.antns.com/mdparse/index.php?type=m3u8&id=https://135zyv6.xw0371.com/2019/02/07/Fat6MQ8YeWsiCzt8/playlist.m3u8
'''

import requests, urllib
import os, sys, time
try:
    import json
except:
    import simplejson as json

def utf2gbk(s):
    return s.decode('utf8').encode('gbk')

def gbk2utf(s):
    return s.decode('gbk').encode('utf8')

def getdata(s, f1, f2):
    p = s.find(f1)
    if p == -1:
        return ''
    d = s[p + len(f1) :]
    p = d.find(f2)
    if p == -1:
        return d
    return d[:p]

def timestamp():
    return str(int(time.time()*1000))
    #1549945342314

def search(name):
    try:
        host = 'http://www.xigua15.com'
        url = 'http://www.xigua15.com/index.php?s=home-search-vod&q=' + urllib.quote(gbk2utf(name)) + '&limit=12&timestamp=' + timestamp()
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
            'Host': 'www.xigua15.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            }
        ret = requests.get(url)#, headers=headers)
        data = ret.content.replace('\\', '')
        data = json.loads(data)
        if data['status'] != 1:
            print utf2gbk(ret.content)
            return
        vod_url = host + data['data'][0]['vod_url']
        #print vod_url
        ret = requests.get(vod_url)
        data = ret.content
        player_list = data.split('player_list')
        if len(player_list) <= 1:
            print '[-] no palyer_list'
            return
        player_list = player_list[1]
        player_url = host + getdata(player_list, 'href="', '"')
        #print player_url
        ret = requests.get(player_url)
        data = ret.content
        data = getdata(data, 'zanpiancms_player = ', ';')
        data = json.loads(data)
        #print data
        url = data['url']
        return url
    except Exception as e:
        print e
        return

if __name__ == '__main__':
    print search(sys.argv[1])
    #print json.dumps('{"data":[{"vod_name":"流浪地球","vod_title":"HD1280高清国语","vod_url":"/kehuanpian/liulangdiqiu/"}],"info":"ok","status":1}')