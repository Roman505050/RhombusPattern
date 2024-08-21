### Rhombus Pattern

Program to print a rhombus pattern of `*` characters.

Code:
```python
a = 6

# Upper part of the rhombus
for i in range(a):
    print(' ' * (a - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))

# Lower part of the rhombus
for i in range(a - 2, -1, -1):
    print(' ' * (a - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))
```

Start by command `python3 main.py` in Linux or `python main.py` in Windows.

Output:
```
     *
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     *
```