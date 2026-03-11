from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    tracker  = []
    for temp_index in range(len(temperatures)):
        while tracker and temperatures[temp_index] > temperatures[tracker[-1]]:
            last_index = tracker.pop()
            answer[last_index] = temp_index - last_index
        tracker.append(temp_index)
    return answer

