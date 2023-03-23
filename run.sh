#!/bin/bash

# Start the first process
python producer.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start script1.py: $status"
  exit $status
fi

# Start the second process
python consumer.py stream &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start script2.py: $status"
  exit $status
fi

# Wait for both processes to finish
wait