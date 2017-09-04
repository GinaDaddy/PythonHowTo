import gzip
f = gzip.open('/Users/bmoon/git/PythonHowTo/resources/gziptest.txt.gz', 'rb')
file_content = f.read()
print file_content
f.close()