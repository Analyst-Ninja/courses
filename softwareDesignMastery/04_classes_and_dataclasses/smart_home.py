from dataclasses import dataclass, field
from enum import StrEnum, auto


class DeviceStatus(StrEnum):
    ACTIVE = auto()
    INACTIVE = auto()
    ERROR = auto()


class DeviceType(StrEnum):
    LIGHT = "Smart Light"
    THERMOSTAT = "Smart Thermostat"
    SECURITY_CAMERA = "Security Camera"
    DOOR_LOCK = "Smart Door Lock"
    SPEAKER = "Smart Speaker"


@dataclass
class DeviceConfig:
    configuration: dict[str, str] = field(default_factory=dict)

    def update_config(self, key: str, value: str):
        """Update or add a configuration setting for the device."""
        self.configuration[key] = value


@dataclass
class IoTDevice:
    name: str
    device_type: DeviceType
    status: DeviceStatus
    config: DeviceConfig = field(default_factory=DeviceConfig, compare=False)
    firmware_version: int = field(default=1, init=False, repr=False, compare=False)

    def __post_init__(self):
        """Post-initialization to set dynamic defaults."""
        if self.device_type in [DeviceType.LIGHT, DeviceType.SPEAKER]:
            self.status = DeviceStatus.ACTIVE
        if self.device_type == DeviceType.THERMOSTAT:
            self.firmware_version = 2

    def activate(self):
        if self.status != DeviceStatus.ACTIVE:
            self.status = DeviceStatus.ACTIVE
            print(f"{self.name} activated.")
        else:
            print(f"{self.name} is already active.")

    def deactivate(self):
        if self.status != DeviceStatus.INACTIVE:
            self.status = DeviceStatus.INACTIVE
            print(f"{self.name} deactivated.")
        else:
            print(f"{self.name} is already inactive.")


@dataclass
class SmartHome:
    devices: list[IoTDevice] = field(default_factory=list)

    def add_device(self, device: IoTDevice) -> IoTDevice:
        """Add a new IoT device to the smart home system."""
        self.devices.append(device)
        print(f"Added {device.name} to the smart home system.")
        return device

    def get_devices(self):
        return self.devices


def main() -> None:
    smart_home = SmartHome()

    light_config = DeviceConfig(configuration={"brightness": "50%"})
    light_config_2 = DeviceConfig(configuration={"brightness": "20%"})

    light = smart_home.add_device(
        IoTDevice(
            name="Living Room Light",
            device_type=DeviceType.LIGHT,
            status=DeviceStatus.INACTIVE,
            config=light_config,
        )
    )
    smart_home.add_device(
        IoTDevice(
            name="Door Security Camera",
            device_type=DeviceType.SECURITY_CAMERA,
            status=DeviceStatus.INACTIVE,
        )
    )
    smart_home.add_device(
        IoTDevice(
            name="Smart Thermostat",
            device_type=DeviceType.THERMOSTAT,
            status=DeviceStatus.INACTIVE,
        )
    )

    light_2 = smart_home.add_device(
        IoTDevice(
            name="Living Room Light",
            device_type=DeviceType.LIGHT,
            status=DeviceStatus.INACTIVE,
            config=light_config_2,
        )
    )

    print(light == light_2)


if __name__ == "__main__":
    main()
