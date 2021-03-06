#!/bin/env python
#-*- encoding=utf8 -*-

import os,sys

if __name__=="__main__":

    print ("__file__=%s" % __file__)

    print ("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))

    print ("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))

    print ("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])

    print ("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))

    print ("os.getcwd()=%s" % os.getcwd())

    print ("sys.path[0]=%s" % sys.path[0])

    print ("sys.argv[0]=%s" % sys.argv[0])

    print ('***获取当前目录***')
    print (os.getcwd())
    print (os.path.abspath(os.path.dirname(__file__)))

    print ('***获取上级目录***')
    print (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print (os.path.abspath(os.path.dirname(os.getcwd())))
    print (os.path.abspath(os.path.join(os.getcwd(), "..")))

    print ('***获取上上级目录***')
    print (os.path.abspath(os.path.join(os.getcwd(), "../..")))