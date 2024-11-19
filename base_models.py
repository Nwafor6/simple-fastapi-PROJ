from pydantic import BaseModel


class ProductItem(BaseModel):
    """
    A product item model.
    """

    name: str
    description: str = None
    price: float
    quantity: int = 0
    image_url: str = None
    tags: list = []


class UpdateProductItem(BaseModel):
    """
    Pydantic model for updating a product.
    """

    name: str = None
    description: str = None
    price: float = None
    quantity: int = None
    image_url: str = None
    tags: list = None
    is_active: bool = None
