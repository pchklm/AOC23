#!/usr/bin/python3

f = open("input", "r")
o = open("output", "w")
result=0
for l in f:
    l=l.replace("one","one1one")
    l=l.replace("two","two2two")
    l=l.replace("three","three3three")
    l=l.replace("four","four4four")
    l=l.replace("five","five5five")
    l=l.replace("six","six6six")
    l=l.replace("seven","seven7seven")
    l=l.replace("eight","eight8eight")
    l=l.replace("nine","nine9nine")
    l=l.replace("zero","zero0zero")
    first=""
    last=""
    for c in l:
        if c in "0123456789":
            if first=="":
                first=c
                last=c
            else:
                last=c
    print(first+last)
    result+=int(first+last)
o.write(str(result))

