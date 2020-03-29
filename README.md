This is me just playing around with Python. I am using simpy to try and simulate real world experince. 

env = simpy.Environment()

env.process(checkpoint_run(env, num_booths, check_time, passenger_arrival))

env.run(until=10)

Running the project
-------------------
 - Python (project_name)
 - Give cashier number 
 - Give servers number 
 - Give ushers number
 - And give the number of customers
