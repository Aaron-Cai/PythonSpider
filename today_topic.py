# coding: utf-8
import urllib2,urllib,re,time,thread,gzip,cStringIO

url_intouchtoday = 'http://view.news.qq.com/original/intouchtoday/n'

no = 3034

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
headers = { 'User-Agent' : user_agent }

req = urllib2.Request(url_intouchtoday+str(no)+'.html',headers = headers)
myResponse = urllib2.urlopen(req)
myPage = myResponse.read()

if myPage[:6] == '\x1f\x8b\x08\x00\x00\x00':
	myPage = gzip.GzipFile(fileobj = cStringIO.StringIO(myPage)).read()

unicodePage = myPage.decode("gbk").encode('utf-8').decode('utf-8')
#print unicodePage

title = re.findall('<div class="hd"><h1>(.*?)</h1></div>',unicodePage,re.S)[0]
daoyu = re.findall('<span class="tit"></span>(.*?)<a href="',unicodePage,re.S)[0]
daoyu = daoyu.replace('\n','')
daoyu = daoyu.strip()
print title,'\n'
print daoyu,'\n\n\n'

article = re.findall('<p data-page-model="text">(.*?)</p>',unicodePage,re.S)
for p in article:
	print p,'\n'

header2 = re.findall('<h2 data-page-model="title">(.*?)</h2>',unicodePage,re.S)
for h in header2:
	print h,'\n'





