#!/usr/bin/python

import urllib.request as urllib2
import os, sys
import math
from gmap_utils import *

import time
import random

def download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite=True):

    start_x, start_y = bd_latlng2xy(zoom, lat_start, lon_start)
    stop_x, stop_y = bd_latlng2xy(zoom, lat_stop, lon_stop)
    
    start_x = int(start_x//256)
    start_y = int(start_y//256)
    stop_x = int(stop_x//256)
    stop_y = int(stop_y//256)
    
    print("x range", start_x, stop_x)
    print("y range", start_y, stop_y)
    root_save="tiles"
    os.makedirs(root_save,exist_ok=True)
    
    for x in range(start_x, stop_x):
        for y in range(start_y, stop_y):
            
            url = None
            filename = None
            
            if satellite:        
                url = "http://shangetu0.map.bdimg.com/it/u=x=%d;y=%d;z=%d;v=009;type=sate&fm=46&udt=20150504&app=webearth2&v=009&udt=20150601" % (x, y, zoom)
                filename = "%d_%d_%d_s.jpg" % (zoom, x, y)
            else:
                # url = "http://online0.map.bdimg.com/onlinelabel/?qt=tile&x=%d&y=%d&z=%d&styles=pl&udt=20160918&scaler=1&p=0" % (x, y, zoom)
                url = 'http://online3.map.bdimg.com/tile/?qt=tile&x=%d&y=%d&z=%d&styles=pl&scaler=1&udt=20180810'% (x, y, zoom)
                filename = "%d_%d_%d_r.png" % (zoom, x, y)
            filename = os.path.join(root_save, filename)
            print('filename',filename)
            if not os.path.exists(filename):
                
                bytes = None
                
                try:
                    req = urllib2.Request(url, data=None)
                    response = urllib2.urlopen(req)
                    bytes = response.read()
                except Exception as e:
                    print("--", filename, "->", e)
                    sys.exit(1)
                print("-- saving", filename)
                
                f = open(filename,'wb')
                f.write(bytes)
                f.close()
                
                time.sleep(1 + random.random())

if __name__ == "__main__":
    zoom = 19

    lat_start, lon_start = 31.022547,121.429391
    lat_stop, lon_stop = 31.041453,121.45749
    
    satellite = True    # roads if false    
    #zoom = 15
	
    #lat_start, lon_start = 29.373026,106.25131
    #lat_stop, lon_stop = 29.755033,106.72734

    #satellite=False

    download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite)
