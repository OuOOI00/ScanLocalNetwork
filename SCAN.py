#!/usr/bin/env python


import scapy.all as scapy
import subprocess as sbp
import optparse as opt
import re


def scp(ip):
    net_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/net_request
    (answered, unanswered) = scapy.srp(arp_request_broadcast, timeout = 1)
    print(answered.summary())


    # scapy.ls(scapy.ARP()) ARP packet information

scp("192.168.0.1/24")

