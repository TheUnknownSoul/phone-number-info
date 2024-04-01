import phonenumbers
import argparse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-pl", "--phone-list", required=False, help="specify the list of phone numbers")
    args = arg_parser.parse_args()
    print('\u001b[38;5;129m')
    print('\u001b[40m')
    print("""
                #############################################################################
                #                                                                           #
                #   ____  _                                              _                  #
                #  |  _ \| |__   ___  _ __   ___   _ __  _   _ _ __ ___ | |__   ___ _ __    #
                #  | |_) | '_ \ / _ \| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|   #
                #  |  __/| | | | (_) | | | |  __/ | | | | |_| | | | | | | |_) |  __/ |      #
                #  |_|   |_| |_|\___/|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|      #
                #  (_)_ __  / _| ___                                                        #
                #  | | '_ \| |_ / _ \                                                       #
                #  | | | | |  _| (_) |                                                      #
                #  |_|_| |_|_|  \___/                                                       #
                #                                                                           #
                #############################################################################
                """)
    print('\u001b[0m')
    if args.phone_list is None:
        phone_number: str = input('Enter phone number with county code to get info ')
        phone = phonenumbers.parse(phone_number)
        tz = timezone.time_zones_for_number(phone)
        print("Phone number from " + geocoder.description_for_number(phone, 'en') + ".")
        print("The Telecom provider of " + str(phone) + " is " + carrier.name_for_number(phone, 'en'))
        print("Phone timezone" + str(tz))
    else:
        with open(args.phone_list) as phones:
            for line in phones:
                line = line.replace('\n', '')
                phone_line = phonenumbers.parse(line)
                tz = timezone.time_zones_for_number(phone_line)
                print("Phone number " + line + " from " + geocoder.description_for_number(phone_line,
                                                                                          'en') + '.')
                print("The Telecom provider of " + line + " is " + carrier.name_for_number(phone_line,
                                                                                           'en') + '.')
                print("Phone timezone" + str(tz))
