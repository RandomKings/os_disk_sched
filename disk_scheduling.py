import sys

def load_cylinder_requests(file_path):
    """Load cylinder requests from a file."""
    with open(file_path, 'r') as file:
        cylinder_reqs = [int(line.strip()) for line in file]
    return cylinder_reqs

def first_come_first_serve(req_list, start_position):
    """First Come First Serve (FCFS) disk scheduling algorithm."""
    total_movement = 0
    current_pos = start_position
    for req in req_list:
        total_movement += abs(req - current_pos)
        current_pos = req
    return total_movement

def elevator_algorithm(req_list, start_pos, max_cylinders=5000):
    """Elevator (SCAN) disk scheduling algorithm."""
    req_list.sort()
    total_movement = 0
    current_pos = start_pos
    pos_index = 0
    
    # Locate starting index
    while pos_index < len(req_list) and req_list[pos_index] < start_pos:
        pos_index += 1
    
    # Ascend
    for i in range(pos_index, len(req_list)):
        total_movement += abs(req_list[i] - current_pos)
        current_pos = req_list[i]
    
    # Descend
    if pos_index > 0:
        total_movement += abs(current_pos - req_list[pos_index - 1])
        current_pos = req_list[pos_index - 1]
        for i in range(pos_index - 2, -1, -1):
            total_movement += abs(req_list[i] - current_pos)
            current_pos = req_list[i]

    return total_movement

def circular_scan_algorithm(req_list, start_pos, max_cylinders=5000):
    """Circular SCAN (C-SCAN) disk scheduling algorithm."""
    req_list.extend([max_cylinders - 1, 0])
    req_list.sort()
    total_movement = 0
    current_pos = start_pos
    pos_index = 0

    # Locate starting index
    while pos_index < len(req_list) and req_list[pos_index] < start_pos:
        pos_index += 1
    
    # Complete circle
    for i in range(pos_index, len(req_list)):
        total_movement += abs(req_list[i] - current_pos)
        current_pos = req_list[i]

    # Return to start
    if pos_index > 0:
        total_movement += abs(current_pos - req_list[0])
        current_pos = req_list[0]
        for i in range(1, pos_index):
            total_movement += abs(req_list[i] - current_pos)
            current_pos = req_list[i]

    return total_movement

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python disk_scheduling_mod.py <initial_head_position>")
        sys.exit(1)

    initial_head_position = int(sys.argv[1])
    requests_file_path = r"C:\Users\p\Desktop\Sem 4\OS_FORUMS\requests.txt"  # Use raw string

    try:
        request_list = load_cylinder_requests(requests_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{requests_file_path}' was not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: The file '{requests_file_path}' contains invalid data.")
        sys.exit(1)

    print("FCFS Total Head Movements:", first_come_first_serve(request_list, initial_head_position))
    print("Elevator Algorithm Total Head Movements:", elevator_algorithm(request_list, initial_head_position))
    print("Circular SCAN Total Head Movements:", circular_scan_algorithm(request_list, initial_head_position))
