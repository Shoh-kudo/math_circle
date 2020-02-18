from collections import defaultdict
from functions.operand import *

class Set:
    def __init__(self, values, types='set', **kwargs):
        if types == 'set' and not isinstance(values, set):
            values = set([values])
        self.values = values
        self.types = types
        self.count = 0

    def __or__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        return Set(union([self.values, elements.values]), types='set')

    def __sub__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        if isinstance(elements.values, (str,int)):
            elements = set([elements.values])
        return Set(diff(elements.values, self.values), types='set')

    def __and__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        return Set(intersection([self.values, elements.values]), types='set')

    def __mul__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        if isinstance(elements.values, (str,int)):
            elements = set([elements.values])
        return Set({tuple(x) for x in direct_product([self.values, elements.values])}, types='set')

    def __pow__(self, num=2):
        assert self.types == 'set', 'set型のみに許されています．'
        assert num==2, '二乗以外は許されません．'
        return power_set(self.values)

    def __contains__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        return all([_ in self.values for _ in elements.values])

    def __truediv__(self, relation):
        assert relation.types == 'func' and self.types == 'set', 'set を func で除算してください．'
        return get_equiv_class(self.values, relation.values)

    def __eq__(self, elements):
        assert self.types == elements.types, f'同じtypes同士で演算してください...'
        return all([
            (self.__lt__(elements)),
            (self.__gt__(elements))
        ])

    def __lt__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        return all([x in elements.values for x in self.values])

    def __gt__(self, elements):
        assert self.types == elements.types == 'set', 'set型のみに許されています．'
        return all([x in self.values for x in elements.values])

    def __getitem__(self, idx):
        assert self.types == 'set', 'set型のみに許されています．'
        if isinstance(idx,int):
            idx = [idx]
        return Set({x for i, x in enumerate(self.values) if i in idx}, types='set')

    def __len__(self):
        assert self.types == 'set', 'set型のみに許されています．'
        return len(self.values)

    def __hash__(self):
        return hash(tuple(self.values))

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.values):
            raise StopIteration
        res = self[self.count]
        self.count += 1
        return res

    def __repr__(self):
        return '{' + ', '.join(map(str,list(self.values))) + '}'
