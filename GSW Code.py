"""The following program is related to the GSW Control Plan. This is version 
number 1. This may require further improvements on the coding in regards to 
setting up of Object Orientated Classes, but for now will see where this gets 
us.
Program Name: GSW Control system 
Author: Mcglobal
Date Started: 12/4/2018
"""

#import RPi.GPIO as GPIO
#import time
#import calendar
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(1,GPIO.OUT)
#GPIO.setup(2,GPIO.OUT)
#GPIO.setup(3,GPIO.OUT)
#GPIO.setup(4,GPIO.OUT)
#GPIO.setup(5,GPIO.OUT)
#GPIO.setup(6,GPIO.OUT)
#GPIO.setup(7,GPIO.OUT)
#GPIO.setup(8,GPIO.OUT)
#GPIO.setup(9,GPIO.OUT)
#GPIO.setup(10,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)
#GPIO.setup(12,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)
#GPIO.setup(14,GPIO.OUT)
#GPIO.setup(15,GPIO.OUT)
#GPIO.setup(16,GPIO.OUT)
#GPIO.setup(17,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)
#GPIO.setup(19,GPIO.OUT)
#GPIO.setup(20,GPIO.OUT)


"""The below code takes the readings from every input so these are availible for
the various output modules and data storage requirements.
I think these input would be the first class."""

def room1_lux():
    """Room 1 Light sensor: L3
      (input GPIO) -> float
    Reference: Sensor 1
      
    Returns a float with the reading from the L3 input Lux sensor located in 
    room 1
    """
    lux_value_room1 = l3_input # l3 = reading from input 1 on RPi.GPIO (TBC)
    if lux_value_room1 >= 100: # Preset Light value TBA
        return True # Lights are ON
    else:
        return False # Lights are off

def room2_lux():
    """Room 2 Light sensor: L4
      (input GPIO) -> float
    Reference: Sensor 2
      
    Returns a float with the reading from the L4 input Lux sensor located in
    room 2
    """
    lux_value_room2 = l4_input # l4 = reading from input 2 on RPi.GPIO
    if lux_value_room2 >= 100: # Preset Light value TBA
        return True # Lights are ON
    else:
        return False # Lights are off
    return lux_value_room2   

def moisture_subject1():
    """Moisture sensor for: Subject 1
      (input GPIO) -> float
    Reference: Sensor 3
    
    Returns a float with the reading from the M1 input moisture sensor for
    subject 1
    """
    moist_value_sub1 = m1_input # m1 = reading from input 3 on RPi.GPIO
    return moist_value_sub1
    
def moisture_subject2():
    """Moisture sensor for: Subject 2
      (input GPIO) -> float
    Reference: Sensor 4
    
    Returns a float with the reading from the M2 input moisture sensor for
    subject 2
    """
    moist_value_sub2 = m2_input # m2 = reading from input 4 on RPi.GPIO
    return moist_value_sub2

def moisture_subject3():
    """Moisture sensor for: Subject 3
      (input GPIO) -> float
    Reference: Sensor 5
    
    Returns a float with the reading from the M3 input moisture sensor for
    subject 3
    """
    moist_value_sub3 = m3_input # m3 = reading from input 5 on RPi.GPIO
    return moist_value_sub3

def moisture_subject4():
    """Moisture sensor for: Subject 4
      (input GPIO) -> float
    Reference: Sensor 6
    
    Returns a float with the reading from the M4 input moisture sensor for
    subject 4
    """
    moist_value_sub4 = m4_input # m4 = reading from input 6 on RPi.GPIO
    return moist_value_sub4

def moisture_subject5():
    """Moisture sensor for: Subject 5
      (input GPIO) -> float
    Reference: Sensor 7
    
    Returns a float with the reading from the M5 input moisture sensor for
    subject 5
    """
    moist_value_sub5 = m5_input # m5 = reading from input 7 on RPi.GPIO
    return moist_value_sub5

def moisture_subject6():
    """Moisture sensor for: Subject 6
      (input GPIO) -> float
    Reference: Sensor 8
    
    Returns a float with the reading from the M6 input moisture sensor for
    subject 6
    """
    moist_value_sub6 = m6_input # m6 = reading from input 8 on RPi.GPIO
    return moist_value_sub6

