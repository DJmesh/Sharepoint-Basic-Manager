def list_items(ctx, list_name):
    """Retorna todos os itens de uma lista especificada no SharePoint."""
    sp_list = ctx.web.lists.get_by_title(list_name)
    items = sp_list.items
    ctx.load(items)
    ctx.execute_query()
    
    item_list = []
    for item in items:
        item_list.append({
            "ID": item.properties["ID"],
            "Title": item.properties["Title"]
        })
    return item_list
