# -*- coding=utf-8 -*-
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

class QYTPING:
    def __init__(self,ip):
        self.ip = ip
        self.length = 100
        self.srcip = ''

    def make_pkt(self):
        if self.srcip:
            self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)
        else:
            self.pkt = IP(dst=self.ip) / ICMP() / (b'v' * self.length)

    def one(self):
        self.make_pkt()
        result = sr1(self.pkt,timeout=1,verbose=False)
        if result:
            print(self.ip, '可达')
        else:
            print(self.ip, '不可达')


    def __str__(self):
        if not self.srcip:
            return '<{0} => dstip: {1},size: {2}>'.format(self.__class__.__name__,self.ip,self.length)
        else:
            return '<{0} => srcip: {1}, dstip: {2},size: {3}>'.format(self.__class__.__name__, self.srcip,self.ip, self.length)

class NewPing(QYTPING):
    pass

if __name__ == '__main__':
    ping = QYTPING('10.0.0.200')
    total_len = 70

    def print_new(word,s='-'):
        print('{0}{1}{2}'.format(s*int((70 - len(word))/2),word, s*int((70 - len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
   # print_new('ping five')
   # ping.ping()
   # print_new('set payload length')
   # ping.length = 200
   # print(ping)
   # ping.ping()
   # print_new('set ping src ip address')
   # ping.srcip = '192.168.1.123'
   # print(ping)
   # ping.ping()
   # print_new('new class NewPing','=')
   # newping = NewPing('192.168.1.1')
   # newping.length = 300
   # print(newping)
   # newping.ping()
