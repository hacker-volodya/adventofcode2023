print(sum((lambda x: [0 if len(set(q).intersection(set(w))) == 0 else 2**(len(set(q).intersection(set(w)))-1) for q, w in x])([[[int(z.strip()) for z in y.split(" ") if z.strip()] for y in x[10:].split('|')] for x in open("input.txt").read().strip().split('\n') ])))