import requests

def download_deb_files(packages_file_path, repo_base_url):
    with open(packages_file_path, 'r') as file:
        content = file.read()

    # Split the content into packages
    packages = content.split('\n\n')

    for package in packages:
        # Find the Filename field for each package
        for line in package.split('\n'):
            if line.startswith('Filename:'):
                filename = line.split(' ')[1].strip()
                deb_url = repo_base_url + filename
                # Download the .deb file
                response = requests.get(deb_url)
                if response.status_code == 200:
                    file_name = deb_url.split('/')[-1]
                    with open(file_name, 'wb') as deb_file:
                        deb_file.write(response.content)
                    print(f'Downloaded {file_name}')
                else:
                    print(f'Failed to download {filename}')
                break  # Proceed to the next package after finding the Filename field

# Example usage
download_deb_files('Packages.misty', 'https://repo.misty.moe/apt/')