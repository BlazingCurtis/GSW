"""The Main run programme for the GSW project"""

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
    

def timer_lights_on_off_room1():
    """The Function to set the time the lights are on this should take in 
    consideration how many days have past and what stage the G is at
    
    Preset_1: 24 hours on for first 30 days 
    Preset_2: 18 hours on 6 hours off from 30 to 60 days
    Preset_3: 12 hours on 12 hours off from 60 to 90 days
    Preset_4: 6 hours on 18 hours off from 90 to 120 days
    """
    localtime = time.localtime(time.time())[3] # Hour of the day
    day_number = days_since_start()
    if day_number < 30:
        return True # Lights On
    elif day_number >= 30 and day_number < 60:
        if localtime >= 10 and localtime < 16:
            return False # Lights Off
        else:
            return True # Lights On
    elif day_number >= 60 and day_number < 90:
        if localtime >= 6 and localtime < 18:
            return False # Lights Off
        else:
            return True # Lights On
    else:
        if localtime >= 0 and localtime < 6:
            return True # Lights On
        else:
            return False # Lights Off
        
def timer_lights_on_off_room2():
    """The Function to set the time the lights are on this should take in 
    consideration how many days have past and what stage the G is at
    
    Preset_1: 24 hours on for first 30 days 
    Preset_2: 18 hours on 6 hours off from 30 to 60 days
    Preset_3: 12 hours on 12 hours off from 60 to 90 days
    Preset_4: 6 hours on 18 hours off from 90 to 120 days
    True = Lights ON
    False = Lights OFF
    """
    localtime = time.localtime(time.time())[3] # Hour of the day
    day_number = days_since_start()
    if day_number < 30:
        return True # Lights On
    elif day_number >= 30 and day_number < 60:
        if localtime >= 10 and localtime < 16:
            return False # Lights Off
        else:
            return True # Lights On
    elif day_number >= 60 and day_number < 90:
        if localtime >= 6 and localtime < 18:
            return False # Lights Off
        else:
            return True # Lights On
    else:
        if localtime >= 0 and localtime < 6:
            return True # Lights On
        else:
            return False # Lights Off
        

def check_lighting_state_room1():
    """Function to check lighting state is correct, and adjust the lighting if 
    required turn on or off for room 1"""
    if timer_lights_on_off_room1() == room1_lux():
        pass
    else:
        light_room1(timer_lights_on_off_room1())
        
def check_lighting_state_room2():
    """Function to check lighting state is correct, and adjust the lighting if 
    required turn on or off for room 2"""
    if timer_lights_on_off_room2() == room2_lux():
        pass
    else:
        light_room2(timer_lights_on_off_room1())
        
def check_water_resivoirs():
    """Function to check the levels of water resivoirs and fill if required"""
    if reservoir1_lower_level():
        while not reservoir1_upper_level():
            water_res1_fill(True)
            time.sleep(5)
            peris_pump_res1(True)
            time.sleep(10)
            peris_pump_res1(False)
        else:
            water_res1_fill(False)
    elif reservoir2_lower_level():
        while not reservoir2_upper_level():
            water_res2_fill(True)
            time.sleep(5)
            peris_pump_res2(True)
            time.sleep(10)  
            peris_pump_res1(False)
        else:
            water_res2_fill(False)        
        
    

def main():
    system_ok = True
    master_water(True) # Turn Master Water Supply ON
    if not trip_sensor(): # Trip Sensor Intruder alert not active
        """Check Lighting State both rooms"""
        check_lighting_state_room1()
        check_lighting_state_room2()
        """Check and Power Bubbler"""
        bubbler(True)
        """Check and Fill Water resivoirs"""
        check_water_resivoirs()
        
    
    
    