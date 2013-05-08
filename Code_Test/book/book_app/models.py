from django.db import models

"""
Boris Taratutin
May 7, 2013

Code Sample | Working with Python & Django

Usage:
	To get up and running;
		python manage.py validate			# Checks your code
		python manage.py sqlall books_app	# Prints SQL that will run
		python manage.py syncdb				# Runs SQL
	

"""


### Main Classes ###

class Book(models.Model):
	## ATTRIBUTES ##
	title = models.CharField(max_length=50)
	
	# Foreign Keys & Other-Table Relations
	# has Many pages (Foreign Key in Page)
	
	
	## METHODS ##

		
	# Returns all of the pages in this book as a list
	def getPages(self):
		return Page.objects.filter(book=self)

	# Returns the number of pages this book has
	def numPages(self):
		return len(self.getPages())
		
	# Printout representation of self
	def __unicode__(self):
		repr_str = ["Title:", self.title, 
					", Num. Pages:", str(self.numPages()),
					", ID: ", str(self.id)]
		return " ".join(repr_str)
	
	
class Page(models.Model):
	## Attributes ##
	number = models.IntegerField()
	
	# Foreign Keys & Other-Table Relations
	book = models.ForeignKey(Book) # Page belongs to a Book
	# has Many sections (Foreign Key in Section)
	
	
	## Methods ##
	
	# Return a list of all the sections that belong to this page
	def getSections(self):
		return Section.objects.filter(page=self)
		
	def numSections(self):
		return len(self.getSections())
		
		
	# Unicode (string) representation of self
	def __unicode__(self):
		return " ".join([	"Page #:", str(self.number),
							", Num. sections: ", str(self.numSections()),
							", Belongs to Book ID: ", str(self.book.id),
							", ID: ", str(self.id)
						])
	
	
	
class Section(models.Model):

	## ATTRIBUTES ##

	# Define the Section Types pseudo-enum
	
	TEXT_SECTION = 0
	IMAGE_SECTION = 1
	TEXT_IMAGE_SECTION = 2
	
	TYPE_DICT = {"text":TEXT_SECTION, "image":IMAGE_SECTION, "image_text":TEXT_IMAGE_SECTION}
	
	# Single Attributes
	number = models.IntegerField()
	section_type = models.IntegerField() # Will be enum; defined below
	
	# Section can have text, image, or both; depending on section_type
	text = models.CharField(max_length=255, blank=True) # Okay to be left blank, depending on s-type
	image = models.ImageField(upload_to='/tmp/img', blank=True) # Okay to be left blank, depending on s-type
	
	# Foreign Keys & Other-Table Relations
	page = models.ForeignKey(Page) # Section belongs to Page
	
	
	## METHODS ##
	
	# Given a string, converts it to a type (text, image, or image-text)
	def convertToTypeInt(self, s):
		if s == "text":
			return TEXT_SECTION
		elif s == "image":
			return IMAGE_SECTION
			

	def htmlTextSection(self):
		return "".join(["<p>", str(self.text), "</p>"])
		
	def htmlImageSection(self):
		return "<img src='%s'/>" % self.image
	
	# Returns the html for displaying the section, no matter what type it is
	def htmlSection(self):
		print "Section type: ", self.section_type
		if self.section_type == self.TEXT_SECTION:
			return self.htmlTextSection()
		
		elif self.section_type == self.IMAGE_SECTION:
			return self.htmlImageSection()
		
		else:
			return str(self.htmlTextSection()) + str(self.htmlImageSection())
			
		
	
	
	# String representation of self
	def __unicode__(self):
		if self.section_type == self.TEXT_SECTION:
			return " ".join(["Text: ", self.text])
			
		elif self.section_type == self.IMAGE_SECTION:
			return " ".join(["Image: ", str(self.image)])
			
		else:
			return ", ".join([self.text, str(self.image)])
		
			
		
	
if __name__ == "__main__":
	from book_app.models import *
	b = Book()
	b.title = "title"
	b.save()
	
	p = Page(1, b)
	#p.book = b
	#b.save()
	
	print b
	


