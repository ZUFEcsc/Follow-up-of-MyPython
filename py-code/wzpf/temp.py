#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 15:04
# @Author : ChenShan
# Function :
# 1.导入所需模块
import requests

# 2.读取json文件
url = 'http://pvp.qq.com/web201605/js/herolist.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
response = requests.get(url, headers=headers)
json_list = response.json()

print(len(json_list)) # 英雄总数量：95个英雄
# print(json_list) # 打印结果,了解json_list的构造

try:
    # 3.提取json文件,下载图片
    for m in range(len(json_list)):
        # 英雄编号
        hero_num = json_list[m]['ename']
        # 英雄名称
        hero_name = json_list[m]['cname']
        # 获取皮肤列表
        skin_name = json_list[m]['skin_name'].split('|')
        # 统计皮肤数量
        skin_count = len(skin_name)
        print('英雄名称：', hero_name, ' 皮肤数量：', skin_count)  # 打印英雄的皮肤数量

        # 遍历每一个图片网址
        for i in range(1, skin_count + 1):
            # 网址拼接, 构造完整的图片网址
            url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'  # 图片网址固定前缀
            url_pic = url + str(hero_num) + '/' + str(hero_num) + '-bigskin-' + str(i) + '.jpg'
            # 获取图片信息
            picture = requests.get(url_pic).content
            # print(picture) # 打印图片网址
            # 下载图片 文件路径为: pic/英雄名-皮肤名.jpg (需要新建pic文件夹)
            with open('pic/' + hero_name + ' - ' + skin_name[i - 1] + '.jpg', 'wb') as f:
                f.write(picture)
except KeyError as e:
    # 捕获异常：解决皮肤名称全部打印完成后会报错的问题
    print('程序执行完毕!')

