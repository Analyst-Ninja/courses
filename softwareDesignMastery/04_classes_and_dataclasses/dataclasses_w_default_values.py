from dataclasses import dataclass, field
from enum import StrEnum, auto


class ConnectivityStatus(StrEnum):
    ONLINE = auto()
    OFFLINE = auto()
    LIMITED = "Limited Connectivity"


@dataclass
class IoTDevice:
    name: str
    device_type: str
    connectivity: ConnectivityStatus
    sensors: list[str] = field(
        default_factory=list
    )  # We can't use [] to initialize the empty list, because it can created issue, it is one single object and will be referred by all the object, that can cause wierd errors
    location: str = "Unknown"
    firmware_version: int = 1

    def add_sensor(self, sensor_name: str) -> None:
        """Adds a new sensor to the device"""
        self.sensors.append(sensor_name)

    def update_firmware(self, new_version: int) -> None:
        """Update firmware version to newer version"""
        if new_version > self.firmware_version:
            self.firmware_version = new_version
        else:
            raise ValueError("Firmware version should be newer to the current version")


def main():
    d1 = IoTDevice(
        name="camera", device_type="video", connectivity=ConnectivityStatus.ONLINE
    )

    d1.add_sensor("photo_diode")

    print(d1)

    d1.update_firmware(3)
    print(d1)


if __name__ == "__main__":
    main()
