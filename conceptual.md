### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

     JS is a browser based language there's no need to install it, it just natively runs in browsers and because of this univeral compatibillity all frontend work is typically done with JS. Python on the other hand must be installed and run locally. Python is more commonnly used for backend server work and things like machine learning. Syntactically JS defines codeblocks with {} whereas Python uses indentation. Python's syntax is gennerally considered to be more "user friendly" and intuitive. JS uses camelCase whereas Python uses snake_case. JS requires varibles to be defined with let and const whereas Python varibales can be assigned with just an =. The data structures of both languages are very similar, there are subtle differences between things like lists/arrays, objects/dictionaries etc but all the basic concepts are the same. Python has a very large built in library that can be easily imported whereas JS has many external libraries that need to be included in the script in order to use them.  


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

     1) You can you get() to assign a default value, if the key is present the associated value will be displayed otherwise it will return the default value.

     2) You can use setdefault()


- What is a unit test?

     A unit test tests one unit of funcionality typically just a single function or method.


- What is an integration test?

     An integration test tests how multiple components work together. 


- What is the role of web application framework, like Flask?
  
    Flask is a framework that streamlines and standardizes the building of web applications it handles the components that are nescessary for running servers such as routing, requests, sessions and so on.
   

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    You would use a query param when you need to access information that is generated when a user performs a search or submits a form. Otherwise you would pass the information as a route parameter.  


- How do you collect data from a URL placeholder parameter using Flask?

    First you need to import request, then you can use request.args to access data. 


- How do you collect data from the query string using Flask?

    You would also use request.args if you want the parameters of the query string, there's a method request.query_string that will return the entire query string. 


- How do you collect data from the body of the request using Flask?

    If I understand the question correctly you would collect the data sent from a post request by first including it as a param in the request and then making a variable in your route that calls a request method to access it. For example if it were coming from an Ajax request it would be something like, score = request.json['score'] 


- What is a cookie and what kinds of things are they commonly used for?

    A cookie is used to save "state" and store smalls bits of data. HTTP is a stateless protocol and cannot remember anything on its own. Cookies as opposed to local storage and session storage can be accessed on both the server and client side. Cookies are commonly used to track data, such as how many times a user has visited, what they click on etc. They are also used to store login creditials and instances of shopping carts etc...


- What is the session object in Flask?

   Like cookies the session object is used to track the session data, it stores the data in a dictionary object of key value pairs. Sessions is a flask tool built ontop of cookies that makes working with cookies easier and more streamlined it also provides extra funcionality such as encoding the data that is stored. 


- What does Flask's `jsonify()` do?

   jsonify() converts a response into readable Json which is necessary when interacting between Python/Flask and Javascript. 
