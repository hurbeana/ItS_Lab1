# default variablen in make:
# $<    die erste Abhängigkeit
# $@    Name des targets
# $+    eine Liste aller Abhängigkeiten
# $^    eine Liste aller Abhängigkeiten, wobei allerdings doppelt vorkommende Abhängigkeiten eliminiert wurden.

DOKUMENT = protokoll
DOCUMENT = protocol

all: en de

clean:
	@echo "make clean leaves generated pdf files untouched. To delete them also, use: \n\tmake distclean\n"
	@for filename in $(DOKUMENT) $(DOCUMENT); do \
		rm -fv $${filename}.tex~; \
		rm -fv $${filename}.aux; \
		rm -fv $${filename}.log; \
		rm -fv $${filename}.out; \
		rm -fv $${filename}.toc; \
		rm -fv $${filename}.pdf.done; \
		rm -fv $${filename}.pdflatex.output; \
	done

distclean: clean
	@rm -fv $(DOKUMENT).pdf
	@rm -fv $(DOCUMENT).pdf

de: $(DOKUMENT).pdf
	@echo "deutsches Dokument erstellt"
	@echo "---------------------------"

en: $(DOCUMENT).pdf
	@echo "english document created"
	@echo "------------------------"

%.pdf: %.tex
	pdflatex $^
	while [ ! -f "$@.done" ]; do \
		grep -q "Rerun to get cross-references right." $(shell basename $@ .pdf).log || ( touch $@.done && break ); \
		pdflatex $^; \
	done
	rm "$@.done"

# end
