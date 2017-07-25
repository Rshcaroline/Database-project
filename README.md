# Database-project

# 开发环境
    Python 3.5.2 |Anaconda 4.2.0 (x86_64) 
    mysql  Ver 14.14 Distrib 5.7.17 
    Django 1.11.0

# 简介
复旦大学计算机科学技术学院与上海高中交流辅导平台是由复旦大学计算机科学技术学院分团委学生会青志实践中心为主办单位，旨在扩大复旦大学计算机科学技术学院影响力、加强上海市各高中与复旦大学计算机学院的交流、丰富计算机学院老师及学生的生活、深化学院学生对知识的理解的一个交流平台，它主要具备“新闻速递”、“科技创新及竞赛辅导预约”、“教授讲座预约”、“复旦科技工作站参观预约”这四个功能。

# 管理权限声明
为保证老师及学生们的隐私，仅为每个高中学校提供一个用户账号，也仅仅与学院建立合作的高中可以登录使用该网站。
# 概念设计ER图

## 关系模式
共12个关系模式

### register相关表
#### 用户基本信息：
	User (id, username, password)

### news 相关表
#### 新闻：
    News (id, title, author, content, created, category_id)
#### 新闻分类：
    Category (id, name)
#### 新闻标签：
    Tag (id, name)
#### 新闻与其对应的标签：（一条新闻可以对应多个标签，一对多）
    News_Tags (id, news_id, tag_id)
#### 评论：（一条评论只能对应一条新闻，所以只用加一个外码约束）
    Comment (id, name, email, content, created, news_id)

### appointment 相关表
#### ACM竞赛生个人信息
    Acm (id, member, gender, major, phone, email, awards, introduction)
####	讲座信息
    Lecture (id, theme, professor, introduction, place, time)
####	科技站项目信息
    Station (id, project_name, introduction)
####	预约信息
    appoint_acm (id, start_time, people, name,email, acm_id) 
    appoint_lecture (id, start_time, people, name, email, lecture_id) 
    appoint_station (id, start_time, people, name, email, station_id)
##	ER图
 
#	功能详解
##	用户注册登陆
用户注册时必须使用未注册过的邮箱进行注册，邮箱查重由前后端共同完成，表单验证（如，密码是否过长，邮箱格式是否正确，选项是否为空等）使用Javascript前端进行，利用Django自带的表单功能做到不刷新页面也可以提示用户进行操作。
	 

##	新闻速递
### 简介
这一部分将会展示一些复旦大学计算机科学技术学院近期的新闻，包括“学生活动”、“重要通知”、“招聘信息”、“招生工作”等。
### news-list
#### 设计思路：
首先要做的就是通过需求来建立模型，即 Model 层，它决定了数据的存取，类似于我们数据库的Tables。 <br>
需求： <br>
新闻拥有标题、作者、正文及发布的时间等基本的元素。同时，一个新闻还会隶属于一个分类，并可能包含一个或多个标签。新闻也可以有一个或多个评论，评论中要记录评论者的称呼、邮箱以及评论内容。 <br>
从中可以看出： <br>
1.	直接与新闻相关的模型应包含三个：新闻、分类以及标签。新闻包含标题、作者、正文、发布时间等基础字段。分类和标签则应有名称； <br>
2.	一个新闻仅隶属于一个分类，反过来一个分类则可以包含多个新闻，这是明显的一对多的关系，因此新闻中应有一个外键关联至分类； <br>
3.	一个新闻可能包含一个或多个标签，反过来一个标签页会包含多个新闻，因此是多对多的关系； <br>
4.	还有一个评论模型来存储用户评论，并主动关联到新闻上去。一个新闻可以有一个或多个评论，但反过来评论只针对一篇新闻，因此也是一对多的关系。 <br>

通过前面所做的各种铺垫，我们现在可以来专注功能的实现了，即剩下的 View 层和 Template 层。这一部分我们着重关注新闻列表页。 <br>
首先来回顾一下需求： <br>
需要有一个“新闻列表”页来呈现发布的新闻。新闻要按发布时间的倒序来排列，每个新闻都要包含标题、作者、分类、发布时间的显示（年-月-日 时:分）及节选的正文内容（前 40 个字）。点击单独的新闻可以进入其详情页。 <br>
接下来建立视图层，视图就是所谓的 V 层，它负责分析并处理来自用户的请求，然后返回所需的结果。“新闻列表”的视图显然是将数据库中的数据按需求中所需的发布时间的倒序取出，然后构造模板，最终将结果返回给用户。 <br>
如此构成了我的news-list页。 <br>

### news-detail
detail界面显示这则新闻的详情，包括标题、作者、分类、发布时间的显示（年-月-日 时:分）、正文内容，以及评论。

### 评论功能
在news-detail界面有一个评论功能，一是把这条新闻对应的评论都输出显示出来，二是可以在下方添加评论，通过表单功能直接从前端传回后端数据库存起来。

##	预约功能
### 竞赛辅导预约
#### 背景：
每年高中都会有科技创新类竞赛或计算机竞赛，很多竞赛较多的高中（如：华师大二附中）特别需要有计算机竞赛经验的学生去辅导，科技创新比赛也需要有大学生一起加入进去，去实现各种想法，但缺少与计算机学院联系的渠道。
#### 形式：
前期对计算机科学技术学院的学生尤其是ACM队队员进行宣传，招收有想法加入到科技创新及竞赛辅导队伍中的学生，将各个有意愿的同学的姓名、照片及竞赛经历存入Acm这个Table，放在网站上，并留下预约按钮，有需求的高中同学，通过学校的网站负责人登录网站查看，选择感兴趣的大学辅导人员，并留下预约信息。由青志部的部员联系对方，安排进一步的辅导。
#### 对象：
以ACM队成员或有计算机竞赛经验的同学为主，其他计算机学院同学为辅

