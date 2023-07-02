class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [[] for i in range(numRows)]
        iteration = [i for i in range(numRows)]
        iteration += [i for i in range(iteration[-1]-1, 0, -1)]

        index = 0
        for char in s:
            location = iteration[index]
            zigzag[location].append(char)
            index += 1
            if index >= len(iteration):
                index = 0
        
        answer = ""
        for row in zigzag:
            answer += "".join(row)
        return answer