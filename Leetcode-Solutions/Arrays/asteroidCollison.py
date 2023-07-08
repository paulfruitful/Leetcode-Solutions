class Solution(object):
    def asteroidCollision(self, asteroids):
      
     stack = []

     for asteroid in asteroids:
        if not stack or asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(asteroid)
            elif stack[-1] == -asteroid:
                stack.pop()
     return stack

            
    
