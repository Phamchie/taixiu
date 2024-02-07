import random
import time
import sys
import os
from log import sessions
from nap import *
from taixiu import start_xocxoc1
from rut import rut_tien

os.system('cls' if os.name == 'nt' else 'clear')

sessions()

os.system('cls' if os.name == 'nt' else 'clear')

with open('assets/xu.txt', 'r') as xu:
    xu = int(xu.read())
    xu1 = "{:,}".format(xu)

with open('data/data_info/nickname.txt', 'r') as nickname:
    nickname = nickname.read()

print(""""
Tên Nhân Vật : {}
Số Dư : {}đ
""".format(nickname, xu1))

print("""
=====Mini Game=====
  1, Tài Xỉu Săn Hũ
  2, Nạp Xu
  3, Rút Tiền
===================
""")

user_input = input("Chọn Game : ")
if user_input == "1":
    start_xocxoc1()
if user_input == "2":
    naps()
if user_input == "3":
    rut_tien()