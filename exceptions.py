class BlankTaqueError(Exception):
          '''Error triggered when the user tries to perform an operation on the Taque list, but the Taque list is empty'''
          pass

class OutOfRangeError(Exception):
          '''Error triggered when a user tries to perform an operation on a given index, but the index is not included in the Taque list'''
          pass
