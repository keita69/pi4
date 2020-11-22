#-------------------------------------------------------------------------------- 
# 
# exec command is "sudo bash start_sensor.sh"
# 
#-------------------------------------------------------------------------------- 
#!/bin/bash
while true
do
  sudo python3 sensor_writer.py
  sleep 60
done
