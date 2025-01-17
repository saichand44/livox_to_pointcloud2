import os

import launch
import launch.actions
import launch.events

import launch_ros
import launch_ros.actions
import launch_ros.events

from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node

import lifecycle_msgs.msg

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    # Path to the RViz configuration file
    rviz_config_path = os.path.join(
        get_package_share_directory('livox_to_pointcloud2'),
        'rviz2',
        'display_livox_to_pointcloud2.rviz'
    )

    ld = launch.LaunchDescription()

    # Static transform publisher for 'map' frame
    map_tf = launch_ros.actions.Node(
        name='map_tf',
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0','0','0','0','0','0','1','world','map']
        )

    # Static transform publisher for 'lidar' frame
    lidar_tf = launch_ros.actions.Node(
        name='lidar_tf',
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0','0','0','0','0','0','1','map','livox_frame']
        )

    # RViz node to launch RViz2 with a specific configuration
    livox_to_pointcloud2_node = Node(
        package='livox_to_pointcloud2',
        executable='livox_to_pointcloud2_node',
        name='livox_to_pointcloud2_node',   
        output='screen',
    )

    # RViz node to launch RViz2 with a specific configuration
    livox_to_pointcloud2_rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['--display-config', rviz_config_path]
    )

    ld.add_action(map_tf)
    ld.add_action(lidar_tf)
    ld.add_action(livox_to_pointcloud2_node)
    ld.add_action(livox_to_pointcloud2_rviz)

    return ld