.PHONY: all

all: index.html

index.html: _main.template _footer.component
	cog -r index.html
