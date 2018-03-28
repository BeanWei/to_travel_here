import jieba
import collections
import difflib

jieba.load_userdict("获取的所有景点或酒店.txt")

text = "将所有评论全部合在一起"

seg_list = list(jieba.cut(text,cut_all=False))

'''
导入Levenshtein->进行文本相似性分析，去除seg_list中的不相关词语
import Levenshtein
BASELIST = 所有景点或酒店的列表
NEEDLIST = []
for i in seg_list：
    similarity=Levenshtein.distance(i,','join(BASELIST))
    if similarity > 0:
       NEEDLIST.append(i) 

删选完以后进行最后的额词频统计

'''
BASELIST = ['所有景点或酒店的列表']
base_txt = ','.join(BASELIST)
NEEDLIST = []
for i in seg_list：
    similarity=difflib.SequenceMatcher(a=base_txt,b=i).quick_ratio()
    if similarity > 0:
       NEEDLIST.append(i) 
wordsFrequency = collections.Counter(NEEDLIST)