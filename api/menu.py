class MenuNavigator:
    def __init__(self, lcd, menu_items, page_size=2, delay=5, sleep_fn=None):
        self.lcd = lcd
        self.menu_items = menu_items
        self.page_size = page_size
        self.selected = 0
        self.page_start = 0
        self.direction = 1
        # self.delay = delay
        #  self.sleep_fn = sleep_fn if sleep_fn else self.default_sleep
    
        self.display()


    def _adjust_page_start(self):
        if self.selected < self.page_start:
            self.page_start = self.selected
        elif self.selected >= self.page_start + self.page_size:
            self.page_start = self.selected - self.page_size + 1


    def display(self, move=0):
        # Update selected index with wrap-around
        self.selected = (self.selected + move) % len(self.menu_items)

        self._adjust_page_start()

        self.lcd.clear()
        for line in range(self.page_size):
            item_index = self.page_start + line
            if item_index < len(self.menu_items):
                prefix = "> " if item_index == self.selected else "  "
                self.lcd.move_to(0, line)
                self.lcd.putstr(prefix + self.menu_items[item_index][:14])
