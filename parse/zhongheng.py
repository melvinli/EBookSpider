from bs4 import BeautifulSoup
import re
'''
    解析纵横中文网(http://www.zongheng.com/)
'''
html = '''<!doctype html>
<html>
<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="copyright" content="本页版权 www.zongheng.com 纵横中文网所有。All Rights Reserved"/>
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="shortcut icon" href="https://static.zongheng.com/favicon.ico" />
        <title>你是我的心事无弹窗,你是我的心事最新章节全文阅读,鬼先生沐沐的小说-纵横中文网</title>
        <meta name="keywords" content="你是我的心事最新章节, 你是我的心事全文阅读, 鬼先生沐 
沐的小说"/>
        <meta name="description" content="《你是我的心事》是鬼先生沐沐在纵横中文网原创首发的
都市娱乐, 鬼先生沐沐的小说你是我的心事最新章节全文阅读,请随时关注更新最快的小说网站纵横中文 
网。"/>
    <link rel="stylesheet" href="http://rcode.zongheng.com/v2018/css/basic.min.css" />      
    <link rel="stylesheet" href="http://rcode.zongheng.com/v2018/css/book.min.css" />       
</head>
<body isfemale = "0" isDoubleMonthTicketOpen = "false"  _pgid="5" scriptSign="book"  bookId="1103020" forumId="392488"  bookName="你是我的心事" catePid="9" donateRate="1" logger="/click/1099/9/1103020/0/0/52486753/2021-03-01/0/book" data-sa-w='{"event":"viewBookDetail","data":{"book_id":"1103020"}}'>

<div class="head-fixed head-simple">









<div class="wrap">
       <div class="head-top clearfix">
           <div class="logo imgbox fl"><a href="http://www.zongheng.com" data-sa-d='{"click_name":"zongheng_logo","page_module":"zongheng_logo"}'><img src="http://rcode.zongheng.com/v2018/images/logo.png" alt="logo"></a></div>
        <form name="searchForm" method="get" action="http://search.zongheng.com/s" target="_blank">
           <div class="search-box">
          <input class="search-text fl" name="keyword" type="text" placeholder="雪中悍刀行" 
autocomplete="off" disableautocomplete value="">
          <input type="submit" class="search-btn fr" >
           </div>
        </form>

           <div class="menu clearfix">
               <a href="http://www.zongheng.com" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"home"}'>首页</a>
               <div class="cate tabA">
                   <a href="##">分类<em class="icon"></em></a>
                   <div class="tabA-float cate-cell">
                       <ul>
                        <li><a href="http://www.zongheng.com/category/1.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"奇
幻玄幻","category_id":"1"}'>奇幻玄幻</a></li>
                        <li><a href="http://www.zongheng.com/category/3.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"武
侠仙侠","category_id":"3"}'>武侠仙侠</a></li>
                        <li><a href="http://www.zongheng.com/category/6.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"历
史军事","category_id":"6"}'>历史军事</a></li>
                        <li><a href="http://www.zongheng.com/category/9.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"都
市娱乐","category_id":"9"}'>都市娱乐</a></li>
                        <li><a href="http://www.zongheng.com/category/21.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":" 
竞技同人","category_id":"21"}'>竞技同人</a></li>
                        <li><a href="http://www.zongheng.com/category/15.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":" 
科幻游戏","category_id":"15"}'>科幻游戏</a></li>
                        <li><a href="http://www.zongheng.com/category/18.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":" 
悬疑灵异","category_id":"18"}'>悬疑灵异</a></li>
                        <li><a href="http://www.zongheng.com/category/40.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":" 
二次元","category_id":"40"}'>二次元</a></li>
                       </ul>
                   </div>
               </div>
               <a href="http://www.zongheng.com/rank.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"paihang"}'>排行</a>
               <a href="http://www.zongheng.com/store.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"bookStore"}'>书库</a>
               <a href="http://www.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"wanben"}'>完 
本</a>
               <a href="http://author.zongheng.com" target="_blank" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"authorArea"}'>作者专区</a>
           </div>


<div class="pay fr">
    <a class="user_pay" href="http://pay.zongheng.com" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"charge"}'>充值</a>
</div>

<div class="right-wrap-login ud_userTox">
    <div class="unlogin ud_unlogin clearfix">
        <div class="login fl"><a class="user_login" href="https://passport.zongheng.com">登 
录</a></div>
        <div class="regist fl"><a class="user_register" href="https://passport.zongheng.com/webreg">注册</a></div>
    </div>
    <div class="logon ud_loged clearfix" style="display:none;">
        <div class="user tabA imgbox">
        <img  class="ud_avatar ud_goUsrCenter" src="http://rcode.zongheng.com/v2018/images/book.png" alt="" target="_blank">
            <div class="user-blank tabA-float">
                <a href="javascript:void(0);" class="quit ud_logout">退出</a>
                <div class="user-name ud_goUsrCenter"><span class="ud_nickName"></span><em class="icon"></em></div>
                <div class="user-info clearfix">
                    <div class="user-info-cell ud_money">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_ticket">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_mticket">
                        <span class="item_loading"></span>
                    </div>
                </div>
                <a href="http://pay.zongheng.com" class="btn" target="_blank">立即充值</a>  
            </div>
        </div>
        <div class="message">
            <a href="http://home.zongheng.com/msgIn.do" class="mes" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"message"}'>消息(<span class="ud_umessage"></span>)</a>
        </div>
        <div class="shelf"><a href="http://home.zongheng.com/bookshelf" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"shelf"}'>书架</a></div>
        <div class="foot-mark tabA">
            <span class="mark clearfix">历史<em class="icon"></em></span>
            <div class="tabA-float float-mark clearfix">
                <!-- loading -->
                <div class="ud_hisloading">
                        <span class="item_loading"></span>
                </div>
                <!-- 没有记录 -->
                <div class="ud_noHistory" style="display: none">
                  <h2>亲爱的书友，您暂时没有阅读记录~</h2>
                  <div class="tips">阅读记录只保存最近阅读的5本小说</div>
                  <div class="enter"><a href="http://home.zongheng.com/bookshelf" target="_blank">进入我的书架</a></div>
                </div>
                <!-- 有记录 -->
                <div class="ud_hasHistory" style="display: none"><ul class="mark-list"></ul></div>
            </div>
        </div>
    </div>
</div>

        </div>
    </div>
</div>
    <div class="wrap">









<div class="head">
        <div class="head-top clearfix">
                <div class="logo imgbox fl">
                        <a href="http://www.zongheng.com" data-sa-d='{"click_name":"zongheng_logo","page_module":"zongheng_logo"}'><img
                                src="http://rcode.zongheng.com/v2018/images/logo.png" alt="logo"></a>
                </div>
                <form id="commSearch" name="searchForm" method="get"
                        action="http://search.zongheng.com/s" target="_blank">
                        <div class="search-box fl" data-hook="searchSuggest">
                                <input class="search-text fl" name="keyword" type="text"    
                                        placeholder="剑道第一仙" autocomplete="off" disableautocomplete /> <input
                                        type="submit" class="search-btn fr" />
                        </div>
                </form>



<div class="pay fr">
    <a class="user_pay" href="http://pay.zongheng.com" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"charge"}'>充值</a>
</div>

<div class="right-wrap-login ud_userTox">
    <div class="unlogin ud_unlogin clearfix">
        <div class="login fl"><a class="user_login" href="https://passport.zongheng.com">登 
录</a></div>
        <div class="regist fl"><a class="user_register" href="https://passport.zongheng.com/webreg">注册</a></div>
    </div>
    <div class="logon ud_loged clearfix" style="display:none;">
        <div class="user tabA imgbox">
        <img  class="ud_avatar ud_goUsrCenter" src="http://rcode.zongheng.com/v2018/images/book.png" alt="" target="_blank">
            <div class="user-blank tabA-float">
                <a href="javascript:void(0);" class="quit ud_logout">退出</a>
                <div class="user-name ud_goUsrCenter"><span class="ud_nickName"></span><em class="icon"></em></div>
                <div class="user-info clearfix">
                    <div class="user-info-cell ud_money">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_ticket">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_mticket">
                        <span class="item_loading"></span>
                    </div>
                </div>
                <a href="http://pay.zongheng.com" class="btn" target="_blank">立即充值</a>  
            </div>
        </div>
        <div class="message">
            <a href="http://home.zongheng.com/msgIn.do" class="mes" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"message"}'>消息(<span class="ud_umessage"></span>)</a>
        </div>
        <div class="shelf"><a href="http://home.zongheng.com/bookshelf" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"shelf"}'>书架</a></div>
        <div class="foot-mark tabA">
            <span class="mark clearfix">历史<em class="icon"></em></span>
            <div class="tabA-float float-mark clearfix">
                <!-- loading -->
                <div class="ud_hisloading">
                        <span class="item_loading"></span>
                </div>
                <!-- 没有记录 -->
                <div class="ud_noHistory" style="display: none">
                  <h2>亲爱的书友，您暂时没有阅读记录~</h2>
                  <div class="tips">阅读记录只保存最近阅读的5本小说</div>
                  <div class="enter"><a href="http://home.zongheng.com/bookshelf" target="_blank">进入我的书架</a></div>
                </div>
                <!-- 有记录 -->
                <div class="ud_hasHistory" style="display: none"><ul class="mark-list"></ul></div>
            </div>
        </div>
    </div>
</div>

        </div>
        <div class="nav clearfix">
                <div class="menu-left fl">

                        <a  href="http://www.zongheng.com" data-sa-d='{"click_name":"firstNav","page_module":"homePage","nav_type":"home"}'>首页<em></em></a>
                        <a  href="http://book.zongheng.com/store.html" data-sa-d='{"click_name":"firstNav","page_module":"homePage","nav_type":"bookStore"}'>书库<em></em></a>
                        <a  href="http://www.zongheng.com/rank.html" data-sa-d='{"click_name":"firstNav","page_module":"homePage","nav_type":"paihang"}'>排行<em></em></a>
                        <a  href="http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html" data-sa-d='{"click_name":"firstNav","page_module":"homePage","nav_type":"wanben"}'>完本<em></em></a>
                        <a href="http://huayu.zongheng.com" target="_blank" data-sa-d='{"click_name":"firstNav","page_module":"homePage","nav_type":"flowerGirl"}'>花语女生网<em></em></a>
                        <a  href="http://www.zongheng.com/comic.html" target="_blank" data-sa-d='{"click_name":"firstNav","page_module":"homePage","nav_type":"comic"}'>漫画<em></em></a>

                        <div class="app-menu tabA">
                                <a href="javascript:void(0);" class="phone">移动端</a>      
                                <div class="app-float tabA-float">
                                        <div class="tit">纵横小说 原创精品</div>
                                        <div class="imgbox tabC_wap">
                                                <div class="tabC" style="display: block;">  
                                                        <img src="http://rcode.zongheng.com/v2018/images/ad-float.png"
                                                                alt="">
                                                </div>
                                                <div class="tabC">
                                                        <img src="http://rcode.zongheng.com/v2018/images/ios-float.png"
                                                                alt="">
                                                </div>
                                                <div class="tabC">
                                                        <img src="http://rcode.zongheng.com/v2018/images/wx-float.png"
                                                                alt="">
                                                </div>
                                        </div>
                                        <div class="tabT_wap app-down">
                                                <span class="tabT ad active"></span> <span class="tabT ios"></span>
                                                <span class="tabT wx"></span>
                                        </div>
                                </div>
                        </div>
                </div>
                <div class="menu-right fr">
                        <a href="http://author.zongheng.com" class="author_zone" data-sa-d='{"click_name":"authorArea","page_module":"homePage"}' target="_blank">作者专区<em></em></a> 
                        <a href="http://game.zongheng.com" class="game_center" data-sa-d='{"click_name":"gameCenter","page_module":"homePage"}' target="_blank">游戏中心<em></em></a>   
                </div>
        </div>
</div>
        <!-- 1. 书封页头部广告位 -->
        <div class="com-recbox" data-sa-d='{"adv_type":"bookDetail00","adv_res":"zongheng","pos":""}'>
        <script type="text/javascript" src="http://static.zongheng.com/upload/hzds/column/240517642435.js"></script>
        </div>
        <div class="h20-blank"></div>
        <!-- 书封页start -->
        <div class="crumb">当前位置： <a href="/"> 首页 </a>> <a href="/category/9.html">都 
市娱乐 </a> >你是我的心事</div>

        <div class="book-html-box clearfix">
            <!-- 书籍详细信息 -->
            <div class="book-top clearfix">
                <div class="book-main fl">
                    <div class="book-detail clearfix">
                        <div class="book-img fl">

                        <em class=""></em>

                                <img src="http://static.zongheng.com/upload/cover/8b/e1/8be164019388819ea5366bdbf2ff1520.jpeg" alt="你是我的心事" width="200" height="264">
                        </div>
                        <div class="book-info">
                            <div class="book-name">你是我的心事




                            </div>
                            <div class="book-label">
                                <a href="http://www.zongheng.com/store/c0/c0/b0/u0/p1/v9/s0/t0/u0/i0/ALL.html" class="state" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"serial","book_id":"1103020"}'>连载中</a>
                            <a href="http://www.zongheng.com/store/c9/c0/b0/u0/p1/v9/s9/t0/u0/i0/ALL.html" class="label" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"category","book_id":"1103020"}'>都市娱乐</a>
                            <span>

                                <a href="http://search.zongheng.com/search/book?keyword=%E9%83%BD%E5%B8%82" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"keyWord","book_id":"1103020","key_word":"都市"}'>都市</a></i>

                                <a href="http://search.zongheng.com/search/book?keyword=%E7%88%BD%E6%96%87" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"keyWord","book_id":"1103020","key_word":"爽文"}'>爽文</a></i>

                                <a href="http://search.zongheng.com/search/book?keyword=%E9%9D%92%E6%98%A5" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"keyWord","book_id":"1103020","key_word":"青春"}'>青春</a></i>

                            </span>
                            </div>
                            <div class="nums"><span>字数 <i>8885 </i> </span> <span>总推荐 <i>3</i> </span> <span>总点击 <i>75</i> </span> <span>周推荐 <i>3</i> </span></div>
                            <div class="book-dec Jbook-dec hide">
                            <p>　　六月的天，六月的雨，遇见六月的你。<br>　　男主角和女主角 
在一次雨天相遇，谁也没有留意谁，然而谁能想到他们竟然会成为同班同学&nbsp;，更甚至擦出了不一样
的火花。<br>　　他是一位孤傲高冷的少年，他叫――白轩，遇见了刁蛮可爱的她，她叫――闻婷。<br>　　
终于在一场美丽的邂逅后，他们的故事开始了。<br>　　那是在一个六月的雨天&hellip;&hellip;&hellip;&hellip;。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;人生有太多太多的相遇，也有太多太多的不易
。<br>　　然而，人生处处有情，又处处有阱，许谁花前月下，为谁执掌天涯。<br>　　也许在最不经意
间、最不在意时候、最想不到的瞬间，你并为发现的那一刻，你已经爱上了她，只是你从来都没有发现而
已。<br>　　&ldquo;爱&rdquo;这个字也许那时的你很陌生，但当你发现的那一刻，可又是那么的刻苦铭
心。<br>　　人生若只如初遇，又何必秋风悲画扇啊！！！<br>　　记录&middot;爱<br>　　记录&middot;你<br>　　此书，书尾有很多关于的爱的记录语，希望书友们可以喜欢。<br>　　</p>
                            </div>
                            <div class="btn-group">
                                <a class="btn read-btn" target="_blank"  href="http://book.zongheng.com/chapter/1103020/64128052.html" data-sa-d='{"page_module":"bookDetail","click_name":"reading","book_id":"1103020"}'>开始阅读</a>
                                <div class="btn store-btn Jaddshelf" data-sa-d='{"page_module":"bookDetail","click_name":"addShelfing","book_id":"1103020"}'>加入书架</div>
                                <div class="fr link-group">
                                   <a class="all-catalog" target="_blank"  href="http://book.zongheng.com/showchapter/1103020.html" data-sa-d='{"page_module":"bookDetail","click_name":"catalogue","book_id":"1103020"}'><em></em>全部目录</a>
                                   <a class="vote" href="javascript:void(0);" id="bookDonate_openRecTicket" data-sa-d='{"page_module":"bookDetail","click_name":"recommond","vote_type":"投推荐票","book_id":"1103020"}'><em></em>投推荐票</a>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="book-new-chapter">
                        <h4>最新章节</h4>
                        <div class="tit"><a href="http://book.zongheng.com/chapter/1103020/64143932.html" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"newestChapter","book_id":"1103020"}'>第七章：兄弟吴昊</a></div>
                        <div class="con">　深夜，星空点点，银河一线，幽静而幽美，可惜的是无 
人欣赏啊！　　闻婷翻过来翻过去，怎么也睡...</div>
                        <div class="time">
                            · 5小时前<br/>
                            · 今日更新1章
                        </div>
                    </div>
                </div>
                <div class="book-side fr">
                    <div class="book-author">
                        <div class="au-head">
                            <a href="http://home.zongheng.com/show/userInfo/52486753.html" target="_blank"><img  src="https://static.zongheng.com/userimage/d3/95/d395e603233051e5db3efb5901ce527fV1_120_120.jpeg" alt="鬼先生沐沐" width="60" height="60" data-sa-d='{"page_module":"bookDetail","click_name":"author","book_id":"1103020"}'></a>
                            <em>本书作家</em>

                        </div>
                        <div class="au-name"><a href="http://home.zongheng.com/show/userInfo/52486753.html" data-sa-d='{"page_module":"bookDetail","click_name":"author","book_id":"1103020"}' >鬼先生沐沐</a></div>
                        <div class="au-words">
                            <span>作品总数<i>4</i></span>
                            <span>累计字数<i>7.1万</i></span>
                            <span>本月更新<i>3天</i></span>
                        </div>
                        <div class="au-says">
                            <h4>作者有话说</h4>

                                <div class="con empty">作者大大正在奋力码字哦~~~</div>      

                        </div>
                    </div>
                    <div class="app-in clearfix">
                        <div class="ewm" data-url="http://dl.zongheng.com/src/apk?bookId=1103020&bookName=%E4%BD%A0%E6%98%AF%E6%88%91%E7%9A%84%E5%BF%83%E4%BA%8B"><img src="http://rcode.zongheng.com/v2018/images/wx_book.png" alt="" width="80" height="79" ></div>
                        <div class="txt">
                            <h3>手机看纵横</h3>
                            <p>新用户免费看7天</p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 书籍详细信息 end-->
            <!-- 2.     一屏下广告位：双倍月票期间可以放置或者其他活动 -->
            <div class="com-recbox" data-sa-d='{"adv_type":"bookDetail01","adv_res":"zongheng","pos":""}'>
        <script type="text/javascript" src="http://static.zongheng.com/upload/hzds/column/240517642436.js"></script>
        </div>
        <div class="h20-blank"></div>
            <div class="book-main fl">

                <!-- 精彩推荐start -->
                <div class="book-recommend">
                    <h3 class="h3-tit">精彩推荐 <span class="span_r exc" id="guess_change"><em class="exc_icon"></em> 换一换</span></h3>
                    <ul class="book-recommend-list clearfix Jrecommend">
                    </ul>
                </div>
                <!-- 精彩推荐end -->
                <!-- 圈子start -->
                <div class="book-forums">
                        <h3 class="h3-tit clearfix">
                        <a class="btn fr Jpostbtn" href="javascript:void(0)" data-sa-d='{"page_module":"bookDetail","click_name":"publishThread","book_id":"1103020"}'>我要发帖</a>《你 
是我的心事》圈子
                        <a class="all-in" href="http://forum.zongheng.com/392488.html" target="_blank" data-sa-d='{"page_module":"bookDetail","click_name":"quanzi","book_id":"1103020"}'>全部帖子<i id="JthreadNum"></i><em class="arrow-r"></em></a>
                        </h3>

                                        <div class="forums-host" id="JleaderList" style="display:none">
                                            <!-- <i>暂无圈主</i>  -->
                                            <i>圈主：</i>
                                        </div>
                                        <div class="forums-txt" id="Jforums-txt">

                                        </div>

                    </div>
                 <!-- 圈子end -->
            </div>

            <div class="book-side fr">

                <!-- 此处月票榜 -->
                <!-- 月票榜start -->
                <div class="tab-lists">
                    <div class="top-title clearfix">
                        <div class="title fl">月票榜</div>
                        <div class="more fr">
                            <a class="more-link" href="http://www.zongheng.com/rank/details.html?rt=1&d=1" target="_blank">更多<em></em></a>
                        </div>
                    </div>
                    <div class="lists">
                        <ul id="monthTicketRankList">

                        </ul>
                    </div>
                </div>
                <!-- 3. 书封页右下角（月票榜下）：宽度固定，高度不限制 -->
                <div class="com-recbox" data-sa-d='{"adv_type":"bookDetail01","adv_res":"zongheng","pos":""}'>
                    <script type="text/javascript" src="http://static.zongheng.com/upload/hzds/column/240517642437.js"></script>
                </div>
            </div>
        </div>

        <!-- 书封end -->
    </div>
    <div class="footer">









<div class="partlink">
    <div class="wrap">
        <div class="title">出版合作联系</div>
        <div class="clearfix">
            <div class="mail fl">

                <div>版权合作联系人：许先生<a href="mailto:xubin@zongheng.com">xubin@zongheng.com</a></div>

                <div>广告合作联系人 : 张女士<a href="mailto:zhangwen@zongheng.com">zhangwen@zongheng.com</a></div>

            </div>

            <div class="help-btn">
                <a class="btn" href="http://www.zongheng.com/help/index.html" target="_blank">帮助中心</a>
                <p>服务时间：24小时</p>
            </div>

            <div class="b1 foot-cell">
                <div class="tit">客服</div>
                <div class="qq">4006289988</div>
                <div class="email"><a href="mailto:zhkf@zongheng.com">zhkf@zongheng.com</a></div>
            </div>
            <div class="b2 foot-cell">
                <div class="tit">举报</div>
                <div class="tel">4006289988</div>
                <div class="email"><a href="mailto:jubao@zongheng.com">jubao@zongheng.com</a></div>
            </div>

            <div class="app foot-blank">
                <div class="imgbox fl">
                    <img src="http://rcode.zongheng.com/v2018/images/app.png" alt="">       
                </div>
                <p>客户端下载</p>
            </div>

            <div class="wchat foot-blank">
                <div class="imgbox fl">
                    <img src="http://rcode.zongheng.com/v2018/images/wx.png" alt="">        
                </div>
                <p>微信公众号</p>
            </div>
        </div>
    </div>
</div>
<div class="copyright">
    <div class="links"><a href="http://www.zongheng.com/company/about.html" target="_blank">关于纵横</a>|
            <a href="http://www.zhwenxue.com/join" target="_blank">诚聘英才</a>|
            <a href="http://www.zongheng.com/company/business.html" target="_blank">商务合作
</a>|
            <a href="http://www.zongheng.com/company/copyright.html" target="_blank">法律声 
明</a>|
            <a href="http://www.zongheng.com/help/index.html" target="_blank">帮助中心</a>| 
            <a href="http://author.zongheng.com" target="_blank">作者投稿</a>|
            <a href="http://www.zongheng.com/company/contact.html" target="_blank">联系我们</a>|
            <a href="http://www.zongheng.com/company/link.html" target="_blank">友情链接</a>|
            <a href="http://news.zongheng.com/zhuanti/wlqz/index.html" target="_blank">谨防 
诈骗</a></div>
            <p>Copyright©<a href="http://www.zongheng.com" target="_blank">www.zongheng.com</a>All Rights Reserved 版权所有 北京幻想纵横网络技术有限公司
                    <a href="http://static.zongheng.com/v2018/images/zs/icp.jpg" target="_blank">京ICP证080527号</a>
                    <a href="http://www.beian.miit.gov.cn" target="_blank">京ICP备11009265号
</a>
                    <a href="http://static.zongheng.com/v2018/images/zs/jww.jpg" target="_blank">京网文[2018]10695-962号</a></p>
            <p>
                    <a href="//static.zongheng.com/v2018/images/zs/cbw20.jpg" target="_blank">新出发京零字第朝130010号</a>  丨  <a href="//static.zongheng.com/v2018/images/zs/yyzz20.jpg" target="_blank">统一社会信用代码91110105678221683F</a>  丨
                    <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502030124" target="_blank">京公网安备 11010502030124号</a>  丨
                    <a href="http://www.cyberpolice.cn/wfjb" target="_blank">公安部网络违法 
犯罪举报网站</a>  丨
            <a href="http://www.12377.cn" target="_blank">网上有害信息举报专区</a>
                </p>
    <p><a href="http://www.zongheng.com" target="_blank">纵横小说网</a>,提供<a href="http://www.zongheng.com/category/1.html" target="_blank">玄幻小说</a>,<a href="/category/9.html" target="_blank">都市小说</a>,<a href="http://huayu.zongheng.com" target="_blank">言情小说</a> 
等<a href="http://book.zongheng.com/store/c0/c0/b0/u0/p1/v0/s9/t0/u0/i1/ALL.html" target="_blank">免费小说</a>阅读。作者发布小说作品时，请遵守国家互联网信息管理办法规定。</p>
    <p>本站所收录小说作品、社区话题、书库评论均属其个人行为，不代表本站立场。</p>
</div>

<script type="text/javascript" src="http://rcode.zongheng.com/v2018/js/lib/require.min.js" defer async data-main="http://rcode.zongheng.com/v2018/js/map.min"></script>

    </div>
</body>

</html>'''

