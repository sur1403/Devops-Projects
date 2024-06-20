import paramiko

# Function to establish SSH connection to a server
def ssh_connect(server_ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip, username=username, password=password)
    return client

# Function to update configuration files on a server
def update_config(server_ip, username, password, config_data):
    client = ssh_connect(server_ip, username, password)
    ftp_client = client.open_sftp()
    
    # Example: Update database configuration file
    remote_config_path = '/path/to/database.properties'
    local_config_path = 'local/path/to/database.properties'
    
    # Read local configuration file
    with open(local_config_path, 'r') as file:
        local_config_content = file.read()
    
    # Write updated configuration to remote server
    with ftp_client.file(remote_config_path, 'w') as remote_file:
        remote_file.write(local_config_content)
    
    # Close SFTP and SSH connection
    ftp_client.close()
    client.close()

# Main function to orchestrate configuration updates across servers
def main():
    # Example configuration data (replace with actual data retrieval logic)
    servers = [
        {'ip': 'server1_ip', 'username': 'username1', 'password': 'password1'},
        {'ip': 'server2_ip', 'username': 'username2', 'password': 'password2'}
    ]
    
    # Example: Read configuration data from a central source (e.g., database, file)
    config_data = {
        'database_host': 'db.example.com',
        'database_port': '5432',
        'database_user': 'admin',
        'database_password': 'secure_password'
    }
    
    # Update configuration files on each server
    for server in servers:
        update_config(server['ip'], server['username'], server['password'], config_data)

if __name__ == "__main__":
    main()
