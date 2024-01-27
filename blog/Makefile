.PHONY: all

posts=$(filter-out index.html,$(wildcard [!_]*.html))

all: index.html

index.html: ../_main.template _index.main.component _footer.component $(posts)
	cog -I ../ -r index.html

$(posts):%.html: ../_main.template _post.main.template _post.main.component _footer.component _%.article.component
	cog -I ../ -r $@
