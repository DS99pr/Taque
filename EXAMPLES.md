# Examples
**taque()**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4, 5], name="myTaqueList")
```
**name**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4, 5], name="myTaqueList")
print(taqueList.name) # myTaqueList
taqueList2 = taque([1, 2, 3, 4, 5])
print(taqueList2.name) # Default
```
**view()**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4, 5])
print(taqueList.view()) # [1, 2, 3, 4, 5]
```
**look()**:
```python
# Taque list index starts at 1
from taque import taque

taqueList = taque(['a', 'b', 'c', 'd', 'e'])
print(taqueList.look(3)) # c
```
**first()**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4, 5])
print(taqueList.first()) # 1
```
**last()**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4, 5])
print(taqueList.last()) # 5
```
**appendFirst()**:
```python
from taque import taque

taqueList = taque([2, 3, 4, 5])
print(taqueList.view()) # [2, 3, 4, 5]
taqueList.appendFirst(1)
print(taqueList.view()) # [1, 2, 3, 4, 5]
```
**appendLast()**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4])
print(taqueList.view()) # [1, 2, 3, 4]
taqueList.appendLast(5)
print(taqueList.view()) # [1, 2, 3, 4, 5]
```
**popFirst()**:
```python
from taque import taque

taqueList = taque([0, 1, 2, 3, 4, 5])
print(taqueList.view()) # [0, 1, 2, 3, 4, 5]
taqueList.popFirst()
print(taqueList.view()) # [1, 2, 3, 4, 5]
```
**popLast()**:
```python
from taque import taque

taqueList = taque([1, 2, 3, 4, 5, 6])
print(taqueList.view()) # [1, 2, 3, 4, 5, 6]
taqueList.popLast()
print(taqueList.view()) # [1, 2, 3, 4, 5]
```
**addSpecific()**:
```python
from taque import taque

taqueList = taque([1, 2, 4, 5])
print(taqueList.view()) # [1, 2, 4, 5]
taqueList.addSpecific(3, 3)
print(taqueList.view()) # [1, 2, 3, 4, 5]
```
**removeSpecific()**:
```python
from taque import taque

taqueList = taque(['a', 'b', 'c', 'c', 'd', 'e'])
print(taqueList.view()) # ['a', 'b', 'c', 'c', 'd', 'e']
taqueList.removeSpecific(4)
print(taqueList.view()) # ['a', 'b', 'c', 'd', 'e']
```
**sort()**:
```python
from taque import taque

taqueList = taque([3, 1, 2])
taqueList.sort(reversed=False)
print(taqueList.view()) # [1, 2, 3]
taqueList.sort(reversed=True)
print(taqueList.view()) # [3, 2, 1]
```
**changeName()**:
```python
from taque import taque

taqueList = taque([])
print(taqueList.name) # Default
taqueList.changeName('TaqueList')
print(taqueList.name) # TaqueList
```
**editElement()**:
```python
from taque import taque

taqueList = taque(['a', 'b', 'g', 'd', 'e'])
print(taqueList.view()) # ['a', 'b', 'g', 'd', 'e']
taqueList.editElement(3, 'c')
print(taqueList.view()) # ['a', 'b', 'c', 'd', 'e']
```
**changeTaqueList()**:
```python
from taque import taque

taqueList = taque(['a', 'b', 'c'])
print(taqueList.view()) # ['a', 'b', 'c']
taqueList.changeTaqueList([1, 2, 3])
print(taqueList.view()) # [1, 2, 3]
```
