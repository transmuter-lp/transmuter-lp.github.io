.PHONY: all

all: index.html

index.html: ssg.py _main.template _footer.component
	cog -r index.html
