from django import template

register = template.Library()

# {% if  products.has_previous %}

# {% if  request|has_query_string  %}
# {request.get_full.path}}&{% else %}?
# {% endif %}

# page={{products.previous_page_number}}
# {% endif %}

@register.simple_tag
def get_paged_link(request, page, obj):
    page_num = page
    items = obj 
    if items.has_previous:
        if bool(request.GET):
            return f"{request.get_full_path}&{page_num}"
        else:
            return f"?{page_num}"
    else:
        return "#" 