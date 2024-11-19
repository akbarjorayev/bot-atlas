def url_modify(original_url, new_resolution="1024px"):
    url_parts = original_url.split("/")
    base_url = "/".join(url_parts[:-1])
    file_name = url_parts[-1]

    new_file_name = f"{new_resolution}-{file_name}"
    modified_url = f"{base_url}/{new_file_name}"

    return modified_url
