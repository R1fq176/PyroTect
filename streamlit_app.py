import streamlit as st

def main():
    st.title("Pyrotect")
    st.write("Telpon damkar "113" untuk panggilan darurat kebakaran!!")
    
    # Path to your .ino file
    file_path = "Final_ProjectICG3.ino"

    # Read the .ino file
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Provide a button to download the file
    st.download_button(
        label="Download Final_ProjectICG3.ino",
        data=file_data,
        file_name="Final_ProjectICG3.ino",
        mime="application/octet-stream"
    )

if __name__ == "__main__":
    main()
