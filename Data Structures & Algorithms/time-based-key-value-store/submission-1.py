class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        # [(1, "foo"), (2, "bar")]
        def binary_search(values) -> str:
            # TODO: Implement
            l = 0
            r = len(values) - 1

            res = ""
            while l <= r:
                mid = (l+r)//2
                midtime = values[mid][0]
                midval = values[mid][1]

                if midtime == timestamp:
                    return midval
                elif midtime < timestamp:
                    res = midval
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        return binary_search(values)