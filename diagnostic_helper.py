# File Name: diagnostic_helper.py
# Purpose: The purpose of this program is to quickly check the performance of a computer or IoT device by running a
#          short series of tests based on the amount of time it takes to perform simple calculations involving integers,
#           floats, and prime numbers. Other information such as speed in writing to a generic .txt file or doing a
#          general "heartbeat" check are available for remote devices that need to check in. This is meant for demo
#          purposes only, and would need to be automated for actual use of remote devices.

import diagnostic_utils
import json


def main():

    diagnostic_utils.show_main_menu()
    main_menu_option = diagnostic_utils.get_user_int(1, 4)

    while main_menu_option != 4:

        if main_menu_option == 1:

            diagnostic_utils.show_single_test_menu()
            single_test_option = diagnostic_utils.get_user_int(1, 5)

            if single_test_option == 1:

                result = diagnostic_utils.perform_memory_test()
                print(json.dumps(result, indent=2, sort_keys=True))
                input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")


            elif single_test_option == 2:

                result = diagnostic_utils.perform_storage_test()
                print(json.dumps(result, indent=2, sort_keys=True))
                input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")

            elif single_test_option == 3:

                result = diagnostic_utils.perform_integer_test()
                print(json.dumps(result, indent=2, sort_keys=True))
                input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")

            elif single_test_option == 4:

                result = diagnostic_utils.perform_float_test()
                print(json.dumps(result, indent=2, sort_keys=True))
                input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")

            elif single_test_option == 5:

                result = diagnostic_utils.perform_prime_test()
                print(json.dumps(result, indent=2, sort_keys=True))
                input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")

            diagnostic_utils.show_main_menu()
            main_menu_option = diagnostic_utils.get_user_int(1, 4)

        elif main_menu_option == 2:

            print("\n\nPlease give choose a number between 0-1000 to identify this computer.")
            computer_id = diagnostic_utils.get_user_int(0, 1000)
            result = diagnostic_utils.perform_daily_diagnostic(computer_id)
            print(json.dumps(result, indent=2, sort_keys=True))
            input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")

            diagnostic_utils.show_main_menu()
            main_menu_option = diagnostic_utils.get_user_int(1, 4)

        elif main_menu_option == 3:

            computer_id = diagnostic_utils.get_user_int(0, 1000)
            result = diagnostic_utils.get_heartbeat(computer_id)
            print(json.dumps(result, indent=2, sort_keys=True))
            input("\n\nThe results of your test are above. When you are ready to continue, please press ENTER: ")

    print("\n\n\nExiting Program...")
    print("***********************************************************")


# Call main function
main()


