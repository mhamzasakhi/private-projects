import sys
import git
from git_contributions_importer import *

repos_path = [
    '/home/sakhi/lopic/backend/',
    '/home/sakhi/signature-pharmacy/backend/',
]
repos = []
for repo_path in repos_path:
    repos.append(git.Repo(repo_path))

mock_repo_path = '/home/tk-lpt-535/Downloads/mhamzasakhi/private-projects/private-projects/'
mock_repo = git.Repo.init(mock_repo_path)

importer = Importer(repos, mock_repo)
importer.set_author(['mhamzasakhi@gmail.com', 'hamza.muhammad@tkxel.io', 'basharat.ali@camp1.tkxel.com'])
importer.set_commit_max_amount_changes(100)
importer.set_changes_commits_max_time_backward(60*60*24*1000)
importer.set_max_changes_per_file(600)
# importer.ignore_file_types(['.csv', '.txt', '.pdf', '.xsl', '.sql'])
importer.set_collapse_multiple_changes_to_one(True)
importer.import_repository()
