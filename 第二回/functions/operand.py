from collections import defaultdict


def union(sets):
    sets = [{s} if isinstance(s,(int,str)) else s for s in sets]
    S = sets[0]
    for s in sets[1:]:
        S = {_ for _ in {*S, *s}}
    return S


def intersection(sets):
    sets = [{s} if isinstance(s,(int,str)) else s for s in sets]
    S = sets[0]
    for s in sets[1:]:
        S = {_ for _ in S if _ in s}
    return S


def diff(A, S):
    return {_ for _ in S if _ not in A}


def flatten(S):
    if not isinstance(S,list):
        return [S]
    x = []
    for s in S:
        x += flatten(s)
    return x


def direct_product(As):
    if isinstance(As,dict):
        As = list(As.values())
    X = []
    if len(As) == 1:
        return As[0]
    for a in As[0]:
        for b in direct_product(As[1:]):
            X += [flatten([a,b])]
    return X


def power_set(S):  # 冪集合
    p_sets = [[]]
    for s in S:
        tmp = []
        for element in p_sets:
            tmp.append(element + [s])
        p_sets.extend(tmp)
    return [set(s) for s in p_sets]


def get_equiv_class(A,f):
    C = defaultdict(set)
    for a in A:
        for b in A:
            if f(a,b):
                C[a].add(b)
    M = {}
    for e,s in C.items():
        M[e] = s
        for me,ms in M.items():
            if s == ms and e != me:
                M.pop([me,e][np.argmax([abs(me),abs(e)])])
                break
    return M, C


def is_surjective(func):  # 全射
    return func.B in func(func.A)


def is_injective(func):  # 単射
    ans = defaultdict(list)
    inv_ans = defaultdict(list)
    for a in func.A:
        for b in func(a):
            ans[b].append(a)
            inv_ans[a].append(b)
    return all([len(v) == 1 for k,v in [*ans.items(),*inv_ans.items()]])


def is_bijective(func):  # 全単射
    return all([
        is_surjective(func),
        is_injective(func)
    ])


def is_map(func):  # 写像
    return all([len(b) == 1 for a,b in func.relations().items()])


def is_identity(func):
    return all([{a}==func(a) for a in func.A.values])
