class TimeMap:

    def __init__(self):
        self.ret = {}  # Stores key -> list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ret:
            self.ret[key].append([value, timestamp])
        else:
            self.ret[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return an empty string
        if key not in self.ret:
            return ""

        values = self.ret[key]  # List of [value, timestamp] pairs for the key
        l, r = 0, len(values) - 1
        ret = ""

        # Perform binary search to find the largest timestamp <= given timestamp
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                ret = values[mid][0]  # Update the result with the current value
                l = mid + 1  # Move to the right to find a larger timestamp
            else:
                r = mid - 1  # Otherwise, move to the left

        return ret

