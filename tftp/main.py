import tftpy

# Define the TFTP server's root directory and address
server_directory = '/app/tftp'
server_address = '0.0.0.0'
server_port = 69

# Create the TFTP server instance
server = tftpy.TftpServer(server_directory)

# Start the server
try:
  print(f"Starting TFTP server on {server_address}:{server_port}")
  server.listen(server_address, server_port)
except KeyboardInterrupt:
  print("TFTP server stopped.")
