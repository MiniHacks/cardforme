import re
import json
import datetime

# Function to extract card information from a markdown file
def extract_card_info(file_path, link_data):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    card_info_dict = {}

    # Use regular expressions to find all card entries in the markdown file
    card_matches = re.finditer(r'Card:\s+(.*?)\nName in code:\s+(.*?)\s+Benefits:(.*?)\nLink:\s+(.*?)\n---', content, re.DOTALL)

    for match in card_matches:
        card_info = {}
        card_info["name_in_code"] = match.group(2)
        benefits = match.group(3).strip().split('\n- ')
        card_info["description"] = benefits

        # Look for a link if available in the markdown file
        card_link = match.group(4).strip()
        card_info["link"] = card_link

        card_name = match.group(1).strip()  # Extract the card name and remove leading/trailing spaces
        card_info_dict[card_info["name_in_code"]] = card_info

    return card_info_dict

# Function to process all markdown files and create the JSON data
def process_markdown_files(file_paths):
    link_data = {}

    card_data = {}

    for file_path in file_paths:
        card_info_dict = extract_card_info(file_path, link_data)
        card_data.update(card_info_dict)

    return card_data

# List of markdown files containing card research data
markdown_files = [
    "research.md",  # Replace with the actual file names
]

# Process the markdown files and create the JSON data
card_json_data = process_markdown_files(markdown_files)

# Generate a timestamp to make the output file name unique
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Write the JSON data to "allCardData.json"
output_file_name = "allCardData.json"

with open(output_file_name, "w", encoding="utf-8") as json_file:
    json.dump(card_json_data, json_file, indent=4, ensure_ascii=False)

print(f"JSON file '{output_file_name}' has been created.")
