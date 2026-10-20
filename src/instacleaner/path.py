from pathlib import Path

#Gets the project root from our nested file
project_root = Path(__file__).resolve().parents[2]

user_folder = list(
    (project_root / "data").glob(
        "instagram-*/connections/followers_and_following"
    )
)
user_folder = [path for path in user_folder if path.is_dir()]

if not user_folder:
    raise FileNotFoundError("No Instagram export found in data/.")

if len(user_folder) > 1:
    raise ValueError("Multiple Instagram exports found. Keep only one in data/.")

#Path to the data
data_dir = user_folder[0]
