wordTen = ["","one","two","three","four","five","six","seven","eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tys = ["","","twenty","thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["","","hundred","thousand"]

def number_to_words(n):
    words = []
    p = 10 ** (len(str(n)) - 1)
    while p >= 100:
        if (p == 1000) or (p == 100):
            words.append(wordTen[int(n/p)])
            words.append(hundreds[int(len(str(p))-1)])
            n = n % p
            p = 10 ** (len(str(n)) - 1)

    if (words) and (n > 0):
        words.append("and")

    if (n >= 20):
        words.append(tys[int(n/p)])
        if (n % p != 0):
            words.append(wordTen[n % p])
    elif (n > 0):
        words.append(wordTen[n])

    return words

count = 0
for i in xrange(1,1000+1):
    count += len(''.join(number_to_words(i)))
print(count)
