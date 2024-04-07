from psutil import cpu_percent #Import psutil library.

cpu_usage=0.0 # Declare global variable.       

def monitor_health_of_server(): #Function declaration.
    print("Monitoring CPU usage...")
    threshold =80 #Define Threshold value.
    
    while(cpu_percent(1)<100):     #Continues until interrupted
        cpu_usage=cpu_percent(1)   #Get the current CPU usage as a percentage.
        print("CPU Usage: ",cpu_usage)

        if(cpu_usage>threshold): #Monitoring health of serve till CPU usage exceeds a predefined threshold.
            print("Alert! CPU usage exceeds threshold: ",cpu_usage) #Print alert.

monitor_health_of_server() #Calling function