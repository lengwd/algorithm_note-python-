# 这里犯了一个错误 在输入的时候把权重也减了一

def read_edges():
    num_nodes = int(input("input num_nodes: "))
    num_edges = int(input("input num_edges: "))


    edges = []

    for i in range(num_edges):
        edge_str = input("input edge (node1 node2 weight): ").split() 
        edge = [int(x)-1 for x in edge_str]
        edge[2] = edge[2] + 1
        
        edges.append(edge)

    return num_nodes, edges


def main():
    num_nodes, edges = read_edges()

    dist = [float("inf") for _ in range(num_nodes)]
    dist[0] = 0

    for _ in range(num_nodes-1):
        temp = dist[:]
        for edge in edges:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + edge[2]

        if dist == temp:
            break
    flag = False
    for edge in edges:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                flag = True
                break
    if flag:
        print("存在负权回路")
    else:
        print(dist)

if __name__ == "__main__":
    main()