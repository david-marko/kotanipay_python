from pydantic import BaseModel, EmailStr
from typing import Dict, Optional


class Integrator(BaseModel):
    """
    Integrator
    """

    organization: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    country_code: str