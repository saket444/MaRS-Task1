import math

def get_rotation_matrix(x_deg, y_deg, z_deg):
    ax, ay, az = map(math.radians, [x_deg, y_deg, z_deg])    #converts to radians

    rx = [[1, 0, 0], [0, math.cos(ax), -math.sin(ax)], [0, math.sin(ax), math.cos(ax)]]     #rotation about x
    ry = [[math.cos(ay), 0, math.sin(ay)], [0, 1, 0], [-math.sin(ay), 0, math.cos(ay)]]     #rotation about y
    rz = [[math.cos(az), -math.sin(az), 0], [math.sin(az), math.cos(az), 0], [0, 0, 1]]     #roation about z

    def multiply(A, B):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    # Returns Rz * Ry * Rx 
    return multiply(rz, multiply(ry, rx))

def main():
    print("--- Mars Rover Object Localization ---")
    
    try:
        print("\nEnter Object Coordinates in Camera Frame:")     #Input: object coordinates, camera frame
        x_cam = float(input("  x_cam: "))
        y_cam = float(input("  y_cam: "))
        z_cam = float(input("  z_cam: "))

        print("\nEnter Rover Position in World Frame:")          #Input: Rover Position (World Frame)
        x_r = float(input("  x: ")) 
        y_r = float(input("  y: "))
        z_r = float(input("  z: "))

        print("\nEnter Rover Rotation (Angles in degrees):")     #Input: Rover Rotation (Degrees)
        xr_deg = float(input("  x_angle: "))
        yr_deg = float(input("  y_angle: "))
        zr_deg = float(input("  z_angle: "))

        R = get_rotation_matrix(xr_deg, yr_deg, zr_deg)           #gets roation matrix

        # 2. Apply Rotation (Matrix-Vector Multiplication)
        rotated = [0, 0, 0]
        cam_coords = [x_cam, y_cam, z_cam]
        for i in range(3):
            for j in range(3):
                rotated[i] += R[i][j] * cam_coords[j]

        # 3. Apply Translation (Add Rover Position)
        x_world = rotated[0] + x_r
        y_world = rotated[1] + y_r
        z_world = rotated[2] + z_r

        # Output Result
        print("\n" + "="*30)
        print("Object Coordinates (World Frame):")
        print(f"({x_world:.2f}, {y_world:.2f}, {z_world:.2f})")        #.2f rounds of to 2 decimal places
        print("="*30)

    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    main()