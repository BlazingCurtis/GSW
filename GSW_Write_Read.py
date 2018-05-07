import time
import calendar


def initial_time():
    """Function to read the data from the time_stamp file to find the initial
    time stamp the GSW started on
    Returns in form of int in a list"""
    infile = open('time_stamp.txt')
    lines = infile.readlines()
    data1 = []
    for line in lines:
        data1.append(line.strip(' \n'))
    infile.close()
    initial = data1[0].split()
    final = []
    for i in initial:
        final.append(int(i))
    return final


def time_write_to_file():
    """Function To collect data for the GSW Project and write to text file"""
    outfile = open('time_stamp.txt', 'a')
    new_data = time.localtime(time.time())
    for data in new_data:
        outfile.write(str(data) + ' ')
    outfile.write('\n')
    outfile.close
 
def days_since_start():
    """Returns the number of days since start day"""
    initial = initial_time()
    actual = time.localtime(time.time())
    if initial[0] == actual[0]:
        return actual[7] - initial[7]
    else:
        if calendar.isleap(initial[0]):
            return (366 - initial[7]) + actual[7]
        else:
            return (365 - initial[7]) + actual[7]
