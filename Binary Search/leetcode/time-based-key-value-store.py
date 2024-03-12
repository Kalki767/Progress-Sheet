class TimeMap:
    '''Approach: Binary Search. The problem asks to design a dictionary that
    stores key value pair. But when a request is made to get we need to return
    associated with the given timestamp. This means we have to return a value
    whose time stamp is less than or equal to the given timestamp. If the given
    time stamp is less than the minimum time stamp we have associated with
    the given key then there would be nothing to return. So in our approach
    we stored the time stamp along with the key not the value and we stored
    the value in another dictionary associated with time stamp as key. Therefore
    when a request is made we take the list associated with the given key and
    apply bisect right to find the position of the time stamp after that we
    need to check if the list associated with the given key is not empty and
    the time stamp is not less than the minimum value we return the value
    otherwise we return "".'''

    def __init__(self):
        self.time_map = defaultdict(list)
        self.time_stamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append(timestamp)
        self.time_stamp[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        time_stamp = self.time_map[key]
        index = bisect_right(time_stamp,timestamp)
        if time_stamp and timestamp >= time_stamp[0]:
            time = time_stamp[index-1]
            return self.time_stamp[time]
        return ""
    #Time Complexity: O(logn)
    #Space Complexity: O(n)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)