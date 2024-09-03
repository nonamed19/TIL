def permutation(arr, r):
    arr = sorted(arr)  # 입력된 배열을 정렬하여 순서를 고정
    used = [0 for _ in range(len(arr))]  # 각 요소의 사용 여부를 체크하기 위한 리스트

    def generate(chosen, used):
        if len(chosen) == r:  # 선택된 요소의 길이가 r과 같으면
            print(chosen)  # 현재 조합 출력
            return

        for i in range(len(arr)):  # 배열의 각 요소에 대해 반복
            if not used[i]:  # 해당 요소가 사용되지 않았다면
                chosen.append(arr[i])  # 요소를 선택 리스트에 추가
                used[i] = 1  # 사용됨으로 표시
                generate(chosen, used)  # 재귀적으로 다음 선택을 진행
                used[i] = 0  # 다시 사용되지 않은 상태로 되돌림
                chosen.pop()  # 마지막으로 추가한 요소를 제거

    generate([], used)  # 빈 리스트와 초기 사용 상태로 재귀 함수 호출


# permutation('ABCD', 2)
# permutation([1, 2, 3, 4, 5], 5)