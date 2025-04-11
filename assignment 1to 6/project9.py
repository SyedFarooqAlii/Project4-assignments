import streamlit as st

st.set_page_config(
    page_title="👨‍💻 Farooq | Python Developer",
    page_icon="💻",
    layout="centered"
)

st.title("👋 Hi, I'm Farooq")
st.subheader("A Passionate Python Developer")
st.markdown("I build Python apps, automate boring stuff, and love making ideas come to life with code.")

st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=120)

st.header("🚀 What I Do")
st.write("""
- 💡 I solve real-world problems using Python
- 🧱 I build Streamlit web apps
- ⚙️ I automate tasks with scripts and bots
- ✍️ I write clean, readable code
""")

st.header("🛠️ Projects")
st.write("""
- 🔢 **BMI Calculator**  
  Built a quick health checker with Streamlit.

- 🎮 **Guess the Number Game**  
  Fun CLI game using Python control flow.

- 🔐 **Password Generator**  
  Generates strong, secure passwords on the fly.
""")

st.header("📬 Let's Connect")
st.write("Want to collaborate or just say hi? Find me here:")

st.markdown("""
- 📧 Email: [farooq@example.com](mailto:farooq@example.com)  
- 🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)  
- 🧑‍💼 LinkedIn: [linkedin.com/in/yourusername](https://linkedin.com/in/yourusername)
""")


st.markdown("---")
st.write("Made with ❤️ in Streamlit | © 2025 Farooq")
