class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a mapping of scores to their original indices
        score_map = {s: i for i, s in enumerate(score)}
        
        # Sort the scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Initialize ranks
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        
        # Assign ranks to the athletes
        result = []
        for s in score:
            index = sorted_scores.index(s)
            result.append(ranks[index])
        
        return result