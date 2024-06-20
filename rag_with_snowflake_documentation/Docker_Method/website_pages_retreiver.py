# Find and Parse Sitemaps to Create List of all website's pages
from usp.tree import sitemap_tree_for_homepage

def getPagesFromSitemap(fullDomain):

    listPagesRaw = []

    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPagesRaw.append(page.url)

    return tuple(set(listPagesRaw))




