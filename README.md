# Storing user passwords in clear text? 

Keeping your passwords secure is important. Even more if you
are storing passwords for others. I'm going to show you a simple way to hash a password using Python.

### TLDR
Code is at the end. Get down to nitty gritty

### Requirements
- Python 3. 
- Passlib 
  - https://passlib.readthedocs.io/en/stable/

### Let's code!

I'm going to write out some code and explain what is happening.
I'll start off by importing our two libraries Passlib and Getpass.
```python
1 |  from passlib.handlers.sha2_crypt import sha512_crypt as hasher
2 |  from getpass import getpass
```

So what do we have here? 

Line 1: Passlib is imported and from the ```handlers.sha2_crypt``` module we import ```sha512_crypt```
as ```hasher```.   

Line 2: From the library ```getpass```  we import ```getpass```.


Now let's create our function that will ask for the username and password. In this function we can also 
include the hash method.

```python
5 | def account_creation():
6 |     username = input("Please enter a username: ")
7 |     password = getpass("Please enter a password: ")
8 |     hashed_password = hasher.hash(password, rounds=200_000)
9 |     database_create(username, hashed_password)
```

Now what did we do?

Line 5: we defined our function and we named it ```account_creation()```

Line 6: asks the user for the username and sets it as a variable named ```username```.

Line 7: prompts the user for the password and sets it as variable named ```password```.

Line 8: hashes our ```password``` using ```hasher.hash``` and sets the rounds to 200 thousand. By default passlib
iterates the hash 29,000 times but we went above and beyond with 200k!

Line 9: we call a function named ```database_create()``` and give it two parameters named ```username``` and ```password```.


Let's create our ```database_create()``` definition that we just passed the username and password through. 

```python
12 | def database_create(username, password):
13 |    file = open(f"{username}.txt", "w")
14 |    file.write(password)
15 |    file.close()
16 |    print("Account created.")
```

Line 12: we define our function ```database_create()``` and pass the ```username``` and ```password``` arguments.

Line 13: we create a variable named ```file``` and assign the Python built in function ```open()```. 
This built in function is used to open or create files. Inside the ```open()``` function we pass an f-string with the 
argument ```username```. As you can see that it is creating a .txt file with the ```username``` that is provided.

Line 14: Our variable ```file``` is used to write the password using the ```write()``` function.

Line 15: We use the ```close()``` function to make sure code and the OS has closed the session.

Line 16 And we print something out to confirm our code completed.

Finally we add our main method. This makes us 10x developers!
```python
19 | if __name__ == "__main__":
20 |     account_creation()
```


And that's it! 


# The Code

```python
from passlib.handlers.sha2_crypt import sha512_crypt as hasher
from getpass import getpass


def database_create(username, password):
    file = open(f"{username}.txt", "w")
    file.write(password)
    file.close()
    print("Account created.")


def account_creation():
    username = input("Please enter a username: ")
    password = getpass("Please enter a password: ")
    hashed_password = hasher.hash(password, rounds=200_000)
    database_create(username, hashed_password)


if __name__ == "__main__":
    account_creation()
```