
with open("source.txt","r") as src,open("target.txt","w")as target:
     for line in src:
          target.write(line)