

import time
import streamlit as st

# Function to read from DHT11 sensor
def read_dht11(pin):
    sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

# Function to read from MQ135 sensor
def read_mq135(adc, channel):
    air_quality = adc.read_adc(channel, gain=1)
    return air_quality

# Function to determine if there's a fire
def is_fire_detected(temperature, air_quality):
    # Define thresholds
    temp_threshold = 50  # Example temperature threshold in Celsius
    air_quality_threshold = 300  # Example air quality threshold (value from ADC)

    if temperature > temp_threshold and air_quality > air_quality_threshold:
        return True
    return False

# Streamlit web interface
def main():
    st.title("Pyrotect")

    dht11_pin = 4  # GPIO pin where DHT11 is connected
    adc = Adafruit_ADS1x15.ADS1115()  # ADC object for reading MQ135
    mq135_channel = 0  # ADC channel where MQ135 is connected

    while True:
        humidity, temperature = read_dht11(dht11_pin)
        air_quality = read_mq135(adc, mq135_channel)

        if humidity is not None and temperature is not None:
            st.write(f"Temperature: {temperature:.2f} °C")
            st.write(f"Humidity: {humidity:.2f} %")
        else:
            st.write("Failed to retrieve data from DHT11 sensor")

        st.write(f"Air Quality: {air_quality}")

        if is_fire_detected(temperature, air_quality):
            st.error("Fire detected!")
        else:
            st.success("No fire detected.")

        time.sleep(2)  # Refresh data every 2 seconds

if __name__ == "__main__":
    main()

