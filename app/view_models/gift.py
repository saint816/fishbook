from .book import BookViewModel

class MyGifts:
    def __init__(self, gifts, wishes_list):
        self.my_gifts = []
        self.my_gifts = self.__parse(gifts, wishes_list)

    def package(self):
        return self.my_gifts

    def __parse(self, gifts, wishes_list):
        my_gifts = []
        for gift in gifts:
            count = 0
            for wish_count in wishes_list:
                if gift.isbn == wish_count[1]:
                    count = wish_count[0]
            else:
                r = {
                    'wishes_count': count,
                    'book': BookViewModel(gift.book),
                    'id': gift.id
                }
                my_gifts.append(r)
        return my_gifts


