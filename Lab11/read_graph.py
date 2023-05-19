def read_graph(f):
    """Read a graph from a file object 'f' (text) containing one
    vertex and its adjacency list per line.  E.g.:

    Input:     | Graph:
    A B C      |  A --> B
    B C        |  |    /^
    C B        |  v   / |
               |  C<-/  /
               |   ^---/

    Return three containers:

    V: (array) Vertex Id -> Vertex Name
    Adj: (array) Vertex Id -> array of Vertex Id
    V_idx: (dictionary) Vertex Name -> Vertex Id
    """
    V = []
    Adj = []
    V_idx = {}
    for line in f:              # for each line in the input f
        l = line.strip().split('|')
        assert len(l) > 0
        v_name = l[0]           # v_name is the source vertex
        if v_name in V_idx:     # We already have vertex v_name
            v = V_idx[v_name]
        else:
            v = len(V)          # Add vertex at the end of V, Adj
            V_idx[v_name] = v
            V.append(v_name)
            Adj.append([])

        if len(l) > 1 and l[2] != '':
            u_name = l[2]
            if u_name in V_idx:  # We already have vertex u_name
                u = V_idx[u_name]
            else:               # Add vertex, as above
                u = len(V)
                V_idx[u_name] = u
                V.append(u_name)
                Adj.append([])
            Adj[v].append(u)

    return Adj, V, V_idx

def all_dependencies(Adj, Name, Idx, p):
    S = []
    D = [False]*len(Adj)
    Q = [None]*len(Adj)
    Q_head = 0
    Q_tail = 0
    u = Idx[p]

    Q[Q_head] = u
    Q_tail += 1
    D[u] = True
    S.append(Name[u])
    while Q_tail != Q_head:
        u = Q[Q_head]
        Q_head += 1
        for v in Adj[u]:
            if not D[v]:
                Q[Q_tail] = v
                Q_tail += 1
                D[v] = True
                S.append(Name[v])
    return S

def count_connected_components(f):
    Adj, Name, Idx = read_graph(f)
    counter = 0

    for vertex in Idx:
        D = [False]*len(Adj)
        Q = [None]*len(Adj)
        Q_head = 0
        Q_tail = 0
        u = Idx[vertex]

        Q[Q_head] = u
        Q_tail += 1
        D[u] = True
        while Q_tail != Q_head:
            u = Q[Q_head]
            Q_head += 1
            for v in Adj[u]:
                if not D[v]:
                    Q[Q_tail] = v
                    Q_tail += 1
                    D[v] = True

    return counter







# f = open('borders.txt', 'r')
# count_connected_components(f)

