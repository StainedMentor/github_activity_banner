import subprocess
import tkinter as tk
from datetime import datetime, timedelta

from selectionWindow import CheckboxGrid

window = None
root = None
year = 2000


def git_commit(commit_message, date):
    try:
        subprocess.run(['git', 'commit', '-m', commit_message, '--date', date, '--allow-empty'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def get_date_for_banner(r, c):
    first_day_of_year = datetime(year, 1, 1)
    first_sunday_of_year = first_day_of_year + timedelta(days=(7 - first_day_of_year.isoweekday()) % 7)
    date = first_sunday_of_year + timedelta(weeks=c, days=r)

    return date.strftime('%Y-%m-%d')



def commit_banner(banner):
    for ri, r in enumerate(banner):
        for ci, c in enumerate(r):
            if c == 1:
                message = "hi"
                date = get_date_for_banner(ri,ci)
                git_commit(message, date)




def on_exit():
    print("Commiting this banner:")
    window.print_grid()
    commit_banner(window.grid_values)
    print("a")
    window.destroy()
    root.destroy()




def main():
    global window, root

    root = tk.Tk()
    root.title("7x50 Checkbox Grid")
    window = CheckboxGrid(root, 7, 50)
    window.pack()
    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()

if __name__ == "__main__":
    main()