def room1_temp():
    """Temperature sensor for: Room 1
      (input GPIO) -> float
    Reference: Sensor 9
    
    Returns a float with the reading from the T1 input for temperature reading
    of room 1 (in DegC (possibly))
    """
    temp_room1 = t1_input # t1 = reading from input 9 on RPi.GPIO
    return temp_room1

def room2_temp():
    """Temperature sensor for: Room 2
      (input GPIO) -> float
    Reference: Sensor 10
    
    Returns a float with the reading from the T2 input for temperature reading
    of room 2 (in DegC (possibly))
    """
    temp_room2 = t2_input # t2 = reading from input 10 on RPi.GPIO
    return temp_room2

def intake_temp():
    """Temperature sensor for: Intake (outside temperature)
      (input GPIO) -> float
    Reference: Sensor 11
    
    Returns a float with the reading from the T3 input for temperature reading
    of the intake (outside temperature) (in DegC (possibly))
    """
    temp_intake = t3_input # t3 = reading from input 11 on RPi.GPIO
    return temp_intake

def room1_humidity():
    """Humidity sensor for: Room 1
      (input GPIO) -> float
    Reference: Sensor 12
    
    Returns a float with the reading from the H1 input for the humidity reading
    of room 1 
    """
    humidity_value1 = h1_input # h1 = reading from input 12 on RPi.GPIO
    return humidity_value1

def room2_humidity():
    """Humidity sensor for: Room 2
      (input GPIO) -> float
    Reference: Sensor 13
    
    Returns a float with the reading from the H1 input for the humidity reading
    of room 2 
    """
    humidity_value2 = h2_input # h2 = reading from input 13 on RPi.GPIO
    return humidity_value2

def room1_co2():
    """Carbon Dioxide sensor for: Room 1
      (input GPIO) -> float
    Reference: Sensor 14
    
    Returns a float with the reading from the O1 input for the carbon dioxide
    reading of room 1 (in PPM)
    """
    co2_value_room1 = o1_input # o1 = reading from input 14 on RPi.GPIO
    return co2_value_room1

def room2_co2():
    """Carbon Dioxide sensor for: Room 2
      (input GPIO) -> float
    Reference: Sensor 15
    
    Returns a float with the reading from the O2 input for the carbon dioxide
    reading of room 2 (in PPM)
    """
    co2_value_room2 = o2_input # o2 = reading from input 15 on RPi.GPIO
    return co2_value_room2

def reservoir1_upper_level():
    """Upper Level Reading for: Reservoir 1
      (input GPIO) -> bool
    Reference: Sensor 16
    
    Returns a float with the reading from the W1 input for the upper level 
    reading of reservoir 1
    """
    upper_levr1 = w1_input # w1 = reading from input 16 on RPi.GPIO
    if upper_levr1 >= 100: # Preset level TBA
        return True # Has reached set value stop filling
    else:
        return False # Empty still filling

def reservoir1_lower_level():
    """Lower Level Reading for: Reservoir 1
      (input GPIO) -> float
    Reference: Sensor 17
    
    Returns a float with the reading from the W2 input for the lower level 
    reading of reservoir 1
    """
    lower_levr1 = w2_input # w2 = reading from input 17 on RPi.GPIO
    if lower_levr1 < 20: # Preset Level TBA
        return True # Res is empty and needs filled
    else:
        return False # Res has water and does not need filled
    
def reservoir2_upper_level():
    """Upper Level Reading for: Reservoir 2
      (input GPIO) -> float
    Reference: Sensor 18
    
    Returns a float with the reading from the W3 input for the upper level 
    reading of reservoir 2
    """
    upper_levr2 = w3_input # w3 = reading from input 18 on RPi.GPIO
    if upper_levr2 >= 100: # Preset level TBA
        return True # Has reached set value stop filling
    else:
        return False # Empty still filling    

