```
http://s.weibo.com/weibo/%25E6%25B5%25B7%25E4%25BF%25A1&typeall=1&suball=1&timescope=custom:2017-11-07-0:2017-11-24-0&page=1
```

搜索关键字是"海信",执行了关键字两次urlencode

```python
# urldecode解密
import urllib.parse
a = '%25E6%25B5%25B7%25E4%25BF%25A1'
a = urllib.parse.unquote(a)
a = urllib.parse.unquote(a)
print(a) # 海信
```



```python
# urlencode加密
import urllib.parse
a = "海信"
a = urllib.parse.quote(a)
a = urllib.parse.quote(a)
print(a) # %25E6%25B5%25B7%25E4%25BF%25A1

```



## &typeall=1&suball=1

```
这俩参数不知道干吗用的,删了好像搜索有点问题,暂时留着不管
```



### &timescope=custom:2017-11-07-0:2017-11-24-0

```
搜索时间范围
2017-11-07-0:2017-11-24-0
从2017年11月07日0点到2017年11月24日0点
```



### &page=1

```
第几页
海信词条当前只有42页,如果请求第43页
http://s.weibo.com/weibo/%25E6%25B5%25B7%25E4%25BF%25A1&typeall=1&suball=1&timescope=custom:2017-11-07-0:2017-11-24-0&page=43
显示
抱歉，未找到“海信”相关结果。

建议:
您可以尝试更换关键词，再次搜索。
您可以关注萌小搜@微博搜索获取搜索技巧。
您也可以尝试在全网内搜索：海信
```

