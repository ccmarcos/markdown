from os import listdir
def post():
    #posts=[];
    for dir in listdir("post"):
        file = open("templates/index.html")
        index = file.read()
        index = index.split("<blog>")
        file.close()
        file = open("post/"+dir)
        indexaux = file.read()
        html = ""
        #html+="<article>"+indexaux+"<article>"
        html+="<section>"+indexaux+"</section>"
        html = index[0]+html+index[1]
        file.close()
        file = open("building/"+dir,"w")
        file.write(html)
        file.close()

post()
print("Finished.");
