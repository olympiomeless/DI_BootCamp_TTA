import math


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def get_visible_items(self):
        start_index = self.current_idx * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]
    
    def go_to_page(self, page_number):
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError(f"Page number must be between 1 and {self.total_pages}")
        self.current_idx = page_number - 1
        return self
    
    def __str__(self):
        items        = self.get_visible_items()
        current_page = self.current_idx + 1   # ✅ conversion 0-based → 1-based pour affichage
        header       = f"Page {current_page}/{self.total_pages} :"
        items_str    = "\n".join(str(item) for item in items)
        return f"{header}\n{items_str}"
    
    def first_page(self):
        self.current_idx = 0
        return self.get_visible_items()
    
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self.get_visible_items()
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p)
print()

# Test chaînage des méthodes (Bug 3)
print(p.next_page().next_page())
print()

# Test first_page / last_page
print(p.first_page())
print()
print(p.last_page())
print()

# Test go_to_page valide
print(p.go_to_page(2))
print()

# Test go_to_page hors plage (Bug 2)
try:
    p.go_to_page(99)
except ValueError as e:
    print(f"✅ ValueError attrapée : {e}")