import subprocess


def remove_all_commits():

    try:
        initial_commit = subprocess.check_output(
            ['git','rev-list', '--max-parents=0', 'HEAD']
        ).strip().decode('utf-8')

        subprocess.run(['git','reset', '--soft', initial_commit],check=True)

        print("All commits have been removed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    remove_all_commits()
