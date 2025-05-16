from fastapi import APIRouter
from pydantic import ValidationError
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from api.annotated_types import PhoneNumber
from api.dependencies.phone_service import PhoneServiceDepends
from api.exception_handlers.factory import ExceptionHandlerFactory
from api.exeptions import InternalServerException, ServiceResponseValidationException, ObjectNotFoundException, \
    ObjectExistsException
from src.exceptions import ObjectNotFoundError, ObjectAlreadyExistError
from src.types import PhoneDataCreateRequestDTO, PhoneDataDTO, PhoneDataUpdateRequestDTO
from src.types.exceptions import (
    HTTPExceptionErrorDTO,
    ObjectAlreadyExistErrorDTO,
    ObjectNotFoundErrorDTO,
)


router = APIRouter()

exception_handler = ExceptionHandlerFactory(
    exc_mapping={
        ValidationError: ServiceResponseValidationException(name="phone"),
        ObjectNotFoundError: ObjectNotFoundException(name="phone"),
        ObjectAlreadyExistError: ObjectExistsException(name="phone"),
    },
    default_exc=InternalServerException(name="phone"),
)


@router.get(
    path="/check_data/{phone}/",
    status_code=HTTP_200_OK,
    response_model=PhoneDataDTO,
    summary="Get Data",
    responses={
        HTTP_404_NOT_FOUND: {"model": ObjectNotFoundErrorDTO},
        HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
    },
    name="check_data",
)
@exception_handler()
async def get_data(phone: PhoneNumber, service: PhoneServiceDepends) -> PhoneDataDTO:
    return await service.get_data(phone=phone)


@router.post(
    path="/write_data",
    status_code=HTTP_201_CREATED,
    response_model=PhoneDataDTO,
    summary="Create Data",
    responses={
        HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
        HTTP_409_CONFLICT: {"model": ObjectAlreadyExistErrorDTO},
    },
    name="write_data",
)
@exception_handler()
async def set_data(
    data: PhoneDataCreateRequestDTO, service: PhoneServiceDepends
) -> PhoneDataDTO:
    return await service.set_data(phone=data.phone, data=data)


@router.patch(
    path="/update_data/{phone}/",
    status_code=HTTP_202_ACCEPTED,
    response_model=PhoneDataDTO,
    summary="Update Data",
    responses={
        HTTP_404_NOT_FOUND: {"model": ObjectNotFoundErrorDTO},
        HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
    },
    name="update_data",
)
@exception_handler()
async def update_data(
    phone: PhoneNumber, data: PhoneDataUpdateRequestDTO, service: PhoneServiceDepends
) -> PhoneDataDTO:
    return await service.update_data(phone=phone, data=data)
