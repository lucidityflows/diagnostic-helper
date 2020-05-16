# File Name: diagnostics_util.py
# Purpose: Helper methods to make diagnostic requests more customizable.

import geocoder
import psutil
import datetime
import os
import time
import random
import math
import random


# Name: get_lat_long
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, and appends key-value pairs for 'latitude' and 'longitude'. Values are
#          String representations of this data. The value of diagnostic_dict is then returned to the user.


def get_lat_long(diagnostic_dict):

    current_location = geocoder.ip('me')
    latitude = current_location.lat
    longitude = current_location.lng
    diagnostic_dict["latitude"] = latitude
    diagnostic_dict["longitude"] = longitude

    return diagnostic_dict


# Name: get_battery_info
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, and appends key-value pairs for 'battery_percentage',
#          'battery_minutes_remaining', and 'plugged_in'. Values are String representations of this data.
#          The value of diagnostic_dict is then returned to the user.


def get_battery_info(diagnostic_dict):

    sensor_battery_tuple = psutil.sensors_battery()
    battery_percentage = sensor_battery_tuple[0]
    battery_seconds_left = sensor_battery_tuple[1]
    battery_minutes_left = (battery_seconds_left // 60)
    plugged_in = str(sensor_battery_tuple[2])

    diagnostic_dict["battery_percentage"] = battery_percentage
    diagnostic_dict["battery_minutes_remaining"] = battery_minutes_left

    return diagnostic_dict


# Name: get_timestamp
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, and appends key-value pairs for 'timestamp'.  Values are String
#          representations of this data. The value of diagnostic_dict is then returned to the user.


def get_timestamp(diagnostic_dict):

    timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    diagnostic_dict["timestamp"] = timestamp

    return diagnostic_dict


# Name: get_heartbeat
# Parameters: None
# Purpose: Creates an empty dictionary named 'heartbeat_dict'. Appends values to the dictionary that represent
#          'latitude', 'longitude', 'timestamp', 'battery_percentage', 'battery_minutes_remaining',
#          'battery_plugged_in', and 'computer_id'. Returns the dictionary to the user.


def get_heartbeat(computer_id):

    heartbeat_dict = {}
    heartbeat_dict = get_lat_long(heartbeat_dict)
    heartbeat_dict = get_timestamp(heartbeat_dict)
    heartbeat_dict = get_battery_info(heartbeat_dict)
    heartbeat_dict["computer_id"] = computer_id

    return heartbeat_dict


# Name: perform_memory_test
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, times hows long it takes to add 1 million items to a list, and appends
#          key-value pairs for 'memory_test_result', 'memory_test_exception', 'memory_test_time_to_complete',
#          'memory_test_start_time', and 'memory_test_end_time'. Values are String representations of this. The
#          value of diagnostic_dict is then returned to the user.


def perform_memory_test():

    try:

        start_time = time.time()
        test_list = []

        for i in range(0, 1000000):
            test_list.append(i)

        end_time = time.time()
        memory_test_result = "pass"
        memory_test_exception = "no issues detected"

    except Exception as e:

        end_time = time.time()
        memory_test_result = "fail"
        memory_test_exception = e

    finally:

        memory_dict = {}
        seconds_to_complete_test = end_time - start_time
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
        seconds_to_complete_test = format(seconds_to_complete_test, ".2f")
        memory_dict["memory_test_result"] = memory_test_result
        memory_dict["memory_test_exception"] = memory_test_exception
        memory_dict["memory_test_start_time"] = start_time
        memory_dict["memory_test_end_time"] = end_time
        memory_dict["memory_test_time_to_complete"] = float(seconds_to_complete_test)

        return memory_dict


# Name: perform_storage_test
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, creates a 1MB .txt file, and appends key-value pairs for 'storage_test_
#          result', 'storage_test_exception', 'storage_test_start_time', 'storage_test_end_time', and
#          'storage_test_time_to_complete'. Values are String representations of this. The value of
#          diagnostic_dict is then returned to the user.


def perform_storage_test():

    try:

        start_time = time.time()
        test_file = open("storage_test_file.txt", "w")
        stat_info = os.stat("storage_test_file.txt")
        counter = 1

        while stat_info.st_size < 1000000:

            test_file.write("This is line " + str(counter) + "\n")
            stat_info = os.stat("storage_test_file.txt")
            counter += 1

        test_file.close()

        end_time = time.time()

        storage_test_result = "pass"
        storage_test_exception = "no issues detected"

    except Exception as e:

        end_time = time.time()
        storage_test_result = "fail"
        storage_test_exception = e

    finally:

        storage_dict = {}
        seconds_to_complete_test = end_time - start_time
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
        seconds_to_complete_test = format(seconds_to_complete_test, ".2f")

        storage_dict["storage_test_result"] = storage_test_result
        storage_dict["storage_test_exception"] = storage_test_exception
        storage_dict["storage_test_start_time"] = start_time
        storage_dict["storage_test_end_time"] = end_time
        storage_dict["storage_test_time_to_complete"] = float(seconds_to_complete_test)

        return storage_dict


# Name: perform_integer_test
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, performs 5000 integer operations, and appends key-value pairs
#          for 'integer_test_result', 'integer_test_exception', 'integer_test_start_time', 'integer_test_end_time',
#          and 'integer_test_time_to_complete'. Values are String representations of this. The value of diagnostic_dict
#          is then returned to the user.


def perform_integer_test():

    try:

        start_time = time.time()
        integer_set = set()

        for i in range(-5000, 5000):

            integer_set.add(i)

        for i in range(0, 5000):

            if i % 4 == 0:

                result = integer_set.pop() + integer_set.pop()

            elif i % 4 == 1:

                result = integer_set.pop() - integer_set.pop()

            elif i % 4 == 2:

                result = integer_set.pop() * integer_set.pop()

            else:

                result = integer_set.pop() / integer_set.pop()

        end_time = time.time()
        integer_test_result = "pass"
        integer_test_exception = "no issues detected"

    except Exception as e:

        end_time = time.time()
        integer_test_result = "fail"
        integer_test_exception = e

    finally:

        integer_dict = {}
        seconds_to_complete_test = end_time - start_time
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
        seconds_to_complete_test = format(seconds_to_complete_test, ".2f")

        integer_dict["integer_test_result"] = integer_test_result
        integer_dict["integer_test_exception"] = integer_test_exception
        integer_dict["integer_test_start_time"] = start_time
        integer_dict["integer_test_end_time"] = end_time
        integer_dict["integer_test_time_to_complete"] = float(seconds_to_complete_test)

        return integer_dict


# Name: perform_float_test
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, and appends key-value pairs for 'float_test_result', 'float_test_exception',
#          'float_test_start_time', 'float_test_end_time', and 'float_test_time_to_complete'. Values are String
#          representations of this. The value of diagnostic_dict is then returned to the user.


def perform_float_test():

    try:

        start_time = time.time()
        float_set = set()

        while len(float_set) < 10000:

            float_set.add(random.random())

        for i in range(0, 5000):

            if i % 4 == 0:

                result = float_set.pop() + float_set.pop()

            elif i % 4 == 1:

                result = float_set.pop() - float_set.pop()

            elif i % 4 == 2:

                result = float_set.pop() * float_set.pop()

            else:

                result = float_set.pop() / float_set.pop()

        end_time = time.time()
        float_test_result = "pass"
        float_test_exception = "no issues detected"

    except Exception as e:

        end_time = time.time()
        float_test_result = "fail"
        float_test_exception = e

    finally:

        float_dict = {}
        seconds_to_complete_test = end_time - start_time
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
        seconds_to_complete_test = format(seconds_to_complete_test, ".2f")

        float_dict["float_test_result"] = float_test_result
        float_dict["float_test_exception"] = float_test_exception
        float_dict["float_test_start_time"] = start_time
        float_dict["float_test_end_time"] = end_time
        float_dict["float_test_time_to_complete"] = float(seconds_to_complete_test)

        return float_dict

# Name: perform_prime_test
# Parameters: diagnostic_dict = a dictionary of key-value pairs that relates to diagnostic information
#                               about the gateway.
# Purpose: Accepts the diagnostic_dict, and appends key-value pairs for 'prime_test_result', 'prime_test_exception',
#          'prime_test_start_time', 'prime_test_end_time', and 'prime_test_time_to_complete'. Values are String
#          representations of this. The value of diagnostic_dict is then returned to the user.


def perform_prime_test():

    try:

        start_time = time.time()
        correct_prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41 , 43, 47, 53, 59, 61, 67,
                             71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                             151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                             233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                             317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                             419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                             503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
                             607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                             701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
                             811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                             911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
                             1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093,
                             1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193,
                             1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289,
                             1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399,
                             1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483,
                             1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571,
                             1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663,
                             1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759,
                             1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873,
                             1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,
                             1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081,
                             2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161,
                             2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281,
                             2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377,
                             2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467,
                             2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593,
                             2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689,
                             2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777,
                             2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879,
                             2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999,
                             3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109,
                             3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221,
                             3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329,
                             3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449,
                             3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539,
                             3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631,
                             3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733,
                             3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851,
                             3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943,
                             3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057,
                             4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159,
                             4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271,
                             4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397,
                             4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513,
                             4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637,
                             4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729,
                             4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861,
                             4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967,
                             4969, 4973, 4987, 4993, 4999}

        found_prime_set = set()

        for i in range(2, 5000):

            for j in range(2, i + 1):

                is_prime = True

                for num in range(2, int(math.sqrt(j)) + 1):

                    if j % num == 0:

                        is_prime = False
                        break

                if is_prime:

                    found_prime_set.add(j)

        end_time = time.time()

        if correct_prime_set == found_prime_set:

            prime_test_result = "pass"
            prime_test_exception = "no issues detected"

        else:

            prime_test_result = "fail"
            prime_test_exception = "Did not accurately find all prime numbers between 0 - 5000"

    except Exception as e:

        end_time = time.time()
        prime_test_result = "fail"
        prime_test_exception = e

    finally:

        prime_dict = {}
        seconds_to_complete_test = end_time - start_time
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
        seconds_to_complete_test = format(seconds_to_complete_test, ".2f")

        prime_dict["prime_test_result"] = prime_test_result
        prime_dict["prime_test_exception"] = prime_test_exception
        prime_dict["prime_test_start_time"] = start_time
        prime_dict["prime_test_end_time"] = end_time
        prime_dict["prime_test_time_to_complete"] = float(seconds_to_complete_test)

        return prime_dict


