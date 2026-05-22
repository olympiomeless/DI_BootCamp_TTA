import math


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_page = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def get_total_pages(self):
        return self.total_pages

    def get_current_page_items(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def next_page(self):
        if self.current_page < self.get_total_pages():
            self.current_page += 1
        return self.get_current_page_items()

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self.get_current_page_items()

    def get_visible_items(self):
        return self.get_current_page_items()
    
    def go_to_page(self, page_number):
        if 1 <= page_number <= self.get_total_pages():
            self.current_page = page_number
    
    def __str__(self):
        return f"Page {self.current_page} of {self.get_total_pages()}: {self.get_current_page_items()}"
    
    def first_page(self):
        self.current_page = 1
        return self.get_current_page_items()
    
    def last_page(self):
        self.current_page = self.get_total_pages()
        return self.get_current_page_items()
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_page)

p.go_to_page(0)
print(p.current_page)