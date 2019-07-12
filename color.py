def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

# Атрибуты

# 0	нормальный режим
# 1	жирный
# 4	подчеркнутый
# 5	мигающий
# 7	инвертированные цвета
# 8	невидимый

# ======================================= #

# Цвет текста

# 30	черный
# 31	красный
# 32	зеленый
# 33	желтый
# 34	синий
# 35	пурпурный
# 36	голубой
# 37	белый

# ======================================= #

# Цвет фона

# 40	черный
# 41	красный
# 42	зеленый
# 43	желтый
# 44	синий
# 45	пурпурный
# 46	голубой
# 47	белый

print("\x1b[1;33mSome test\x1b[0m") # bold
print("\x1b[5;32mSome test\x1b[0m")
