class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_count = 0
        counts = []
        for t in set(tasks):
            counts.append(tasks.count(t))
            max_count = max(max_count, tasks.count(t))
        return max((max_count - 1) * (n + 1) + counts.count(max_count), len(tasks))
