def min_max_filter(request,products):
    min_price = request.GET.get("min",None)
    max_price = request.GET.get("max",None)
    if min_price:
        products = products.objects.filter(price__gte=min_price)
    if max_price:
        products = products.objects.filter(price__lte=max_price)  

    return products