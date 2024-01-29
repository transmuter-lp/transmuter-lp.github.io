.PHONY: all

all: index.html

index.html: ssg.py _main.template _footer.component
	touch index.html
	cog -p 'import ssg' -r index.html
