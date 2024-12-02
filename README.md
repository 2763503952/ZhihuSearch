# ZhihuSearch

此项功能实现了在非登录的状态下爬取知乎搜索内容。

## 使用方法

### 本地运行
#### 1 运行需要的前置条件

本地环境运行需要有node js环境和drissionpage自动化模块。 

#### 2 运行
进入main.py文件，将keyword变量改成你要搜索的内容，直接点击运行。

## 结构说明
settings文件夹里包含配置文件。
sprider文件夹下有两个文件ZhiHu.py是知乎爬虫文件，Zhihu_Cookie.py是自动化获取未登录状态的cookie。

## 实现方式
1.用drissionpage自动化，进入知乎的搜索页获取cookie，这样可以防止知乎封禁账号，用未登录状态爬取只会被检测ip和cookie，cookie被检查到可以服用自动化重新获取cookie，ip被封禁可用代理ip。
2.通过js逆向出请求头中的x96参数，知乎所需要的两个重要的参数一个是x96另一个是cookie里的key为d_c0的值。
## ！！！程序纯属个人学习！！！







