class book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

superman_book = book("Superman",345)
print(len(superman_book))

world_war_book = book("World_war",7890)
print(len(world_war_book))