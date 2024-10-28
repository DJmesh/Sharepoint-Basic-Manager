from sharepoint_connector import connect_to_sharepoint

def delete_list(list_name):
    ctx = connect_to_sharepoint()
    try:
        sp_list = ctx.web.lists.get_by_title(list_name)
        sp_list.delete_object()
        ctx.execute_query()
        print(f"Lista '{list_name}' excluída com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir a lista '{list_name}': {e}")
