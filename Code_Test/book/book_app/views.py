# Create your views here.

from django.http import HttpResponse

from models import Book, Page, Section


def book_index(request):
	""" Displays an Index of all the Books in the System """
	
	html = "<html><body><h1>Book Viewing Utility</h1>"
	
	html += "<br/><br/>"
	html += "<h3>Books:</h3>"
	html += "<ul>"
	
	for book in Book.objects.all():
		html += "<li>%s</li>" % book.title
	
	html += "</ul>"
	html += "</body></html>"
	return HttpResponse(html)
	
def get_book(request, book_id):
	
	
	book = Book.objects.get(id=book_id)
	
	html = "<html><body><h2>Displaying book</h2>"
	
	html += "<ul>"
	html += "<li>Title: %s</li>" % book.title
	html += "<li>ID: %s</li>" % book.id
	html += "<li>Num Pages: %s</li>" % book.numPages()
	html += "</ul>"
	
	html += "<br/><br/>"
	
	html += "Read: " # TODO: ADD LINK to PAGE 1
	
	
	html += "</body></html>"
	return HttpResponse(html)
	
def get_page(request, book_id, page_num):
	""" Displays the number page (and all its sections) 
		for the given book id """
	html = "<html><body><h2>Reading Page %s of Book %s</h2>" % (page_num, Book.objects.get(id=book_id).title)
	
	page = Page.objects.get(number=page_num, book_id=book_id) # Get the page
	sections = page.getSections()
	print sections
	for s in sections:
		print s
		html += str(s.htmlSection())
	
	
	html += "</body></html>"
	return HttpResponse(html)
