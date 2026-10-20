import instacleaner.path as path
import instacleaner.follow_calc as fc

def main():
  
  print(f"Path used: {path.data_dir}")
  fc.follower_reciprocracy(path.data_dir)
  
if __name__ == "__main__":
  main()