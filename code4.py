def replace(good,bad,name):
    file = open(name)
    contents = file.read()
    contents = contents[:-4]
    file.seek(0)
    bad_keys = list(bad.keys())
    bad_keys.sort(key = lambda x:len(x),reverse=True)
    good_keys = list(good.keys())
    good_keys.sort(key=lambda x: len(x), reverse=True)
    for i in bad_keys:
        if i in contents:
            for k in good_keys:
                if good[k] == bad[i] and len(i.split()) == len(k.split()):
                    contents = contents.replace(i,k)
                    break
    print(contents)


def file_score(good,bad,name):
    bad_score = 0
    good_score = 0
    file = open(name)
    for i in sorted(bad.keys()):
        if i in file.read():
            file.seek(0)
            bad_score += bad[i]*(file.read()).count(i)
        file.seek(0)
    for i in sorted(good.keys()):
        if i in file.read():
            file.seek(0)
            good_score += good[i]*(file.read()).count(i)
        file.seek(0)
    if bad_score > good_score:
        replace(good,bad,name)
    file.close()

bad = {}
good = {}
name = input()
read_data(name)
separator(good,bad,'unigrams.txt')
separator(good,bad,'bigrams.txt')

file_score(good,bad,name)
