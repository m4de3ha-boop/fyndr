import streamlit as st
from data import load_items, save_items

def run():
    st.header("🎒 Student Panel")

    df = load_items()

    st.subheader("✏️ Register What You Lost")
    lost_name = st.text_input("Name of Lost Item")
    lost_desc = st.text_area("Description of what you lost")
    student_name = st.text_input("Your Name")

    if st.button("Search"):
        if lost_name:
            matches = df[df["name"].str.contains(lost_name, case=False)]
            
            if matches.empty:
                st.error("No matching items found ")
            else:
                st.success("Found possible matches")
                for i, row in matches.iterrows():
                    st.image(row["image"])
                    st.write(f"**Item:** {row['name']}")
                    st.write(f"**Description:** {row['desc']}")

                    if st.button(f"Claim {row['id']}"):
                        df.loc[i, "status"] = "claimed"
                        df.loc[i, "claimed_by"] = student_name
                        save_items(df)
                        st.success("Item claimed! Staff will confirm ")
        else:
            st.error("fill in all the details")
