#!/usr/bin/python3
import os, argparse, sys
from pathlib import Path

parser = argparse.ArgumentParser(description='Package manager for kapturOS')
parser.add_argument('--p', type=str, help='Package name')
parser.add_argument('--u', nargs='?', const='Sora_Repo', default=None, help='Update repository (optional repo name)')
parser.add_argument('--r', type=str, help='Use the repo')
parser.add_argument('--s', type=str, help='Search package')
parser.add_argument('--remove', type=str, help='Remove the package')
arg = parser.parse_args()

def update_repo(u):
    repo_dir = f"/repo/{u}"
    os.chdir(repo_dir)
    os.system("git reset --hard")
    os.system("git clean -fd")
    os.system("git pull origin main")
    sys.exit()
    

def install_package(p, r):
    repo = r or "Sora_Repo"  
    repo_dir = f"/repo/{repo}/{p}"

    os.chdir(repo_dir)
    os.system("chmod +x recipe.sh")
    os.system("./recipe.sh")

    sys.exit()

def search(S):
    root_dir = Path("/repo")
    search_package = S

    for path in root_dir.rglob(search_package):
        if path.is_dir():
            rel_path = path.relative_to(root_dir)
            print(f"Package find in {rel_path}")

    sys.exit()

def remove(remove):
    path_package = f"/opt/sora/{remove}"
    os.remove(path_package)

    print(f"Package {remove} is remove from /opt/sora")

def main(u, p, r, S, R):
    if u is not None:
        update_repo(u)
    elif p:
        install_package(p, r)
    elif S:
        search(S)
    elif R:
        remove(R)
    else:
        print("No valid arguments provided. Use --help for options.")
        sys.exit(1)

if __name__ == '__main__':
    main(arg.u, arg.p, arg.r, arg.s, arg.remove)


    


    
