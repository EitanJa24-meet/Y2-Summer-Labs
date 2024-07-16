from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html>
        <h1>Art Gallery</h1>
        <p>welcome to the art gallery</p>
        <img border = "2px" src = \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMtt3aOrfYZ1KnQq4GK0vf9gkNBC07f72UWQ&s\"></img>
        <img border = "2px" src = \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSddqc-p4xRroa90v8AImxUooUElCQV45yPoQ&s\"></img>
        <img border = "2px" src = \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAjscjbQCYz1J1yy8NBw8vRNb8UoIq_WwaJw&s\"></img>
        <br>
        <h1>Food Gallery</h1>
        <a href = \'/food1\' >go to the a favorite food photo</a>     
        <br>
        <br>
        <a href = \'/food3\' >go to the a protien photo</a>
        <br>
        <br>
        <h1>Pets Gallery</h1>
        <a href = \'/pets1\' >go to the the dog photo</a>    
        <br>
        <br>
        <h1>Space Gallery</h1>
        <a href = \'/space2\' >go to the the earth photo</a>   
        </html>''')

# food gallery
@app.route('/food1')
def food1(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzCYCjq8DZ9e-9nnRrHAPoxSmezR-BSalyKA&s\"></img>
        <br>
        <a href = \'/food2\' >go to the the best pastry photo</a>
        <br>
        <br>
        <a href = \'/home\' >go to the main menu</a> 
        </html>''')


@app.route('/food2')
def food2(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://www.allrecipes.com/thmb/Xbf-_X0A-SDlt25bFmsPPtxy5_Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/229276-easy-cinnamon-rolls-DDMFS-4x3-a225ddff4e7948e9b239557f14a9c05b.jpg\"></img>
        <br>
        <a href = \'/food3\' >go to the a protien photo</a>
        <br>
        <br>  
        <a href = \'/food1\' >go to the a favorite food photo</a>     
        </html>''')
 
@app.route('/food3')
def food3(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt0RheC3QV2FvKe0TM18z-6bhhS9fgOX1pgA&s\"></img>
        <br>
        <a href = \'/home\' >go to the main menu</a> 
        <br> 
        <br>
        <a href = \'/food2\' >go to the the best pastry photo</a>     
        </html>''') 



# pets gallery
# dog
@app.route('/pets1')
def pets1(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*\"></img>
        <br>
        <a href = \'/pets2\' >go to the the cat photo</a>
        <br>
        <br>
        <a href = \'/home\' >go to the main menu</a> 
        <br>
        <br>
        <a href = \'/pets3\' >go to the the bunny photo</a>
        </html>''')

# cat
@app.route('/pets2')
def pets2(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://studyfinds.org/wp-content/uploads/2023/10/shutterstock_1151252645-scaled.jpg\"></img>
        <br>
        <a href = \'/pets3\' >go to the the bunny photo</a>
        <br>
        <br>  
        <a href = \'/pets1\' >go to the the dog photo</a>     
        </html>''')
 
 # bunny
@app.route('/pets3')
def pets3(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://cdn.shopify.com/s/files/1/0015/5117/1636/files/Bunny_outside.jpg?v=1687550353\"></img>
        <br>
        <a href = \'/pets1\' >go to the the dog photo</a>  
        <br> 
        <br>
        <a href = \'/pets2\' >go to the the cat photo</a>     
        </html>''') 


# space gallery
# sun
@app.route('/space1')
def space1(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://static.bhphotovideo.com/explora/sites/default/files/ts-space-sun-and-solar-viewing-facts-versus-fiction.jpg\"></img>
        <br>
        <a href = \'/space2\' >go to the the earth photo</a>     
        </html>''')

# earth
@app.route('/space2')
def space2(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsRtkc3Q7ZzFb_IrmEh-VzAlTrb6BxBzZGFg&s\"></img>
        <br>
        <a href = \'/space1\' >go to the the sun photo</a>     
        <br>
        <br>
        <a href = \'/home\' >go to the main menu</a> 
        <br>
        <br>
        <a href = \'/space3\' >go to the the mars photo</a>
        </html>''')
 # mars
@app.route('/space3')
def space3(): 
    return  ('''<html>
        <img border = "2px" width = "400px" src = \"https://starwalk.space/gallery/images/mars-the-ultimate-guide/1920x1080.jpg\"></img>
        <br>
        <a href = \'/space2\' >go to the the earth photo</a>     
        </html>''') 


# run the code
if __name__ == '__main__':
    app.run(debug=True)

