import os
import sys
import json
import configparser

# Exercise 1: Check required environment variables
def check_required_env_vars(required_vars):
    """Check if all required environment variables exist."""
    missing_vars = []
    
    for var in required_vars:
        if os.getenv(var) is None:
            missing_vars.append(var)
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set these variables before running the script.")
        return False
    
    print("All required environment variables are set!")
    return True

# Exercise 2: Set environment variables based on deployment environment
def configure_environment():
    """Set environment variables based on the DEPLOY_ENV variable."""
    deploy_env = os.getenv('DEPLOY_ENV', 'development').lower()
    
    if deploy_env == 'development' or deploy_env == 'dev':
        print("Configuring for DEVELOPMENT environment")
        os.environ['DB_HOST'] = 'localhost'
        os.environ['API_URL'] = 'http://dev-api.example.com'
        os.environ['LOG_LEVEL'] = 'DEBUG'
        os.environ['FEATURE_FLAGS'] = 'beta,testing'
    
    elif deploy_env == 'staging':
        print("Configuring for STAGING environment")
        os.environ['DB_HOST'] = 'staging-db.example.com'
        os.environ['API_URL'] = 'https://staging-api.example.com'
        os.environ['LOG_LEVEL'] = 'INFO'
        os.environ['FEATURE_FLAGS'] = 'beta'
    
    elif deploy_env == 'production' or deploy_env == 'prod':
        print("Configuring for PRODUCTION environment")
        os.environ['DB_HOST'] = 'prod-db.example.com'
        os.environ['API_URL'] = 'https://api.example.com'
        os.environ['LOG_LEVEL'] = 'WARNING'
        os.environ['FEATURE_FLAGS'] = ''
    
    else:
        print(f"Unknown environment: {deploy_env}, using development defaults")
        os.environ['DB_HOST'] = 'localhost'
        os.environ['API_URL'] = 'http://dev-api.example.com'
        os.environ['LOG_LEVEL'] = 'DEBUG'
    
    return deploy_env

# Example usage
if __name__ == "__main__":
    # Check required environment variables
    required_vars = ['DB_USER', 'DB_PASSWORD', 'DB_HOST']
    if not check_required_env_vars(required_vars):
        sys.exit(1)
    
    # Configure environment based on deployment stage
    deploy_env = configure_environment()
    print(f"Configured for {deploy_env} environment")