#!/usr/bin/env bash
pyuic5 -x views/ensayator.ui -o views/ensayator_ui.py
#pyuic5 -x dialogs/exception_dialog.ui -o dialogs/exception_dialog.py
pyrcc5 views/resources.qrc -o views/resources.py