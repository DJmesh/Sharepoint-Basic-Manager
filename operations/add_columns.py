from sharepoint_connector import connect_to_sharepoint

def add_columns_to_list(ctx, list_name, columns):
    sp_list = ctx.web.lists.get_by_title(list_name)
    ctx.load(sp_list)
    ctx.execute_query()

    for column in columns:
        internal_name, field_type, display_name = column
        try:
            field_exists = any(f.properties['Title'] == display_name for f in sp_list.fields)
            if not field_exists:
                field_schema = f'''
                <Field 
                    DisplayName="{display_name}" 
                    Name="{internal_name}" 
                    Type="{field_type}" 
                    Group="Custom Columns" />
                '''
                sp_list.fields.create_field_as_xml(field_schema).execute_query()
                print(f"Coluna '{display_name}' adicionada com sucesso!")
            else:
                print(f"Coluna '{display_name}' já existe e não será duplicada.")
        except Exception as e:
            print(f"Erro ao adicionar a coluna '{display_name}': {e}")
