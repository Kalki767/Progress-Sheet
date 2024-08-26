# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def lcm(a,b):
        return (a*b)//math.gcd(a,b)
    def fractionAddition(self, expression: str) -> str:
        '''Approach: Math. The problem asks to evaluate some fraction given in a string
        format. So since we are only given either addition or subtraction we can
        simply use the basic maths to perform those operations. That means we take
        the LCM of the denominators and divide the LCM by the denominator and multiply
        the quotient with the numerator and we continue doing this for all fractions.
        Therefore to perform this operation first we need to know each denominators
        and their assocaited numerator. Since the same denominator might appear multiple
        times and finding the LCM of the same number is just a waste we can use the
        denominators as key and their associated numerator values as a list. After 
        doing that we can simply find the LCM and add the numerators together. Finally
        we need to make the fraction irreducible for that case we find the gcd of the
        numerator and denominator and divide them by that number and return them as
        a string. There is one exception to that if the numerator is 0 we can simply
        return 0/1.'''

        #Step1: store the denominator and numerator as key, value pairs
        denominators = defaultdict(list)
        negative = False
        index = 0
        if expression[0] == '-': #check if the first fraction is negative
            negative = True
            index += 1
        while index < len(expression):

            #hold the value of the numerator
            numerator = []
            while index < len(expression) and expression[index] != '/':
                numerator.append(expression[index])
                index += 1
            num = int(''.join(numerator))
            if negative: #check it's negativity
                num *= -1
            negative = False
            index += 1

            #hold the value of the denominator
            denom = []
            while index < len(expression) and (expression[index] != '+' and expression[index] != '-'):
                denom.append(expression[index])
                index += 1
            denominator = int(''.join(denom))
            denominators[denominator].append(num)

            if index < len(expression) and expression[index] == '-':
                negative = True
            index += 1
        
        #Step2: Take all the denominators and find their LCM
        denominator = 1
        for key in denominators.keys():
            denominator = lcm(denominator,key)
        
        #Step3: divide the LCM by each denominator and multiply that value with the associated numerator
        numerator = 0
        for key, value in denominators.items():
            quotient = denominator//key
            for val in value:
                cur = quotient * val
                numerator += cur
        
        #Step4: check for edge case like when the numerator is 0
        if numerator == 0:
            return '0/1'

        #Step5: Take the gcd of the numerator and denominator and divide them
        num = numerator * -1 if numerator < 0 else numerator
        Gcd = math.gcd(num,denominator)
        numerator //= Gcd
        denominator //= Gcd
        answer = [str(numerator),'/',str(denominator)]

        return "".join(answer)
        #Time Complexity: O(n) where n is the length of the input
        #Space Complexity: O(n)