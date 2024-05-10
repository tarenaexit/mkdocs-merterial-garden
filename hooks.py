from datetime import datetime
from material.plugins.blog.structure import Archive

"""
def on_page_markdown(markdown, *, page, config, files):
    if isinstance(page, Archive):
        page.meta["template"] = "my-custom-template.html"
"""

def on_config(config, **kwargs):
    config.copyright = f"版权所有 © 2024-{datetime.now().year} <a href=\"https://github.com/tarenaexit/mkdocs-merterial-garden/discussions\" target=\"_blank\">天边飘过一行字</a>"