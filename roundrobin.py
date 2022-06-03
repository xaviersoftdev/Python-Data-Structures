from listqueue import ListQueue


def round_robin(job_queue):
    """ Each job in the job queue has a time slice of
    10 time units. An unfinished job will be returned
    to the rear of the queue. """
    while not job_queue.isEmpty():
        currentJob = job_queue.peek()
        print("Current Job: ", job_queue.peek())
        if currentJob <= 10:
            print("Job finished")
            job_queue.pop()
        elif currentJob > 10:
            print("Job unfinished")
            currentJob -= 10
            job_queue.add(currentJob)
            job_queue.pop()
        print("Job Queue: ", job_queue)








def test_round_robin():
    job_list = [17, 5, 32, 8, 24]
    job_queue = ListQueue(job_list)
    print("Initial job queue:", job_queue)
    round_robin(job_queue)


test_round_robin()
