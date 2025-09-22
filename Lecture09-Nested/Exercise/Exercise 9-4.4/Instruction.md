##Exercise 9-4.4:  Write a function ```to_dict(like_list)``` accepting the list of the form ```[[u1,u2], [u3,u4], ...]``` 
containing the list of who likes whom in a social media platform. The function has to create a dictionary in the form
```{user:``` list of all users the key user likes ```}```, e.g.,

```to_dict([['A', 'B'], ['A', 'C'], ['C', 'B']]) = {'A': ['B', 'C'], 'C': ['B']}```.
