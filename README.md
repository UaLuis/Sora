# Sora

Sora is a package manager designed for kapturOS, providing simple commands to update repositories, install packages, search for packages, and remove installed packages.

## Features

- **Update repository**: Pull the latest changes from a specified repository.
- **Install package**: Installs a package using its recipe script from the selected repository.
- **Search package**: Recursively searches for a package directory within `/repo`.
- **Remove package**: Deletes the installed package file from `/opt/sora`.

## Usage

Sora is run from the command line and accepts several arguments:

```bash
python3 sora.py [OPTIONS]
```

### Options

- `--u [REPO_NAME]`  
  Update the specified repository (default: `Sora_Repo` if not specified).
  - Example:  
    ```bash
    python3 sora.py --u MyRepo
    ```

- `--p PACKAGE_NAME`  
  Install the given package from a repository. Use `--r` to specify the repo (default: `Sora_Repo`).
  - Example:  
    ```bash
    python3 sora.py --p mypackage --r MyRepo
    ```

- `--s PACKAGE_NAME`  
  Search for a package directory in `/repo`.
  - Example:  
    ```bash
    python3 sora.py --s mypackage
    ```

- `--remove PACKAGE_NAME`  
  Remove the installed package from `/opt/sora`.
  - Example:  
    ```bash
    python3 sora.py --remove mypackage
    ```

### Help

Run with `--help` to see all options:
```bash
python3 sora.py --help
```

## Code Overview

- **Argument parsing**: Uses argparse for command-line options.
- **Main logic**: Functions for each operation, called based on provided arguments.
- **Repository interaction**: Uses `git` commands to update repositories.
- **Package install**: Runs `recipe.sh` for the selected package.
- **Package search**: Recursively lists all directories matching the package name.
- **Package removal**: Deletes the package file from the install location.

## Requirements

- Python 3
- Git installed and available in PATH
- kapturOS directory structure (`/repo`, `/opt/sora`)

## License

MIT License

---

*Generated from the logic in [`sora.py`](sora.py).*
