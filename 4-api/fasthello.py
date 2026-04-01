from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")    # Define a route
def root():      # Define a function that will be called when the route is requested
    return {"message": "Hello World"} # Serializes to JSON automatically

@app.get("/hi/{name}")
def say_hi(name:str):
    return{'message': f'HI, {name}'}

@app.get("/roll/{number}d{sides}")  # Define a route with path parameters for rolling dice
def roll_dice(number: int, sides: int):  # Define a function that takes the number of dice and the number of sides as parameters
    import random  # Import the random module to generate random numbers
    rolls = random.randint(1, sides, number)  # Generate a list of random rolls
    return {
        "number_of_rolls": number,
        "number_of_sides": sides,
        "totalrolls": rolls
    }  # Return the rolls as a JSON response
    
#Correct version
@app.get("/roll/{number}d{sides}")  # Define a route with path parameters for rolling dice
def roll_dice(number: int, sides: int):  # Define a function that takes the number of dice and the number of sides as parameters
    import random  # Import the random module to generate random numbers
    rolls = random.randint(1, sides) * number  # Generate a random total for rolls by multiplying a random number between 1 and the number of sides by the number of dice
    return {
        "number_of_rolls": number,
        "number_of_sides": sides,
        "total_of_rolls": rolls
    }  # Return the rolls as a JSON response  
