from datetime import datetime
from sharepoint_connector import connect_to_sharepoint

def add_item_to_list(ctx, list_name, item_data):
    sp_list = ctx.web.lists.get_by_title(list_name)
    ctx.load(sp_list)
    ctx.execute_query()

    item_data["Data_x0020_de_x0020_Registro"] = datetime.now().isoformat()

    try:
        item = sp_list.add_item(item_data).execute_query()
        print(f"Item adicionado com sucesso! ID: {item.properties['ID']}")
    except Exception as e:
        print(f"Erro ao adicionar item: {e}")
