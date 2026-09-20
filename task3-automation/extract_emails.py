import re

input_file = "sample_data/sample.txt"
output_file = "extracted_emails.txt"

with open(input_file, "r") as file:
    text = file.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)

unique_emails = list(set(emails))

with open(output_file, "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print("Found", len(unique_emails), "email address(es).")
print("Saved to", output_file)