def reservoir2_lower_level():
    """Lower Level Reading for: Reservoir 2
      (input GPIO) -> float
    Reference: Sensor 19
    
    Returns a float with the reading from the W4 input for the lower level 
    reading of reservoir 2
    """
    lower_levr2 = w4_input # w4 = reading from input 19 on RPi.GPIO
    if lower_levr2 < 20: # Preset Level TBA
        return True # Res is empty and needs filled
    else:
        return False # Res has water and does not need filled

def reservoir1_ph():
    """pH reading for: Reservoir 1
      (input GPIO) -> float
    Reference: Sensor 20
    
    Returns a float with the reading from the P1 input for the pH reading 
    of reservoir 1
    """
    ph_res1 = p1_input # p1 = reading from input 20 on RPi.GPIO
    return ph_res1

def reservoir2_ph():
    """pH reading for: Reservoir 2
      (input GPIO) -> float
    Reference: Sensor 21
    
    Returns a float with the reading from the P2 input for the pH reading 
    of reservoir 2
    """
    ph_res2 = p2_input # p2 = reading from input 21 on RPi.GPIO
    return ph_res2

def trip_sensor():
    """Trip sensor for: Intruder alert
      (input GPIO) -> bool
    Reference: Sensor 22
    
    Returns a True or False depending on the state of the sensor Q1. If 
    activated returns True, otherwise False. This sensor is for intruder alerts.
    """
    return q1_input # q1 = reading from input 22 on RPi.GPIO (0 = False, any othe value = True)


"""The below code is for the outputs these could be our secoond class"""


def master_water(status):
    """Relay Control for: Water ON/OFF (Master In)
      (bool) -> output GPIO 1
    Reference Output: Solenoid 1
    
    Activates GPIO1 output if status is True. Deactivates GPIO1 if False
    """
    if status:
        GPIO.output(1, GPIO.HIGH)
    else:
        GPIO.output(1, GPIO.LOW)

def subject1_water(status):
    """Relay Control for: Water ON/OFF (Subject 1)
      (bool) -> output GPIO 2
    Reference Output: Solenoid 2
    
    Activates GPIO2 output if status is True. Deactivates GPIO2 if False
    """
    if status:
        GPIO.output(2, GPIO.HIGH)
    else:
        GPIO.output(2, GPIO.LOW)
        
def subject2_water(status):
    """Relay Control for: Water ON/OFF (Subject 2)
      (bool) -> output GPIO 3
    Reference Output: Solenoid 3
    
    Activates GPIO3 output if status is True. Deactivates GPIO3 if False
    """
    if status:
        GPIO.output(3, GPIO.HIGH)
    else:
        GPIO.output(3, GPIO.LOW)
        
def subject3_water(status):
    """Relay Control for: Water ON/OFF (Subject 3)
      (bool) -> output GPIO 4
    Reference Output: Solenoid 4
    
    Activates GPIO4 output if status is True. Deactivates GPIO4 if False
    """
    if status:
        GPIO.output(4, GPIO.HIGH)
    else:
        GPIO.output(4, GPIO.LOW)
        
def subject4_water(status):
    """Relay Control for: Water ON/OFF (Subject 4)
      (bool) -> output GPIO 5
    Reference Output: Solenoid 5
    
    Activates GPIO5 output if status is True. Deactivates GPIO5 if False
    """
    if status:
        GPIO.output(5, GPIO.HIGH)
    else:
        GPIO.output(5, GPIO.LOW)
        
def subject5_water(status):
    """Relay Control for: Water ON/OFF (Subject 5)
      (bool) -> output GPIO 6
    Reference Output: Solenoid 6
    
    Activates GPIO6 output if status is True. Deactivates GPIO6 if False
    """
    if status:
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(6, GPIO.LOW)
        
def subject6_water(status):
    """Relay Control for: Water ON/OFF (Subject 6)
      (bool) -> output GPIO 7
    Reference Output: Solenoid 7
    
    Activates GPIO7 output if status is True. Deactivates GPIO7 if False
    """
    if status:
        GPIO.output(7, GPIO.HIGH)
    else:
        GPIO.output(7, GPIO.LOW)
        
def water_res1_fill(status):
    """Relay Control for: Water Reservior 1 Fill
      (bool) -> output GPIO 8
    Reference Output: Solenoid 8
    
    Activates GPIO8 output if status is True. Deactivates GPIO8 if False
    """
    if status:
        GPIO.output(8, GPIO.HIGH)
    else:
        GPIO.output(8, GPIO.LOW)
        
