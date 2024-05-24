class Job:
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit


def sequence(names, deadlines, profits):
    jobs = [Job(i, j, k) for i, j, k in zip(names, deadlines, profits)]
    jobs.sort(key=lambda x: x.profit, reverse=True)

    maxtime = max(deadlines)
    result = [False] * maxtime
    outjob = ["-1"] * maxtime

    for job in jobs:
        for j in range(min(maxtime - 1, job.deadline - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                outjob[j] = job.name
                break
    return outjob


# names = ['a', 'b', 'c', 'd', 'e']
# deadlines = [2, 1, 2, 1, 3]
# profits = [100, 19, 27, 25, 15]

num_jobs = int(input("Enter the number of jobs: "))
print("Enter the names, deadlines, and profits as space-separated arrays:")
names = input("Names: ").split()
deadlines = list(map(int, input("Deadlines: ").split()))
profits = list(map(int, input("Profits: ").split()))

job = sequence(names, deadlines, profits)

print("The sequence of jobs to be executed is:")
print(job)
