from webbrowser import get
from getmac import get_mac_address
from netaddr import IPNetwork
import urllib.request
import random
import os.path
import socket
import threading


def work_with_ips():
    with open("ips.txt","r") as inp:
      ipranges = inp.readlines()
    random_range = random.choice(ipranges)
    print('selected random range is:',random_range)
    with open("selected_ip_range.txt","a") as inp:
        for ip in IPNetwork(random_range):
            ip = str(ip)
            inp.write((ip))
            inp.write('\n')
    print("ip list created successfully")



def is_ip_is_camera(ip):
    with open("list.txt","r") as inp:
            ip_mac = get_mac_address(ip)
            print(type(ip_mac))
            if (ip_mac is None) or (len(ip_mac) == 0):
                print(ip,"is not alive")
                return False
            #print(type(ip_mac))
            else:
                for line in inp:
                    if ip.startswith(line):
                        print("does starts")
                        return True
                    else:
                        print("doesnt start")
                        return False
                

def check_alive_ips(count,ip):
    conn = is_ip_is_camera(ip)
    if(conn):
        count+=1
        print (ip,"is camera : )))))))))))))))))))))))))))))))))))))))))))))")
        with open("cameras_ips.txt","a") as inp:
            ip=str(ip)            
            inp.write(ip)
            inp.write('\n')
    else:
        print (ip,"is not a camera")
        print("======================================")
    return count            


def ips2array():
    f = open('selected_ip_range.txt','r')
    lines = f.read().splitlines()
    f.close()
    return lines

def check_One_By_One(iparray):
    for ips in iparray:
        count_alive = check_alive_ips(0,ips)
    return count_alive 

def multi_ip(iparray):
    splitlen = len(iparray)//8
    print('split len is ', splitlen)
    t1 = threading.Thread(target=check_One_By_One, args=(iparray[:splitlen],))
    t1.start()

    t2 = threading.Thread(target=check_One_By_One, args=(iparray[splitlen:2*splitlen],))
    t2.start()

    t3 = threading.Thread(target=check_One_By_One, args=(iparray[2*splitlen:3*splitlen],))
    t3.start()

    t4 = threading.Thread(target=check_One_By_One, args=(iparray[3*splitlen:4*splitlen],))
    t4.start()

    t5 = threading.Thread(target=check_One_By_One, args=(iparray[4*splitlen:5*splitlen],))
    t5.start()

    t6 = threading.Thread(target=check_One_By_One, args=(iparray[5*splitlen:6*splitlen],))
    t6.start()

    t7 = threading.Thread(target=check_One_By_One, args=(iparray[6*splitlen:7*splitlen],))
    t7.start()

    t8= threading.Thread(target=check_One_By_One, args=(iparray[7*splitlen:8*splitlen],))
    t8.start()
def main():
        if os.path.isfile('selected_ip_range.txt'):
            os.remove("selected_ip_range.txt")
        work_with_ips()
        iparray = ips2array()
        multi_ip(iparray)

print("===========================================================")
print("Camahsa BY Nic")
print("#mahsaamini")
print("===========================================================")
main()
