class MenuNavigator:
    def __init__(self, lcd, menu_items, page_size=2):
        self.lcd = lcd
        self.menu_stack = [(menu_items, 0, 0)]  # (items, selected, page_start)
        self.page_size = page_size
        self.display()

    def current(self):
        return self.menu_stack[-1]

    def display(self, move=0):
        items, selected, page_start = self.current()
        selected = (selected + move) % len(items)
        # Adjust page_start
        if selected < page_start:
            page_start = selected
        elif selected >= page_start + self.page_size:
            page_start = selected - self.page_size + 1
        # Save state
        self.menu_stack[-1] = (items, selected, page_start)
        self.lcd.clear()
        for line in range(self.page_size):
            idx = page_start + line
            if idx < len(items):
                label = items[idx]["label"] if isinstance(items[idx], dict) else items[idx]
                prefix = "> " if idx == selected else "  "
                self.lcd.move_to(0, line)
                self.lcd.putstr(prefix + label[:14])

    def enter(self):
        items, selected, _ = self.current()
        item = items[selected]
        label = item["label"] if isinstance(item, dict) and "label" in item else str(item)
        if label == "Temp & Humidity":
            print("hello")
        # if label == "PH Level":
        #     print("hello")
        if isinstance(item, dict) and "submenu" in item:
            self.menu_stack.append((item["submenu"], 0, 0))
            self.display()

    def back(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.display()