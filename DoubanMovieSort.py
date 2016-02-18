#!/bin/python2.7
# -*- coding:utf-8 -*-

'''
#           Douban Movie Top250                         #
#       github.com/alanzjl/DoubanMovieSort              #
#===================================================    #
#       Douban movies are coming!                       #
#       Douban Movie Top250 are sorted by combined      #
#   method, which means not only user-rates are consi-  #
#   dered. Thus some splendid but old movies ranks lower#
#   than some new movies. I feel really angry. So here  #
#   comes this script                                   #
'''

import re
import urllib

class book:
    title = ""
    author = ""
    url = ""
    img = ""
    rate = ""
    quote = ""

    def __init__(self, Title, Author, Url, Img, Rate, Quote):
        self.title = Title
        self.author = Author
        self.url = Url
        self.img = Img
        self.rate = Rate
        self.quote = Quote

    def content(self):
        return "Title:%s\tAuthor:%s\tUrl:%s\tImg:%s\tRate:%s\tQuote:%s\n"\
              %(self.title,self.author,self.url,self.img,self.rate,self.quote)

def finder(page, pat):
    content = re.search(pat,page)
    if not content:
        print "Failed in url"
        exit(1)
    return content.group()

def makeHtml(blist,path):
    fp = open(path,'w+')
    Start = '''<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="unsafe-url">
    <title>
豆瓣电影TOP250
</title>

    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">

    <link rel="apple-touch-icon" href="/pics/movie/apple-touch-icon.png">
    <link href="http://img3.douban.com/f/shire/bdb62d45fb145651da30ac3fec98f21c40cfc962/css/douban.css" rel="stylesheet" type="text/css">
    <link href="http://img3.douban.com/f/shire/905cdec30f13cd440e6f988dc5d2d99919f5a1d5/css/separation/_all.css" rel="stylesheet" type="text/css">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="http://img3.douban.com/f/movie/e9d9543ebc06f2964039a2e94898f84ce77fc070/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="http://img3.douban.com/f/shire/07f5c81e9c7fcdd676bf2078c79d6c5ffbb93b80/js/douban.js"></script>
    <script type="text/javascript" src="http://img3.douban.com/f/shire/0a62663763aed4fe860029f99d1755b8caa524e7/js/separation/_all.js"></script>

<link href="http://img3.douban.com/f/movie/dcfd6c93a0b44f2495c6ab3cdf21d8508b97bb03/css/movie/top_movies.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="http://img3.douban.com/f/shire/29449d396dacb28fd9949c709ccf02a46b910156/js/do.js" data-cfg-autoload="false"></script>
<script type='text/javascript'>
    Do.ready(function(){
            $("#mine-selector input[type='checkbox']").click(function(){
                var val = $(this).is(":checked")?$(this).val():"";
                window.location.href = '/top250?filter=' + val;
            })
    })
</script>

    <style type="text/css">
.site-nav-logo img{margin-bottom:0;}
</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="http://img3.douban.com/misc/mixed_static/3e426057637c9d1b.css">

    <link rel="shortcut icon" href="http://img3.douban.com/favicon.ico" type="image/x-icon">
</head>

<body>

    <script type="text/javascript">var _body_start = new Date();</script>


<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="http://movie.douban.com">豆瓣电影</a>
    </div>

  </div>
  </div>
</div>

    <div id="wrapper">
    <div id="content">

    <h1>豆瓣电影TOP250逆序 | Alanzjl</h1>

        <div class="grid-16-8 clearfix">


            <div class="article">

<ol class="grid_view">'''
    End = '''</ol>
            </div>
            <div class="extra">
            </div>
        </div>
    </div>
    <div id="footer">
            <div class="footer-extra"></div>
<span id="icp" class="fleft gray-link">
    &copy; 2005－2016 douban.com, all rights reserved 北京豆网科技有限公司
</span>
</body>
</html>'''
    fp.write(Start)
    count = 1;
    for i in blist:
        url = i.url
        title = i.title
        img = i.img
        author = i.author
        rate = i.rate
        quote = i.quote

        content = '''<li>
            <div class="item">
                <div class="pic">
                    <em class="">'''+'%s'%count+'''</em>
                    <a href="http://movie.douban.com/subject/1292052/">
                        <img alt="''' + title + '''" src="'''+img+'''" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="'''+url+'''" class="">
                            <span class="title">'''+title+'''</span>
                    </div>
                    <div class="bd">
                        <p class="">'''+author+'''</p>
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">'''+rate+'''</span>
                                <span property="v:best" content="10.0"></span>
                        </div>

                            <p class="quote">
                                <span class="inq">'''+quote+'''</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>'''
        fp.write(content)
        fp.write('\n\n\n')
        count+=1
    fp.write(End)


def run():
    count = 0
    run_times = 0;
    while count < 250:
        url = 'http://movie.douban.com/top250?start=%d&filter='%count
        page = urllib.urlopen(url).read()

        titlePat = re.compile(r'(?<=<span class="title">).*?(?=</span>)')
        authorPat = re.compile(r'''(?<= <div class="bd">
                        <p class="">
).*?(?=</p>)''',re.S)
        urlPat = re.compile(r'''(?<=<div class="hd">
                        <a href=").*?(?=" class="">)''',re.S)
        imgPat = re.compile(r'http://img3.*?\.jpg',re.M)
        ratePat = re.compile(r'(?<=<span class="rating_num" property="v:average">).*?(?=</span>)',re.S)
        quotePat = re.compile(r'''(?<= <p class="quote">
                                <span class="inq">).*?(?=</span>)''',re.S)

        open('12345','w+').write(page)
        title = finder(page, titlePat)
        author = finder(page, authorPat)
        url = finder(page, urlPat)
        img = finder(page, imgPat)
        rate = finder(page, ratePat)
        quote = finder(page, quotePat)

        #print "%s %s %s %s %s\n"%(len(title),len(author),len(url),len(img),len(rate))
        newBook = book(title, author, url, img, rate, quote)
        bookList.append(newBook)
        print "%s: "%count
        print newBook.content(),

        count += 1

bookList = []
run()
bookListSorted = sorted(bookList, key=lambda ele:ele.rate, reverse=1)

makeHtml(bookListSorted,'DoubanMovie.html');

fp = open('123','w+')
count = 1
for i in bookListSorted:
    fp.write("%s: "%count)
    fp.write(i.content())
    count+=1
#print rateList


