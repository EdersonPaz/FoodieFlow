from typing import Optional
from pydantic import BaseModel


class Categoria(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        from_attributes = True
