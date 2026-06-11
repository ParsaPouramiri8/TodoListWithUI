import customtkinter as ctk
import functions

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("750x600")
app.title("Todo App")


# ---------------- UI FRAMES ----------------
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

top_frame = ctk.CTkFrame(main_frame)
top_frame.pack(fill="x", pady=10)

list_frame = ctk.CTkScrollableFrame(main_frame)
list_frame.pack(fill="both", expand=True)


# ---------------- ENTRY ----------------
entry = ctk.CTkEntry(top_frame, width=400, placeholder_text="Add todo...")
entry.pack(side="left", padx=10)


# Enter shortcut
entry.bind("<Return>", lambda e: add_todo())


# ---------------- CORE FUNCTIONS ----------------
def refresh():
    for w in list_frame.winfo_children():
        w.destroy()

    todos = functions.load_todos()

    for i, t in enumerate(todos):

        row = ctk.CTkFrame(list_frame)
        row.pack(fill="x", pady=5, padx=5)

        # checkbox
        def toggle(i=i):
            functions.toggle(i)
            refresh()

        check = ctk.CTkCheckBox(row, text="", command=toggle)
        check.pack(side="left", padx=5)

        if t["done"]:
            check.select()

        # label
        label = ctk.CTkLabel(
            row,
            text=t["text"],
            text_color="gray" if t["done"] else "white"
        )
        label.pack(side="left", padx=10)

        # edit inline entry (hidden by default)
        edit_entry = ctk.CTkEntry(row, width=200)

        def enable_edit(e=edit_entry, text=t["text"]):
            e.delete(0, "end")
            e.insert(0, text)
            e.pack(side="left", padx=10)

        def save_edit(i=i, e=edit_entry):
            functions.edit(i, e.get())
            refresh()

        # buttons
        edit_btn = ctk.CTkButton(
            row,
            text="Edit",
            width=60,
            command=enable_edit
        )
        edit_btn.pack(side="right", padx=3)

        save_btn = ctk.CTkButton(
            row,
            text="Save",
            width=60,
            command=lambda i=i, e=edit_entry: save_edit(i, e)
        )
        save_btn.pack(side="right", padx=3)

        del_btn = ctk.CTkButton(
            row,
            text="X",
            width=40,
            fg_color="red",
            command=lambda i=i: (functions.delete(i), refresh())
        )
        del_btn.pack(side="right", padx=3)

        up_btn = ctk.CTkButton(
            row,
            text="↑",
            width=40,
            command=lambda i=i: (functions.move_up(i), refresh())
        )
        up_btn.pack(side="right", padx=3)

        down_btn = ctk.CTkButton(
            row,
            text="↓",
            width=40,
            command=lambda i=i: (functions.move_down(i), refresh())
        )
        down_btn.pack(side="right", padx=3)


def add_todo():
    text = entry.get().strip()
    if not text:
        return

    functions.add(text)
    entry.delete(0, "end")
    refresh()


# ---------------- ADD BUTTON ----------------
add_btn = ctk.CTkButton(
    top_frame,
    text="Add",
    command=add_todo
)
add_btn.pack(side="left")


# ---------------- START ----------------
refresh()
app.mainloop()