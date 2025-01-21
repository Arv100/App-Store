from vercel_blob import put, delete

def delete_from_blob(url):
    delete(url)

def add_to_blob(folder_name,file):
    blob_name = f"{folder_name}/{file.name}"  # Specify the folder path and file name
    response = put(blob_name, file.read(), {
        'access': 'public',  # Adjust access level as needed
    })
    return response