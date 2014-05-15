# coding: utf-8
import urllib,urllib2,re,xbmcplugin,xbmcgui

#Nhaccuatui by longly

def CATEGORIES():
	addDir(u'Phim M\u1EDBi & HOT'.encode('utf8'),'http://www.nhaccuatui.com/video.html',1,"DefaultFolder.png")
        addDir(u'Phim hot nh\u1ea5t'.encode('utf8'),'http://www.nhaccuatui.com/video-giai-tri-phim.html',1,"DefaultFolder.png")
        addDir(u'Nh\u1EA1c \u00C2u M\u1EF9'.encode('utf8'),'http://www.nhaccuatui.com/video-am-nhac-au-my.html',1,"DefaultFolder.png")
	addDir(u'Nh\u1EA1c H\u00E0n Qu\u1ED1c'.encode('utf8'),'http://www.nhaccuatui.com/video-am-nhac-han-quoc.html',1,"DefaultFolder.png")
	addDir(u'Nh\u1EA1c Vi\u1EC7t Nam'.encode('utf8'),'http://www.nhaccuatui.com/video-am-nhac-viet-nam.html',1,"DefaultFolder.png")
	addDir(u'Nh\u1EA1c Hoa'.encode('utf8'),'http://www.nhaccuatui.com/video-am-nhac-nhac-hoa.html',1,"DefaultFolder.png")
	addDir(u'Nh\u1EA1c Nh\u1EADt'.encode('utf8'),'http://www.nhaccuatui.com/video-am-nhac-nhac-nhat.html',1,"DefaultFolder.png")
	addDir(u'Gi\u1EA3i Tr\u00ED Kh\u00E1c'.encode('utf8'),'http://www.nhaccuatui.com/video-giai-tri-khac.html',1,"DefaultFolder.png")
	addDir(u'Th\u1EC3 Lo\u1EA1i Kh\u00E1c'.encode('utf8'),'http://www.nhaccuatui.com/video-am-nhac-the-loai-khac.html',1,"DefaultFolder.png")

	addDir('N+ Show','http://www.nhaccuatui.com/N+show-danh-sach.html',1,"DefaultFolder.png")

	addDir(u'H\u00E0i K\u1ECBch'.encode('utf8'),'http://www.nhaccuatui.com/video-giai-tri-hai-kich.html',1,"DefaultFolder.png")
	addDir(u'Clip Vui','http://www.nhaccuatui.com/video-giai-tri-funny-clip.html',1,"DefaultFolder.png")
                       
def INDEX(url):
	print "index "+str(url)
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	print "index2 "+str(url)
        link=response.read()
	print "index3 "+str(url)
        response.close()
        match=re.compile('<div class=\"box_absolute\">.+?href="(.+?)".+?src="(.+?)".+?alt="(.+?)".+?</a>', re.DOTALL).findall(link)
	print match
        for url,thumbnail,name in match:
		print "new "+str(url)
                addDir(name,url,2,thumbnail)

def VIDEOLINKS(url,name,thumbnail):
	print "video link:"+str(url)
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"contentURL" content="(.+?)"', re.DOTALL).findall(link)
	print match
        for url1 in match:
                addLink(name,url1,thumbnail)
        

                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
	print "addlink:"+str(url)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
	#name = name.encode('utf8')
	#print name
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote(name)+"&thumbnail="+urllib.quote_plus(str(iconimage))
        ok=True
        liz=xbmcgui.ListItem(urllib.unquote(name), iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addNCTLink(name,url,iconimage):        
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"contentURL" content="(.+?)"', re.DOTALL).findall(link)
	print match
        for url1 in match:
                addLink(name,url1, iconimage)


params=get_params()
url=None
name=None
mode=None
thumbnail=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        thumbnail=urllib.unquote_plus(params["thumbnail"])
except:
        pass

print "Mode1: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Thumbnail: "+str(thumbnail)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print "index: "+url
        INDEX(url)
        
elif mode==2:
        VIDEOLINKS(url,name,thumbnail)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
