# models.py
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    UnicodeSetAttribute,
    UTCDateTimeAttribute,
    ListAttribute,
    BooleanAttribute,
)
import os
from dotenv import load_dotenv
from datetime import datetime

# Load .env file
load_dotenv()

# Get and validate region
aws_region = os.getenv("AWS_REGION")


class Thread(Model):
    """
    A DynamoDB model representing a forum thread.
    """

    class Meta:
        table_name = "Thread"
        region = aws_region

    forum_name = UnicodeAttribute(hash_key=True)
    subject = UnicodeAttribute(range_key=True)
    views = NumberAttribute(default=0)
    replies = NumberAttribute(default=0)
    answered = NumberAttribute(default=0)
    tags = UnicodeSetAttribute()
    last_post_datetime = UTCDateTimeAttribute()


class Product(Model):
    """
    A DynamoDB model representing a product.
    """

    class Meta:
        table_name = "Product"
        region = aws_region
        read_capacity_units = 1
        write_capacity_units = 1

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    description = UnicodeAttribute(null=True)
    price = NumberAttribute()
    quantity = NumberAttribute()
    image_url = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
    updated_at = UTCDateTimeAttribute(default=datetime.now)
    tags = ListAttribute(null=True)
    is_active = BooleanAttribute(default=True)
