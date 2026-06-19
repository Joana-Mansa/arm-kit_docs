# Set multiple joint angles

This guide shows how to move several joints to target positions in one go. It
assumes you have already worked through {doc}`../tutorials/first-arm`.

## Goal

Pose the arm by commanding a list of joints at once, then step the simulation
until they settle.

## Steps

Load the arm as usual:

```python
from armkit.controller import ArmController

arm = ArmController(gui=True)
arm.load_arm()
```

Command a set of joints. Pair each joint index with its target angle in radians:

```python
targets = {0: 0.4, 1: -0.6, 3: 1.0}

for joint_index, angle in targets.items():
    arm.set_joint_angle(joint_index, angle)
```

Step the simulation so the arm moves towards the pose:

```python
arm.step(480)  # ~2 seconds, enough for larger moves to settle
```

Read the joints back to confirm the pose:

```python
for joint_index in targets:
    print(f"joint {joint_index}: {arm.get_joint_angle(joint_index):.3f} rad")
```

## Notes

- Joint indices run from `0` to `arm.num_joints() - 1`.
- Large moves need more steps to settle. If a joint has not reached its target,
  step the simulation further rather than re-sending the command.
