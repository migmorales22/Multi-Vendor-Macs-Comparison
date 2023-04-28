# Multi-Vendor-Macs-Comparison
This Python script utilizes the netmiko library to connect to different devices through SSH and retrieve the VLANs present on a specific interface. The script can handle devices from different vendors, including Huawei, Cisco IOS, and Cisco XE. After retrieving the VLANs, the script sorts them in ascending order and writes them to a file named "vlans_<device_IP>.txt". Then, it compares the VLANs on two different devices by finding the missing VLANs in each device and writes them to separate files named "missing_in_device1_<device_IP1>.txt" and "missing_in_device2_<device_IP2>.txt".

To run the script, the user is prompted to enter the IP address, interface, and vendor of each device, as well as the SSH credentials. The script logs the SSH session output to separate files named "ssh1.log" and "ssh2.log".

## Usage:
1. Open the Multi-Vendor-Macs-Comparison.py file in a text editor of your choice, and add the necessary credentials to the script:
```js
# Replace 'XXXX' with your own device credentials
sorted_vlans_device1 = get_sorted_vlans(device_ip=device_ip1,
                                        device_type = vendor1,
                                        username = 'XXXX',
                                        password = 'XXXX',
                                        interface = interface1,
                                        session_log = 'ssh1.log',
                                        )
sorted_vlans_device2 = get_sorted_vlans(device_ip=device_ip2,
                                        device_type = vendor2,
                                        username = 'XXXX',
                                        password = 'XXXX',
                                        interface = interface2,
                                        session_log = 'ssh2.log',
                                        )
```
2. Run the script by executing the following command:
```js
python3 Multi-Vendor-Macs-Comparison.py
```
3. Follow the prompts to enter the required information, including the IP address and device type of each device, as well as the interface to be compared.
4. The script will output a list of VLANs that are missing in each device, as well as write the results to separate text files in the project directory.
5. Review the results and troubleshoot any issues as needed.

**Note:** Be sure to replace 'XXXX' with the correct credentials for each device before running the script.

## Output:
After the script completes, it will display the VLANs that are missing on each device in the terminal. It will also generate two files, which contain the same information in text format.

```js
Please enter the IP of the device1: 10.179.28.4
Please specify the interface for the device1: GigabitEthernet6/1/2
Please specify one of this options (huawei, cisco_ios, cisco_xe): huawei
Found 16 VLANs: [10, 61, 326, 387, 1401, 1723, 2468, 2657, 3025, 3028, 3030, 3579, 3705, 3737, 3747, 3750]
Please enter the IP of the device2: 10.179.28.5
Please specify the interface for the device2: GigabitEthernet5/1/1
Please specify one of this options (huawei, cisco_ios, cisco_xe): huawei
Found 6 VLANs: [10, 1401, 3025, 3028, 3030, 3579]
VLANs missing in Device 1 but present in Device 2: []
VLANs missing in Device 2 but present in Device 1: [61, 326, 387, 1723, 2468, 2657, 3705, 3737, 3747, 3750]
```

## Conclusion:
With this script, you can easily compare VLANs across different devices and identify any inconsistencies. This can be helpful in troubleshooting network connectivity issues or ensuring consistent network configurations across devices.

## Requirements:

* netmiko==4.1.2
* Python 3.11 =>
