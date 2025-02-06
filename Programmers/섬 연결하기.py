import heapq

# MST -> Prim 알고리즘

def solution(n, costs):
    answer = 0
    q = []
    
    # 인접 리스트 만들기
    map = {}
    for edge in costs:
        a, b, cost = edge
        
        # cost, node 순 append
        if a not in map:
            map[a] = [(cost, b)]
        else:
            map[a].append((cost, b))
        
        if b not in map:
            map[b] = [(cost, a)]
        else:
            map[b].append((cost, a))
    
    visit = set([0])
    
    for edge in map[0]:
        cost, b = edge
        heapq.heappush(q, (cost, b))
    
    while q:
        cost, next_node  = heapq.heappop(q)
        
        if next_node not in visit:
            visit.update([next_node])
            answer += cost
            
            for edge in map[next_node]:
                b, cost = edge
                heapq.heappush(q, (b, cost))
        
    return answer