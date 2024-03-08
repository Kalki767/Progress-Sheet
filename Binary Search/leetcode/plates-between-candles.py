class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        '''Approach: Binary Search Combined with prefix sum. The problem
        asks to find the number of plates between two given candles. We will
        have number of queries and for each query we need to append the
        number of plates between the two candles that are in range of the
        given query. Here the given left and right positions in the query
        might not be the positions where the candles are placed in that case
        we need to find the left and right most candles by using bisect left
        on the list of candles which contains the positions of the candles.
        After that using the prefix sum the number of plates that we have
        is the number of plates at the right candle minus the number of plate
        at the left candle. But there are some edge cases like index out of
        bound error so we need to handles the left and right most indexes 
        carefully and if one of them are out of bound then we will simply
        append 0 to our result.'''
        Candles = []
        prefix_sum = []
        running_sum = 0
        answer = []

        for i in range(len(s)): #calculating the prefix sum and holding the indexes on which a candle is there
            if s[i] == '|':
                Candles.append(i)
            else:
                running_sum += 1
            prefix_sum.append(running_sum)

        '''iterate through the querry and find the left and right most 
        candles for each query and calculate the plates based on the value 
        of the candles.'''
        for left , right in queries:
            left_index = bisect_left(Candles,left)
            right_index = bisect_left(Candles,right)
            if right_index == len(Candles) or Candles[right_index] > right:
                right_index -= 1
            plates = 0
            if 0 <= left_index < len(Candles) and 0 <= right_index < len(Candles):
                plates = prefix_sum[Candles[right_index]] - prefix_sum[Candles[left_index]]
            if plates < 0:
                plates = 0
            answer.append(plates)

        return answer
        #Time Complexity: O(mlogn) where m is length of query and n is the length of candles
        #Space Complexity : O(n) n is length of s 