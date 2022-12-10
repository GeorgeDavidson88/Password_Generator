import os
import random
from tkinter import PhotoImage, StringVar

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.resizable(0, 0)

        self.title("Password Generator")
        self.iconphoto(True, PhotoImage(
            file=os.path.join("graphics", "icon.png")))

        self.password_lenght = StringVar(self, f"Password Lenght (16)")

        self.lowercase_var = StringVar(self, "on")
        self.uppercase_var = StringVar(self, "on")
        self.numbers_var = StringVar(self, "on")

        self.symbols_var = StringVar(self, "off")
        self.ambiguous_characters = StringVar(self, "off")
        self.exclude_similar_characters = StringVar(self, "off")

        self.password = StringVar(self, "Password1")

        def top():
            self.top_frame = customtkinter.CTkFrame(master=self)
            self.top_frame.place(anchor="n", x=250, y=10,
                                 width=480, height=70)

            self.password_lenght_lable = customtkinter.CTkLabel(
                master=self.top_frame, textvariable=self.password_lenght)
            self.password_lenght_lable.place(anchor="n", x=240, y=10)

            self.password_slider = customtkinter.CTkSlider(
                master=self.top_frame, from_=8, to=24, command=lambda lenght: self.password_lenght.set(f"Password Lenght ({round(lenght)})"))
            self.password_slider.place(
                anchor="n", x=240, y=40, width=460, height=20)
            self.password_slider.set(16)

        def middle():
            self.middle_frame = customtkinter.CTkFrame(master=self)
            self.middle_frame.place(anchor="center", x=250,
                                    y=150, width=480, height=120)

            self.lowercase_checbox = customtkinter.CTkCheckBox(
                master=self.middle_frame, text="Lowercase (abcde)", variable=self.lowercase_var, onvalue="on", offvalue="off")
            self.lowercase_checbox.place(anchor="nw", x=10, y=10)

            self.uppercase_checbox = customtkinter.CTkCheckBox(
                master=self.middle_frame, text="Uppercase (ABCDE)", variable=self.uppercase_var, onvalue="on", offvalue="off")
            self.uppercase_checbox.place(anchor="w", x=10, y=60)

            self.uppercase_checbox = customtkinter.CTkCheckBox(
                master=self.middle_frame, text="Numbers (12345)", variable=self.numbers_var, onvalue="on", offvalue="off")
            self.uppercase_checbox.place(anchor="sw", x=10, y=110)

            self.lowercase_checbox = customtkinter.CTkCheckBox(
                master=self.middle_frame, text="Symbols (!@#$%&*?+=)", variable=self.symbols_var, onvalue="on", offvalue="off")
            self.lowercase_checbox.place(anchor="nw", x=200, y=10)

            self.uppercase_checbox = customtkinter.CTkCheckBox(
                master=self.middle_frame, text="Ambiguous Characters (^`'\":;/\\<>(){}[]~.,)", variable=self.ambiguous_characters, onvalue="on", offvalue="off")
            self.uppercase_checbox.place(anchor="w", x=200, y=60)

            self.uppercase_checbox = customtkinter.CTkCheckBox(
                master=self.middle_frame, text="Exclude Similar Characters (0,o,1,l,L,i,I)", variable=self.exclude_similar_characters, onvalue="on", offvalue="off")
            self.uppercase_checbox.place(anchor="sw", x=200, y=110)

        def bottom():
            self.bottom_frame = customtkinter.CTkFrame(master=self)
            self.bottom_frame.place(anchor="s", x=250, y=290,
                                    width=480, height=70)

            self.generate_button = customtkinter.CTkButton(
                master=self.bottom_frame, text="Generate", command=self.generate_password)
            self.generate_button.place(
                anchor="w", x=10, y=35, width=225, height=50)

            self.password_frame = customtkinter.CTkFrame(
                master=self.bottom_frame)
            self.password_frame.place(
                anchor="e", x=470, y=35, width=225, height=50)

            self.password_lable = customtkinter.CTkLabel(
                master=self.password_frame, textvariable=self.password)
            self.password_lable.place(anchor="center", x=112.5, y=25)

        top()
        middle()
        bottom()

    def generate_password(self):
        print(f"Lenght: {self.password_lenght.get()[17:-1]}")
        print(f"Lowercase: {self.lowercase_var.get()}")
        print(f"Uppercase: {self.uppercase_var.get()}")
        print(f"Numbers: {self.numbers_var.get()}")
        print(f"Symbols: {self.symbols_var.get()}")
        print(f"Ambiguous Characters: {self.ambiguous_characters.get()}")
        print(
            f"Exclude Similar Characters : {self.exclude_similar_characters.get()}")
        print("--------------------------------")

        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "1234567890"
        symbols = "!@#$%&*?+="
        ambiguous_characters = "^`'\":;/\\<>(){}[]~.,"
        similar_characters = "0o1lLiI"

        self.password.set(f"Password{random.randint(1, 99)}")

    def mainloop(self):
        return super().mainloop()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()