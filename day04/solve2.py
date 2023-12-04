import functools, itertools; print(
    functools.reduce(
        # a[0] is an accumulator for card count
        # a[1][0] holding number of copies for current card (a[1][0] + 1 - number of copies plus original card)
        # a[1][1:] holding copies of next cards
        lambda a, b: (
            # adding count of current card to accumulator
            a[0] + a[1][0] + 1, 
            # adding `a[1][0] + 1` copies for each of next `b` cards which we won with current card
            [x+y for x, y in itertools.zip_longest(a[1][1:] + [0], [1 + a[1][0]] * b, fillvalue=0)]
         ), 
        (lambda x: [len(set(q).intersection(set(w))) for q, w in x]) # counting intersections of win and our numbers
        ([
            [
                [int(z.strip()) for z in y.split(" ") if z.strip()] 
                for y in x[10:].split('|')
            ] 
            for x in open("input.txt").read().strip().split('\n') 
        ]), 
        [0, [0]]
    )[0]
)