class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [ [score[i], i] for i in range(len(score)) ]
        score = sorted(score, key = lambda x: x[0])[::-1]

        rank = ["0"] * len(score)
        for i in range(len(score)):
            if i == 0:
                rank[score[i][1]] = "Gold Medal"
            elif i == 1:
                rank[score[i][1]] = "Silver Medal"
            elif i == 2:
                rank[score[i][1]] = "Bronze Medal"
            else:
                rank[score[i][1]] = str(i + 1)

        return rank
