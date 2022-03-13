def calculate(ops):
    # ops = ["5", "3", "4", "C", "D", "7", '+', "+"] ops is an list
    score = []
    ans = 0
    # countPlus = 0
    for i in range(0, len(ops)):
        if ops[i] != "+" and ops[i] != "C" and ops[i] != "D":
            score.append(ops[i])
        if ops[i] == "C":
            score.pop(len(score) - 1)
        if ops[i] == "D":
            newVal = int(score[len(score) - 1]) * 2
            score.append(str(newVal))
        if ops[i] == "+":
            ans += sum(int(number) for number in score)
    return ans
