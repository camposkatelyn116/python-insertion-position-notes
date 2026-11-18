# Find an insertion point after ties: implementation

## What the example does

bisect_right inserts after existing equal values. Searching is logarithmic, but actually inserting into a Python list still shifts elements in linear time.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "items": [
    1,
    3,
    3,
    8
  ],
  "target": 3
}
```

Expected result:

```json
3
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
