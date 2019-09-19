

all: $(patsubst src/%.md,out/%.png,$(wildcard src/*.md))

out/%.png: src/%.md
	mkdir -p out
	pandoc $< -M xnos-warning-level=0 -M pagestyle=empty \
           --filter pandoc-latex-extensions -o tmp.pdf
	pdfcrop --margins "15 5 5 5" tmp.pdf
	pdftoppm tmp-crop.pdf $(patsubst %.png,%,$@) -png -r 120 -f 1 -singlefile
	rm tmp.pdf tmp-crop.pdF

%.tex: src/%.md
	pandoc $< -M xnos-warning-level=0 -M pagestyle=empty \
           --filter pandoc-latex-extensions -o $@

.PHONY: clean
clean:
	rm -rf out