# Name: fulfill_test_order
# Parameters: test_name = a string that represents the name of the diagnostic test that needs to be performed.
# Purpose: Accepts 'test_name' and performs a diagnostic test according to the string value. Returns a dictionary
#          of the test results.


def fulfill_test_order(test_name):

    print("Testname requested == " + test_name)

    test_dictionary = {}

    if test_name == 'gatewayHB':

        test_dictionary = get_gw_heartbeat()

    elif test_name == 'memory':

        test_dictionary["memory"] = perform_memory_test()

    elif test_name == 'storage':

        test_dictionary["storage"] = perform_storage_test()

    elif test_name == 'integer':

        test_dictionary["integer"] = perform_integer_test()

    elif test_name == 'float':

        test_dictionary["float"] = perform_float_test()

    elif test_name == 'prime':

        test_dictionary["prime"] = perform_prime_test()

    elif test_name == 'daily_diagnostic':

        test_dictionary["daily_diagnostic"] = perform_daily_diagnostic()

    else:

        print("No valid test was requested.")

    return test_dictionary


def fulfill_custom_test_list(test_set, gateway_id):

    test_dict = {}

    test_dict["gateway_id"] = gateway_id

    if "integer" in test_set:

        test_dict["integer"] = perform_storage_test()

    if "float" in test_set:

        test_dict["float"] = perform_float_test()

    if "prime" in test_set:

        test_dict["prime"] = perform_prime_test()

    if "storage" in test_set:

        test_dict["storage"] = perform_storage_test()

    if "memory" in test_set:

        test_dict["memory"] = perform_memory_test()

    return test_dict


