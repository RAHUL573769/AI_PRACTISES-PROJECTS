class Gender:
    def __init__(self, name, gender, address):
        self.name1 = name
        self.gender1 = gender
        self.address1 = address

    def __str__(self):
        return f"Name: {self.name1}, Gender: {self.gender1}, Address: {self.address1}"


class Address:
    def __init__(self, city, pin, state):
        self.city1 = city
        self.state1 = state
        self.pin1 = pin

    def __str__(self):
        return f"{self.city1}, {self.state1} - {self.pin1}"


# Object creation
add1 = Address("gurgaon", 1234, "haryana")
g1 = Gender("Rahul", "Male", add1)

# Printing object
print(g1)


# ====


# example
class Customer:

  def __init__(self,name,gender,address):
    self.name = name
    self.gender = gender
    self.address = address

  def print_address(self):
    print(self.address._Address__city,self.address.pin,self.address.state)

  def edit_profile(self,new_name,new_city,new_pin,new_state):
    self.name = new_name
    self.address.edit_address(new_city,new_pin,new_state)

class Address:

  def __init__(self,city,pin,state):
      self.__city = city
      self.pin = pin
      self.state = state

  def get_city(self):
    return self.__city

  def edit_address(self,new_city,new_pin,new_state):
    self.__city = new_city
    self.pin = new_pin
    self.state = new_state

add1 = Address('gurgaon',122011,'haryana')
cust = Customer('nitish','male',add1)

cust.print_address()

cust.edit_profile('ankit','mumbai',111111,'maharastra')
cust.print_address()
# method example
# what about private attribu




class Customer1:
    def __init__(self, name, age, address):
        self.name1 = name
        self.age1 = age
        self.address1 = address

    def print_address(self):
        print(self.address1.pincode1)
        print(self.address1.state1)


class Address1:
    def __init__(self, pincode, state):
        self.pincode1 = pincode
        self.state1 = state


add = Address1(4100, "Chittagong")

customer = Customer1("Rahul", 45, add)

customer.print_address()