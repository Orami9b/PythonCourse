class Account:
   def __init__(self, filepath):
      self.filepath = filepath
      with open(self.filepath, "r") as file:
         self.balance = int(file.read())

   def withdraw(self, amount):
      self.balance -= amount
      self.commit()
   
   def deposit(self, amount):
      self.balance += amount
      self.commit()

   def commit(self):
      with open(self.filepath, "w") as file:
         file.write(str(self.balance))

class Checking(Account):
   def __init__(self, filepath, fee):
      Account.__init__(self, filepath)
      self.fee = fee

   def transfer(self, amount):
      self.balance -= amount + self.fee
      self.commit()