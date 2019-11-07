# -*- coding: UTF-8 -*-

import requests
import json

#评论所在链接
url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token='

#请求评论的消息头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400',
    'Referer':'https://music.163.com/song?id=551816010',  
	'Origin':'https://music.163.com',
	'Host':'music.163.com'
}

#加密信息，直接复制
user_data = {   
	'params':'MOMTKPkbc4IL/Hww2fWcdBWJBR8Sp4+lNyNTXuK1npEr9JjXdSMiGFenyxoKOvMcQp4A2FXElWaI7UxCOrEN+QZgOtpJLevo1s73u63A41EyZGsgKS2+AGIn/DmbQ8sVBOwj/V8Uzcgh/M6wY4VUM988iZurUq98GF1Ct1Y5iNwUzoFlmTo8GYVWWcaxKz0u', 
	'encSecKey':'132e56f557df26b19aa4ec1c0dc15cedaabeba648efda1bfed774359f836d000603ba1b1c81a6c3bc0a212ac626d588962a258ca5ed5726c75f169869f0abeafb488a6eec0ae374270ee85c62b177d73b93ff9c7a31834883f10980ddb3a9ae86975bda7185bc03bad503b399c0b415429f82899cba4e36d2413c6adc8ac7bcd'
}

#发送请求
response = requests.post(url,headers=headers,data=user_data)

#数据获取
data = json.loads(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
	item = {
		'nickname':hotcommment['user']['nickname'],
        'content':hotcommment['content'],
        'likedCount':hotcommment['likedCount']
	}
	hotcomments.append(item)
	
#数据整理成表
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]


from pyecharts import Bar
bar = Bar("热评中点赞数示例图")
bar.add("点赞数", nickname, liked_count, is_stack=True, mark_line=["min", "max"], mark_point=["average"])
bar.render()


from wordcloud import WordCloud 
import matplotlib.pyplot as plt
#通过抓取的数据，生成词云
content_text = "".join(content_list)
wordcloud = WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
