# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:03:36 2019

@author: Administrator
"""

#import PIL.Image as Image
#
#im = Image.open('img.png')#返回一个Image对象
#print('宽：%d,高：%d'%(im.size[0],im.size[1]))
#
#
#toImage=Image.new('RGBA',(120*16,120))
#
#
#for j in range(320,336):
#
#    pic_fole_head=Image.open('{}.png'.format(j))
#    pic_fole_head=pic_fole_head.resize((120,120))
#    pic_fole_head.save("{}.png".format(j))
#    loc=((j-320)*120,0)   
#    #loc=((j-320)*62,0)
#    print("第"+str(j)+"存放位置"+str(loc))
#    toImage.paste(pic_fole_head,loc)
#toImage.save('merged.png')

import requests

headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
url='https://yys.res.netease.com/pc/zt/20161108171335/data/shishen/{}.png?v1'
for i in range(200,428):
    r=requests.get(url.format(i),headers=headers)
    with open ("{}.png".format(i),'wb') as f:
        f.write(r.content)