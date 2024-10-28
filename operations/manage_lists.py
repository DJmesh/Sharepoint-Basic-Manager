from sharepoint_connector import connect_to_sharepoint

def get_all_lists(ctx):
    """Retorna todas as listas no site do SharePoint."""
    lists = ctx.web.lists
    ctx.load(lists)
    ctx.execute_query()
    return [sp_list.properties['Title'] for sp_list in lists]

def delete_list(ctx, list_name):
    """Deleta uma lista especificada."""
    try:
        sp_list = ctx.web.lists.get_by_title(list_name)
        sp_list.delete_object()
        ctx.execute_query()
        print(f"Lista '{list_name}' excluída com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir a lista '{list_name}': {e}")
