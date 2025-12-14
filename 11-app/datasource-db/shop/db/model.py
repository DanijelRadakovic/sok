from dataclasses import dataclass
from typing import Optional

@dataclass
class Shop:
    id: Optional[int]
    pib: str
    name: str
    address: str
    phone: str

@dataclass
class Category:
    id: Optional[int]
    code: str
    name: str

@dataclass
class Article:
    id: Optional[int]
    code: str
    name: str
    description: str
    price: float
    on_sale: bool
    shop_id: int = None