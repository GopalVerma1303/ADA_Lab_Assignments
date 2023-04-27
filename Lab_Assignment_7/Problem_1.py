import random


class Job:
    def __init__(self, start_time, duration):
        self.start_time = start_time
        self.duration = duration
        self.finish_time = start_time + duration
        self.conflicts = 0

    def __lt__(self, other):
        return self.finish_time < other.finish_time

    def conflicts_with(self, other_job):
        if self.start_time >= other_job.finish_time or self.finish_time <= other_job.start_time:
            return False
        return True

    def calculate_conflicts(self, jobs):
        for job in jobs:
            if self != job and self.conflicts_with(job):
                self.conflicts += 1

    def get_start_time(self):
        return self.start_time

    def get_finish_time(self):
        return self.finish_time

    def get_conflicts(self):
        return self.conflicts


# create 10 random jobs
jobs = []
for i in range(10):
    start_time = random.randint(0, 9)
    duration = random.randint(2, 6)
    job = Job(start_time, duration)
    jobs.append(job)

# sort jobs by finish time
jobs.sort()

# perform greedy algorithm to generate to-do list
to_do = []
for job in jobs:
    conflicts = 0
    for to_do_job in to_do:
        if job.conflicts_with(to_do_job):
            conflicts += 1
    if conflicts == 0:
        to_do.append(job)

# output to-do list
print("To-do list:")
for job in to_do:
    print("Job starting at", job.get_start_time(),
          "ending at", job.get_finish_time())

# determine conflicts for each job
for job in jobs:
    job.calculate_conflicts(jobs)
    print("Job starting at", job.get_start_time(), "ending at",
          job.get_finish_time(), "has", job.get_conflicts(), "conflicts.")