### 讲座预约
#### 背景：
上海市很多高中都希望复旦大学计算机学院的教授可以到高中进行科普类的讲座，但部分高中在学期初就需要将本学期中所有的讲座提前排好（如：杨浦高中），或者需要讲座但没有预约渠道，急需要一个平台。
#### 形式：
前期经过学院的同意，联系计算机学院7大研究方向的愿意办讲座的教授们，并将教授的姓名、照片及研究方向，放在网站上，或者直接将目前已有的一些讲座信息存入Lecture这个Table，放到网上，设置预约按钮，由高中负责人选择感兴趣的教授，填上预约的学校，所要预约的讲座的时间、地点，这些信息同样反馈到青志部部员，再由青志部的同学找到教授协商讲座时间。
#### 对象：
计算机学院教授

### 科技站参观预约
#### 背景：
各个高中希望与复旦大学计算机学院有进一步的联系交流，复旦大学计算机科学技术学院科技工作站可以提供前沿科技产品的参观体验活动，也欢迎更多的同学来参观。                                                                                                                                                              
#### 形式：
网站上放上科技工作站的介绍，并设有预约按钮，由高中负责人填写参观时间、人数，青志部协商时间。


#		感想及实用性分析
###	感想
从五一节开始准备，到六月初写完，整个project耗时一个月。 <br>
一开始在网上查了大量的资料之后，果断放弃了用得不太熟练的java，也放弃了传说中好用的框架flask，最终决定了选择Python+Django的框架来实现这个网页。 <br>
在配置开发环境的时候遇到了很多问题，比如mysql的调用路径不对、数据库连接不上等等，在这里就不多述了。真的，花了整个五一节都在装开发环境和照着官方的tutorial走一遍教程，不断的搜各种解决方法，不知道往电脑上装了多少乱七八糟的东西。最坑人的一点大概是，网上有非常多教程，但是几乎都没有一个注明了版本，很多解决方案跟我的版本不同，导致很多命令我这边终端根本识别不了，可以说是踩了不少的坑。 <br>

在分析要实现一个什么网页和建立一个什么数据库的时候，我想到了我在学生会分管的青志实践部其实一直有一个需求，想要建立一个与上海的高中进行交流沟通的平台，因为他们需要我们学院的ACM队的同学去为他们进行竞赛辅导，我们的确也做到了派出学生进行每周一次的辅导。但是还希望能扩大一些功能，除了竞赛辅导预约ACM队的成员以外，还希望有类似于预约教授讲座，预约科技站的参观与讲解，公布计算机学院的一些近期的新闻等。 <br>
所以最终我选定了写一个“复旦大学计算机科学技术学院与上海高中交流辅导平台”，也就有了这个网站。 <br>
在写网站的过程中也出了不少的bug，比如写project已经实现了一些功能之后，我发现一输入中文数据库就炸。查了半天资料才发现之前我照着tutorial走的那个教程建的数据库是只能存英文的，于是又从头开始建库建表。mysql> create database databasepj default character set utf8; 因为要插入中文，所以创建时字符集设为utf8，还要注意SQL语句后面的分号。 <br>
比如经常调UI就调一个下午，比如自带的表单的传输和样式的定制有点不灵活，比如用户登录注册到底要输入哪些信息、预约的时候要输入哪些信息的设计，比如html里面想要用循环输出图片当时却一直不能用id来定位图片的url… <br>
不过还好最终所有问题都被攻克掉，这样一趟下来还是很有收获的，特别是做的东西是自己喜欢的并且一直想做的，finally！ <br>
###	实用性分析
如我前面分析道，其实这个网站一直是学院这边的一个需求，解决的都是一些非常实际的问题。学院其实一直有启动资金为这个项目备着，建立这个网站的最终目的也是为了加强跟各高中的联系和交流，扩大计算机学院的影响力。<br>
并且该网站可以减少青志部的工作量，目前的“竞赛辅导”“讲座预约”“科技站参观”的流程都是靠我和学院的老师去交流，去和高中老师确定时间，需要花费大量的时间在沟通上，并且经常会出现两边的信息不对称的情况，很想有一个信息罗列的网站让老师们自己来进行选择和预约，我们这边只需要从数据库查看预约信息并进行进一步的安排人员即可，可以显著减轻我们的负担。<br>
我也联系了学工部的老师，询问了一下网站相关的问题，他跟我说等网站写好之后可以外挂在计算机学院的相关链接下。<br>
所以各方面考虑来看，该网站的实用性是很强的。<br>

#	后期改进部分
由于时间限制，该网站目前实现的还只是信息的罗列和简单的预约功能。<br>
后期希望做到以下改进：<br>
1.	继续美化UI。<br>
2.	增加个人信息界面，可以上传头像，完善更多个人信息，查看预约详情，修改预约订单。<br>
3.	增加备注信息，使预约功能更加的人性化。<br>
4.	增加反馈环节，可以对预约订单添加一些“用户点评”。<br>
5.	增加联系功能，可以由网页向青志部的公共邮箱发送联系邮件。<br>
6.	将网站和计算机科学技术学院的官网“连”起来，做到自动从学院网站“扒”新闻，并将“扒”下来的新闻存入News这个Table并在news-list和news-detail界面实时更新。<br>
7.	希望做到预约成功后可以由网页自动的给预约者预留的邮箱发送预约详情的邮件。<br>
8.	增加搜索和检索功能，希望通过新闻的“Tag”和“Category”检索到新闻。<br>
