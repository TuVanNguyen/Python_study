# A Proper Class

## 2.1 Writing a Proper Python Class
  * Each class should have:
    * **docstring**: documents purpose of class and how to use it
    * `__str__`: magic method to represent object as string such as when using `print()`
    * `__repr__`: magic method to represent object without string conversion in interactive shell, debugger, etc
    * `__eq__`: equality comparator 
    * `__lt__`: less than comparator to enable sorting
    * access control: use `private` to make members visible only within the class
  * If the class is a container for other classes, it should have:
    * `__len__`: magic method to count number of objects contained in the class
    * ability to iterate over the items in the class
    * allow users to access items using `[]` notation

## Access Specifiers

Access Specifiers control how accessible class members are.


* public: can be accessed from inside and outside the class
* protected: can only be accessed within the class and its subclasses
* private: can only be accessed from within the class

```
class Myclass:

  def __init__(self):
    self.public_attribute = "I'm public!" 
    self._protected_attribute = "I'm protected." # underscore prefix
    self.__private_attribute = "I'm private" # double underscore prefix

  def public_method(self):
    print("This is public!")

  def _protected_method(self): # underscore prefix
    print("This is protected.")

  def __private_method(self): # double underscore prefix
    print("This is private.") 
```
    
     
