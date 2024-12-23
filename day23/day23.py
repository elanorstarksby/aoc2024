import networkx as nx


def read_in():
    with open("input.txt", "r") as input_file:
        lines = tuple(tuple(a.split("-")) for a in input_file.read().split('\n'))
    return lines


def build(values):
    graph = {}
    for a, b in values:
        if a not in graph:
            graph[a] = set()
        graph[a].add(b)
        if b not in graph:
            graph[b] = set()
        graph[b].add(a)
    return graph


def p1(values):
    parties = set()
    graph = build(values)
    for start, ends in graph.items():
        # print(start, ends)
        for end in ends:
            # print("",end, graph[end])
            for end_link in graph[end]:
                if start in graph[end_link]:
                    # print(" ",end_link, graph[end_link])
                    # print(start, end, end_link)
                    parties.add(tuple(sorted((start, end, end_link))))
    # print(len(parties))
    count = 0
    for party in parties:
        for computer in party:
            if computer[0] == "t":
                count += 1
                break
    return count


def p2(values):
    graph = nx.Graph()
    for start, end in values:
        graph.add_edge(start, end)
    clique = nx.algorithms.clique.find_cliques(graph)
    return ",".join(sorted(max(clique, key=lambda a: len(a))))


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
