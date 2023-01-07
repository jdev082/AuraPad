install:
	sudo cp -r AuraPad.py /usr/bin/aurapad
	sudo chmod +x /usr/bin/aurapad
	sudo cp -r AuraPad.desktop /usr/share/applications
	sudo cp -r icon.png /opt/apicn.png

uninstall:
	sudo rm -rf /usr/bin/aurapad
	sudo rm -rf /usr/share/applications/AuraPad.desktop
	sudo rm -rf /opt/apicn.png

check:
	bash checkdeps.sh
