import os
import shutil
import sys
from pathlib import Path
from copy_static import copy_all_files_from_sources
from page_generator import generate_pages_recursive

def main():
    #Get sys.args for base path
    if sys.argv[1] != "":
        base_path = sys.argv[1]
    else:
        base_path = "/"

    #Setting up all paths
    script_path = Path(__file__).parent.parent
    #public_path = script_path / "public"       #For local testing
    docs_path = script_path / "docs"            #For Github deploy
    static_path = script_path / "static"
    content_path = script_path / "content"
    
    #Deleting public folder + creating new empty one
    if os.path.exists(docs_path):
        shutil.rmtree(docs_path)
    os.mkdir(docs_path)

    #Copying all static resources from static dir to public dir
    print("Starting copy process... Generating public folder...")
    copy_all_files_from_sources(static_path, docs_path)

    #Generating all web pages
    generate_pages_recursive(content_path, f"{script_path}/template.html", docs_path, base_path)

main()