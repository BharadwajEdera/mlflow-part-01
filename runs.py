import os
import subprocess
try:
    os.environ.pop('PYTHONIOENCODING')
except KeyError:
    pass
os.chdir(os.getcwd())
p1s = range(0,5)
p2s = range(0,5)

for p1 in p1s:
    for p2 in p2s:
        # print(f"python demo.py -p1 {p1} -p2 {p2}")
        # demp_path = os.path.join(os.getcwd() , 'demo.py') 
        # print('demp_path : ',demp_path)
        print(os.listdir(os.getcwd()))
        os.system(f"python demo.py -p1 {p1} -p2 {p2}")
        # subprocess.Popen(f"python demo.py -p1 {p1} -p2 {p2}",stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True).communicate()[0]