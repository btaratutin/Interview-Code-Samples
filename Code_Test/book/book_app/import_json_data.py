import json

from models import Book, Page, Section


# Imports the given json file to the model
def importFromJSON(json_filename):
	
	f = open(json_filename, 'r') # Open the json file
	data = json.loads(f.read())  # Read all the data & parse into dict
	
	books = data["books"]
	
	# Iterate through json file and parse structured data into objects
	for book in books:
		# Extract, create, and save a book entry
		b = Book(title=book["title"])
		b.save()
		
		# Extract pages from book to process - and process them
		pages = book["pages"]
		for page_num, page in enumerate(pages):
			# Extract, create, and save a page entry
			p = Page(number=page_num+1, book=b)
			p.save()
			
			
			# Extract sections from page to process - and do so
			sections = page["sections"]
			for section_num, section in enumerate(sections):
				# Create Section and set various attributes of it
				s = Section()
				s.number = section_num+1
				s.section_type = Section.TYPE_DICT[section["type"]]
				s.page = p
				
				# Try to get what data have, and store that
				text = section.get("text", None)
				image = section.get("image", None)
				
				if text: s.text = text
				if image: s.image = image
				
				# Save the section item
				s.save()
			
def run():
	importFromJSON("./sample_book_data.json")
				
if __name__ == "__main__":

	#from ..manage import djangosetup
	#djangosetup.setUpDjangoEnvironment()
	run()
	
	# OR from the command line:
	# 	import book_app.import_json_data as dd
	#	dd.run()

	
