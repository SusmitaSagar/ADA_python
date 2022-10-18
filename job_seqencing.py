job = (input("enter the job: " ))
job = job.split()

profit = (input("enter the profit: "))
profit = profit.split()

deadline = (input("enter the deadlibne: "))
deadline = deadline.split()

job = [x for x in job]
profit = [int(x) for x in profit]
deadline = [int(x) for x in deadline]

jpd_tuple = [(job[i],profit[i],deadline[i]) for i in range (0,len(job))]
#arr = sorted(jpd_tuple , key=lambda x: x[2] , reverse=True)
print(jpd_tuple) #jdptuple ios list of tuple
sort = sorted(jpd_tuple, key=lambda j:j[2], reverse=True)
n=sort[0][2]
print("No of slots : " , n)
 
def  job_sequencing(jpd_tuple, max_deadline):
    sorted(jpd_tuple , key=lambda j: j[2] , reverse=True) #sorted based on deadline in decreasing orddee  
    res = []
    
    for i in reversed(range(max_deadline )): #iterate slotes
        max_profit = jpd_tuple[0]
        for item in jpd_tuple:     # linear search O(n)
           if (item[2] == i+1):  #step 3  multiple job with samne deadline
             if item[1]>max_profit[1]:   
                max_profit = item
        res.append(max_profit)        
    return  res 
print(job_sequencing(jpd_tuple,n))    




        

















