import streamlit as st

def main():
    st.title("Pyrotect")
    st.write("Telpon damkar "113" untuk panggilan darurat kebakaran!!")

    # Create a sample file content
    sample_text = """Download program deteksi kebakaran dengan berbagai alat : Arduino IDE Software ; sensor DHT 11 dan sensor MQ 135 ; ESP32 ; Small Board; Kabel"""
    
    # Convert the text to bytes
    sample_text_bytes = sample_text.encode('utf-8')

    # Provide a button to download the file
    st.download_button(
        label="Download program",
        data=sample_text_bytes,
        file_name="",
        mime="text/plain"
    )

if __name__ == "__main__":
    main()
