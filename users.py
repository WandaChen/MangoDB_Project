#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""
#OSM_File = "kaohsiung_map.osm"
OSM_File = "kaohsiung_taiwan.osm"

def get_user(element):   #get the valid user id
    uid_value = None
    if element.has_key("uid") and (element["uid"] != None):
        uid_value = element["uid"]
    else:
        pass
        
    return uid_value


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename): 
        if (element.tag in ["node", "way", "relation"]):
            user = get_user(element.attrib)
            if user not in users:     #add user
                users.add(user) 
        else:
            pass
        pass

    return users


def test():

    users = process_map(OSM_File)
    pprint.pprint(len(users))
    #pprint.pprint(users)
    #assert len(users) == 6



if __name__ == "__main__":
    test()
