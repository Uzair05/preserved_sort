# preserved_sort

A python script which can remove redundant lines.

## Philosophy

A replacement to the convential bash sequence `sort -u -f <filename>`. I will try to implement this following the techniques of functional programming, while ensuring type safety.  
To do so, I am using the typing library.

## Prerequisites

```bash
pip install -U typing
```

## Goal

The goal was to create a script capable of removing redundant lines of text without compromising on order of text.

I also intended to try achive doing in in a functional programming manner.

My script achives this in O(n) time.

## Example

Take the example of a text file with contents:

```
bee
apple
apple
```

A textfile, conventionally, needed to be sorted by bash command:

```bash
sort -u -f <filename>
```

Or

```bash
sort -f <filename> | uniq
```

The results would be:

```
apple
bee
```

We can see that the order of entries is not respected.

To overcome this I wrote a script.

## Note

The script preserves whitespace. This feature is implemented in line 128-131.

```python
            if arr[st].val == '':
                res.extend(arr[st:pt])
            else:
                res.append(reduceArray(arr, st, pt))
```

you can replace it with the following code to remove this feature.

```python
            res.append(reduceArray(arr, st, pt))
```
