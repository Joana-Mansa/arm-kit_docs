"""Minimal end-to-end example: load a robot arm and bend one joint.

Run it from the repository root with::

    python examples/move_arm.py

A PyBullet window opens, the KUKA arm appears, and its second joint sweeps to
0.5 rad and back. Close the window to end the script.
"""

import time

from armkit.controller import ArmController


def main() -> None:
    arm = ArmController(gui=True)
    arm.load_arm()
    print(f"Loaded a robot with {arm.num_joints()} joints.")

    # Sweep joint 1 to 0.5 rad, hold, then return to 0.
    for target in (0.5, 0.0):
        arm.set_joint_angle(1, target)
        arm.step(240)  # ~1 second of simulated time
        print(f"Joint 1 is now at {arm.get_joint_angle(1):.3f} rad")
        time.sleep(0.5)

    input("Press Enter to close the simulation...")
    arm.disconnect()


if __name__ == "__main__":
    main()
