def solve_rover_arm_input():
    print("--- Rover Manipulator Arm Wear Calculator ---")

    try:
        # Taking inputs for limits, wear factors, and target sequence [cite: 147]
        l_input = input("Enter Max Limits for [Inner, Middle, Outer]: ")
        L = [int(x) for x in l_input.split()]
        
        w_input = input("Enter Wear Factors for [W1, W2, W3]: ")
        W = [int(x) for x in w_input.split()]
        
        t_input = input("Enter Sequence of Targets: ")
        targets = [int(x) for x in t_input.split()]
        
        D = int(input("Enter max allowed difference (D) between Inner and Outer: "))

        # Starting state of the arm [cite: 143]
        current_config = (0, 0, 0)
        total_wear_cost = 0

        print(f"\nInitial State: {current_config}")

        for target in targets:
            best_config = None
            min_move_cost = float('inf')

            # Checking every combination to satisfy: Inner + Middle + Outer = Target 
            for i in range(L[0] + 1):
                for m in range(L[1] + 1):
                    o = target - i - m
                    
                    # Check if 'Outer' is within segment limits [cite: 137]
                    if 0 <= o <= L[2]:
                        # Stability condition: |Inner - Outer| <= D [cite: 140, 141, 142]
                        if abs(i - o) <= D:
                            
                            # Calculate movement cost from the current configuration [cite: 144]
                            cost = (abs(i - current_config[0]) * W[0] +
                                    abs(m - current_config[1]) * W[1] +
                                    abs(o - current_config[2]) * W[2])
                            
                            # Pick the configuration with the minimum wear cost [cite: 146]
                            if cost < min_move_cost:
                                min_move_cost = cost
                                best_config = (i, m, o)

            if best_config:
                total_wear_cost += min_move_cost
                current_config = best_config
                print(f"Target {target} reached: {best_config} (Move Cost: {min_move_cost})")
            else:
                print(f"Target {target} is unreachable with current stability limits.")
                return

        print("\n" + "="*30)
        print(f"Final Minimum Total Wear Cost: {total_wear_cost}")
        print("="*30)

    except (ValueError, IndexError):
        print("Invalid input format. Please enter numbers separated by spaces.")

if __name__ == "__main__":
    solve_rover_arm_input()