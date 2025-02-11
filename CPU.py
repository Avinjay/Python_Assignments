import psutil
import time

# inp = float(input("Enter Threshold "))

# def threshold(inp):
try:
    print("Monitoring CPU usage...") 
    #print(x)
        # Track CPU percentage continuously
    while 1:
    # Get CPU usage percentage (1 second interval)
        cpu_percentage = psutil.cpu_percent(interval=1)
            
            # Print the CPU usage
            #print("CPU percent", cpu_percent,"%")
            #print(type(cpu_percent))       
        if (cpu_percentage > 15):
            print("Alert!CPU usage exceeds threshold:",cpu_percentage,"%" )
            
            # Optional: Add a delay before checking again
            time.sleep(1)
except Exception as e:
    print("The error is:",e)   

#threshold(inp)        
