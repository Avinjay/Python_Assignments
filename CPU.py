import psutil
import time


def threshold(inp):
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
            if (cpu_percentage > inp):
                print("Alert!CPU usage exceeds threshold:",cpu_percentage,"%" )
                
                # Optional: Add a delay before checking again
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by the user.")
    except Exception as e:
        print("The error is:",e)   

try:
    inp = float(input("Enter Threshold after this program will throw alert\n"))
    threshold(inp)
except KeyboardInterrupt:
    print("\nMonitoring stopped by the user.")
    
        
