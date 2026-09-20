import re
import requests

url = "https://example.com"
output_file = "page_title.txt"

response = requests.get(url)

if response.status_code == 200:
    match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)

    if match:
        title = match.group(1).strip()
        print("Page title:", title)

        with open(output_file, "w") as file:
            file.write(title)

        print("Saved to", output_file)
    else:
        print("No title tag found on the page.")
else:
    print("Failed to fetch page. Status code:", response.status_code)
