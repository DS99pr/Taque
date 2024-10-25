'''The Taque list.

Description:
 A Taque list is a list that is similar to the Deque list, but not the same.
Note:
 The index in Taque starts with 1, and the name of the Taque list is not required. When you don't give a name, it will be set as "Default".
Content:
 Class *exceptions*: Where custom Taque errors are stored
 Class *taque*: Taque DataType
Usage:
 To use the Taque list, import the class, create an instance, and perform the operations on it that you have written in the project documentation (located on DS99pr/Taque)
 Example:
  from Taque import taque

  taqueList = taque([1, 2, 3], "Name For Taque")
  print(taqueList.view()) # [1, 2, 3]
  taqueList.appendFirst(0)
  print(taqueList.view()) # [0, 1, 2, 3]
Author:
 @DS99pr, a.k.a. __ds99__
Created on:
 25.10.2024
Last updated:
 25.10.2024

For bug reports or suggestions, please open an issue on the GitHub repository.
'''

class exceptions:
    class BlankTaqueError(Exception):
          '''Error triggered when the user tries to perform an operation on the Taque list, but the Taque list is empty'''
          pass
    
    class OutOfRangeError(Exception):
          '''Error triggered when a user tries to perform an operation on a given index, but the index is not included in the Taque list'''
          pass

class taque:
     '''A Taque list is a new custom data type in which the m.in index starts with 1. Taque is very similar to the Deque list, but it has its differences.'''
     def __init__(self, obj: list, name: str = None):
         '''If you do not specify a name for the Taque list, the system will automatically replace it with "Default"'''
         self.__taque__ = obj
         if name: 
          self.name = name
         else:
          self.name = "Default"
     def view(self):
         '''Returns the contents of a Taque list'''
         return self.__taque__
     def first(self):
         '''Returns the first element of a Taque list'''
         if len(self.__taque__) != 0:
          return self.__taque__[0]
         else:
          raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
     def last(self):
         '''Returns the last element of the Taque list'''
         if len(self.__taque__) != 0:
          return self.__taque__[-1]
         else:
          raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
     def appendFirst(self, object):
         '''Adds an item to the top of the Taque list'''
         self.__taque__.insert(0, object)
     def appendLast(self, object):
         '''Adds an element to the end of the Taque list'''
         self.__taque__.append(object)
     def popFirst(self):
         '''Removes the first item in the Taque list'''
         if len(self.__taque__) != 0:
          self.__taque__.pop(0)
         else:
          raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
     def popLast(self):
         '''Removes the last item in the Taque list'''
         if len(self.__taque__) != 0:
          self.__taque__.pop()
         else:
          raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
     def addSpecific(self, index: int, object):
         '''Adds an element at a given index (from 1) to the Taque list'''
         self.__taque__.insert(index-1, object)
     def removeSpecific(self, index: int):
        '''Removes an element from the given index (from 1) from the Taque list'''
        try:
         if len(self.__taque__) != 0:
          self.__taque__.pop(index-1)
         else:
          raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
        except IndexError:
          raise exceptions.OutOfRangeError("Item not found with this index - this operation cannot be performed")
     def sort(self, reversed: bool = False):
        '''Sorts the Taque list'''
        if len(self.__taque__) != 0:
         self.__taque__.sort(reverse=reversed)
        else:
         raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
     def look(self, index: int):
       '''Returns an item at a given index (from 1) of the Taque list'''
       try:
        if len(self.__taque__) != 0:
         return self.__taque__[index-1]
        else:
         raise exceptions.BlankTaqueError("The taque is empty - this operation cannot be performed") 
       except IndexError:
        raise exceptions.OutOfRangeError("Item not found with this index - this operation cannot be performed")
     def changeName(self, newName: str):
       '''Renames a Taque list'''
       self.name = newName