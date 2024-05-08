import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the package name where your configurations are stored
    package_name = 'firebot'

    # Path to your robot's URDF and controller configurations
    urdf_file_path = os.path.join(get_package_share_directory(package_name), 'src','description', 'firebot_description.urdf.xacro')
    controllers_config_path = os.path.join(get_package_share_directory(package_name), 'config', 'my_controllers.yaml')

    # The controller_manager node
    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        output='screen',
        parameters=[{'robot_description': open(urdf_file_path, 'r').read()},
                    controllers_config_path]
    )

    # A node to load and start controllers, assuming you have pre-configured controller in your config
    load_and_start_controller_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['your_controller_name'],
        output='screen'
    )

    # A node to list hardware interfaces, could be launched separately for debugging/inspection
    list_hardware_interfaces_node = Node(
        package='controller_manager',
        executable='list_hardware_interfaces',
        output='screen'
    )

    # Combine all nodes into a single launch description
    return LaunchDescription([
        controller_manager_node,
        load_and_start_controller_node,
        list_hardware_interfaces_node
    ])

