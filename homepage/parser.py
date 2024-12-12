import json
from bs4 import BeautifulSoup

def parse_bookmarks_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    def parse_folder(folder):
        folder_name = folder.find('h3').text if folder.find('h3') else None
        bookmarks = []
        
        # Parse bookmarks in the current folder
        links = folder.find_all('a', recursive=True)
        for link in links:
            bookmarks.append({
                "title": link.text.strip(),
                "url": link.get('href')
            })

        # Recursively parse subfolders
        subfolders = folder.find_all('dl', recursive=True)
        for subfolder in subfolders:
            subfolder_data = parse_folder(subfolder)
            if subfolder_data["bookmarks"]:  # Include only non-empty subfolders
                bookmarks.append(subfolder_data)

        return {"group": folder_name, "bookmarks": bookmarks}

    # Start parsing from the root <dl>
    root_dl = soup.find('dl')
    groups = []
    for top_level_folder in root_dl.find_all('dl', recursive=True):
        folder_data = parse_folder(top_level_folder)
        if folder_data["group"] or folder_data["bookmarks"]:  # Exclude empty folders
            groups.append(folder_data)

    return groups

def main():
    input_file = "bookmarks.html"  # Replace with your input file path
    output_file = "bookmarks.json"  # Replace with your output file path

    bookmarks = parse_bookmarks_html(input_file)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(bookmarks, json_file, indent=4)

    print(f"Bookmarks have been exported to {output_file}")

if __name__ == "__main__":
    main()
