from pathlib import Path
import environ

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Adjust path depth to match your structure

# Initialize environ
env = environ.Env(
    DEBUG=(bool, False)  # Set default casting and fallback values
)

# Read the .env file
environ.Env.read_env(BASE_DIR / '.env')

# Use the variables
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
