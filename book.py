class Book:
    """Book class"""
    def __init__(self, id_, title, author, year, status="в наличии"):
        """Book constructor"""
        self.id = id_
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @classmethod
    def from_dict(cls, book_dict):
        return cls(
            id_=book_dict.get('id'),
            title=book_dict.get('title'),
            author=book_dict.get('author'),
            year=book_dict.get('year'),
            status=book_dict.get('status')
        )
