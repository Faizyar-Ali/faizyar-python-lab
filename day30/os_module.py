import os 

print(os.getcwd())
os.chdir("/faizyar-python-lab/day21")
print(os.getcwd())
os.chdir("/faizyar-python-lab")

if not os.path.exists("Garbage"):
   os.mkdir("Garbage")
path=r"d:/faizyar-python-lab/garbage"
os.chdir(path)
for i in range(1,11):
    if  not os.path.exists(f"mark {i}"):
           os.mkdir(f"mark {i}")
for i in range(1,11):
    os.rename(f"mark {i}",f"zucker {i}")