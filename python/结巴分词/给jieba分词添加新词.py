import sys
sys.path.append("../")
print(sys.path)
import jieba
jieba.load_userdict("user.dict")
print(", ".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式")))
print(", ".join(jieba.cut("我爱你阿尔托利亚")))