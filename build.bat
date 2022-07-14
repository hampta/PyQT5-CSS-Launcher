@echo off
python -m nuitka --onefile --output-dir=build --remove-output --prefer-source-code --enable-plugin=anti-bloat --noinclude-pytest-mode=nofollow --noinclude-setuptools-mode=nofollow --lto=yes --jobs=16 --follow-imports --low-memory --nofollow-import-to=PyQt5 --plugin-enable=pyside2 --no-pyi-file ./main.py
pause