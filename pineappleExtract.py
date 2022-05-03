# print the double nested ssid field from all json files in a directory
# formatted for use with Hak5 Wifi Pineapple json output
# usage: python3 ssidExtract.py <directory>

import os
import json
import sys

directory = sys.argv[1]
print("\"" + "Dataset" + "\",\"" + "BSSID" + "\",\"" + "SSID" + "\",\"" + "Encryption" + "\",\"" + "Channel" + "\",\"" + "Signal" + "\"")
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # print filename in a box
        # print("-" * len(filename) + "\n" + filename + "\n" + "-" * len(filename))
        #print column headers File, BSSID, SSID, encryption, channel, and signal
        with open(os.path.join(directory, filename)) as f:
            data = json.load(f)

            # Try without a key
            try:
                for mac in data[0]["aps"]:
                    ssid = data[0]["aps"][mac]["ssid"]
                    encryption = data[0]["aps"][mac]["encryption"]
                    channel = data[0]["aps"][mac]["channel"]
                    signal = data[0]["aps"][mac]["signal"]
                    # print mac, ssid, encryption, channel, and signal in quotes, comma separated, and in columns
                    print("\"" + filename + "\",\"" + mac + "\",\"" + ssid + "\",\"" + encryption + "\",\"" + str(channel) + "\",\"" + str(signal) + "\"")

            except KeyError:
                pass
            except TypeError:
                pass

            # Try using the first key found
            for key in data:
                try:
                    for mac in data[key]["aps"]:
                        ssid = data[key]["aps"][mac]["ssid"]
                        encryption = data[key]["aps"][mac]["encryption"]
                        channel = data[key]["aps"][mac]["channel"]
                        signal = data[key]["aps"][mac]["signal"]
                        # print the ssid in quotes
                        print("\"" + filename + "\",\"" + mac + "\",\"" + ssid + "\",\"" + encryption + "\",\"" + str(channel) + "\",\"" + str(signal) + "\"")


                except KeyError:
                    pass
                except TypeError:
                    pass

            # print("## END OF LIST ##")
            # print("\n")