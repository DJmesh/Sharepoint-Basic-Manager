from office365.sharepoint.lists.creation_information import ListCreationInformation
from sharepoint_connector import connect_to_sharepoint

def create_list(ctx, list_name, description):
    new_list_info = ListCreationInformation()
    new_list_info.Title = list_name
    new_list_info.Description = description
    new_list_info.BaseTemplate = 100

    try:
        ctx.web.lists.add(new_list_info)
        ctx.execute_query()
        print(f"Lista '{list_name}' criada com sucesso no SharePoint!")
    except Exception as e:
        print(f"Erro ao criar a lista: {e}")
