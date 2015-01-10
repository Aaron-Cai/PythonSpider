# -*- coding: utf-8 -*-  
import urllib2,urllib,string
###########################################################################################################
# response = urllib2.urlopen('http://www.baidu.com')
# html = response.read()

# print html

# values = {'name':'WHY',
# 			'location':'SDU',
# 			'language':'Python'}

# data = urllib.urlencode(values)
# print data
############################################################################################################
# urlbaidu = 'http://www.baidu.com/s?wd='
# url404 = 'http://bbs.csdn.net/callmewhy'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 6; Windows NT)'


# headers = {'User-Agent':user_agent}



# try:
# 	response = urllib2.urlopen(urlbaidu+'camera')
# except urllib2.URLError,e:
# 	if hasattr(e,'reason'):
# 		print 'Failed to reach the server for the reason below:'
# 		print e.reason
# 	if hasattr(e,'code'):
# 		print 'Error code: ',e.code

# print response.info()
# print response.geturl()
# the_page = response.read()
# # print the_page[:5000]
# open("page.html",'w').write(the_page)
########################################################################################################

# import urllib2

# # 创建一个密码管理者
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# # 添加用户名和密码

# top_level_url = "http://example.com/foo/"

# # 如果知道 realm, 我们可以使用他代替 ``None``.
# # password_mgr.add_password(None, top_level_url, username, password)
# password_mgr.add_password(None, top_level_url,'why', '1223')

# # 创建了一个新的handler
# handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# # 创建 "opener" (OpenerDirector 实例)
# opener = urllib2.build_opener(handler)

# a_url = 'http://www.baidu.com/'

# # 使用 opener 获取一个URL
# opener.open(a_url)

# # 安装 opener.
# # 现在所有调用 urllib2.urlopen 将用我们的 opener.
# urllib2.install_opener(opener)
###################################################################################################
# import urllib2

# user_agent = 'Mozilla/4.0 (compatible; MSIE 6; Windows NT)'
# headers = {'User-Agent':user_agent}


# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)
# url = 'http://www.baidu.com'
# req = urllib2.Request(url = url,headers = headers)
# response = urllib2.urlopen(req)
###################################################################################################

def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
		sName = string.zfill(i,5) + '.html'
		print 'downloading ' + str(i) + ' page and saving it as ' + sName + 'from '+url+str((i-1)*50)+'......'
		m = urllib2.urlopen(url+str((i-1)*50)).read()
		open(sName,'w').write(m)

bdurl = str(raw_input(u'link:\n'))
begin_page = int(raw_input(u'begin:\n'))
end_page = int(raw_input(u'end:\n'))

baidu_tieba(bdurl,begin_page,end_page)
 

