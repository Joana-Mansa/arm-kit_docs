# Run without a window (headless)

When you run simulations in a script, on a server, or in CI, you do not want a
graphical window to open. ArmKit supports a headless mode for exactly this.

## Goal

Run the same simulation with no window, suitable for automation.

## Steps

Create the controller with `gui=False`:

```python
from armkit.controller import ArmController

arm = ArmController(gui=False)
arm.load_arm()
```

Everything else works the same — command joints and step the simulation:

```python
arm.set_joint_angle(1, 0.5)
arm.step(240)
print(f"{arm.get_joint_angle(1):.3f} rad")
arm.disconnect()
```

No window appears, and the script can run unattended.

## When to use this

- Continuous integration, where there is no display.
- Generating data in batch across many simulations.
- Running on a remote machine over SSH.
