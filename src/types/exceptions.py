from typing import Literal

from src.types.base import ImmutableDTO


class ObjectNotFoundErrorDTO(ImmutableDTO):
    detail: Literal["object_not_found"] = "object_not_found"


class ObjectAlreadyExistErrorDTO(ImmutableDTO):
    detail: Literal["object_already_exists"] = "object_already_exists"


class HTTPExceptionErrorDTO(ImmutableDTO):
    detail: Literal["something_went_wrong"] = "something_went_wrong"
