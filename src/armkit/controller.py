"""A thin, documented wrapper around PyBullet for a simulated robot arm.

This module is intentionally small. Its purpose is to provide clean,
docstring-driven Python that Sphinx can turn into a published API reference,
and to give the how-to guides a stable surface to call.

All angles are in **radians** and all distances are in **metres**, matching
PyBullet's conventions.
"""

from __future__ import annotations

import pybullet as p
import pybullet_data


class ArmController:
    """Control a simulated robot arm inside a PyBullet physics world.

    The controller wraps the lower-level PyBullet calls needed to start a
    simulation, load a robot from a URDF model, read its joints, and command
    joint positions.

    Args:
        gui: If ``True``, open the PyBullet graphical window so you can watch
            the arm move. If ``False``, run headless (no window), which is what
            you want in CI or when generating data in batch.

    Example:
        Load the default arm and bend its second joint::

            from armkit.controller import ArmController

            arm = ArmController(gui=True)
            arm.load_arm()
            arm.set_joint_angle(1, 0.5)
            arm.step(240)
            arm.disconnect()
    """

    def __init__(self, gui: bool = True) -> None:
        self.mode = p.GUI if gui else p.DIRECT
        self.client = p.connect(self.mode)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        self.robot_id: int | None = None

    def load_arm(self, urdf: str = "kuka_iiwa/model.urdf") -> int:
        """Load a robot arm from a URDF file into the simulation.

        Args:
            urdf: Path to the URDF model. Defaults to the KUKA iiwa arm that
                ships with ``pybullet_data``, so it works without any extra
                downloads.

        Returns:
            The body unique id that PyBullet assigns to the loaded robot. Keep
            it if you need to reference the robot in raw PyBullet calls.
        """
        self.robot_id = p.loadURDF(urdf, useFixedBase=True)
        return self.robot_id

    def num_joints(self) -> int:
        """Return the number of joints on the loaded robot.

        Raises:
            RuntimeError: If no robot has been loaded yet.
        """
        if self.robot_id is None:
            raise RuntimeError("Call load_arm() before querying joints.")
        return p.getNumJoints(self.robot_id)

    def set_joint_angle(self, joint_index: int, angle: float) -> None:
        """Command a single joint to a target angle.

        The joint is driven towards ``angle`` using PyBullet's position
        controller. Call :meth:`step` afterwards to let the simulation move the
        joint towards the target.

        Args:
            joint_index: Zero-based index of the joint, from ``0`` to
                ``num_joints() - 1``.
            angle: Target angle in radians.

        Raises:
            RuntimeError: If no robot has been loaded yet.
        """
        if self.robot_id is None:
            raise RuntimeError("Call load_arm() before commanding joints.")
        p.setJointMotorControl2(
            bodyUniqueId=self.robot_id,
            jointIndex=joint_index,
            controlMode=p.POSITION_CONTROL,
            targetPosition=angle,
        )

    def get_joint_angle(self, joint_index: int) -> float:
        """Read the current angle of a joint in radians.

        Args:
            joint_index: Zero-based index of the joint.

        Returns:
            The joint's current position in radians.
        """
        if self.robot_id is None:
            raise RuntimeError("Call load_arm() before reading joints.")
        position, _velocity, _forces, _torque = p.getJointState(
            self.robot_id, joint_index
        )
        return position

    def step(self, steps: int = 1) -> None:
        """Advance the physics simulation.

        Args:
            steps: Number of simulation steps to run. PyBullet steps at 240 Hz
                by default, so ``step(240)`` advances roughly one second.
        """
        for _ in range(steps):
            p.stepSimulation()

    def disconnect(self) -> None:
        """Close the connection to the physics server and free resources."""
        p.disconnect(self.client)
