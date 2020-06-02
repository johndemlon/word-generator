full = ""
for l in open("a.txt","r").readlines():
    full = full + l
for l in open("b.txt","r").readlines():
    full = full + l
for l in open("c.txt","r").readlines():
    full = full + l
for l in open("d.txt","r").readlines():
    full = full + l
for l in open("e.txt","r").readlines():
    full = full + l
for l in open("f.txt","r").readlines():
    full = full + l
for l in open("g.txt","r").readlines():
    full = full + l
for l in open("h.txt","r").readlines():
    full = full + l
for l in open("i.txt","r").readlines():
    full = full + l
for l in open("j.txt","r").readlines():
    full = full + l
for l in open("k.txt","r").readlines():
    full = full + l
for l in open("l.txt","r").readlines():
    full = full + l
open("full.txt","w").write(full)
n=0
for liner in open("full.txt","r").readlines():
    n = n + 1
print(n)
