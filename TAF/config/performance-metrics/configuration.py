import os

SECURITY_SERVICE_NEEDED=os.getenv("SECURITY_SERVICE_NEEDED")
COMPOSE_IMAGE=os.getenv("COMPOSE_IMAGE")

# Service Port
APP_SERVICE_RULES_PORT = 59701
if SECURITY_SERVICE_NEEDED == 'true':
    DEVICE_REST_PORT = "8443/device-rest"
    DEVICE_VIRTUAL_PORT = "8443/device-virtual"
else:
    DEVICE_REST_PORT = 59986
    DEVICE_VIRTUAL_PORT = 59900


# Suite: 1_resource_usage
# Prior release (IRELAND) image size (MB) for x86
CONSUL_IMAGE = 122.35
DATA_IMAGE = 20.24
METADATA_IMAGE = 16.58
COMMAND_IMAGE = 15.86
NOTIFICATIONS_IMAGE = 16.65
SCHEDULER_IMAGE = 15.93
APP_SERVICE_CONFIGURABLE_IMAGE = 24.73
SYS_MGMT_AGENT_IMAGE = 311.89
DEVICE_VIRTUAL_IMAGE = 24.39
DEVICE_REST_IMAGE = 21.08
KUIPER_IMAGE = 36.18
REDIS_IMAGE = 32.32
PROXY_IMAGE = 25.66
SECRETSTORE_IMAGE = 28.71
KONG_IMAGE = 143.55
KONG_DB_IMAGE = 157.31
VAULT_IMAGE = 207.45
BOOTSTRAPPER_IMAGE = 18.58

# Prior release (IRELAND) binary size (MB) for x86
CONSUL_BINARY = 0
DATA_BINARY = 11.98
METADATA_BINARY = 10.91
COMMAND_BINARY = 10.20
NOTIFICATIONS_BINARY = 10.50
SCHEDULER_BINARY = 10.27
APP_SERVICE_CONFIGURABLE_BINARY = 15.94
SYS_MGMT_AGENT_BINARY = 10.02
DEVICE_VIRTUAL_BINARY = 16.10
DEVICE_REST_BINARY = 12.80
KUIPER_BINARY = 0
REDIS_BINARY = 0
PROXY_BINARY = 0
SECRETSTORE_BINARY = 0
KONG_BINARY = 0
KONG_DB_BINARY = 0
VAULT_BINARY = 0
BOOTSTRAPPER_BINARY = 0

# Prior release (IRELAND) image size (MB) for arm64
CONSUL_IMAGE_ARM64 = 113.84
DATA_IMAGE_ARM64 = 19.15
METADATA_IMAGE_ARM64 = 15.66
COMMAND_IMAGE_ARM64 = 14.98
NOTIFICATIONS_IMAGE_ARM64 = 15.72
SCHEDULER_IMAGE_ARM64 = 15.06
APP_SERVICE_CONFIGURABLE_IMAGE_ARM64 = 23.40
SYS_MGMT_AGENT_IMAGE_ARM64 = 298.88
DEVICE_VIRTUAL_IMAGE_ARM64 = 22.95
DEVICE_REST_IMAGE_ARM64 = 19.90
KUIPER_IMAGE_ARM64 = 74.76
REDIS_IMAGE_ARM64 = 33.01
PROXY_IMAGE_ARM64 = 24.24
SECRETSTORE_IMAGE_ARM64 = 27.13
KONG_IMAGE_ARM64 = 153.85
KONG_DB_IMAGE_ARM64 = 155.06
VAULT_IMAGE_ARM64 = 196.55
BOOTSTRAPPER_IMAGE_ARM64 = 17.54

# Prior release (IRELAND) binary size (MB) for arm64
DATA_BINARY_ARM64 = 11.18
METADATA_BINARY_ARM64 = 10.24
COMMAND_BINARY_ARM64 = 9.56
NOTIFICATIONS_BINARY_ARM64 = 9.82
SCHEDULER_BINARY_ARM64 = 9.64
APP_SERVICE_CONFIGURABLE_BINARY_ARM64 = 14.90
SYS_MGMT_AGENT_BINARY_ARM64 = 9.45
DEVICE_VIRTUAL_BINARY_ARM64 = 14.95
DEVICE_REST_BINARY_ARM64 = 11.91

# Footprint threshold value
# ex. 1.5 = prior release + 50%
FOOTPRINT_THRESHOLD = 1.2

# Suite: 2_service_startup_time
# Retry setting to fetch service startup time
WAIT_TIME = 5
RETRY_TIMES = 5

# Startup time threshold value (in seconds)
STARTUP_TIME_THRESHOLD = 300

# Loop time for retrieving services startup time
STARTUP_TIME_LOOP_TIMES = 5


# Suite: 3_resource_usage_with_autoevent
# CPU threshold value (percentage)
CPU_USAGE_THRESHOLD = 50

# Memory threshold value (in MB)
MEM_USAGE_THRESHOLD = 300

# Loop time for retrieving CPU and Memory
GET_CPU_MEM_LOOP_TIMES = 10

# Interval time for retrieving CPU and Memory (in seconds)
GET_CPU_MEM_INTERVAL = 7


# Suite: 4_ping_response_time
# Loop time for sending ping request
PING_RES_LOOP_TIMES = 100

# Ping response time threshold value (in milliseconds)
PING_RES_THRESHOLD = 100

# Allow the failure times for ping response time over than threshold setting
ALLOWABLE_OUTLIER = 5


# Suite: 5_event_exported_time
# Loop time for sending ping request
EXPORTED_LOOP_TIMES = 10

# Export time threshold value (in milliseconds)
EXPORT_TIME_THRESHOLD = 1200
