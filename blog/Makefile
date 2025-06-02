.PHONY: all

posts=$(filter-out index.html,$(wildcard [!_]*.html))

all: index.html

index.html: ../_template.html _index.main.html _footer.html $(posts)
	touch index.html
	ssg index.html

$(posts):%.html: ../_template.html _post.html _post.main.html _footer.html _%.article.html
	touch $@
	ssg $@
