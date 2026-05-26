# PASSED, FAILED, RUNNING, SKIP, QUEUED, ERROR

# input
# build id
# build status

# build id + stats (unique combination)
# Order data

# build id: 1
# build status: QUEUED

# build id: 1
# build status: RUNNING

# Can you tell me order status for build id 1
# [QUEUED, RUNNING]

# build id: 1
# build status: RUNNING

# build id: 1
# build status: PASSED

# Can you tell me order status for build id 1
# [QUEUED, RUNNING, PASSED]

# Can you tell me order status for build id 2
# []