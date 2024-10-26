# Documentation:
- **taque(obj=list, name=str)**: **Creates a Taque list**
- **view()**: **Displays the entire Taque list**
- **look()**: **Display a Taque list item using an index**
- **first()**: **Displays the first item in the Taque list**
- **last()**: **Displays the last item in the Taque list**
- **appendFirst(obj)**: **Adds an element to the top of the Taque list**
- **appendLast(obj)**: **Adds an element to the end of the Taque list**
- **popFirst()**: **Removes the first item in the Taque list**
- **popLast()**: **Deletes the last item in the Taque list**
- **addSpecific(index=int, obj)**: **Adds an element to a specific index in the list**
- **removeSpecific(index=int)**: **Removes an element from a specific index in a Taque list**
- **sort(reversed=bool)**: **Sorts the Taque list**
- **changeName(newName=str)**: **Renames a Taque list**
# Errors documentation:
- **exceptions.BlankTaqueError**: **Error triggered when the user tries to perform an operation on the Taque list, but the Taque list is empty**
- **exceptions.OutOfRangeError**: **Error triggered when a user tries to perform an operation on a given index, but the index is not included in the Taque list**
