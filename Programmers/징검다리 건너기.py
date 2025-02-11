def solution(stones, k):
    
    # 이진 탐색
    
    answer = 0
    start, end = 1, max(stones)  # 돌의 최소, 최대 
    while start <= end:
        cnt = 0  # 건너지 못하는 연속된 횟수
        mid = (start+end) // 2
        # stones 확인
        for s in stones:
            if (s-mid) <= 0:
                cnt += 1
                if cnt >= k:  # 건너지 못하는 연속된 횟수가 k명 이상이면
                    break
            
            else:   # 연속 끊김!
                cnt = 0
        
        if cnt >= k:
            end = mid-1  # 돌 줄여보기
        else:
            start = mid+1  # 돌 늘려보기
            answer = start
    
    return answer