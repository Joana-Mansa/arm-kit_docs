/**
 * @file joint_limits.hpp
 * @brief Joint range and velocity limit checking for a serial robot arm.
 *
 * This header is the C++ counterpart to the Python @c armkit package. It exists
 * mainly to demonstrate how a C++ API reference is generated with Doxygen and
 * folded into the same Sphinx site as the Python reference via Breathe.
 */

#ifndef ARMKIT_JOINT_LIMITS_HPP
#define ARMKIT_JOINT_LIMITS_HPP

#include <vector>

/// Top-level namespace for all ArmKit C++ interfaces.
namespace armkit {

/**
 * @brief Result of a limit check.
 *
 * Returned by ArmKit limit-checking calls so that a caller can distinguish a
 * hard violation from a value that is merely close to the boundary.
 */
enum class LimitStatus {
  Ok,        ///< Value is inside the permitted range.
  NearLimit, ///< Value is inside the range but within the warning margin.
  Violation  ///< Value is outside the permitted range.
};

/**
 * @brief Position and velocity limits for a single revolute joint.
 *
 * Angles are in radians and velocities in radians per second. Limits are
 * treated as inclusive bounds.
 */
struct JointLimit {
  double min_position;  ///< Lower position bound, in radians.
  double max_position;  ///< Upper position bound, in radians.
  double max_velocity;  ///< Maximum absolute velocity, in radians per second.
};

/**
 * @brief Checks joint commands against a configured set of limits.
 *
 * A JointLimitChecker is constructed once for a given kinematic chain and then
 * queried per control cycle. It performs no allocation after construction.
 *
 * @par Example
 * @code
 * armkit::JointLimitChecker checker({{-3.14, 3.14, 2.0}});
 * if (checker.CheckPosition(0, 3.20) == armkit::LimitStatus::Violation) {
 *   // reject the command
 * }
 * @endcode
 */
class JointLimitChecker {
 public:
  /**
   * @brief Constructs a checker for a chain of joints.
   * @param limits One JointLimit per joint, ordered from base to tool.
   * @param warning_margin Fraction of the range, between 0.0 and 0.5, within
   *        which LimitStatus::NearLimit is reported. Defaults to 5 percent.
   * @throws std::invalid_argument if @p limits is empty or a limit is inverted.
   */
  explicit JointLimitChecker(std::vector<JointLimit> limits,
                             double warning_margin = 0.05);

  /**
   * @brief Checks a commanded joint position.
   * @param joint_index Zero-based index of the joint, from base to tool.
   * @param position Commanded position in radians.
   * @return LimitStatus::Violation if outside the bounds, LimitStatus::NearLimit
   *         if within the warning margin, otherwise LimitStatus::Ok.
   * @throws std::out_of_range if @p joint_index is not a configured joint.
   *
   * @note This is a purely kinematic check. It does not account for dynamic
   *       effects, collision geometry, or the safety-rated limits enforced by
   *       the controller itself.
   */
  LimitStatus CheckPosition(std::size_t joint_index, double position) const;

  /**
   * @brief Checks a commanded joint velocity.
   * @param joint_index Zero-based index of the joint, from base to tool.
   * @param velocity Commanded velocity in radians per second. The sign is
   *        ignored; only the magnitude is compared against the limit.
   * @return LimitStatus::Violation if the magnitude exceeds the limit,
   *         otherwise LimitStatus::Ok.
   * @throws std::out_of_range if @p joint_index is not a configured joint.
   */
  LimitStatus CheckVelocity(std::size_t joint_index, double velocity) const;

  /// @brief Returns the number of configured joints.
  std::size_t JointCount() const noexcept;

 private:
  std::vector<JointLimit> limits_;
  double warning_margin_;
};

}  // namespace armkit

#endif  // ARMKIT_JOINT_LIMITS_HPP
