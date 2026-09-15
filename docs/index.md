# ArmKit Documentation

ArmKit is a tiny Python wrapper around the [PyBullet](https://pybullet.org)
physics engine. It lets you load a robot arm into a simulation and move its
joints in a few lines of code: no hardware required.

This site is also a worked example of a **Docs-as-Code** documentation set: it
is written in Markdown, kept under version control in Git, built with Sphinx,
and published automatically by a CI pipeline.

The documentation follows the [Diátaxis](https://diataxis.fr) framework, which
separates docs by what the reader is trying to do.

```{toctree}
:maxdepth: 1
:caption: Tutorials

tutorials/first-arm
```

```{toctree}
:maxdepth: 1
:caption: How-to guides

how-to/set-joint-angles
how-to/run-headless
```

```{toctree}
:maxdepth: 1
:caption: Reference

reference/api
```

```{toctree}
:maxdepth: 1
:caption: Explanation

explanation/forward-kinematics
```

```{toctree}
:maxdepth: 1
:caption: Contributing

style-guide
```

## Where to start

:::{list-table}
:header-rows: 1

* - If you want to…
  - Go to
* - Get something running for the first time
  - {doc}`tutorials/first-arm`
* - Solve a specific task
  - {doc}`how-to/set-joint-angles`
* - Look up a function signature
  - {doc}`reference/api`
* - Understand a concept
  - {doc}`explanation/forward-kinematics`
:::
