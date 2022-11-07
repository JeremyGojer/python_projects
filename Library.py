class Library:
	
	def __init__(self, book_id, book_name):
		self.book_id = book_id
		self.book_name = book_name
		
	def __repr__(self):
		return 'book = Library(' + str(self.book_id) + ',' + self.book_name + ')'


book1 = Library(1, 'Alpha')
book2 = Library(2, 'Beta')
print(book1.__repr__())
		
	