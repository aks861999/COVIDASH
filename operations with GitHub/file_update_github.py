from github import Github
from github import InputGitTreeElement
import re
user = "username"
password = "*************your_auth_token************"
g = Github(user,password)
repo = g.get_user().get_repo('name_of_your_repository')
commit_message = 'intitial'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

file_name = r'folder_name/filename.extension'
with open(l[i],errors='ignore') as input_file:
    data = input_file.read()   
file = repo.get_contents(r"folder_name/filename.extension")
repo.update_file(r"folder_name/filename.extension", commit_message,data, file.sha)