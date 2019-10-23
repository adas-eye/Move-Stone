# find some file
find . -regex '.*\.txt\|.*\.doc\|.*\.mp3'  

# except some file
find . -type f ! -name "*.html"   