# Function Name: perform_daily_diagnostic
# Paramaters: computer_id = an integer meant to identify the computer that is conducting a daily diagnostic
# Purpose:
def perform_daily_diagnostic(computer_id):

    diagnostic_dictionary = {}

    diagnostic_dictionary["memory"] = perform_memory_test()
    diagnostic_dictionary["storage"] = perform_storage_test()
    diagnostic_dictionary["integer"] = perform_integer_test()
    diagnostic_dictionary["float"] = perform_float_test()
    diagnostic_dictionary["prime"] = perform_prime_test()

    diagnostic_dictionary["gateway_id"] = gateway_id

    return diagnostic_dictionary

# Function Name: string_to_list
def string_to_list(list_as_string):

    list_as_string = list_as_string[1:-1]
    string_as_list = list(list_as_string.split(','))

    for index in range(0, len(string_as_list)):
        string_as_list[index] = string_as_list[index].strip('\"')

    return string_as_list


# Function Name: show_menu
# Parameters: None
# Purpose: To display the menu options to the user in a clear and concise manner.
def show_menu():

    print("""
        
********************** Diagnostic Helper ******************
*                                                         *
*                                                         *
*                      1 - Run Tests                      *
*                      2 - Export Results to Excel        *
*                      3 - Exit                           *
*                                                         *
*                                                         *
*                                                         *
***********************************************************

          """)


# Function Name: get_user_int
# Parameters:
#       Param1- 'minValue' = an int that represents the minimum allowable value
#       Param2- 'maxValue' = an int that represents the maximum allowable value
# Purpose: This function accepts two ints, a min and max value, and prompts the user to enter a
#          valid choice. It will prevent invalid selections and check for ValueErrors. When a
#          valid choice is made, that value will be returned to the user.


def get_user_int(min_value, max_value):

    while True:

        try:

            user_int = int(input("\n\nEnter the number associated with your choice: "))

            if (user_int >= min_value) and (user_int <= max_value):

                return user_int

            else:

                print("Error! Your choice must be no smaller than " + str(min_value) +
                      " and no larger than " + str(max_value))
        except ValueError:

            print("Your value was not valid! Your number must be no smaller than " + str(min_value) +
                  " and no longer than " + str(max_value))


# Function Name: get_user_response
# Parameters: None
# Purpose: This function returns a boolean value of 'True' or 'False' in response to a user's input.
#          The only way to designate a 'True' return value is to enter a 'Y' or 'y'. Any other response
#          will return a 'False'.


def get_user_response():

    user_response = input("\n\nIf this value is correct, enter 'y', if not then press 'enter' to continue: ")

    if user_response.lower() == 'y':

        return True

    else:

        return False



