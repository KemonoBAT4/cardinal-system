import subprocess

# retrieve all changes from the upstream of the applications
def run_git_command(commnad):
  result = subprocess.run(command, shell=True, capture_output=True, text=True)
  # print(result.stdout) # print result
  # print(result.stderr) # print errors

# navigate to the repository directory
repo_path = "/path/to/the/repo"
subprocess.run(f'cd {repo_path}', shell=True)

# ex: run git commands
run_git_command("git status")
