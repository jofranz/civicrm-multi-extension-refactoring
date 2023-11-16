#! /usr/bin/python

from subprocess import getstatusoutput

print(getstatusoutput("pwd"))

git_status = "git status"
git_status_return = getstatusoutput(git_status)
# todo check if word "repository" is found

if git_status_return[1].find("nothing to commit") < 0:
    print("There are uncommitted changes which need to be resolved before continuing. Exiting:" + git_status_return[1])
    quit()

git_pull = "git pull"
git_pull_return = getstatusoutput(git_pull)
print(git_pull_return)

print('\n\n checkout_branch:')

checkout_branch = "git checkout -b civix-upgrade"
checkout_branch_return = getstatusoutput(checkout_branch)
print(checkout_branch_return)

print('\n\n civix_upgrade:')

civix_upgrade = "civix upgrade --yes --no-interaction"
civix_upgrade_return = getstatusoutput(civix_upgrade)
# print(civix_upgrade_return)

print('\n\n git_add_all_unommitted_changes:')

git_add_all_unommitted_changes = "git add -A"
git_add_all_unommitted_changes_return = getstatusoutput(git_add_all_unommitted_changes)
print(git_add_all_unommitted_changes_return)

print('\n\n use_civix_version_as_commit_message:')

# use_civix_version_as_commit_message = 'echo "\"$(civix --version)\"" | xargs git commit -m'

info_name = "civix upgrade 23.02.1"

use_civix_version_as_commit_message = 'git commit -m "' + info_name + '"'
use_civix_version_as_commit_message_return = getstatusoutput(use_civix_version_as_commit_message)
#  print(use_civix_version_as_commit_message_return)

push_branch = "git push --set-upstream origin civix-upgrade"
push_branch_return = getstatusoutput(push_branch)
print(push_branch_return)
print("\n\n")

git_checkout_master = "git checkout master"
git_checkout_master_return = getstatusoutput(git_checkout_master)

delete_local_branch = "git branch -d civix-upgrade"
delete_local_branch_return = getstatusoutput(delete_local_branch)

print("Suggested branch name:\n" + info_name)


## check if repo is on github

# github create PR
# github merge PR
# delete_branch_remote = "git push origin --delete civix-upgrade"
