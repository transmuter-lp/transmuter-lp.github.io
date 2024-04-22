.PHONY: all

all: index.html

index.html: ssg.py _template.html _footer.html
	touch index.html
	cog -p 'import ssg; init = False' -r index.html
