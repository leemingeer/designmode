#coding: utf-8
class S:
    instance = None
    # __new__方法用来制作单例
    def __new__(cls, *args, **kwargs):
        if S.instance == None:
            S.instance = super().__new__(cls) # 这句话是用来分配内存的，
        return S.instance
s1 = S()
print(id(s1))
s2 = S()
print(id(s2))