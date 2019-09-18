

all: $(patsubst src/%.md,%.png,$(wildcard src/*.md))

%.png: src/%.md
	pandoc $< -M xnos-warning-level=0 -M pagestyle=empty \
           --filter pandoc-latex-extensions -o tmp.pdf
	pdfcrop --margins 5 tmp.pdf
	pdftoppm tmp-crop.pdf $(patsubst %.png,%,$@) -png -r 100 -f 1 -singlefile
	rm tmp.pdf tmp-crop.pdF

.PHONY: clean
clean:
	rm *.png
