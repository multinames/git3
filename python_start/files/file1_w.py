#ouf = open('file.txt',w)
#ouf.write('Some text\n')
#ouf.write(str(25))
#ouf.close()

with open ('input.txt','w') as ouf:
    ouf.write ('Some text\n')
    ouf.write (str(25))
