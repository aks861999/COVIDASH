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


element_list = list()

file_name = r'folder_name/filename.extension'

file=r'local_directory_to_file'

with open(file,errors='ignore') as input_file:
        data = input_file.read()
element = InputGitTreeElement(file_name, '100644', 'blob', data)
element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)