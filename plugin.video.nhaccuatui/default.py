# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui

#Nhaccuatui by longly

def CATEGORIES():
	addDir(u'T\u00ECm Ki\u1EBFm\n'.encode('utf8'),'http://www.nhaccuatui.com/video.html',3,"DefaultFolder.png")
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
	dialog = xbmcgui.DialogProgress()
	dialog.create('Nhaccuatui', 'Loading...')
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=chunk_read(response, dialog)
		response.close()
	except:
		link=''
		pass
	dialog.close()
	match=re.compile('<div class=\"box_absolute\">.+?href="(.+?)".+?src="(.+?)".+?alt="(.+?)".+?</a>', re.DOTALL).findall(link)
	for url,thumbnail,name in match:
		addLink(name,url,2,thumbnail)
	#match=re.compile('=\"box_pageview\".+?class=\"active\".+?href=\"(.+?)\".+?</div>', re.DOTALL).findall(link)
	match=re.compile('=\"box_pageview\"(.+?)</div>', re.DOTALL).findall(link)
	bShowReturnMain = False
	if match:
		smatch=re.compile(' class=\"active\".+?href=\"(.+?)\"', re.DOTALL).findall(match[0])
		if smatch:
			addDir(u'Trang k\u1EBF>'.encode('utf8'), smatch[0], 1, "DefaultFolder.png")
			bShowReturnMain = True
	if bShowReturnMain:
		addTopMenu();
					

def VIDEOLINKS(url,name,thumbnail):
	dialog = xbmcgui.DialogProgress()
	dialog.create('Nhaccuatui', 'Loading…')
	try:
		print "video link: "+str(url)
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=chunk_read(response, dialog)
		#link=response.read()
		response.close()
	except:
		pass
	dialog.close()
	#match=re.compile('"contentURL" content="(.+?)"', re.DOTALL).findall(link)
	match=re.compile('"embedURL" content=".+?swf\?file=(.+?)"', re.DOTALL).findall(link)
	if match:
		try:
			#print "video link: "+str(url)
			req = urllib2.Request(match[0])
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
			response = urllib2.urlopen(req)
			link=chunk_read(response, dialog)
			#link=response.read()
			response.close()
		except:
			pass
		dialog.close()
		print link
		match=re.compile('(http://[^\]]+?mp4)', re.DOTALL).findall(link)
		if match:
			print match
			playVideo(name, match[len(match)-1])
	#print match
	#for url1 in match:
	#	playVideo(name,url1)
				
def playVideo(name, url):
	listitem = xbmcgui.ListItem(name)
	listitem.setInfo('video', {'Title': name, 'Genre': 'Video'})
	xbmc.Player( xbmc.PLAYER_CORE_MPLAYER ).play(url, listitem)
								
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


def addTopMenu():
	liz=xbmcgui.ListItem(u"Tr\u1EDF v\u1EC1 menu ch\u00EDnh>".encode('utf8'), iconImage="DefaultVideo.png", thumbnailImage="DefaultVideo.png")
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	#print "addlink:"+str(url)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=sys.argv[0],listitem=liz, isFolder=True)
	return True


def addLink(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote(name)+"&thumbnail="+urllib.quote_plus(str(iconimage))
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	#print "addlink:"+str(url)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
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
	#print match
	for url1 in match:
		addLink(name,url1, iconimage)

def Search():
	try :
		keyboard = xbmc.Keyboard('','Enter search text')
		keyboard.doModal ( )
		if (keyboard.isConfirmed()) :
				searchText = keyboard.getText()
		INDEX('http://www.nhaccuatui.com/tim-kiem/mv?q='+urllib.quote(searchText))
	except : pass

def chunk_report(bytes_so_far, chunk_size, total_size):
	 percent = float(bytes_so_far) / total_size
	 percent = round(percent*100, 2)
	 sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % 
			 (bytes_so_far, total_size, percent))
	 if bytes_so_far >= total_size:
			sys.stdout.write('\n')

def chunk_read(response, dialog, chunk_size=8192):
	#total_size = response.info().getheader('Content-Length').strip()
	total_size = 100000
	bytes_so_far = 0
	data_list = []

	while 1:
			chunk = response.read(chunk_size)
			bytes_so_far += len(chunk)

			if not chunk:
				 break
			data_list.append(chunk)
			if dialog:
				percent = float(bytes_so_far) / total_size
				percent = round(percent*100, 2)
				if (percent>100):
					percent = 100
				dialog.update(int(percent))
	return ''.join(data_list)

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

print "Mode: "+str(mode)+", URL: "+str(url)+", Name: "+str(name)+", Thumbnail: "+str(thumbnail)

if mode==None or url==None or len(url)<1:
	print ""
	CATEGORIES()
			 
elif mode==1:
	print "index: "+url
	INDEX(url)
				
elif mode==2:
	VIDEOLINKS(url,name,thumbnail)

elif mode==3:
	Search()
elif mode==4:
	playVideo(name, url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
