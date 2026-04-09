def muchiko_filter(data, window_size):
    # This filter calculates the average of numbers in a sliding window [cite: 101, 105]
    output = []
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        avg = sum(window) // window_size # Using floor division to get whole numbers [cite: 107, 112]
        output.append(avg)
    return output

def sanchiko_filter(data, window_size):
    # This filter sorts the window and picks the middle number (median) [cite: 113, 119]
    output = []
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        window.sort() # Sorting is required for Sanchiko [cite: 116, 117]
        median = window[window_size // 2]
        output.append(median)
    return output

def main():
    print("--- Martian Sensor Data Filter ---")
    
    # Example data from the task [cite: 102, 114]
    raw_data = [4, 7, 6, 1, 8]
    size = 3
    
    print(f"Original Data: {raw_data}")
    
    # Running Muchiko
    muchiko_result = muchiko_filter(raw_data, size)
    print(f"Muchiko Filter (Average): {muchiko_result}")
    
    # Running Sanchiko
    sanchiko_result = sanchiko_filter(raw_data, size)
    print(f"Sanchiko Filter (Median): {sanchiko_result}")
    

if __name__ == "__main__":
    main()