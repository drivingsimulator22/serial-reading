import serial
# COM6 : SIMTools COM
# COM2 : Python Com
# COM6 --> COM2 from virtual port software.
# identifying serial com and baudrate
ser = serial.Serial(
    port='COM2',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
#################################
print("Connected to: " + ser.portstr) #   <--- Making sure we're connected to COM2
while(True):
        line = ser.read(17)
        if "P" in str(line):    ##### Used this line to remove empty readings.
            x = str(line)      ###### Turning the byte into string
            x = x[2:]          ###### Removing first character "b" and quote from beginning of string
            x = x[:-1:] + "," ####### Removing quote at the end of the bytearray and adding "," at the end to use as a delimiter later
            indiv_reading=[]            ####### We put individual readings into this list to join later into 
            final_list=[]        ####### Final list after joining each number.
            for i in x: ######## This loop to remove P,R,Y from string
                if i == "P" or i == "R" or i =="Y":
                    pass
                else:
                    if i != ",":               ######### Split string into numbers using "," as delimiter
                        indiv_reading.append(i)   #### append each number into string to join later and add to final list
                    elif i == ",": 
                        joined ="".join(indiv_reading)   #### join the list using "," as a delimiter 
                        final_list.append(joined)        #### append the joined list into the final list that contains all values
                        indiv_reading=[]                 #### reset first list to re-use again.
            print(final_list)


ser.close()