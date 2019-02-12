# Class to implement Queue
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
    def sort(self):
        self.items.sort(key = lambda x: x.arrivalTime)
        
    def __getitem__(self, i):
        return self.items[i]

# Encapsulates the particulars of a process
class Process:
    def __init__(self, jobID, processingTime, arrivalTime):
        self.jobID = jobID
        self.processingTime = processingTime
        self.arrivalTime = arrivalTime
        self.startTime = None
        self.completionTime = None
        self.responseTime = None

ch = 'y'

pQueue = Queue()                                                                # Creating a new Queue instance

while ch == 'y' or ch == 'Y':                                                   # While the response is 'y' or 'Y'
    jobID = int(raw_input("Enter Job ID. \n>> "))                               # Job ID
    processingTime = int(raw_input("Enter Processing Time of the job. \n>> "))  # Processing time / Burst Time
    arrivalTime = int(raw_input("Enter Arrival Time of the job. \n>> "))        # Arrival Time / Release Time
    
    p = Process(jobID, processingTime, arrivalTime)                             # Creating a new process instance
    pQueue.enqueue(p)                                                           # Enqueuing the process
    
    ch = raw_input("Process enqueued! Want to enter more?\n>> ")

pQueue.sort()                                                                   # Sorting the queue in O(n * log(n))
currentTime = 0                                                                 # Current Time

for i in range(pQueue.size()):
    if currentTime < pQueue[i].arrivalTime:
        currentTime = pQueue[i].arrivalTime
    
    pQueue[i].startTime = currentTime
    pQueue[i].completionTime = currentTime + pQueue[i].processingTime
    currentTime = pQueue[i].completionTime
    pQueue[i].responseTime = pQueue[i].completionTime - pQueue[i].arrivalTime

print "The maximum response time among the jobs can be minimized"
print "\tJOB ID\tProcessing\tArrival\tStart Time\tCompletion\tResponse\n"
    
while pQueue.size() > 0:
    currentProcess = pQueue.dequeue()
    
    print "\t" + str(currentProcess.jobID) + "\t" + str(currentProcess.processingTime) + "\t\t" + str(currentProcess.arrivalTime) + "\t" + str(currentProcess.startTime) + "\t\t" + str(currentProcess.completionTime) + "\t\t" + str(currentProcess.responseTime)
