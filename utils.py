import requests
# https://github.com/SilviuPe/youtube_tool

def gather_information_about_repo(projects: list):

    data = []

    for project in projects:
        repo_link = project['github_link']

        repo_data = {
            'repo_link': repo_link,
        }

        link_elements = repo_link.split('/')

        # Get repo URL
        repo_name = link_elements[-1]
        username = link_elements[-2]
        repo_url = f'https://api.github.com/repos/{username}/{repo_name}'

        # Gather more information regarding the repository
        response = requests.get(repo_url)
        json_data = response.json()

        # Get the default branch
        default_branch = json_data['default_branch']

        # Get the banner url
        banner_url = f'https://raw.githubusercontent.com/{username}/{repo_name}/{default_branch}/Banner.png'
        i_response = requests.get(banner_url)
        if i_response.status_code == 200:
            repo_data['banner_url'] = banner_url

        data.append(repo_data)

    return data