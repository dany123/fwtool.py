# Run `pyinstaller fwtool.spec` to generate an executable

import subprocess, sys

# Generate filename
suffix = {'linux2': '-linux', 'win32': '-win', 'darwin': '-osx'}
output = 'fwtool-' + subprocess.check_output(['git', 'describe', '--always', '--tags']).strip() + suffix.get(sys.platform, '')

# Analyze files
a = Analysis(['fwtool.py'])

# Generate executable
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, name=output)
