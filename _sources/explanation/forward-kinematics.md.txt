# How joint angles become arm positions

This page explains a concept; it is not a set of steps to follow. Read it when
you want to understand *why* the arm ends up where it does.

## The question

When you call `set_joint_angle(1, 0.5)`, the arm's hand moves to some point in
space. How does a list of joint angles turn into the position of the hand?

## Forward kinematics

A robot arm is a chain of rigid links connected by joints. Each joint adds a
known rotation or slide. **Forward kinematics** is the calculation that takes
the angle of every joint and works out, link by link along the chain, where the
end of the arm — the *end effector* — sits in space.

The key property is that forward kinematics has exactly one answer. Given a full
set of joint angles, there is a single position and orientation for the hand. The
simulator does this calculation for you every time you step it, which is why
reading `get_joint_angle()` after a move is enough to know the arm's pose.

## The harder direction

The reverse question — "what joint angles put the hand *here*?" — is called
**inverse kinematics**, and it is much harder. There may be several valid
answers, or none. ArmKit deliberately stays on the forward side: you command
joints, and the simulator tells you where the arm went.

## Why this matters for the docs

Tutorials and how-to guides in this site command joints and then read positions
back. That works precisely because forward kinematics is unambiguous. If we were
commanding hand positions instead, the guides would need to discuss which of the
several possible solutions the arm should choose.
