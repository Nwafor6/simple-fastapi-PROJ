from botocore.exceptions import ClientError
from pynamodb.exceptions import TableError
from models import Product


def create_product_table():
    """Create the DynamoDB table for products"""
    try:
        if not Product.exists():
            try:
                Product.create_table(wait=True)
                print("Table 'Product' created successfully")
                return True
            except ClientError as ce:
                print(f"AWS Client Error: {ce.response['Error']['Message']}")
                return False
            except TableError as te:
                print(f"Table Error: {str(te)}")
                return False
        else:
            print("Table 'Product' already exists")
            return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False


create_product_table()