def water_res2_fill(status):
    """Relay Control for: Water Reservior 2 Fill
      (bool) -> output GPIO 9
    Reference Output: Solenoid 9
    
    Activates GPIO9 output if status is True. Deactivates GPIO9 if False
    """
    if status:
        GPIO.output(9, GPIO.HIGH)
    else:
        GPIO.output(9, GPIO.LOW)
        
def add_co2_room1(status):
    """Relay Control for: Room 1 Apply CO2
      (bool) -> output GPIO 10
    Reference Output: Solenoid 10
    
    Activates GPIO10 output if status is True. Deactivates GPIO10 if False
    """
    if status:
        GPIO.output(10, GPIO.HIGH)
    else:
        GPIO.output(10, GPIO.LOW)
        
def add_co2_room2(status):
    """Relay Control for: Room 2 Apply CO2
      (bool) -> output GPIO 11
    Reference Output: Solenoid 11
    
    Activates GPIO11 output if status is True. Deactivates GPIO11 if False
    """
    if status:
        GPIO.output(11, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
        
def light_room1(status):
    """Relay Control for: Light 1 ON/OFF
      (bool) -> output GPIO 12
    Reference Output: Relay 1
    
    Activates GPIO12 output if status is True. Deactivates GPIO12 if False
    """
    if status:
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
        
def light_room2(status):
    """Relay Control for: Light 2 ON/OFF
      (bool) -> output GPIO 13
    Reference Output: Relay 2
    
    Activates GPIO13 output if status is True. Deactivates GPIO13 if False
    """
    if status:
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(13, GPIO.LOW)
        
def fan_1(status):
    """Relay Control for: Fan ON/OFF
      (bool) -> output GPIO 14
    Reference Output: Relay 3
    
    Activates GPIO14 output if status is True. Deactivates GPIO14 if False
    """
    if status:
        GPIO.output(14, GPIO.HIGH)
    else:
        GPIO.output(14, GPIO.LOW)
        
def fan_speed_toogle(status):
    """Relay Control for: Toogle Fan Speed 1 & 2
      (bool) -> output GPIO 15
    Reference Output: Relay 4
    
    Activates GPIO15 output if status is True (Increased Fan Speed). Deactivates
    GPIO14 if False (Standard Fan Speed)
    """
    if status:
        GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(15, GPIO.LOW)
    # Will need to confirm how this function will operate with the output of GPIO
    # and how it will change the motor speed.
        
def fan_aux(status):
    """Relay Control for: Aux Fan ON/OFF (Heat Venting)
      (bool) -> output GPIO 16
    Reference Output: Relay 5
    
    Activates GPIO16 output if status is True. Deactivates GPIO16 if False
    """
    if status:
        GPIO.output(16, GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.LOW)
        
def peris_pump_res1(status):
    """Relay Control for: Peristaltic Pump Reservoir 1
      (bool) -> output GPIO 17
    Reference Output: Relay 6
    
    Activates GPIO17 output if status is True. Deactivates GPIO17 if False
    """
    if status:
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
        
def peris_pump_res2(status):
    """Relay Control for: Peristaltic Pump Reservoir 2
      (bool) -> output GPIO 18
    Reference Output: Relay 7
    
    Activates GPIO18 output if status is True. Deactivates GPIO18 if False
    """
    if status:
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
        
def water_misting(status):
    """Relay Control for: Water Misting Gizmo
      (bool) -> output GPIO 19
    Reference Output: Relay 8
    
    Activates GPIO19 output if status is True. Deactivates GPIO19 if False
    """
    if status:
        GPIO.output(19, GPIO.HIGH)
    else:
        GPIO.output(19, GPIO.LOW)

def bubbler(status):
    """Relay Control for: Bubbler
      (bool) -> output GPIO 20
    Reference Output: Relay 9
    
    Activates GPIO20 output if status is True. Deactivates GPIO20 if False
    """
    if status:
        GPIO.output(20, GPIO.HIGH)
    else:
        GPIO.output(20, GPIO.LOW)
        
        
"""The below code is for helper functions for the main programme to run"""

def initial_time(file):
    """Function to read the data from the time_stamp file to find the initial
    time stamp the GSW started on
    Returns in form of int in a list"""
    infile = open(file)
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


def time_write_to_file(file, write_mode):
    """Function To collect data for the GSW Project and write to text file"""
    outfile = open(file, write_mode)
    new_data = time.localtime(time.time())
    for data in new_data:
        outfile.write(str(data) + ' ')
    outfile.write('\n')
    outfile.close
 
def days_since_start():
    """Returns the number of days since start day"""
    initial = initial_time('time_stamp.txt')
    actual = time.localtime(time.time())
    if initial[0] == actual[0]:
        return actual[7] - initial[7]
    else:
        if calendar.isleap(initial[0]):
            return (366 - initial[7]) + actual[7]
        else:
            return (365 - initial[7]) + actual[7]
        
def mins_since_event(file):
    """Returns the number of minutes since recorded event from text file."""
    initial = initial_time(file)
    actual = time.localtime(time.time())
    if initial[3] == actual[3]:
        return actual[4] - initial[4]
    else:
        return (60 - initial[4]) + actual[4]
    

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
        time_write_to_file('res1empty.txt', 'w')
        while not reservoir1_upper_level():
            water_res1_fill(True)
            time.sleep(5)
            peris_pump_res1(True)
            time.sleep(10)
            peris_pump_res1(False)
        else:
            water_res1_fill(False)
            time_write_to_file('res1full.txt', 'w')
    elif reservoir2_lower_level():
        time_write_to_file('res2empty.txt', 'w')
        while not reservoir2_upper_level():
            water_res2_fill(True)
            time.sleep(5)
            peris_pump_res2(True)
            time.sleep(10)  
            peris_pump_res1(False)
        else:
            water_res2_fill(False) 
            time_write_to_file('res2full.txt', 'w')

def check_ph_level_res(num):
    """Function to check the pH level of resivoir num (1 or 2), only test after 
    30mins since the resivoir was filled."""
    time_since_empty = mins_since_event('res' + str(num) + 'empty.txt')
    time_since_test = mins_since_event('ph_test_res' + str(num) + '.txt')
    time_since_fill = mins_since_event('res' + str(num) + 'full.txt')
    if len(time_since_test) > 0:
        if time_since_test >= 30 and time_since_fill < 110:
            time_write_to_file('ph_test_res' + str(num) + '.txt', 'w')
            ph_notify(reservoir1_ph(), num)
        else:
            pass
    else:       
        if time_since_empty >= 30:
            time_write_to_file('ph_test_res' + str(num) + '.txt', 'w')
            ph_notify(reservoir1_ph(), num)
        else:
            pass
            
    
def ph_notify(reading, reservoir_num):
    """Gets the reading from the pH levels in either reservoir 1 or 2 and 
    notify of the result. Records to text file"""
    
    
    
"""The below code is for the main programme to run and do its thing as provided
by the description from the GSW wooksheet"""

def main():
    time_write_to_file('time_stamp.txt', 'a')
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
        """Check pH levels of reservoirs"""
        check_ph_level_res(1)
        check_ph_level_res(2)





def main():
    """Main Programme"""
    system_ok = True
    while system_ok:
        _L3 = room1_lux()
        _L4 = room2_lux()
        _M1 = moisture_subject1()
        _M2 = moisture_subject2()
        _M3 = moisture_subject3()
        _M4 = moisture_subject4()
        _M5 = moisture_subject5()
        _M6 = moisture_subject6()
        _T1 = room1_temp()
        _T2 = room2_temp()
        _T3 = intake_temp()
        _H1 = room1_humidity()
        _H2 = room2_humidity()
        _O1 = room1_co2()
        _O2 = room2_co2()
        _W1 = reservoir1_upper_level()
        _W2 = reservoir1_lower_level()
        _W3 = reservoir2_upper_level()
        _W4 = reservoir2_lower_level()
        _P1 = reservoir1_ph()
        _P2 = reservoir2_ph()
        _Q1 = trip_sensor()