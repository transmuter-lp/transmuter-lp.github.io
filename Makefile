.PHONY: all

all: index.html

index.html: _template.html _footer.html
	touch index.html
	cog -p 'import ssg' -r index.html
