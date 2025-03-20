# Helper function to validate each field:
def validate_product_field(product, field):
    if field == 'price':  # Price should be a positive (int) or (float)
        assert isinstance(product['price'], (int, float)), f"Product price is not a valid number: {product['price']}"
        assert product['price'] > 0, f"Product price is non-positive: {product['price']}"
    elif field == 'rating':  # 'rate' and 'count' are keys in 'rating', and rate should be between 1 - 5
        assert isinstance(product['rating'], dict), f"Product rating is not a dictionary: {product['rating']}"
        assert 'rate' in product['rating'], "Product rating is missing 'rate' field"
        assert 'count' in product['rating'], "Product rating is missing 'count' field"
        assert 1 <= product['rating']['rate'] <= 5, f"Product rating is out of bounds: {product['rating']['rate']}"
    elif field == 'id':  # ID should be a positive (int)
        assert isinstance(product['id'], int) and product['id'] > 0, f"Product ID is invalid: {product['id']}"
    elif field == 'category':  # Check for valid 'category'
        assert isinstance(product['category'], str) and len(product['category']) > 0, f"Product category is invalid: {product['category']}"
    elif field == 'title':  # Check for valid 'title'
        assert isinstance(product['title'], str) and len(product['title']) > 0, f"Product title is invalid: {product['title']}"
    elif field == 'description':  # Check for valid 'description'
        assert isinstance(product['description'], str) and len(product['description']) > 0, f"Product description is invalid: {product['description']}"
    elif field == 'image':  # Check for valid 'image'
        assert isinstance(product['image'], str) and len(product['image']) > 0, f"Product image is invalid: {product['image']}"
