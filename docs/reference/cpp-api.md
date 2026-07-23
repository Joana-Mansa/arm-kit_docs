# C++ API reference

The C++ interfaces below are generated from Doxygen comments in the ArmKit
headers and rendered here by Breathe, so this page and the source cannot drift
apart. The Python reference is generated the same way, by `autodoc`, and both
appear in a single published site.

:::{note}
The limit checks documented here are kinematic only. They are independent of
any safety-rated limits enforced by the controller itself.
:::

## Limit checking

### JointLimitChecker

```{doxygenclass} armkit::JointLimitChecker
:project: armkit_cpp
:members:
```

### JointLimit

```{doxygenstruct} armkit::JointLimit
:project: armkit_cpp
:members:
```

### LimitStatus

```{doxygenenum} armkit::LimitStatus
:project: armkit_cpp
```
