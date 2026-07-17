class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        freq_list = sorted(freq, key=lambda x: freq[x], reverse=True)[:k]

        return freq_list