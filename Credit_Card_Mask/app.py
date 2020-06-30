def maskify(cc):
    return (cc[:-4].replace(cc[:-4], ('#'*len(cc[:-4])))+ cc[-4:])

maskify("4556364607935616")
maskify("64607935616")
maskify("1")
maskify("")
maskify("Skippy")
maskify("Nananananananananananananananana Batman!")

'''
Best Answer:

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
'''