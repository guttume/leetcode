class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]
            if expr.isdigit():  # If the expression is a number, return it as an int.
                return [int(expr)]

            results = []
            
            # Iterate through the expression
            for i in range(len(expr)):
                if expr[i] in '+-*':
                    # Compute results of left and right segments
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    # Combine the results based on the operator
                    for l in left_results:
                        for r in right_results:
                            if expr[i] == '+':
                                results.append(l + r)
                            elif expr[i] == '-':
                                results.append(l - r)
                            elif expr[i] == '*':
                                results.append(l * r)

            memo[expr] = results  # Cache the result for the current expression
            return results

        return compute(expression)