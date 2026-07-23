#include "armkit/joint_limits.hpp"

#include <cmath>
#include <stdexcept>

namespace armkit {

JointLimitChecker::JointLimitChecker(std::vector<JointLimit> limits,
                                     double warning_margin)
    : limits_(std::move(limits)), warning_margin_(warning_margin) {
  if (limits_.empty()) {
    throw std::invalid_argument("JointLimitChecker requires at least one joint");
  }
  if (warning_margin_ < 0.0 || warning_margin_ > 0.5) {
    throw std::invalid_argument("warning_margin must be between 0.0 and 0.5");
  }
  for (const auto& limit : limits_) {
    if (limit.min_position >= limit.max_position) {
      throw std::invalid_argument("min_position must be below max_position");
    }
    if (limit.max_velocity <= 0.0) {
      throw std::invalid_argument("max_velocity must be positive");
    }
  }
}

LimitStatus JointLimitChecker::CheckPosition(std::size_t joint_index,
                                            double position) const {
  if (joint_index >= limits_.size()) {
    throw std::out_of_range("joint_index is not a configured joint");
  }
  const JointLimit& limit = limits_[joint_index];
  if (position < limit.min_position || position > limit.max_position) {
    return LimitStatus::Violation;
  }
  const double range = limit.max_position - limit.min_position;
  const double margin = range * warning_margin_;
  if (position - limit.min_position < margin ||
      limit.max_position - position < margin) {
    return LimitStatus::NearLimit;
  }
  return LimitStatus::Ok;
}

LimitStatus JointLimitChecker::CheckVelocity(std::size_t joint_index,
                                            double velocity) const {
  if (joint_index >= limits_.size()) {
    throw std::out_of_range("joint_index is not a configured joint");
  }
  if (std::abs(velocity) > limits_[joint_index].max_velocity) {
    return LimitStatus::Violation;
  }
  return LimitStatus::Ok;
}

std::size_t JointLimitChecker::JointCount() const noexcept {
  return limits_.size();
}

}  // namespace armkit
