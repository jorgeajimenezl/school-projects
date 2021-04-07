import math

import pandas as pd

EXITATION_TABLE_JK = [
    ['0 X', '1 X'],
    ['X 1', 'X 0']
]

EXITATION_TABLE_D = [
    [0, 1],
    [0, 1]
]

EXITATION_TABLE_T = [
    [0, 1],
    [1, 0]
]

EXITATION_TABLES = {
    'jk': EXITATION_TABLE_JK,
    'd': EXITATION_TABLE_D,
    't': EXITATION_TABLE_T
}

def evaluate_moore(graph, start, g, input):
    u = start
    for x in input:
        yield g[u]
        u = graph[u][x] 
    yield g[u]

def evaluate_mealy(graph, start, input):
    u = start
    for x in input:
        u, z = graph[u][x]
        yield z

def d2b(x, count=None):
    s = []
    while x > 0:
        s.append(x & 1)
        x >>= 1
    if count:
        count -= len(s)
        for i in range(count):
            s.append(0)
    s.reverse()
    return s

def d2bs(x, count=None, sep=''):
    r = d2b(x, count)
    return sep.join(map(str, r))

# Only for binary automaton
def create_exitation_table(graph, assignation=None, bistable='jk'):
    n = len(graph)
    m = (n - 1).bit_length()

    assert len(graph) >= 1
    if not assignation:
        assignation = list(range(0, (1 << m)))

    assert len(assignation) >= n

    state_table = []
    columns = ['q(t)', '|'.join([f'Q{i}' for i in reversed(range(m))]), 'X(t)/0', 'X(t)/1']
    for i in reversed(range(m)):
        fmt = None

        if bistable == 'jk':
            fmt = f'J{i}K{i}'
        elif bistable == 'd':
            fmt = f'D{i}'
        elif bistable == 't':
            fmt = f'T{i}'
        else:
            raise Exception

        columns.append(f'{fmt}/0')
        columns.append(f'{fmt}/1')        

    for u in range(n):
        row = [f"q{u}", d2bs(assignation[u], m, '|')]
        assert len(graph[u]) == 2 # ensure binary
        ret_u = d2b(assignation[u], m)

        exitations = []

        for k in graph[u]:
            v, z = k if isinstance(k, tuple) else (k, None)
            assert v < n
            
            row.append(d2bs(assignation[v], m))
            ret_v = d2b(assignation[v], m)

            for j in range(m):
                exitation = EXITATION_TABLES[bistable][ret_u[j]][ret_v[j]]
                exitations.append(exitation)            
        
        for j in range(m):
            row.append(exitations[j])
            row.append(exitations[j + m])

        state_table.append(row)

    return pd.DataFrame(state_table, columns=columns)
    
EXERCISE = {
    'e1/1': {
        'graph': [
            [1, 0], # q0
            [1, 2], # q1
            [3, 0], # q2
            [1, 2], # q3
        ],
        'start': 0,
        'input': [0, 1, 0, 1, 0, 1, 0, 1],
        'g': [0, 0, 0, 1]
    },
    'e6': {
        'graph':  [
            [1, 1],
            [2, 2],
            [3, 2],
            [3, 2]
        ],
        'start': 0,
        'g': [0, 0, 0, 1],
        'input': [1, 1, 0, 1, 0]
    }
}

def check_automaton(automaton, sol):
    LARGE = 16

    for i in range(1 << LARGE):
        input = [0] * LARGE
        for j in range(LARGE):
            if (i & (1 << j)) != 0:
                input[j] = 1

        oa = list(automaton(input))
        ob = list(sol(input))
        for j in range(LARGE):
            if oa[j] != ob[j]:
                print("ERROR:", input)
                return

def main():
    graph = [
        [(0, 0), (1, 0)],   #q0
        [(2, 0), (3, 1)],   #q1
        [(2, 0), (3, 0)],   #q2
        [(4, 0), (6, 11)],  #q3
        [(4, 0), (6, 10)],  #q4
        [(5, 10), (6, 10)], #q5
        [(5, 10), (6, 11)], #q6
    ]

    start = 0
    # g = [0, 0, 11, 0, 0, 0, 10, 1, 1]
    input = [1, 1, 0, 1, 1]
    print(list(evaluate_mealy(graph, start, input)))
    # def check(x):
    #     last = 0
    #     ct = 0
    #     for i in x:
    #         ct += i
    #         if last == 1 and i == 1 and ct >= 3:
    #             yield 11
    #         elif last == 1 and i == 1:
    #             yield 1
    #         elif ct >= 3:
    #             yield 10
    #         else:
    #             yield 0
    #         last = i

    # check_automaton(lambda x: evaluate_mealy(graph, start, x), check)
    # table = create_exitation_table(graph, assignation=[0, 1, 3, 2, 6, 7, 5])
    # print(table)

if __name__ == '__main__':
    main()
