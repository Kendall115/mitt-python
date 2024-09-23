# MQTT Sensors Dashboard Backend

This project simulates sensors readings using python and mqtt.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Kendall115/mqtt-python.git
```

2. Navigate to the project directory:

```bash
cd mqtt-python
```

# Usage

To start a sensor, navigate to any folder and execute the command

```python
python sensors_name.py
```

For example: python sensor_humidity4.py. This will activate the sensor, and you will see a menu where you can choose option 1 to send a reading or option 2 to disconnect.

As you send readings, they will appear in real time on the dashboard. If the sensor is not already listed, simply send a reading, and the backend will automatically create a new sensor and add the reading.

## Configuration

Before running the application make sure mqtt broker is running and is using port 1883.
