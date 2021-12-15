from info import var  # impoting filename 

# using Exception handling concepts 
try:  #If there is no exception, then only the try clause will run, except the clause is finished
    # taking input from user 
    image_width = int(input("Enter image width :"))
    image_height = int(input("Enter image height :"))
    batch_size = int(input("Enter batch size :"))
    epochs_kitti = int(input("Enter epochs kitti :"))
    arch_layers = int(input("Enter arch layers :"))
except Exception as e: #If any exception occurs the try clause will be skipped and except clause will run.
    print("please input num") 
else: # The code enters the else block only if the try clause does not raise an exception.
    # creating new file with the help of write mode and then adding the var string.
    with open("data.txt","w")as wr:
        wr.write(var)