def outdegree(graph, node):
    return sum(1 for val in graph[node] if val > 0)


def TrustRank(graph, seedSet, d=0.85, maxIterations=100):
    N = len(graph)
    trustScores = [0.0] * N

    # Initialize trust scores
    for i in range(N):
        if i in seedSet:
            trustScores[i] = 1 / len(seedSet)

    # TrustRank Algorithm
    for iteration in range(maxIterations):
        newTrustScores = [0.0] * N
        for i in range(N):
            newTrustScores[i] = (1 - d) * trustScores[i]
            for j in range(N):
                if graph[i][j] > 0:
                    newTrustScores[i] += d * trustScores[j] / outdegree(graph, j)

        trustScores = newTrustScores

    return trustScores


# Example usage
if __name__ == "__main__":
    # Sample adjacency matrix for demonstration
    # graph[i][j] = 1 means a directed edge from node i to node j
    graph = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    # Seed set containing indices of trustworthy nodes
    seedSet = {0, 1}

    # Execute TrustRank
    trustScores = TrustRank(graph, seedSet)

    print("Trust Scores:", trustScores)
