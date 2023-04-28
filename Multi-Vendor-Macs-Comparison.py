from netmiko import ConnectHandler


def get_sorted_vlans(device_ip, device_type, username, password, interface,session_log):
    # Connect to device
    connection = ConnectHandler(device_type=device_type, ip=device_ip,
                                username=username, password=password, 
                                session_log=session_log)

    # Determine command based on device_type
    if device_type == 'huawei':
        command = f'display mac-address dynamic interface {interface}'
        mac_addresses = connection.send_command(command ,read_timeout=120)
        vlan_set = set()
        for line in mac_addresses.split('\n'):
            if '-' in line:
                mac = line.split()[0]
                if len(mac) == 14 and mac.count('-') == 2:
                    vlan = line.split()[1]
                    if vlan.isdigit() and 1 <= int(vlan) <= 4096:
                        vlan_set.add(int(vlan)) 

    elif device_type == 'cisco_ios':
        command = f'show mac address-table dynamic interface {interface}'
        mac_addresses = connection.send_command(command ,read_timeout=120)
        vlan_set = set()
        for line in mac_addresses.split('\n'):
            if '.' in line:
                mac = line.split()[1]
                if len(mac) == 14 and mac.count('.') == 2:
                    vlan = line.split()[0]
                    if vlan.isdigit() and 1 <= int(vlan) <= 4096:
                        vlan_set.add(int(vlan))

    elif device_type == 'cisco_xe':
        command = f'show mac address-table dynamic | include {interface}'
        mac_addresses = connection.send_command(command ,read_timeout=120)
        vlan_set = set()
        for line in mac_addresses.split('\n'):
            if '.' in line:
                mac = line.split()[1]
                if len(mac) == 14 and mac.count('.') == 2:
                    vlan = line.split()[0]
                    if vlan.isdigit() and 1 <= int(vlan) <= 4096:
                        vlan_set.add(int(vlan))

    else:
        raise ValueError(f"Unknown device type: {device_type}")


    # Sort the VLANs in ascending order
    sorted_vlans = sorted(vlan_set)

    print(f"Found {len(vlan_set)} VLANs: {sorted_vlans}")

    # Write VLANs to file
    with open(f'vlans_{device_ip}.txt', 'w') as f:
        f.write('\n'.join(str(vlan) for vlan in sorted_vlans))
        
    return sorted_vlans

device_ip1 = input('Please enter the IP of the device1: ' )
interface1 = input('Please specify the interface for the device1: ')
vendor1 = input('Please specify one of this options (huawei, cisco_ios, cisco_xe): ')
sorted_vlans_device1 = get_sorted_vlans(device_ip=device_ip1,
                                        device_type = vendor1,
                                        username = 'XXXX',
                                        password = 'XXXX',
                                        interface = interface1,
                                        session_log = 'ssh1.log',
                                        )

device_ip2 = input('Please enter the IP of the device2: ' )
interface2 = input('Please specify the interface for the device2: ')
vendor2 = input('Please specify one of this options (huawei, cisco_ios, cisco_xe): ')
sorted_vlans_device2 = get_sorted_vlans(device_ip=device_ip2,
                                        device_type = vendor2,
                                        username = 'XXXX',
                                        password = 'XXXX',
                                        interface = interface2,
                                        session_log = 'ssh2.log',
                                        )

# Convert the lists to sets
set_vlans_device1 = set(sorted_vlans_device1)
set_vlans_device2 = set(sorted_vlans_device2)

# Find the difference between the sets
missing_in_device1 = sorted(list(set_vlans_device2 - set_vlans_device1))
missing_in_device2 = sorted(list(set_vlans_device1 - set_vlans_device2))

# Print the results
print(f"VLANs missing in Device 1 but present in Device 2: {missing_in_device1}")
print(f"VLANs missing in Device 2 but present in Device 1: {missing_in_device2}")

# Open files for writing results
with open(f"missing_in_device1_{device_ip1}.txt", "w") as f1, open(f"missing_in_device2_{device_ip2}.txt", "w") as f2:
    # Write missing VLANs from device1 to file
    f1.write(f"VLANs missing in Device 1 but present in Device 2: {missing_in_device1}")
    
    # Write missing VLANs from device2 to file
    f2.write(f"VLANs missing in Device 2 but present in Device 1: {missing_in_device2}")
    
