WWW = ../www/

all:
	cp *.css ${WWW}
	-cp images/*.* ${WWW}/images
	./generate.py ${WWW} *.html

upload:
	ncftpput -R -m -u ssding 69.65.33.56 / ../www

backup:
	make clean
	cd ../..; tar cvzf dingdingding.tgz dingdingding; \
		ncftpput -u ssding 69.65.33.56 / dingdingding.tgz

clean:
	-rm -f ${WWW}/*
	-rm -f ${WWW}/images/*

checkin:
	ci -l images/*.* *.* Makefile