html_author = '''<!doctype html>
<html>
    <head>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="shortcut icon" href="https://static.zongheng.com/favicon.ico" />
    <title>纵横中文网</title>

    <title>纵横中文网</title>
    <link rel="stylesheet" href="http://rcode.zongheng.com/v2018/css/basic.min.css" />
    <link rel="stylesheet" href="http://rcode.zongheng.com/v2018/css/user.min.css" />

</head>

<body scriptSign="userpage" userId="52486753">
<div class="head-fixed head-simple">


<div class="wrap">








           <div class="head-top clearfix">
           <div class="logo imgbox fl"><a href="http://www.zongheng.com" data-sa-d='{"click_name":"zongheng_logo","page_module":"zongheng_logo"}'><img src="http://rcode.zongheng.com/v2018/images/logo.png" alt="logo"></a></div>
        <form name="searchForm" method="get" action="http://search.zongheng.com/s" target="_blank">
           <div class="search-box">
          <input class="search-text fl" name="keyword" type="text" placeholder="雪中悍刀行" autocomplete="off" disableautocomplete value="">
          <input type="submit" class="search-btn fr" >
           </div>
        </form>

           <div class="menu clearfix">
               <a href="http://www.zongheng.com" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"home"}'>首页</a>
               <div class="cate tabA">
                   <a href="##">分类<em class="icon"></em></a>
                   <div class="tabA-float cate-cell">
                       <ul>
                        <li><a href="http://www.zongheng.com/category/1.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"奇幻玄幻","category_id":"1"}'>奇幻玄幻</a></li>
                        <li><a href="http://www.zongheng.com/category/3.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"武侠仙侠","category_id":"3"}'>武侠仙侠</a></li>
                        <li><a href="http://www.zongheng.com/category/6.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"历史军事","category_id":"6"}'>历史军事</a></li>
                        <li><a href="http://www.zongheng.com/category/9.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"都市娱乐","category_id":"9"}'>都市娱乐</a></li>
                        <li><a href="http://www.zongheng.com/category/21.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"竞技同人","category_id":"21"}'>竞技同人</a></li>
                        <li><a href="http://www.zongheng.com/category/15.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"科幻游戏","category_id":"15"}'>科幻游戏</a></li>
                        <li><a href="http://www.zongheng.com/category/18.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"悬疑灵异","category_id":"18"}'>悬疑灵异</a></li>
                        <li><a href="http://www.zongheng.com/category/40.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"二次元","category_id":"40"}'>二次元</a></li>
                       </ul>
                   </div>
               </div>
               <a href="http://www.zongheng.com/rank.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"paihang"}'>排行</a>
               <a href="http://www.zongheng.com/store.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"bookStore"}'>书库</a>
               <a href="http://www.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"wanben"}'>完本</a>
               <a href="http://author.zongheng.com" target="_blank" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"authorArea"}'>作者专区</a>
           </div>


<div class="pay fr">
    <a class="user_pay" href="http://pay.zongheng.com" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"charge"}'>充值</a>
</div>

<div class="right-wrap-login ud_userTox">
    <div class="unlogin ud_unlogin clearfix">
        <div class="login fl"><a class="user_login" href="https://passport.zongheng.com">登录</a></div>
        <div class="regist fl"><a class="user_register" href="https://passport.zongheng.com/webreg">注册</a></div>
    </div>
    <div class="logon ud_loged clearfix" style="display:none;">
        <div class="user tabA imgbox">
        <img  class="ud_avatar ud_goUsrCenter" src="http://rcode.zongheng.com/v2018/images/book.png" alt="" target="_blank">
            <div class="user-blank tabA-float">
                <a href="javascript:void(0);" class="quit ud_logout">退出</a>
                <div class="user-name ud_goUsrCenter"><span class="ud_nickName"></span><em class="icon"></em></div>
                <div class="user-info clearfix">
                    <div class="user-info-cell ud_money">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_ticket">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_mticket">
                        <span class="item_loading"></span>
                    </div>
                </div>
                <a href="http://pay.zongheng.com" class="btn" target="_blank">立即充值</a>
            </div>
        </div>
        <div class="message">
            <a href="http://home.zongheng.com/message" class="mes" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"message"}'>消息(<span class="ud_umessage"></span>)</a>
        </div>
        <div class="shelf"><a href="http://home.zongheng.com/bookshelf" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"shelf"}'>书架</a></div>
        <div class="foot-mark tabA">
            <span class="mark clearfix">历史<em class="icon"></em></span>
            <div class="tabA-float float-mark clearfix">
                <!-- loading -->
                <div class="ud_hisloading">
                        <span class="item_loading"></span>
                </div>
                <!-- 没有记录 -->
                <div class="ud_noHistory" style="display: none">
                  <h2>亲爱的书友，您暂时没有阅读记录~</h2>
                  <div class="tips">阅读记录只保存最近阅读的5本小说</div>
                  <div class="enter"><a href="http://home.zongheng.com/bookshelf" target="_blank">进入我的书架</a></div>
                </div>
                <!-- 有记录 -->
                <div class="ud_hasHistory" style="display: none"><ul class="mark-list"></ul></div>
            </div>
        </div>
    </div>
</div>
        </div>
</div>

    </div>
    <div class="wrap">
          <div class="head-simple">








           <div class="head-top clearfix">
           <div class="logo imgbox fl"><a href="http://www.zongheng.com" data-sa-d='{"click_name":"zongheng_logo","page_module":"zongheng_logo"}'><img src="http://rcode.zongheng.com/v2018/images/logo.png" alt="logo"></a></div>
        <form name="searchForm" method="get" action="http://search.zongheng.com/s" target="_blank">
           <div class="search-box">
          <input class="search-text fl" name="keyword" type="text" placeholder="雪中悍刀行" autocomplete="off" disableautocomplete value="">
          <input type="submit" class="search-btn fr" >
           </div>
        </form>

           <div class="menu clearfix">
               <a href="http://www.zongheng.com" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"home"}'>首页</a>
               <div class="cate tabA">
                   <a href="##">分类<em class="icon"></em></a>
                   <div class="tabA-float cate-cell">
                       <ul>
                        <li><a href="http://www.zongheng.com/category/1.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"奇幻玄幻","category_id":"1"}'>奇幻玄幻</a></li>
                        <li><a href="http://www.zongheng.com/category/3.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"武侠仙侠","category_id":"3"}'>武侠仙侠</a></li>
                        <li><a href="http://www.zongheng.com/category/6.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"历史军事","category_id":"6"}'>历史军事</a></li>
                        <li><a href="http://www.zongheng.com/category/9.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"都市娱乐","category_id":"9"}'>都市娱乐</a></li>
                        <li><a href="http://www.zongheng.com/category/21.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"竞技同人","category_id":"21"}'>竞技同人</a></li>
                        <li><a href="http://www.zongheng.com/category/15.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"科幻游戏","category_id":"15"}'>科幻游戏</a></li>
                        <li><a href="http://www.zongheng.com/category/18.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"悬疑灵异","category_id":"18"}'>悬疑灵异</a></li>
                        <li><a href="http://www.zongheng.com/category/40.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"category","category_name":"二次元","category_id":"40"}'>二次元</a></li>
                       </ul>
                   </div>
               </div>
               <a href="http://www.zongheng.com/rank.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"paihang"}'>排行</a>
               <a href="http://www.zongheng.com/store.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"bookStore"}'>书库</a>
               <a href="http://www.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"wanben"}'>完本</a>
               <a href="http://author.zongheng.com" target="_blank" data-sa-d='{"click_name":"floatNav","page_module":"floatNavPage","nav_type":"authorArea"}'>作者专区</a>
           </div>


<div class="pay fr">
    <a class="user_pay" href="http://pay.zongheng.com" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"charge"}'>充值</a>
</div>

<div class="right-wrap-login ud_userTox">
    <div class="unlogin ud_unlogin clearfix">
        <div class="login fl"><a class="user_login" href="https://passport.zongheng.com">登录</a></div>
        <div class="regist fl"><a class="user_register" href="https://passport.zongheng.com/webreg">注册</a></div>
    </div>
    <div class="logon ud_loged clearfix" style="display:none;">
        <div class="user tabA imgbox">
        <img  class="ud_avatar ud_goUsrCenter" src="http://rcode.zongheng.com/v2018/images/book.png" alt="" target="_blank">
            <div class="user-blank tabA-float">
                <a href="javascript:void(0);" class="quit ud_logout">退出</a>
                <div class="user-name ud_goUsrCenter"><span class="ud_nickName"></span><em class="icon"></em></div>
                <div class="user-info clearfix">
                    <div class="user-info-cell ud_money">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_ticket">
                        <span class="item_loading"></span>
                    </div>
                    <div class="user-info-cell ud_mticket">
                        <span class="item_loading"></span>
                    </div>
                </div>
                <a href="http://pay.zongheng.com" class="btn" target="_blank">立即充值</a>
            </div>
        </div>
        <div class="message">
            <a href="http://home.zongheng.com/message" class="mes" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"message"}'>消息(<span class="ud_umessage"></span>)</a>
        </div>
        <div class="shelf"><a href="http://home.zongheng.com/bookshelf" target="_blank" data-sa-c='{"event":"clickSelf"}' data-sa-d='{"click_name":"shelf"}'>书架</a></div>
        <div class="foot-mark tabA">
            <span class="mark clearfix">历史<em class="icon"></em></span>
            <div class="tabA-float float-mark clearfix">
                <!-- loading -->
                <div class="ud_hisloading">
                        <span class="item_loading"></span>
                </div>
                <!-- 没有记录 -->
                <div class="ud_noHistory" style="display: none">
                  <h2>亲爱的书友，您暂时没有阅读记录~</h2>
                  <div class="tips">阅读记录只保存最近阅读的5本小说</div>
                  <div class="enter"><a href="http://home.zongheng.com/bookshelf" target="_blank">进入我的书架</a></div>
                </div>
                <!-- 有记录 -->
                <div class="ud_hasHistory" style="display: none"><ul class="mark-list"></ul></div>
            </div>
        </div>
    </div>
</div>
        </div>
        </div>
        <div class="user_msg user-author">
            <div class="user-head"><img src="https://static.zongheng.com/userimage/d3/95/d395e603233051e5db3efb5901ce527fV1_120_120.jpeg" alt=""></div>
            <div class="user-info">

            <a href="javascript:;" class="btn" data-id="52486753"><i>+</i>关注</a>

                <p class="name">鬼先生沐沐<b class="vip vip0"></b><span>作者</span></p>
                <p class="intro" title="酒鬼；鬼先生沐沐"><i>简介<em>|</em></i>酒鬼；鬼先生沐沐</p>

                 <p class="num">
                                    <span><i>关注<em>|</em></i><a  href="http://home.zongheng.com/show/attention/52486753.html#follow" target="_blank">0</a></span>
                                <span><i>被关注<em>|</em></i><a href="http://home.zongheng.com/show/attention/52486753.html#fans" target="_blank">0</a></span>
                                <span><i>圈子<em>|</em></i><a href="http://home.zongheng.com/show/attention/52486753.html#forum" target="_blank">4</a></span></p>

                <p class="signdate"><span>·</span>2020年06月04日 加入纵横</p>
            </div>
        </div>

        <div class="user-author-detail">
            <div class="author-tag">
            <span class="icon i00"></span>纵横作家


            </div>
            <div class="author-detail">
                <p class="author-detail-msg">纵横中文网作家。代表作有《你是我的心事》《童话镇之灵槐寺》等。</p>
                <p class="author-ach">本站作品<span>4</span>|&nbsp;&nbsp;&nbsp;&nbsp;累计字数<span>70563</span></p>
            </div>
        </div>
        <div class="h20-blank"></div>


        <div class="author-books">
            <div class="title">Ta的作品</div>
            <div class="scroll-demo book-lists">
                <!-- 滚动内容区 -->
                <div class="book-list-blank scroll-wrap">
                <!-- 滚动内容 -->
                <div class="book-lists-con">


                    <div class="list-cell clearfix">
                        <div class="imgbox"><a href="http://book.zongheng.com/book/1103020.html" target="_blank"><img src="https://static.zongheng.com/upload/cover/8b/e1/8be164019388819ea5366bdbf2ff1520.jpeg" alt="你是我的心事"></a></div>
                        <div class="list-cell-msg">
                            <p class="tit"><a href="http://book.zongheng.com/book/1103020.html" target="_blank">你是我的心事</a></p> 
                            <p class="ms"><a href="http://www.zongheng.com/category/9.html" target="_blank">都市娱乐</a><span>|</span>连载中<span>|</span>8885</p>
                            <p class="ac" title="　　六月的天，六月的雨，遇见六月的你。
　　男主角和女主角在一次雨天相遇，谁也没有留意谁，然而谁能想到他们竟然会成为同班同学 ，更甚至擦出了不一样的火花。
　　他是一位孤傲高冷的少年，他叫――白轩，遇见了刁蛮可爱的她，她叫――闻婷。
　　终于在一场美丽的邂逅后，他们的故事开始了。
　　那是在一个六月的雨天&hellip;&hellip;&hellip;&hellip;。
      人生有太多太多的相遇，也有太多太多的不易。
　　然而，人生处处有情，又处处有阱，许谁花前月下，为谁执掌天涯。
　　也许在最不经意间、最不在意时候、最想不到的瞬间，你并为发现的那一刻，你已经爱上了她，只是你从来都没有发现而已。
　　&ldquo;爱&rdquo;这个字也许那时的你很陌生，但当你发现的那一刻，可又是那么的刻苦铭心。
　　人生若只如初遇，又何必秋风悲画扇啊！！！
　　记录&middot;爱
　　记录&middot;你
　　此书，书尾有很多关于的爱的记录语，希望书友们可以喜欢。
　　">　　六月的天，六月的雨，遇见六月的你。
　　男主角和女主角在一次雨天相遇，谁也没有留意谁，然而谁能想到他们竟然会成为同班同学 ，更甚至擦出了不一样的火花。
　　他是一位孤傲高冷的少年，他叫――白轩，遇见了刁蛮可爱的她，她叫――闻婷。
　　终于在一场美丽的邂逅后，他们的故事开始了。
　　那是在一个六月的雨天&hellip;&hellip;&hellip;&hellip;。
      人生有太多太多的相遇，也有太多太多的不易。
　　然而，人生处处有情，又处处有阱，许谁花前月下，为谁执掌天涯。
　　也许在最不经意间、最不在意时候、最想不到的瞬间，你并为发现的那一刻，你已经爱上了她，只是你从来都没有发现而已。
　　&ldquo;爱&rdquo;这个字也许那时的你很陌生，但当你发现的那一刻，可又是那么的刻苦铭心。
　　人生若只如初遇，又何必秋风悲画扇啊！！！
　　记录&middot;爱
　　记录&middot;你
　　此书，书尾有很多关于的爱的记录语，希望书友们可以喜欢。
　　</p>
                            <p class="recent"><a href="http://book.zongheng.com/chapter/1103020/64143932.html" target="_blank">最新章
节：<span>第七章：兄弟吴昊</span></a></p>
                            <p class="date">03-04 10:12</p>
                        </div>
                        <a class="read" href="http://book.zongheng.com/chapter/1103020/64128052.html" target="_blank">立即阅读</a>   

                        <a class="add" data-bookid="1103020" href="javascript:;" >加入书架</a>

                    </div>

                    <div class="list-cell clearfix">
                        <div class="imgbox"><a href="http://book.zongheng.com/book/1086597.html" target="_blank"><img src="https://static.zongheng.com/upload/cover/16/b0/16b06c9e4d54ac4859a9b105406d5780.jpeg" alt="童话镇之灵槐寺"></a></div>
                        <div class="list-cell-msg">
                            <p class="tit"><a href="http://book.zongheng.com/book/1086597.html" target="_blank">童话镇之灵槐寺</a></p>
                            <p class="ms"><a href="http://www.zongheng.com/category/18.html" target="_blank">悬疑灵异</a><span>|</span>连载中<span>|</span>5889</p>
                            <p class="ac" title="我们的故事从这里开始，但从来不会在这里结束。
　　这是一个充满奇幻的镇子，而我们的故事就才这个镇子讲起。
　　这个镇子便叫童话镇。
　　
　　《童话镇之灵槐寺》
　　灵槐山上灵槐寺，灵槐寺中灵槐树，灵槐树下灵槐洞，灵槐洞里灵槐河，灵槐河下灵槐村，我们的故事就从这个村子讲起。">我们的故事从这里开 
始，但从来不会在这里结束。
　　这是一个充满奇幻的镇子，而我们的故事就才这个镇子讲起。
　　这个镇子便叫童话镇。
　　
　　《童话镇之灵槐寺》
　　灵槐山上灵槐寺，灵槐寺中灵槐树，灵槐树下灵槐洞，灵槐洞里灵槐河，灵槐河下灵槐村，我们的故事就从这个村子讲起。</p>
                            <p class="recent"><a href="http://book.zongheng.com/chapter/1086597/64140783.html" target="_blank">最新章
节：<span>第五章：天降异象</span></a></p>
                            <p class="date">03-03 21:18</p>
                        </div>
                        <a class="read" href="http://book.zongheng.com/chapter/1086597/63674577.html" target="_blank">立即阅读</a>   

                        <a class="add" data-bookid="1086597" href="javascript:;" >加入书架</a>

                    </div>

                    <div class="list-cell clearfix">
                        <div class="imgbox"><a href="http://book.zongheng.com/book/1069171.html" target="_blank"><img src="https://static.zongheng.com/upload/cover/79/88/79887a05e5c660f5c5018f8c7b6bd0d5.jpeg" alt="童话镇之仙情篇"></a></div>
                        <div class="list-cell-msg">
                            <p class="tit"><a href="http://book.zongheng.com/book/1069171.html" target="_blank">童话镇之仙情篇</a></p>
                            <p class="ms"><a href="http://www.zongheng.com/category/35.html" target="_blank">短篇美文</a><span>|</span>已完结<span>|</span>39104</p>
                            <p class="ac" title="　　我们的故事从这里开始，但从来不会在这里结束。
　　这是一个充满奇幻的镇子，而我们的故事就才这个镇子讲起。
　　这个镇子便叫童话镇。
　　
　　《童话镇之仙情篇》篇一：
　　
　　她是一位仙子，经过凡间时，爱上一位凡人，从此他们的坎坷之路便开始了，这就是所谓的一见钟情吧！
　　
　　《童话镇之仙情篇》篇二：
　　
　　她是朵荷花仙，一次被一位少年所救，经过少年的精心照顾后，对少年产生了爱慕之意，这便是所谓的日久生情吧！">　　我们的故事从这里开始 
，但从来不会在这里结束。
　　这是一个充满奇幻的镇子，而我们的故事就才这个镇子讲起。
　　这个镇子便叫童话镇。
　　
　　《童话镇之仙情篇》篇一：
　　
　　她是一位仙子，经过凡间时，爱上一位凡人，从此他们的坎坷之路便开始了，这就是所谓的一见钟情吧！
　　
　　《童话镇之仙情篇》篇二：
　　
　　她是朵荷花仙，一次被一位少年所救，经过少年的精心照顾后，对少年产生了爱慕之意，这便是所谓的日久生情吧！</p>
                            <p class="recent"><a href="http://book.zongheng.com/chapter/1069171/63486939.html" target="_blank">最新章
节：<span>第三十六章：终</span></a></p>
                            <p class="date">12-08 15:55</p>
                        </div>
                        <a class="read" href="http://book.zongheng.com/chapter/1069171/63067631.html" target="_blank">立即阅读</a>   

                        <a class="add" data-bookid="1069171" href="javascript:;" >加入书架</a>

                    </div>

                    <div class="list-cell clearfix">
                        <div class="imgbox"><a href="http://book.zongheng.com/book/1055753.html" target="_blank"><img src="https://static.zongheng.com/upload/cover/31/13/31132f2b5e9d99708308cd9ad5253c2a.jpeg" alt="童话镇之殪琥蛐篇"></a></div>
                        <div class="list-cell-msg">
                            <p class="tit"><a href="http://book.zongheng.com/book/1055753.html" target="_blank">童话镇之殪琥蛐篇</a></p>
                            <p class="ms"><a href="http://www.zongheng.com/category/35.html" target="_blank">短篇美文</a><span>|</span>已完结<span>|</span>16685</p>
                            <p class="ac" title="我们的故事从这里开始，但从来不会在这里结束。
　　这是一个充满奇幻的镇子，而我们的故事就从这个镇子讲起。
　　这个镇子便叫童话镇。
　　
　　童话镇之殪琥蛐篇
　　
　　殪琥蛐是一种以吃人为生的生物，似人非人，有着人的身体，蜥蜴的面容，蛐的翼，善于飞翔，最主要是可以幻化成人的模样。
　　他弑杀成性，但颇喜赌约。">我们的故事从这里开始，但从来不会在这里结束。
　　这是一个充满奇幻的镇子，而我们的故事就从这个镇子讲起。
　　这个镇子便叫童话镇。
　　
　　童话镇之殪琥蛐篇
　　
　　殪琥蛐是一种以吃人为生的生物，似人非人，有着人的身体，蜥蜴的面容，蛐的翼，善于飞翔，最主要是可以幻化成人的模样。
　　他弑杀成性，但颇喜赌约。</p>
                            <p class="recent"><a href="http://book.zongheng.com/chapter/1055753/62713584.html" target="_blank">最新章
节：<span>第十五章：终</span></a></p>
                            <p class="date">09-15 17:37</p>
                        </div>
                        <a class="read" href="http://book.zongheng.com/chapter/1055753/62554216.html" target="_blank">立即阅读</a>   

                        <a class="add" data-bookid="1055753" href="javascript:;" >加入书架</a>

                    </div>


                    <div class="correct-bot"></div>
                </div>
                <!-- 滚动条 -->
                <!--div class="book-lists-wheel scroll-bar" style="display:none;"><span class="bar scroll-slider"></span></div-->    
                </div>

                <div class="list-cell-more"><a href="javascript:;">全部作品</a></div>

            </div>
        </div>

        <div class="h40-blank"></div>
        <nav class="nav-tab">
            <i class="trends"><a href="#trends">动态</a></i>
            <i class="invitation"><a href="#invitation">帖子</a></i>
            <i class="read"><a href="#read">阅读</a></i>
            <i class="support"><a href="#support">捧场</a></i>
        </nav>
        <div class="nav-content"></div>
    </div>
    <div class="h40-blank"></div>
    <div class="footer">








<div class="partlink">
    <div class="wrap">
        <div class="title">出版合作联系</div>
        <div class="clearfix">
            <div class="mail fl">

                <div>版权合作联系人：许先生<a href="mailto:xubin@zongheng.com">xubin@zongheng.com</a></div>

                <div>广告合作联系人 : 张女士<a href="mailto:zhangwen@zongheng.com">zhangwen@zongheng.com</a></div>

            </div>
            <div class="help-btn">
                <a class="btn" href="http://www.zongheng.com/help/index.html" target="_blank">帮助中心</a>
                <p>服务时间：24小时</p>
            </div>

            <div class="b1 foot-cell">
                <div class="tit">客服</div>
                <div class="qq">4006289988</div>
                <div class="email"><a href="mailto:zhkf@zongheng.com">zhkf@zongheng.com</a></div>
            </div>
            <div class="b2 foot-cell">
                <div class="tit">举报</div>
                <div class="tel">4006289988</div>
                <div class="email"><a href="mailto:jubao@zongheng.com">jubao@zongheng.com</a></div>
            </div>

            <div class="app foot-blank">
                <div class="imgbox fl">
                    <img src="http://rcode.zongheng.com/v2018/images/app.png" alt="">
                </div>
                <p>客户端下载</p>
            </div>

            <div class="wchat foot-blank">
                <div class="imgbox fl">
                    <img src="http://rcode.zongheng.com/v2018/images/wx.png" alt="">
                </div>
                <p>微信公众号</p>
            </div>
        </div>
    </div>
</div>
<div class="copyright">
    <div class="links"><a href="http://www.zongheng.com/company/about.html" target="_blank">关于纵横</a>|<a href="http://www.zhwenxue.com/join" target="_blank">诚聘英才</a>|<a href="http://www.zongheng.com/company/business.html" target="_blank">商务合作</a>|<a href="http://www.zongheng.com/company/copyright.html" target="_blank">法律声明</a>|<a href="http://www.zongheng.com/help/index.html" target="_blank">帮助中心</a>|<a href="http://author.zongheng.com" target="_blank">作者投稿</a>|<a href="http://www.zongheng.com/company/contact.html" target="_blank">联系我们</a>|<a href="http://www.zongheng.com/company/link.html" target="_blank">友情链接</a>|<a href="http://news.zongheng.com/zhuanti/wlqz/index.html" target="_blank">谨防诈骗</a>|<a href="http://www.zongheng.com/company/sitemap.html" target="_blank">网站地图</a></div>
    <p>Copyright©<a href="http://www.zongheng.com" target="_blank">www.zongheng.com</a>All Rights Reserved 版权所有 北京幻想纵横网络 
技术有限公司   京ICP证：080527号《网络文化经营许可证》   <a href="http://www.beian.miit.gov.cn" target="_blank">京ICP备11009265号</a>   <a href="http://static.zongheng.com/images/license/business-license.jpg" target="_blank">京网文[2015]2368-459号</a></p>
    <p>新出发京零字第朝130010号  丨  统一社会信用代码91110105678221683F  丨 <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502030124" target="_blank">京公网安备         11010502030124号</a>  丨 <a href="http://www.cyberpolice.cn/wfjb/" target="_blank">公安部网络违法犯罪举报网站</a></p>
    <p><a href="http://www.zongheng.com" target="_blank">纵横小说网</a>,提供<a href="http://www.zongheng.com/category/1.html" target="_blank">玄幻小说</a>,<a href="/category/9.html" target="_blank">都市小说</a>,<a href="http://huayu.baidu.com" target="_blank">言情小
说</a>等<a href="http://book.zongheng.com/store/c0/c0/b0/u0/p1/v0/s9/t0/u0/i1/ALL.html" target="_blank">免费小说</a>阅读。作者发布小 
说作品时，请遵守国家互联网信息管理办法规定。</p>
    <p>本站所收录小说作品、社区话题、书库评论均属其个人行为，不代表本站立场。</p>
</div>

<script type="text/javascript" src="http://rcode.zongheng.com/v2018/js/lib/require.min.js" defer async data-main="http://rcode.zongheng.com/v2018/js/map.min"></script>

    </div>
    <div class="backToTop">
        <div class="sidekf">
            <a href="#"></a>
        </div>
        <div class="returntop">
            <a href="javascript:;"></a>
        </div>
    </div>
</body>
</html>'''
class ParseZhongheng:

    '''解析书籍基本信息'''
    def parse_book_details(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # 书名
        book_name = soup.find("div", class_="book-name").text.strip()
        # 书简介
        book_desc = soup.find("div", class_="book-dec Jbook-dec hide").find("p").text
        # 作者节点标签
        author_label = soup.find("div", class_="au-name").find("a")
        # 作者名称
        book_author = author_label.text.strip()
        # 作者Url
        book_author_url = author_label["href"]
        # 标签
        labels = soup.find("div", class_="book-label").find("span").find_all("a")
        # 封面地址
        book_corver = soup.find("img", alt=book_name)["src"]
        # 目录地址
        book_chapter_url = soup.find("a", class_="all-catalog")["href"]
        # 书籍字数
        book_text_count = soup.find("div",class_="nums").find("span").text
        

        # print(book_name)
        # print(book_desc)
        # print(book_author)
        # print(book_author_url)
        # for a in labels:
        #     print(a.text)
        # print(book_corver)
        # print(book_chapter_url)
        print(re.findall(r"\d+", book_text_count)[0]) # 正则提取数字
        
    '''解析作者页面信息'''
    def parse_author(self, html_author):
        soup = BeautifulSoup(html_author, "html.parser")

        # 关于作者
        author_about = soup.find("p", class_="author-detail-msg").text
        # 作者累计字数
        author_write_count = soup.find("p", class_="author-ach").find_all("span")[-1].text
        # TODO 作者的作品列表

        # print(author_about)
        print(author_write_count)


ad = ParseZhongheng()
# ad.parse_book_details(html)
ad.parse_author(html_author)