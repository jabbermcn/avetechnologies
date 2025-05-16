from src.types.base import ImmutableDTO


__all__ = ["PhoneDataDTO", "PhoneDataCreateRequestDTO", "PhoneDataUpdateRequestDTO"]


class PhoneDataDTO(ImmutableDTO):
    phone: str
    address: str


class PhoneDataCreateRequestDTO(ImmutableDTO):
    phone: str
    address: str


class PhoneDataUpdateRequestDTO(ImmutableDTO):
    phone: str
    address: str
