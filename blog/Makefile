.PHONY: all

posts=$(filter-out index.html,$(wildcard [!_]*.html))

all: index.html

index.html: ../ssg.py ../_template.html _index.main.html _footer.html $(posts)
	touch index.html
	cog -I ../ -p 'import ssg; init = False' -r index.html

$(posts):%.html: ../ssg.py ../_template.html _post.html _post.main.html _footer.html _%.article.html
	touch $@
	cog -I ../ -p 'import ssg; init = False' -r $@
