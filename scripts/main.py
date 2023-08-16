import pathlib

import docutils.core

ENCODING = 'utf-8'
ROOT_DIR = pathlib.Path(__file__).parent.parent
CHANGELOG_RST_FILENAME = 'changelog.rst'
CHANGELOG_RST_FILEPATH = ROOT_DIR / CHANGELOG_RST_FILENAME
OUTPUT_DIR = ROOT_DIR / 'output'
CHANGELOG_HTML_ORIGINAL_FILENAME = 'index-original.html'
CHANGELOG_HTML_ORIGINAL_FILEPATH = OUTPUT_DIR / CHANGELOG_HTML_ORIGINAL_FILENAME
CHANGELOG_HTML_FILENAME = 'index.html'
CHANGELOG_HTML_FILEPATH = OUTPUT_DIR / CHANGELOG_HTML_FILENAME

if __name__ == '__main__':
    docutils.core.publish_file(
        source_path=CHANGELOG_RST_FILEPATH.__str__(),
        destination_path=CHANGELOG_HTML_ORIGINAL_FILEPATH.__str__(),
        settings_overrides={
            'embed_stylesheet': False,
            'stylesheet_path': 'assets/style.css'
        },
        writer_name="html5")

    with CHANGELOG_HTML_ORIGINAL_FILEPATH.open(encoding=ENCODING, mode='rt') as f_in:
        with CHANGELOG_HTML_FILEPATH.open(encoding=ENCODING, mode='wt') as f_out:
            for line in f_in:
                f_out.write(
                    line
                    .replace(
                        '<title>Changelog</title>',
                        """<title>Wizard Changelog</title>
                                  <link rel="shortcut icon" href="../assets/favicon.ico">
                                  <script src="../assets/custom.js"></script>
                               """
                    )
                    .replace(
                        '<h1 class="title">Changelog</h1>',
                        ''
                    )
                    .replace(
                        '<main id="changelog">',
                        """<header>
                                    <h1>
                                        <img src="./assets/logo.svg" alt="Logo" class="logo">
                                        <div class="title">| Changelog</div>
                                    </h1>
                                  </header>
                                  <main id="changelog">
                        """
                    )
                )
    CHANGELOG_HTML_ORIGINAL_FILEPATH.unlink()
