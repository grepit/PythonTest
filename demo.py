#! /usr/bin/env python
"""Simple class to demo used for test case"""
class WorldData():
    def __init__(self, path):
        self.route = path

    def write_result(self):
        print(self.route)
        return self.route  

if __name__ == '__main__':

    socialData = WorldData("happy") 
    socialData.write_result()
