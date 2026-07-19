# Parent Class: SmartDevice
class SmartDevice:
    """Base class representing a general smart device."""

    def __init__(self, name, device_id):
        # Public attribute
        self.name = name

        # Private attributes (encapsulated)
        self.__device_id = self.__validate_device_id(device_id)
        self.__power_status = False  # False = OFF, True = ON

    #  Validation 
    def __validate_device_id(self, device_id):
        # Device ID cannot be empty
        if not device_id or str(device_id).strip() == "":
            raise ValueError("Device ID cannot be empty.")
        return device_id

    #  Getters and Setters (using @property) 
    @property
    def device_id(self):
        """Getter for device_id (read-only, cannot be changed directly)."""
        return self.__device_id

    @property
    def power_status(self):
        """Getter for power_status."""
        return self.__power_status

    @power_status.setter
    def power_status(self, status):
        """Setter for power_status. Only accepts True/False."""
        if not isinstance(status, bool):
            raise ValueError("Power status must be True or False.")
        self.__power_status = status

    #  Methods 
    def turn_on(self):
        self.power_status = True
        print(f"[{self.name}] is now ON.")

    def turn_off(self):
        self.power_status = False
        print(f"[{self.name}] is now OFF.")

    def display_info(self):
        status = "ON" if self.__power_status else "OFF"
        print(f"Name: {self.name} | Device ID: {self.__device_id} | Power: {status}")




# Child Class: SecurityCamera
class SecurityCamera(SmartDevice):
    """Represents a smart security camera."""

    def __init__(self, name, device_id):
        super().__init__(name, device_id)  # initialize inherited attributes
        self.recording_status = False  # additional attribute

    def start_recording(self):
        if not self.power_status:
            print(f"[{self.name}] Cannot start recording. Camera is OFF.")
            return
        self.recording_status = True
        print(f"[{self.name}] Recording started.")

    def stop_recording(self):
        self.recording_status = False
        print(f"[{self.name}] Recording stopped.")

    def display_info(self):
        super().display_info()
        rec = "Recording" if self.recording_status else "Not Recording"
        print(f"   -> Camera Status: {rec}")






# Child Class: SmartLight
class SmartLight(SmartDevice):
    """Represents a smart light with adjustable brightness."""

    def __init__(self, name, device_id):
        super().__init__(name, device_id)  # initialize inherited attributes
        self.__brightness = 0  # additional attribute (encapsulated)

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        # Brightness must be between 0 and 100
        if value < 0 or value > 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = value

    def increase_brightness(self, amount=10):
        if not self.power_status:
            print(f"[{self.name}] Cannot adjust brightness. Light is OFF.")
            return
        new_value = min(100, self.__brightness + amount)
        self.brightness = new_value
        print(f"[{self.name}] Brightness increased to {self.__brightness}.")

    def decrease_brightness(self, amount=10):
        if not self.power_status:
            print(f"[{self.name}] Cannot adjust brightness. Light is OFF.")
            return
        new_value = max(0, self.__brightness - amount)
        self.brightness = new_value
        print(f"[{self.name}] Brightness decreased to {self.__brightness}.")

    def display_info(self):
        super().display_info()
        print(f"   -> Brightness: {self.__brightness}%")







# Child Class: TemperatureSensor
class TemperatureSensor(SmartDevice):
    """Represents a smart temperature sensor."""

    def __init__(self, name, device_id, temperature=25.0):
        super().__init__(name, device_id)  # initialize inherited attributes
        self.temperature = temperature  # additional attribute

    def read_temperature(self):
        if not self.power_status:
            print(f"[{self.name}] Cannot read temperature. Sensor is OFF.")
            return
        print(f"[{self.name}] Current Temperature: {self.temperature}°C")

    def display_info(self):
        super().display_info()
        print(f"   -> Temperature: {self.temperature}°C")





# Menu-Driven Interface
def build_devices():
    """Create the required sample objects."""
    devices = [
        TemperatureSensor("Living Room Sensor", "TS001", 24.5),
        SmartLight("Bedroom Light", "SL001"),
        SecurityCamera("Front Door Camera", "SC001"),
    ]
    return devices


def choose_device(devices):
    """Let the user pick a device from the list."""
    print("\nSelect a device:")
    for i, device in enumerate(devices, start=1):
        print(f"{i}. {device.name}")
    try:
        choice = int(input("Enter device number: "))
        if 1 <= choice <= len(devices):
            return devices[choice - 1]
        else:
            print("Invalid device number.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    devices = build_devices()

    menu = """
========== SMART DEVICE MANAGEMENT SYSTEM ==========
1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit
======================================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\n--- All Devices ---")
            for device in devices:
                device.display_info()

        elif choice == "2":
            device = choose_device(devices)
            if device:
                device.turn_on()

        elif choice == "3":
            device = choose_device(devices)
            if device:
                device.turn_off()

        elif choice == "4":
            sensors = [d for d in devices if isinstance(d, TemperatureSensor)]
            if not sensors:
                print("No temperature sensors available.")
            else:
                for sensor in sensors:
                    sensor.read_temperature()

        elif choice == "5":
            lights = [d for d in devices if isinstance(d, SmartLight)]
            if not lights:
                print("No smart lights available.")
            else:
                light = lights[0]
                action = input("Type 'i' to increase or 'd' to decrease brightness: ")
                if action.lower() == "i":
                    light.increase_brightness()
                elif action.lower() == "d":
                    light.decrease_brightness()
                else:
                    print("Invalid option.")

        elif choice == "6":
            cameras = [d for d in devices if isinstance(d, SecurityCamera)]
            if not cameras:
                print("No security cameras available.")
            else:
                for camera in cameras:
                    camera.start_recording()

        elif choice == "7":
            print("Exiting Smart Device Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()
