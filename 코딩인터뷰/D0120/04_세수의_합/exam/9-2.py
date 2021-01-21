from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        # 정렬
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            # left 는 i + 1번째로, right 는 맨마지막 원소로
            left, right = i + 1, len(nums) - 1

            # 반복문 실행 (left 가 right 보다 같거나 커진다는 것은 리스트를 모두 탐색했다는 의미)
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:  # sum 이 0 보다 작으면 left + 1 을 해줌으로써 더 큰 값을 더한다.
                    left += 1
                elif sum > 0:  # sum 이 0 보다 면 right - 1 을 해줌으로써 더 작은 값을 더한다.
                    right -= 1
                else:
                    # `sum = 0`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
