def solution(tickets):
    answer = []
    
    graph = {}
    for s, e in tickets:
        if s not in graph:
            graph[s] = [e]
        else:
            graph[s].append(e)
    
    for key in graph:
        graph[key].sort(reverse=True)
    
    stack = [] 
    stack.append('ICN')
        
    while stack:
        node = stack[-1]
                    
        if node in graph and graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            answer.append(stack.pop())
                
    answer = answer[::-1]
                
    return answer