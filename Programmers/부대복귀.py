import sys
import heapq

def solution(n, roads, sources, destination):
    answer = []
    
    # 인접 리스트
    graph = {}
    for node1, node2 in roads:
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)
        
        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)
    
    # 초기화
    costs = [sys.maxsize] * (n+1)
    costs[destination] = 0 
    
    hq = [] 
    heapq.heappush(hq, (0, destination)) # cost, node
    
    
    # 다익스트라
    while hq:
        cost, node = heapq.heappop(hq)
        
        for next_node in graph[node]:
            if costs[next_node] > costs[node] + 1:
                costs[next_node] = costs[node] + 1
                heapq.heappush(hq, (costs[next_node], next_node))
    
    # destination 비용만 추출
    for each_source in sources:
        if costs[each_source] != sys.maxsize:
            answer.append(costs[each_source])
        else:
            answer.append(-1)
    
    return answer