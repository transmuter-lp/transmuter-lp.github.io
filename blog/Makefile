.PHONY: all

posts=$(filter-out index.html,$(wildcard [!_]*.html))

all: index.html

index.html: ../ssg.py ../_main.template _index.main.component _footer.component $(posts)
	touch index.html
	cog -I ../ -p 'import ssg' -r index.html

$(posts):%.html: ../ssg.py ../_main.template _post.main.template _post.main.component _footer.component _%.article.component
	touch $@
	cog -I ../ -p 'import ssg' -r $@
