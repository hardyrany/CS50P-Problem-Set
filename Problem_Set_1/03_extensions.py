"""Discovering File Extension"""


def main():
    """Find file extensions through typing file"""
    user_input = input(
        "Type: happy.gif\n"
        "Type: happy.jpg\n"
        "Type: happy.jpeg\n"
        "Type: happy.jng\n"
        "Type: document.pdf\n"
        "Type: document.txt\n"
        "Type: document.zip\n"
    )
    output_file_type = extension(user_input)
    print(output_file_type)


def extension(mime_type):
    """Return MIME types based on file extentions"""
    types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
        }

    mime_type = mime_type.strip().casefold()
    extension_type = "." + mime_type.split(".")[-1]

    return types.get(extension_type, "application/octet-stream")


if __name__ == "__main__":
    main()
