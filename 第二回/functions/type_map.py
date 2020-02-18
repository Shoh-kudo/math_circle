from collections import defaultdict
from functions import Set
from functions.operand import *
import inspect

class Map(Set):
    def __init__(self, values=None, types='func', A=Set(set([])), B=Set(set([])), init=False, txt=''):
        super().__init__(values=values, types=types, A=A, B=B)
        self.values = self.make_func(values)
        self.txt = txt
        if len(self.txt) == 0:
            self.txt = inspect.getsource(self.values)
        self.A = A
        self.B = B
        if len(self.B) == 0 and len(A) != 0:
            self.target_init()
        self.types = types

    def make_func(self, values):
        if values is not None:
            return values
        return self.func

    def func(self, x):
        raise NotImplementedError()

    def param_set(self, A=None, B=None):
        if A is not None:
            self.A = A
        if B is not None:
            self.B = B

    def target_init(self):
        self.B = self.B | Set(union([self.values(x) for x in self.A.values]))

    def relations(self):
        if isinstance(self.A, Set):
            return {
                x: self(x) for x in self.A.values
            }
        elif isinstance(self.A, list):
            return {
                tuple([a]): self(a) for a in self.A if self(a) is not None
            }

    def image(self):
        relations = self.relations()
        dmn = [a for a,b in relations.items() if isinstance(b,set)]
        img = [b for a,b in relations.items()]
        return Set(union(dmn)), Set(union(img))

    def delta(self):
        relations = self.relations()
        inv_rlts = defaultdict(set)
        for key, vals in relations.items():
            for val in vals:
                inv_rlts[val].add(key)
        return inv_rlts

    def _inv(self, x):
        delta = self.delta()
        if not isinstance(x, Set):
            if not isinstance(x, set):
                x = set([x])
            x = Set(x)
        return union([delta[a] for a in x.values])

    def inv(self):
        return Map(self._inv, types=self.types, A=self.B, B=self.A, init=True)

    def __eq__(self, function):
            assert self.types == function.types, '同じtypes同士で演算してください...'
            a_relation = self.relations()
            b_relation = function.relations()
            return all([
                (a_relation.keys() == b_relation.keys()),
                (v == b_relation[k] for k,v in a_relation.items() if k in b_relation.keys()),
                (v == a_relation[k] for k,v in b_relation.items() if k in a_relation.keys())
            ])

    def __call__(self, x):
        func = self.values
        if not isinstance(self.values, list):
            func = [self.values]
        if isinstance(x, Set):
            for f in func:
                x = Set(union([f(a) for a in x.values]))
            return x
        for f in func:
            x = f(x)
        return x

    def __mul__(self, function):
        assert self.types == function.types == 'func', 'func型同士で演算してください...'
        funcs = self.values
        txt = self.txt
        if not isinstance(funcs, list):
            funcs = [self.values]
        funcs.append(function)
        txt += function.txt
        return Map(funcs, txt=txt)

    def __repr__(self):
        return self.txt
