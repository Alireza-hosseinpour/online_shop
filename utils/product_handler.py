def update_product_info(data, product):
    product.name = data.validated_data['name']
    product.price = data.validated_data['price']
    product.description = data.validated_data['description']
    product.entity = data.validated_data['entity']
    product.category = data.validated_data['category']
    product.image = data.validated_data['image']
    product.save()
