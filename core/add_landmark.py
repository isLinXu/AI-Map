
from PIL import Image,ImageDraw
import os
import numpy as np

from gmap_utils import *

class Landmark(object):
    def __init__(self,path_map):
        image=Image.open(path_map)
        draw = ImageDraw.Draw(image)
        self.image=image
        self.draw=draw

    def init_range_lat_lon(self,zoom, lat_start, lat_stop, lon_start, lon_stop):
        x_start, y_start = bd_latlng2xy(zoom, lat_start, lon_start)
        x_stop, y_stop = bd_latlng2xy(zoom, lat_stop, lon_stop)
        self.zoom=zoom
        self.x_start = int(x_start / 256) * 256
        self.y_start = int(y_start / 256) * 256
        self.x_stop = int(x_stop / 256)*256
        self.y_stop = int(y_stop / 256) * 256

    def add_landm(self,lat,lng,radius=10,color="red",width=None):
        x,y=self._latlng2xy(lat,lng)
        self._add_sphere(self.draw,(x,y),radius,color,width)

    def save_img(self,path_save):
        self.image.save(path_save)

    def _add_sphere(self,draw,center,radius=10,color="red",width=None):
        if width is None:
            width=radius
        x,y=center[0],center[1]
        draw.ellipse((x-radius,y-radius,x+radius,y+radius),outline=color,width=width)

    def _latlng2xy(self,lat,lng):
        x,y=bd_latlng2xy(self.zoom,lat,lng)
        x=x-self.x_start
        y=self.y_stop-y
        return x,y

def read_work_location(path):
    with open(path,encoding='utf8') as f:
        lines=f.readlines()
    lines=[line.strip() for line in lines]
    locations=[line.split(":")[-1] for line in lines]
    locations=[loc.split(",") for loc in locations]
    locations=[[float(loc[1]),float(loc[0])] for loc in locations]
    return locations

def main():
    path_img="map_r.png"
    path_save="map_lm.png"
    path_wl = "WorkLocation.txt"
    locations = read_work_location(path_wl)

    zoom = 15
    lat_start, lon_start = 29.373026, 106.25131
    lat_stop, lon_stop = 29.755033, 106.72734

    m_landm=Landmark(path_img)
    m_landm.init_range_lat_lon(zoom,lat_start,lat_stop,lon_start,lon_stop)
    for i,loc in enumerate(locations):
        print("{} th of all {} ...".format(i,len(locations)))
        m_landm.add_landm(*loc,radius=30,width=5)
    m_landm.save_img(path_save)



if __name__ == '__main__':
    main()
