import pathlib
import sys

from datetime import datetime


ROOT_DIR = pathlib.Path(__file__).parent.parent
CHANGELOG_RST_FILENAME = 'changelog.rst'
CHANGELOG_RST_FILEPATH = ROOT_DIR / CHANGELOG_RST_FILENAME

PATTERN = """Changelog
*********


"""

def version_string(version, component=None):
    if component:
        anchor = f'{version}-{component}'
        title = f'{version} ({component})'

    else:
        anchor = f'{version}'
        title = f'{version}'

    title_underline = "=" * len(title)

    release_date = datetime.now().strftime('%-d %B %Y')

    template = f"""Changelog
*********


.. _v{anchor}:

{title}
{title_underline}

* *Release: {release_date}*

* **Features:**

  * 

* **Bugfixes:**

  *

* **Misc:**

  *


"""
    
    return template
    

if __name__ == '__main__':
    version = sys.argv[1]
    component = sys.argv[2] if len(sys.argv) > 2 else None

    new_version_string = version_string(version, component)
    
    with open(CHANGELOG_RST_FILENAME) as f:
        content = f.read()

    new_content = content.replace(PATTERN, new_version_string)

    with open(CHANGELOG_RST_FILENAME, 'w') as f:
        f.write(new_content)
