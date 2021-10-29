import redfish

def get_gpu(REDFISH_OBJ, SYSTEM_URL):

    NUM_PCI_DEVICES = REDFISH_OBJ.get("/redfish/v1//Chassis/1/Devices/").obj['Members@odata.count']

    for i in range(NUM_PCI_DEVICES + 1):
        PCI_Devices = REDFISH_OBJ.get("/redfish/v1/Chassis/1/Devices/" + str(i)).dict
        if PCI_Devices.get('DeviceType') == "GPU":
            print("Host:", SYSTEM_URL)
            print("\t", "Manufacturer:", PCI_Devices.get('Manufacturer'))
            print("\t", "Model:", PCI_Devices.get('Name'))
            print("\t", "Serial:", PCI_Devices.get('SerialNumber'))
            print("\t", "PCIe Slot:", PCI_Devices.get('Location'))
    
def main():
    
    SYSTEM_URL = "https://16.85.161.201"
    LOGIN_ACCOUNT = "admin"
    LOGIN_PASSWORD = "admin123"
    try:
        REDFISH_OBJ = redfish.redfish_client(base_url=SYSTEM_URL, username=LOGIN_ACCOUNT, password=LOGIN_PASSWORD, timeout=2, max_retry=1)
        REDFISH_OBJ.login()

        get_gpu(REDFISH_OBJ, SYSTEM_URL)

        REDFISH_OBJ.logout()
    except redfish.rest.v1.RetriesExhaustedError:
        print(SYSTEM_URL, "is not an iLO address.")

if __name__ == "__main__":
    main()