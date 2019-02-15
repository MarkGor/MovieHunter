# 电影下载小工具

某网站电影资源一键下载脚本。

**仅供娱乐和技术研究，如有任何人用作商业或非法用途，产生任何法律纠纷均于作者无关**

使用方法：

直接试用已经编译好的exe：

```
bin/main.exe 电影名
```

或者自行安装python环境后试用

```
python main.py 电影名
```

依赖：
1. python2.7
2. requests、simplejson

说明：

1. 仅支持电影下载，其他功能可自行增加
2. 视频资源为m3u8，并没有严格遵循其格式解析，仅仅简单解析ts列表，多线程下载ts
3. 所有ts下载完成后，自行合并

具体细节，请看代码，以及注释。


```
pip install requests
pip install simplejson
```

# 赞我

![img](pay.png)