import argparse
from bs4 import BeautifulSoup
from collections import defaultdict
import os
import sys

def build_base_selector(el):
    if el.get("id"):
        id_val = el['id'].strip()
        if " " in id_val:
            return f'{el.name}[id^="{id_val.split()[0]}"]'
        else:
            return f"#{id_val}"
    elif el.get("class"):
        class_val = " ".join(el['class']).strip()
        if " " in class_val:
            return f'{el.name}[class^="{class_val.split()[0]}"]'
        else:
            return f"{el.name}." + ".".join(el['class'])
    else:
        return el.name

def generate_selectors(parent, selectors, seen):
    tag_counts = defaultdict(int)
    for child in parent.find_all(recursive=False):
        if not child.name:
            continue

        base_selector = build_base_selector(child)
        tag_counts[base_selector] += 1
        count = tag_counts[base_selector]

        if base_selector not in seen:
            selectors.append(f"{base_selector} {{ }}")
            seen.add(base_selector)

        if count > 1:
            selectors.append(f"{base_selector}:nth-of-type({count}) {{ }}")

        generate_selectors(child, selectors, seen)

def main():
    parser = argparse.ArgumentParser(description='Generate CSS skeleton from HTML')
    parser.add_argument('--input', type=str, required=True, help='Input HTML file path')
    parser.add_argument('--output', type=str, default="index.css", help='Output CSS file path')
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    if os.path.exists(output_file):
        response = input(f"⚠️  Warning: The output file '{output_file}' already exists. Shall I overwrite it? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("⛔ Operation cancelled. No file was overwritten.")
            sys.exit(0)

    with open(input_file, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    has_css = any(
        link.get("href", "").endswith(".css")
        for link in soup.find_all("link", rel="stylesheet")
    )

    if not has_css:
        link_tag = soup.new_tag("link", rel="stylesheet", href=output_file)
        if soup.head:
            soup.head.append(link_tag)
        else:
            new_head = soup.new_tag("head")
            new_head.append(link_tag)
            soup.html.insert(0, new_head)

    with open(input_file, "w", encoding="utf-8") as f:
        f.write(str(soup))

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(""":root {}
html {}
body {}

@media screen and (max-width: 600px) {
    /* Styles for phones */
}

@media screen and (min-width: 601px) and (max-width: 768px) {
    /* Styles for tablets */
}

@media screen and (min-width: 769px) and (max-width: 1024px) {
    /* Styles for small laptops/desktops */
}

@media screen and (min-width: 1025px) {
    /* Styles for large desktops */
}

""")

        selectors = []
        seen = set()

        generate_selectors(soup.body if soup.body else soup, selectors, seen)

        for line in selectors:
            outfile.write(line + "\n\n")


if __name__ == "__main__":
    main()
