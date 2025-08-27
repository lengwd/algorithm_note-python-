def read_edges():
    num_nodes = int(input("input num_nodes: "))
    num_edges = int(input("input num_edges: "))


    edges = []
    table_first = [-1 for _ in range(num_nodes)]
    table_next = [-1 for _ in range(num_edges)]

    for i in range(num_edges):
        edge_str = input("input edge (node1 node2 weight): ").split() 
        edge = [int(edge_str[0])-1, int(edge_str[1])-1, int(edge_str[2])]

        edges.append(edge)

        table_next[i] = table_first[edge[0]]
        table_first[edge[0]] = i

    return num_nodes, edges, table_first, table_next

def main():
    num_nodes, edges, table_first, table_next = read_edges()
    book = [0] * num_nodes

    dis = [float("inf")] * num_nodes
    dis[0] = 0

    head = 0
    tail = 0
    
    book[0] = 1
    queue = [0]

    tail += 1

    while head < tail:
        k = table_first[queue[head]]
        while k != -1:
            if dis[edges[k][0]] + edges[k][2] < dis[edges[k][1]]:
                dis[edges[k][1]] = dis[edges[k][0]] + edges[k][2]
                if book[edges[k][1]] == 0:
                    book[edges[k][1]] = 1
                    queue.append(edges[k][1])
                    tail += 1
            k = table_next[k]

        book[queue[head]] = 0 
        head += 1
    
    
    print(dis)

if __name__ == "__main__":
    main()