from typing import Annotated

from fastapi import Path


PhoneNumber = Annotated[
    str,
    Path(
        title="Phone Number",
        description="<p>Phone Number</p>",
        alias="phone",
    ),
]
