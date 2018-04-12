"""The following program is related to the GSW Control Plan. This is version 
number 1. This may require further improvements on the coding in regards to 
setting up of Object Orientated Classes, but for now will see where this gets 
us.
Program Name: GSW Control system 
Author: Mcglobal
Date: 12/4/2018
"""

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
    return lux_value_room1

def room2_lux():
    """Room 2 Light sensor: L4
      (input GPIO) -> float
    Reference: Sensor 2
      
    Returns a float with the reading from the L4 input Lux sensor located in
    room 2
    """
    lux_value_room2 = l4_input # l4 = reading from input 2 on RPi.GPIO
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
      (input GPIO) -> float
    Reference: Sensor 16
    
    Returns a float with the reading from the W1 input for the upper level 
    reading of reservoir 1
    """
    upper_lev_res1 = w1_input # w1 = reading from input 16 on RPi.GPIO
    return upper_lev_res1

def reservoir1_lower_level():
    """Lower Level Reading for: Reservoir 1
      (input GPIO) -> float
    Reference: Sensor 17
    
    Returns a float with the reading from the W2 input for the lower level 
    reading of reservoir 1
    """
    lower_lev_res1 = w2_input # w2 = reading from input 17 on RPi.GPIO
    return lower_lev_res1

def reservoir2_upper_level():
    """Upper Level Reading for: Reservoir 2
      (input GPIO) -> float
    Reference: Sensor 18
    
    Returns a float with the reading from the W3 input for the upper level 
    reading of reservoir 2
    """
    upper_lev_res2 = w3_input # w3 = reading from input 18 on RPi.GPIO
    return upper_lev_res2

def reservoir2_lower_level():
    """Lower Level Reading for: Reservoir 2
      (input GPIO) -> float
    Reference: Sensor 19
    
    Returns a float with the reading from the W4 input for the lower level 
    reading of reservoir 2
    """
    lower_lev_res2 = w4_input # w4 = reading from input 19 on RPi.GPIO
    return lower_lev_res2

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