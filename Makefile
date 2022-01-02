all: an-plugin.ankiaddon

an-plugin.ankiaddon: an
	(cd an && zip -r ../an-plugin.ankiaddon .)

clean:
	rm -f an-plugin.ankiaddon

.PHONY: all clean