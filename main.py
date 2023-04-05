#!/usr/bin/python3
import os
import subprocess as sp


def main():
    root = input("Directory to check> ")
    if not root:
        print("No directory given, using default (~/dev)")
        root = "/home/lucien/dev"

    for dirname in os.listdir(root):
        # run git remote inside each directory
        os.chdir(os.path.join(root, dirname))
        if not os.path.exists(".git"):
            # This is not a git repo, we want to hear about it.
            print(f"{dirname} is not a git repo")
            continue

        completed_process = sp.run(["git", "remote"], stdout=sp.PIPE)
        stdout = completed_process.stdout.decode("utf-8")
        remotes = stdout.splitlines()

        if len(remotes) == 0:
            # This is the case we really want to know about.
            print(f"{dirname} has no remotes")
            continue
        if len(remotes) >= 1:
            # Say nothing, this is the preferred case.
            continue

        # We shouldn't get this far, but if we do we want to know what's going on.
        print(completed_process)


if __name__ == "__main__":
    main()
