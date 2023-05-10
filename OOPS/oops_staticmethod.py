class Print_Info:
    @staticmethod
    def display_name(name:str):
        return name.upper()

    @staticmethod
    def display_company(name: str):
        return name.capitalize()

    @staticmethod
    def pr():
        print("Running")

print(Print_Info.display_name("kumar"))
print(Print_Info.display_company("shell"))
Print_Info.pr()

