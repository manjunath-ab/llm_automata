# Find and Parse Sitemaps to Create List of all website's pages
from usp.tree import sitemap_tree_for_homepage

def getPagesFromSitemap(fullDomain):

    listPagesRaw = []

    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPagesRaw.append(page.url)

    return listPagesRaw



raw_list=getPagesFromSitemap("https://docs.snowflake.com/en/")
print(len(raw_list))
listPages=tuple(set(raw_list))
print(len(listPages))
