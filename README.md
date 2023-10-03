# Wizard Changelog

[![User Guide](https://img.shields.io/badge/docs-User%20Guide-informational)](https://guide.ds-wizard.org)
[![License](https://img.shields.io/github/license/ds-wizard/guide-changelog)](LICENSE)

*Changelog for Data Stewardship Wizard*

### Requirements

 - **Python** (recommended 3.11)
 - **Makefile** (recommended 3.81)


### Run

For building the changelog, please run the following from the root of the project 

```bash
$ make build
```

### Add new version

There is a helper script to create a new version template in the file (the component is optional, used for hotfixes):

```bash
$ python scripts/version.py <version> (<component>)
```

For example:

```bash
$ python scripts/version.py 3.27
$ python scripts/version.py 3.27.1 backend
```

## License

This project is licensed under the Apache License v2.0 - see the [LICENSE](LICENSE) file for more details.