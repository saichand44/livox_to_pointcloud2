#pragma once

#include <iostream>
#include <rclcpp/rclcpp.hpp>
#include <livox_to_pointcloud2/livox_converter.hpp>

namespace livox_to_pointcloud2
{
class LivoxToPointCloud2 : public rclcpp::Node 
{
private:
    LivoxConverter converter;
    rclcpp::SubscriptionBase::SharedPtr livox_sub;
    rclcpp::Publisher<sensor_msgs::msg::PointCloud2>::SharedPtr points_pub;

public:
    LivoxToPointCloud2(const rclcpp::NodeOptions& options);
    ~LivoxToPointCloud2();
};
}   // namespace livox_to_pointcloud2
