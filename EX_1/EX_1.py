def verse(verse):
    str = verse.lower().split()
    def f(x): return sum(1 for i in x if i in 'йуеёыаоэюия')
    tmp = f(str[0])
    if all([f(i) == tmp for i in str]):
        return 'true'
    return 'false'


print(verse("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
