#!/usr/bin/python3
import os
import subprocess as sp


def main():
    root = input("Directory to check> ")

    not_repo = []
    no_remote = []

    for dirname in os.listdir(root):
        # run git remote inside each directory
        full_path = os.path.join(root, dirname)

        if not os.path.isdir(full_path):
            # Ignore files
            continue

        os.chdir(full_path)
        if not os.path.exists(".git"):
            # This is not a git repo, we want to hear about it.
            not_repo.append(dirname)
            continue

        completed_process = sp.run(["git", "remote"], stdout=sp.PIPE)
        stdout = completed_process.stdout.decode("utf-8")
        remotes = stdout.splitlines()

        if len(remotes) == 0:
            # This is the case we really want to know about.
            no_remote.append(dirname)
            continue
        if len(remotes) >= 1:
            # Say nothing, this is the preferred case.
            continue

        # We shouldn't get this far, but if we do we want to know what's going on.
        print(completed_process)

    print("\nThe following projects have not had git repos initialized:")
    for dirname in not_repo:
        print(dirname)

    print("\nThe following projects are not backed up to the cloud:")
    for dirname in no_remote:
        print(dirname)


if __name__ == "__main__":
    main()
