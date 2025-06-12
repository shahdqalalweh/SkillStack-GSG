



class LibraryItem:
    def __init__ (self, item_id, title, auther,is_available):
        self.item_id = item_id
        self.title = title
        self.auther = auther
        self.is_available = is_available

    def git_basic_info(self):
        print('item id = ' , self.item_id)
        print ('title = ', self.title)
        print ('auther = ' , self.auther)
        print('is available = ', self.is_available)

    def check_availability(self):
        return self.is_available
    

    