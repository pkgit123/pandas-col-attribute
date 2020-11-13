# pandas-col-attribute
Playbook to get attribute from column object

Example use.  Subtracting two date columns in pandas results in timedelta object.  To convert into days, need to get the `.days` attribute from the timedelta object.

In order to get the attributes from a column, use the `.apply()` method combined with the `attrgetter()` function.  Combining the two: `.apply(attrgetter('attribute_name'))`

```
from operator import attrgetter
```

### References:
* https://stackoverflow.com/questions/57930254/pandas-apply-function-to-column-then-get-attribute
