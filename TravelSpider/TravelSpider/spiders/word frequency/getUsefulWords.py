import jieba
import collections
import difflib
import os
import json


with open(os.path.abspath(os.path.dirname(os.getcwd()))+'/AllanswersJD.json','r',encoding='utf-8') as f:
    viewsets = json.loads(f.read())
    cityID = viewsets[0]['cityID']
    tid = viewsets[0]['tid']
    answers = ''
    for i in viewsets:
        answers += i['answers']
    jieba.load_userdict(os.getcwd()+'/10444_viewset.txt')
    seg_list = list(jieba.cut(answers,cut_all=False))
    base_txt = ''
    for line in open(os.getcwd()+'/10444_viewset.txt',encoding='utf-8').readlines():
        base_txt = base_txt + line.split(' ns')[0]+','
    base_txt = base_txt.rstrip(',')
    NEEDLIST = []
    for i in seg_list:
        similarity=difflib.SequenceMatcher(a=base_txt,b=i).quick_ratio()
        if similarity > 0.3:
            NEEDLIST.append(i) 
    with open(os.getcwd()+'/'+str(cityID)+'_'+tid+'.txt','a+',encoding='utf-8') as f:
        for each in collections.Counter(NEEDLIST).items():
            (a,b) = each
            print(a,b,sep='\t',end='\n',file=f)




'''

jieba.load_userdict("获取的所有景点或酒店.txt")

text = "将所有评论全部合在一起"

seg_list = list(jieba.cut(text,cut_all=False))

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
