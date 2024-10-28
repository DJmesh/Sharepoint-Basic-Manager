from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

def connect_to_sharepoint(domain, site_name, username, password):
    site_url = f"https://{domain}.sharepoint.com/sites/{site_name}"
    ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
    return ctx

def list_all_sites(ctx):
    """Retorna todos os sites disponíveis para o usuário."""
    sites = ctx.web.webs
    ctx.load(sites)
    ctx.execute_query()
    return [site.properties['Title'] for site in sites]
