import requests
import json

# ak = '复制上文中的AK'
ak = 'dYg9wxs2v2xfaNEpTmcR4S6jZ0idkHN6'

origin = '40.01116,116.339303'  # 起始点经纬度坐标
destination = '39.936404,116.452562'  # 终点经纬度坐标
url = 'https://api.map.baidu.com/directionlite/v1/walking?origin=' \
      + origin + '&destination=' + destination + '&ak=' + ak + '&coord_type=wgs84'

'''
url数据解释
1. walking是步行导航的意思，如果想要其他导航方式可参考官方文档
   riding是骑行导航
   driving是驾车导航
   transit是公交导航
   等等
2. origin是起始点的经纬度坐标，前者为纬度，后者为经度
3. destination是终点的经纬度坐标
4. ak是就是上文中的ak
5. coord_type=wgs84的意思是gps坐标。因为默认是百度经纬度坐标。所有格式见下图
'''

response = requests.get(url)  # 请求连接
answer = response.json()  # 获取json格式
answer_json = json.dumps(answer, indent=4)  # 增加缩进，不然可能得到的数据都在一行

print(answer_json)  # 打印查看