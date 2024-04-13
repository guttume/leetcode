class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        stack = []

        for pos, spd in cars:
            eta = (target - pos) / spd
        
            stack.append(eta)
    
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
    
        return len(stack)