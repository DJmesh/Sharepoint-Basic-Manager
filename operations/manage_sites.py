from sharepoint_connector import connect_to_sharepoint

def list_sites(ctx):
    """Retorna todos os sites disponíveis para o usuário."""
    sites = ctx.web.webs
    ctx.load(sites)
    ctx.execute_query()
    return [site.properties['Title'] for site in sites]

def create_site(ctx, title):
    """Cria um novo site no SharePoint (se permitido pela API)."""
    new_site_info = {
        "Title": title,
        "WebTemplate": "STS#0", 
    }
    ctx.web.webs.add(new_site_info)
    ctx.execute_query()
    print(f"Site '{title}' criado com sucesso.")
