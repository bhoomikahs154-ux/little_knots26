from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/keychains")
def keychains():

    products = [

        {
            "name": "Sunflower Keychain",
            "price": "₹169",
            "image": "flower.jpg"
        },
        {
            "name": "Sunflower Keychain",
            "price": "₹169",
            "image": "sunflower.jpg"
        }, 

        {
            "name": "Evil Eye Keychain",
            "price": "₹169",
            "image": "evil eye.jpeg"
        },

        {
            "name": "Bow Keychain",
            "price": "₹129",
            "image": "bow.jpeg"
        },

        {
            "name": "Bow Keychain",
            "price": "₹129",
            "image": "pinkbow.jpeg"
        },

        {
            "name": "Meshed Bow Keychain",
            "price": "₹129",
            "image": "meshed bow red.jpeg"
        },

        {
            "name": "Meshed Bow Keychain",
            "price": "₹129",
            "image": "meshed bow.jpeg"
        },

        
        {
            "name": "Peacock feather Keychain",
            "price": "₹169",
            "image": "peacock feather.jpeg"
        }, 
        {
            "name": "Penguin Keychain",
            "price": "₹299",
            "image": "penguin.jpeg"
        }, 
        {
            "name": "White Bunny Keychain",
            "price": "₹299",
            "image": "bunny.jpeg"
        }, 
        {
            "name": "Chick Keychain[Yellow]",
            "price": "₹299",
            "image": "chick.jpeg"
        }, 
        {
            "name": "white chick Keychain",
            "price": "₹299",
            "image": "white chick.jpeg"
        }, 
        {
            "name": "Fish Keychain",
            "price": "₹149",
            "image": "fish.jpeg"
        }, 
        {
            "name": "Rainbow Keychain",
            "price": "₹169",
            "image": "rainbow.jpeg"
        }, 
        {
            "name": "Pink Heart Keychain",
            "price": "₹199",
            "image": "pinkheart.jpeg"
        }, 
        {
            "name": "Red Heart Keychain",
            "price": "₹199",
            "image": "red heart.jpeg"
        }
        , 
        {
            "name": "Heart Keychains",
            "price": "₹199",
            "image": "heart2.jpeg"
        }, 
        {
            "name": "Red Heart Keychain",
            "price": "₹99",
            "image": "heart.jpeg"
        }, 
        {
            "name": "Penguin Keychain",
            "price": "₹299",
            "image": "penguin2.jpeg"
        }, 
        {
            "name": "Octopus Keychain",
            "price": "₹99",
            "image": "octo.jpeg"
        }
        , 
        {
            "name": "Octopus Keychain",
            "price": "₹99",
            "image": "octo1.jpeg"
        }, 
        {
            "name": "Octopus Keychain",
            "price": "₹99",
            "image": "octo2.jpeg"
        }, 
        {
            "name": "Octopus Keychain",
            "price": "₹99",
            "image": "octo3.jpeg"
        }, 
        {
            "name": "Daisy Keychain[cream]",
            "price": "₹129",
            "image": "daisy.jpeg"
        }, 
        {
            "name": "Daisy Keychain",
            "price": "₹129",
            "image": "daisy(2).jpeg"
        }, 
        {
            "name": "Daisy Keychain",
            "price": "₹129",
            "image": "daisy2.jpeg"
        }, 
        
        {
            "name": "Tulip Keychain",
            "price": "₹169",
            "image": "tulip charm.jpeg"
        }

    ]

    return render_template(
        "keychains.html",
        products=products
    )

@app.route("/bouquets")
def bouquets():

    products = [

        {
            "name": "Single tulip Bouquet[PURPLE]",
            "price": "₹299",
            "image": "purple tulip b.jpeg"
        },

        {
            "name": " Single tulip Bouquet[WHITE]",
            "price": "₹299",
            "image": "white tulip b.jpeg"
        },

        {
            "name": " Single tulip Bouquet[RED]",
            "price": "₹299",
            "image": "red tulip b.jpeg"
        },
        
        {
            "name": " Single Rose Bouquet",
            "price": "₹349",
            "image": "rose b.jpeg"
        },
        
        {
            "name": " Pink Rose Bouquet",
            "price": "₹799",
            "image": "pink b.jpeg"
        },
        
        {
            "name": " Tulip Bouquet",
            "price": "₹699",
            "image": "tulip b.jpeg"
        },
        
        {
            "name": " Tulip Bouquet",
            "price": "₹699",
            "image": "tulip white b.jpeg"
        },

        {
            "name": " Flower Bouquet",
            "price": "₹799",
            "image": "mixed flower b.jpeg"
        }
        ,
        {
            "name": " Red Rose Bouquet[10 roses]",
            "price": "₹2999",
            "image": "red b.jpeg"
        }
        ,
        {
            "name": " Red Rose Bouquet[10 roses]",
            "price": "₹2999",
            "image": "red b2 .jpeg"
        }
       ,
        {
            "name": " Coustomized Rose-lilly  Bouquet",
            
            "image": "rose-lilly.jpeg"
        }

    ]

    return render_template(
        "bouquets.html",
        products=products
    )

@app.route("/others")
def others():
    products = [
       {
            "name": " Sun Flower Pot",
            "price": "₹349 + Shipping",
            "image": "pot.jpeg"
        },

         {
            "name": "Tulip hair tie",
            "price": "₹199",
            "image": "tulip charm.jpeg"
        },

         {
            "name": "Car charm",
            "price": "₹399",
            "image": "car charm.jpeg"
        },
        


    ]
    return render_template("others.html", products=products)
    
@app.route("/how-to-order")
def how_to_order():
    return render_template("how-to-order.html")

if __name__ == "__main__":
    app.run(debug=True)