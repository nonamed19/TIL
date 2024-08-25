def combination(arr, r):
    arr = sorted(arr)  # 입력된 배열을 정렬하여 순서를 고정

    def generate(chosen):
        if len(chosen) == r:  # 선택된 요소의 길이가 r과 같으면
            print(chosen)  # 현재 조합 출력
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0  # 다음 선택의 시작 위치 설정
        for nxt in range(start, len(arr)):  # 시작 위치부터 배열의 각 요소에 대해 반복
            chosen.append(arr[nxt])  # 요소를 선택 리스트에 추가
            generate(chosen)  # 재귀적으로 다음 선택을 진행
            chosen.pop()  # 마지막으로 추가한 요소를 제거

    generate([])  # 빈 리스트로 재귀 함수 호출


# combination('ABCDE', 2)
# combination([1, 2, 3, 4, 5], 3)