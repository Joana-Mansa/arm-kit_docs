# Move your first robot arm

This tutorial takes you from an empty terminal to a robot arm moving on screen.
By the end you will have installed ArmKit, opened a physics simulation, loaded a
robot, and watched it bend a joint on command.

You do not need any robotics background, and you do not need a real robot. You
will need Python 3.10 or newer and about ten minutes.

## Before you start

Check that Python is available:

```console
$ python --version
Python 3.12.3
```

If that prints a version number, you are ready.

## Step 1 — Install ArmKit

Create a fresh virtual environment so this project stays isolated from the rest
of your system, then install the package:

```console
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -e .
```

The `-e` flag installs the project in *editable* mode, which is convenient
while you are still exploring the code.

## Step 2 — Open a simulation

Start Python and create a controller. This opens a window with an empty physics
world:

```python
from armkit.controller import ArmController

arm = ArmController(gui=True)
```

A grey PyBullet window appears. It is empty for now — that is expected. You have
a physics world with gravity, but nothing in it yet.

## Step 3 — Load a robot

Add a robot arm to the world:

```python
arm.load_arm()
print(arm.num_joints())
```

A KUKA robot arm appears at the centre of the scene. The printed number is how
many joints it has — seven for this model.

```{note}
`load_arm()` uses a robot model that ships with PyBullet, so nothing extra is
downloaded. You can pass your own URDF file later if you want a different robot.
```

## Step 4 — Move a joint

Command the second joint (index `1`) to bend to 0.5 radians, then advance the
simulation so the motion actually plays out:

```python
arm.set_joint_angle(1, 0.5)
arm.step(240)
```

Watch the arm swing. Commanding a joint only sets a *target*; the arm reaches it
as the simulation steps forward. `step(240)` runs about one second of simulated
time.

Confirm where the joint ended up:

```python
print(f"{arm.get_joint_angle(1):.3f} rad")
```

The value should be close to `0.500`.

## Step 5 — Tidy up

Close the connection when you are done:

```python
arm.disconnect()
```

## What you did

You installed ArmKit, opened a simulation, loaded a robot, and drove one of its
joints to a target angle. That loop — *command, step, read back* — is the core
of controlling any simulated robot.

## Next steps

- Move several joints at once: {doc}`../how-to/set-joint-angles`
- Run without a window, for scripts and CI: {doc}`../how-to/run-headless`
- Understand how joint angles become arm positions:
  {doc}`../explanation/forward-kinematics`
