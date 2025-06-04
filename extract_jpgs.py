import re


def extract_jpgs(input_file):
    with open(input_file, "rb") as f:
        data = f.read()

    # Wzorzec wyszukiwania plików JPEG (rozpoczyna się od FF D8 FF, kończy na FF D9)
    jpg_pattern = re.compile(b'\xFF\xD8\xFF[\xE0\xE1](.*?)\xFF\xD9', re.DOTALL)

    matches = jpg_pattern.findall(data)

    for i, match in enumerate(matches):
        with open(f"extracted_{i}.jpg", "wb") as img_file:
            img_file.write(b'\xFF\xD8\xFF' + match + b'\xFF\xD9')

    print(f"Wyodr\u0119bniono {len(matches)} plik\u00f3w JPEG.")


if __name__ == "__main__":
    extract_jpgs("large.jpg")
