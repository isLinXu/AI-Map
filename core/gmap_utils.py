# http://oregonarc.com/2011/02/command-line-tile-cutter-for-google-maps-improved/
# http://media.oregonarc.com/fish/tile.py

import math
import urllib
import urllib.request as urllib2
import json
from urllib.request import urlopen

#akey = '2jyKeVBnklxsB2Zyduy6wXdnwWEPUjaz'
akey = 'dYg9wxs2v2xfaNEpTmcR4S6jZ0idkHN6'

def latlon2px(z,lat,lon):
    x = 2**z*(lon+180)/360*256
    y = -(.5*math.log((1+math.sin(math.radians(lat)))/(1-math.sin(math.radians(lat))))/math.pi-1)*256*2**(z-1)
    return x,y

def latlon2xy(z,lat,lon):
    x,y = latlon2px(z,lat,lon)
    x = int(x/256)#,int(x%256)
    y = int(y/256)#,int(y%256)
    return x,y

def bd_latlng2xy(z,lat,lng):
    # coords = str(lng) + ',' + str(lat)
    # url = 'http://api.map.baidu.com/geoconv/v1/?coords='+coords+'&ak=1jyKeVBnklxsB2Zyduy6wXdnwWEPUjaZ'
    url='http://api.map.baidu.com/geoconv/v1/?'
    args = {'coords':str(lng)+','+str(lat),
            'from':5,
            'to':6,
            'output':'json',
            'ak':akey}
    data = urllib.parse.urlencode(args)
    response = urllib2.urlopen(url+data)
    # with urlopen(url, timeout=3) as html:
    #     http_info = html.info()
    #     raw_data = html.read().decode(http_info.get_content_charset())
    # data = json.loads(raw_data)
    # response = urllib2.urlopen(url)
    result = response.read()
    result = json.loads(result)
    print('result:', result)
    loc = result["result"][0]
    # loc=data['result'][0]
    res = 2**(18-z)
    #x,y=0,0
    x = loc[u'x']/res
    y = loc[u'y']/res
    return x,y

if __name__ == "__main__":
    z=19
    lat=31.025819
    lng=121.434229
    x,y = bd_latlng2xy(z,lat,lng)
    print(x//256)
    print(y//256) # only right when lat>0 lng>0