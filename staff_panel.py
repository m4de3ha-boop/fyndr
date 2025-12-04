import streamlit as st
from data import load_items, save_items
import uuid

PASSWORD = "admin123"   # change this!

def run():
    st.header("👩‍🏫 Staff Panel")

    pw = st.text_input("Enter Staff Password:", type="password")
    if pw != PASSWORD:
        st.warning("Wrong password")
        return

    df = load_items()

    st.subheader("➕ Add a Lost Item")
    name = st.text_input("Item Name")
    desc = st.text_area("Description")
    img = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    if st.button("Upload"):
        if name and desc and img:
            id = str(uuid.uuid4())[:8]

            with open(f"images_{id}.jpg", "wb") as f:
                f.write(img.getbuffer())

            df.loc[len(df)] = [id, name, desc, f"images_{id}.jpg", "lost", ""]
            save_items(df)
            st.success("Item uploaded successfully ")
        else:
            st.error("Fill everything")

    st.subheader("📦 All Items")
    st.dataframe(df)

    st.subheader("✅ Claimed Items")
    st.dataframe(df[df["status"] == "claimed"])
