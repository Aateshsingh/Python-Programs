'''def welcome():
    print("Hey you are welcome from Harry")
if __name__== "__main__":
    welcome()'''

#import random , string
st = input("Enter a message:")
words = st.split(" ")
coding = input("1 for coding and 0 for decoding:")
coding = True if (coding == "1") else False
print(coding)
if (coding):
    nwords = []
    for word in words:
        if (len(st)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(st) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))