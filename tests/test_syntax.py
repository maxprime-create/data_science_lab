import py_compile, glob, os


def test_all_py_syntax():
    # compile all python files to ensure they parse (exclude tests dir)
    py_files = [f for f in glob.glob('**/*.py', recursive=True) if 'tests' not in f.replace('\\','/') and not f.startswith('.') ]
    for f in py_files:
        py_compile.compile(f, doraise=True)
