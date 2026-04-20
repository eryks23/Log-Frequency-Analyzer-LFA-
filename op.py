import re
from collections import defaultdict

def analyze_file():
    file_path = input("Enter the path to the file: ").strip()
    data = defaultdict(int)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                
                if not line: 
                    continue
                
                if re.fullmatch(r'.+', line):
                    data[line] += 1
                    
                if not data:
                    print("The file is empty or contains no valid lines")
                    return
                
        sorted_data = sorted(data.items(), key=lambda x: x[1])
        
        print(f"\n{'ITEM':<20} | {'COUNT'}")
        print("-" * 35)
        
        for name, count in sorted_data:
            print(f"{name:<20} | {count}")
            
        print("-" * 35)
        print(f"Least frequent: {sorted_data[0][0]} ({sorted_data[0][1]})")
        print(f"Most frequent: {sorted_data[-1][0]} ({sorted_data[-1][1]})")
        
    except FileNotFoundError:
        print("Error: The specified file was not found")
        
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    analyze_file()