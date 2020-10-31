from pySmartDL import SmartDL

url = "http://fayllar1.ru/11/G'urur%20va%20andisha%201080p%20O'zbek%20tilida%20(asilmedia.net).mp4"
dest = "C:\Downloads" # or ‘~/Downloads/’ on linux

obj = SmartDL(url, dest)
obj.start() # [*] 0.23 Mb / 0.37 Mb @ 88.00Kb/s [##########——–] [60%, 2s left]

path = obj.get_dest()